function convertPdfTo() {
    // get files
    const files = pdf24.getServerFilesForDefaultFileZone();
    if (files.length == 0) {
        return;
    }
    
    $('#form').hide();
    
    const outputFileType = $('#params [name="outputFileType"]').val();
    const conversionMode = $('#params [name="conversionMode"]').val();
    const conversionModeVisible = $('#params [name="conversionMode"]').is(':visible');
    
    if(outputFileType == 'pdfa') {
        outputFileType = 'pdf';
        conversionMode = 'pdfa';
    }
    
    // start process
    pdf24.workerServer.doPostJson('convertPdfTo', {
        files : files,
        outputFileType : outputFileType,
        dpi : parseInt($('#params [name="dpi"]').val()),
        imageQuality : parseFloat($('#params [name="imageQuality"]').val()) / 100,
        conversionMode : conversionMode
    }, function(result) {
        const monitorUrl = pdf24.workerServer.getJobMonitorUrl({
            jobId : result.jobId
        });
        pdf24.initAndShowWorkerZone(monitorUrl, {
            updateHistory: true
        });
    }, function(xhr) {
        $('#form').show();
        alert('Sorry, an error occurred.');
    });
    
    pdf24.addLastUsedTool('convertPdfTo');
    
    const trackLabel = outputFileType;
    if(conversionModeVisible) {
        trackLabel += ' - ' + conversionMode;
    }
    pdf24.trackPageEvent('ToolUsage', 'ResultGeneration', trackLabel);
}