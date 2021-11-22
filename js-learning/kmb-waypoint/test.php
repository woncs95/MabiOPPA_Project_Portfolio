<?php
namespace App\Http\Controllers\Admin;
use App\Applicant;
use App\ApplicantUserState;
use App\ApplicationPortals;
use App\ApplicationState;
use App\Document;
use App\Http\Controllers\Controller;
use App\Http\Requests\ApplicantUpdateRequest;
use App\Institution;
use App\JobTitle;
use App\Mail\DeclineMail;
use App\Mail\InviteMail;
use App\Mail\ReservedMail;
use App\Mail\TransmitMail;
use App\Mail\SecretaryTransmitMail;
use App\User;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Input;
use Illuminate\Support\Facades\Mail;
use Illuminate\Support\Facades\Route;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\DB;
class ApplicantController extends Controller
{
    private static $maillist = ['test@klinikum-mittelbaden.de'];
    /***
     * returns overview over all applicants filtered by $request
     * @param Request $request
     * @return $this
     */
    public function index(Request $request)
    {
        $auth_user = Auth::user();
        $query = Applicant::query();
        $dateRange = array();
        $dateRange[0] = date('d-m-Y', strtotime("21.12.2017"));
        $dateRange[1] = date('d-m-Y');
        if($request->exists('daterange')) {
            $startDate = date_create_from_format('d-m-Y',substr($request['daterange'], 0, 10));
            $endDate = date_create_from_format('d-m-Y',substr($request['daterange'], 13, 10));
            $dateRange[0] = date_format($startDate, 'd-m-Y');
            $dateRange[1] = date_format($endDate, 'd-m-Y');
        }
        $query = $this->getFilteredQuery($query, $request);
        $this->orderByKeyword($query, $request['desc'], $request['sort']);
        $applicants = $query->orderBy('created_at', 'desc')->simplePaginate(30);
        $links = $applicants->appends(Input::except('page'))->links();
        $route = Route::currentRouteName();
        $states = ApplicationState::all();
        $status = array();
        $status[-1] = __('messages.all_status');
        foreach ($states as $state) {
            $status[$state->id] = $state->state;
        }
        $application_portals_array = array();
        $application_portals = DB::table('application_portals')->get();
        foreach ($application_portals as $application_portal){
            $application_portals_array[$application_portal->id]=$application_portal->name;
        }
        $institutions = array();
        $institutions[-1] = __('messages.all_institutions');
        foreach (Institution::all()->sortBy('name') as $institution) {
            $institutions[$institution->id] = $institution->name;
        }
        $jobTitles = array();
        $jobTitles[-1] = __('Alle Berufe');
        foreach (JobTitle::all() as $jobTitle) {
            $jobTitles[$jobTitle->id] = $jobTitle->name;
        }
        $headPhysicians = self::getHeadPhysiciansAsArray();
        $headPhysiciansForQuery = array();
        $headPhysiciansForQuery[-1] = __('messages.all_head_physicians');
        foreach($headPhysicians as $key => $value) {
            $headPhysiciansForQuery[$key] = $value;
        }
        return view('admin.applicants')->with(compact('application_portals_array','applicants', 'links', 'status', 'headPhysicians', 'route', 'institutions', 'jobTitles', 'auth_user', 'dateRange', 'headPhysiciansForQuery'));
    }
    /***
     * Applies filters to the given $query and returns it afterwards
     * moved here to shorten the index function
     * @param $query
     * @param $request
     * @return mixed - $query
     */
    public static function getFilteredQuery($query, $request) {
        if ($request->exists('status') && $request['status'] > -1) {
            $query = $query->whereHas('states', function($q) use($request){
                $q->where('application_state_id', '=', $request['status']);
            });
        }
        if ($request->exists('job_title_id') && $request['job_title_id'] > -1) {
            $query = $query->where('job_title_id', $request['job_title_id']);
        }
        if ($request->exists('institution') && $request['institution'] > -1) {
            $query = $query->where('institution_id', $request['institution']);
        }
        if($request->exists('head_physician_id') && $request['head_physician_id'] > -1) {
            $query = $query->whereHas('states', function($q) use($request){
                $q->where('user_id', '=', $request['head_physician_id']);
            });
        }
        if($request->exists('displayed') && $request['displayed'] == 1){
            $query = $query->where('displayed', false);
        }
        else {
            $query = $query->where('displayed', true);
        }
        if($request->exists('daterange')) {
            $startDate = date_create_from_format('d-m-Y', substr($request['daterange'], 0, 10));
            $endDate = date_create_from_format('d-m-Y', substr($request['daterange'], 13, 10));
            $query = $query
                ->where('created_at', '>', date_format($startDate, 'Y-m-d') . " 00:00:00")
                ->where('created_at', '<', date_format($endDate, 'Y-m-d') . " 23:59:59");
        }
        if ($request->exists('query') && !empty($request['query'])) {
            $query->where(function ($query) use ($request) {
                foreach (preg_split("/[\s]+/", $request['query']) as $term) {
                    $query->orWhere('last_name', 'LIKE', '%' . $term . '%')
                        ->orWhere('first_name', 'LIKE', '%' . $term . '%')
                        ->orWhere('email', 'LIKE', '%' . $term . '%')
                        ->orWhere('id', $term)
                        ->orWhere('job_title', 'LIKE', '%' . $term . '%')
                        ->orWhereHas('jobTitle', function ($query) use ($term) {
                            $query->where('name', 'LIKE', '%' . $term . '%');
                        });
                }
            });
        }
        return $query;
    }
    /***
     * return the detailed view of an applicant
     * @param $id
     * @return $this
     */
    public function show($id)
    {
        $applicant = Applicant::findOrFail($id);
        $headPhysicians = self::getHeadPhysiciansAsArray();
        $coveringLetter = preg_split("/<br\/>|\n/", $applicant->covering_letter);
        $route = Route::currentRouteName();
        $application_portals_array = array();
        $application_portals = DB::table('application_portals')->get();
        foreach ($application_portals as $application_portal){
            $application_portals_array[$application_portal->id]=$application_portal->name;
        }
        return view('admin.applicant_show')->with(compact('application_portals_array','applicant', 'headPhysicians', 'coveringLetter', 'route'));
    }
    /***
     *
     * @param Request $request
     * @param $id
     * @return mixed
     */
    public function transmitApplicant(Request $request, $id)
    {
        if (!$request->exists('head_physicians')) {
            return redirect(route('admin.applicants.index'))->withFailure(__('messages.failure_transmit'));
        }
        $applicant = Applicant::findOrFail($id);
        $sender = Auth::user()->first();
        foreach ($request['head_physicians'] as $headID) {
            $headPhysician = User::findOrFail($headID);
            Mail::to($headPhysician->email)->send(new TransmitMail($applicant, $headPhysician, true, $sender));
            $to = $headPhysician->secretaryEmails()->get();
            if(count($to) > 0) {
                Mail::to($to)->send(new SecretaryTransmitMail($applicant, $headPhysician));
            }
            $aus = $headPhysician->states()->whereHas('applicant', function ($query) use ($applicant) {
                $query->where('id', $applicant->id);
            })->get();
            if (count($aus) == 0) {
                $aus = new ApplicantUserState();
                $aus->applicant()->associate($applicant);
                $aus->user()->associate($headPhysician);
                $aus->applicationState()->associate(1); // see Seeder for more information, 1 stands for transmitted
                $aus->save();
            }
        }
        if($request->has('view')) {
            return redirect(route($request->get('view'), $applicant->id))->withSuccess(__('messages.success_transmit'));
        }
        return redirect(route('admin.applicants.index'))->withSuccess(__('messages.success_transmit'));
    }
    /***
     * This is actually not working for admins. It's sending an email to "test@klinikum-mittelbaden.de"
     * The real inviteApplicant function can be found in app/Http/Controllers/ApplicantController.php
     * @param $id
     * @return mixed
     */
    public function inviteApplicant($id)
    {
        $applicant = Applicant::findOrFail($id);
        $inviteMail = new InviteMail($applicant);
        Mail::to(self::$maillist)->send($inviteMail);
        return redirect(route('admin.applicants.show', $id))->withSuccess(__('messages.applicant_invited'));
    }
    /***
     * Sets Applicants status to reserved and sends E-Mail to applicant and admin
     * @param $id
     * @return mixed
     ***/
    public function reserveApplicant($id)
    {
        $applicant = Applicant::findOrFail($id);
        $reserveMail = new ReservedMail($applicant);
        Mail::to($applicant->email)->send($reserveMail);
        $applicant->managementState()->associate(3);
        $applicant->save();
        return redirect(route('admin.applicants.show', $id))->withSuccess(__('messages.applicant_reserved'));
    }
    /***
     * Sets Applicants status to declined and sends E-Mail to applicant and admin. E-Mail is based on msgId
     * @param $id
     * @param $msgId
     * @return mixed
     */
    public function declineApplicant($id, $msgId)
    {
        $applicant = Applicant::findOrFail($id);
        $declineMail = new DeclineMail($applicant);
        $declineMail->setMsgId($msgId);
        Mail::to($applicant->email)->send($declineMail);
        $applicant->managementState()->associate(ApplicationState::findOrFail(4));
        $applicant->save();
        return redirect(route('admin.applicants.show', $id))->withSuccess(__('messages.applicant_declined'));
    }
    /***
     * Sets Applicants status to declined
     * @param $id
     * @return mixed
     */
    public function declineApplicantManagement($id)
    {
        $applicant = Applicant::findOrFail($id);
        $applicant->managementState()->associate(ApplicationState::findOrFail(5));
        $applicant->save();
        return redirect(route('admin.applicants.show', $id))->withSuccess(__('messages.applicant_declined'));
    }
    /***
     * "deletes" applicant -> sets displayed to false, doesn't delete the entry
     * @param $id
     * @return mixed
     */
    public function deleteApplicant($id)
    {
        $applicant = Applicant::findOrFail($id);
        $applicant->displayed = false;
        $applicant->save();
        return redirect(route('admin.applicants.show', $id))->withSuccess(__('messages.applicant_deleted'));
    }
    /***
     * "recoveres" applicant -> sets displayed to true
     * @param $id
     * @return mixed
     */
    public function recoverApplicant($id) {
        $applicant = Applicant::findOrFail($id);
        $applicant->displayed = true;
        $applicant->save();
        return redirect(route('admin.applicants.show', $id))->withSuccess(__('messages.applicant_recovered'));
    }
    /***
     * returns the edit view of an applicant
     * @param $id
     * @return $this
     */
    public function edit($id)
    {
        $applicant = Applicant::findOrFail($id);
        $institutions = array();
        foreach (Institution::all() as $institution) {
            $institutions[$institution->id] = $institution->name;
        }
        $jobTitles = array();
        foreach (JobTitle::all() as $jobTitle) {
            $jobTitles[$jobTitle->id] = $jobTitle->name;
        }
        return view('admin.applicant_edit')->with(compact('applicant','institutions','jobTitles'));
    }
    /***
     * updates the information of an applicant
     * $request is given by the edit view
     * @param ApplicantUpdateRequest $request
     * @param $id
     * @return $this
     */
    public function update(ApplicantUpdateRequest $request, $id)
    {
        $institution = Institution::findOrFail($request->get('institution'));
        $jobTitle = JobTitle::findOrFail($request->get('job_title_id'));
        $applicant = Applicant::findOrFail($id);
        $applicant->update($request->except('covering_letter'));
        $applicant->covering_letter = str_replace(PHP_EOL, '<br/>', $request->get('covering_letter'));
        $applicant->institution()->associate($institution);
        $applicant->jobTitle()->associate($jobTitle);
        $applicant->save();
        for ($i = 0 ; $i < env('PDF_AMOUNT',5) ; $i++) {
            $fileName = 'file' . $i;
            if ($request->hasFile($fileName)) {
                $file = $request->file($fileName);
                if ($file->isValid() && $file->getClientOriginalExtension() == "pdf") {
                    $path = storage_path('pdf\\applicant\\' . $applicant->id . '\\documents\\');
                    if(!(file_exists($path))) {
                        mkdir($path);
                    }
                    $files = array_slice($files = scandir($path), 2);
                    $amountOfFiles = 0;
                    foreach($files as $fileCounter){
                        $amountOfFiles++;
                    }
                    $fileIndex = $amountOfFiles + 1;
                    $file->move($path, 'document' . $fileIndex . '.pdf');
                    $document = new Document();
                    $document->applicant()->associate($applicant);
                    $document->document_path = $path . 'document' . $fileIndex . '.pdf';
                    $document->original_name = e($file->getClientOriginalName());
                    $document->save();
                } else {
                    // sending back with error message.
                    $applicant->documents->each(function ($item) {
                        $item->delete();
                    });
                    $request->flash();
                    return redirect()->route('applicant.edit')->withErrors(['file' . $i => __('messages.invalid_file_format')]);
                }
            }
        }
        return redirect(route('admin.applicants.edit', $id))->withSuccess(__('messages.user_updated'));
    }
    /***
     * Orders given $query by $keywords. $desc is the trigger for asc / desc ordering.
     * @param $query
     * @param $desc
     * @param $keyword
     * @return mixed
     */
    private function orderByKeyword($query, $desc, $keyword)
    {
        if (isset($desc) && $desc == 'yes') {
            $order = 'desc';
        } else {
            $order = 'asc';
        }
        switch ($keyword) {
            case 'id':
                $query->orderBy('id', $order);
                break;
            case 'job_title':
                $query->orderBy('job_title', $order);
                break;
            case 'first_name':
                $query->orderBy('first_name', $order);
                break;
            case 'last_name':
                $query->orderBy('last_name', $order);
                break;
            case 'created_at':
                $query->orderBy('created_at', $order);
                break;
            default:
                break;
        }
        return $query;
    }
    /***
     * @return array - all headPhysicians ordered by "last_name"
     */
    private function getHeadPhysiciansAsArray()
    {
        $headPhysiciansArray = array();
        $headPhysicians = User::headPhysicians()->orderBy('last_name')->get();
        foreach ($headPhysicians as $user) {
            $headPhysiciansArray[$user->id] = $user->fullName();
        }
        return $headPhysiciansArray;
    }
}