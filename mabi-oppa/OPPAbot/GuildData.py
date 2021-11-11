from dataclasses import dataclass
import pandas as pd

command_data ={'organization':'',
'RunCounter_channel_id':'',
'RunCounter_channel_name':'',
'RunCounter_command_enter':False,
'RosterMaker_channel_id':'',
'RosterMaker_channel_name':'',
'RosterMaker_command_enter':False,
'RaidCalendar_channel_id':'',
'RaidCalendar_channel_name':'',
'RaidCalendar_command_enter':False}

@dataclass
class GuildData:
    guild_name: str
    rco_channel_id: int
    rco_channel_name: str
    rco_command_enter: bool
    rm_channel_id: int
    rm_channel_name: str
    rm_command_enter: bool
    rca_channel_id: int
    rca_channel_name: str
    rca_command_enter: bool = False

    def dataToExel(self):
        command_data['organization'] = self.guild_name
        command_data['RunCounter_channel_id'] = self.rco_channel_id
        command_data['RunCounter_channel_name'] = self.rco_channel_name
        command_data['RunCounter_command_enter'] = self.rco_command_enter
        command_data['RosterMaker_channel_id'] = self.rm_channel_id
        command_data['RosterMaker_channel_name'] = self.rm_channel_name
        command_data['RosterMaker_command_enter'] = self.rm_command_enter
        command_data['RaidCalendar_channel_id'] = self.rca_channel_id
        command_data['RaidCalendar_channel_name'] = self.rca_channel_name
        command_data['RaidCalendar_command_enter'] = self.rca_command_enter
        df_command_data = pd.DataFrame(command_data)
        df_command_data.to_excel('test.xlsx')






