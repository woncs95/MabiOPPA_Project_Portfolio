import pandas as pd
import os


def setreport():
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, './report.csv')
    print(f"file path is: {file_path}")
    try:
        csv_input = pd.read_csv(file_path)
        csv_input["guildname2"] = [24680, "counter2", "recruit2","roster2"]
        csv_input.to_csv(file_path)

    except FileNotFoundError:
        report = {}
        report['guildname1'] = {}
        guildname1=report['guildname1']
        guildname1['channel_id'] = 13579
        guildname1['runcounter'] = "counter1"
        guildname1['recruit'] = "recruit1"
        guildname1['roster'] = "roster1"
        df = pd.DataFrame(report)
        df.to_csv("report.csv")
