import pandas as pd
import pytz

def read_all_NL():

    df = pd.read_csv('Entsoe_prices_2023/outfile_DA_2023_Jan_Dec.csv', parse_dates=['time_stamp'])
    df.columns = ['time_stamp', 'lbmp']

    # df = pd.concat(dfs)
    df.sort_values('time_stamp', inplace=True)
    df.reset_index(inplace=True, drop=True)
    df['hour'] = df.index



    # Ensure 'time_stamp' is in datetime format, and if it's timezone-aware, convert it to UTC first
    df['time_stamp'] = pd.to_datetime(df['time_stamp'], utc=True)

    # Convert to Amsterdam timezone
    amsterdam_tz = pytz.timezone('Europe/Amsterdam')
    df['time_stamp'] = df['time_stamp'].dt.tz_convert(amsterdam_tz)

    return df