import json 
import pandas as pd
import os

with open('data/DI_CONNECT/DI-Connect-Fitness/ryanyoung_1999@hotmail.co.uk_0_summarizedActivities.json', 'r') as file:
    data = json.load(file)

df = pd.DataFrame(data[0]['summarizedActivitiesExport'])
df = df[df['activityType'] == 'running']

df['date_time'] =(pd.to_datetime(df['beginTimestamp'],unit='ms'))

df['runTimeSeconds'] = df['elapsedDuration']/1000
df['runTimeMinutes'] = df['runTimeSeconds']/60
df['movingTimeSeconds'] = df['movingDuration']/1000
df['movingTimeMinutes'] = df['movingTimeSeconds']/60

df['zone0Seconds'] = df['hrTimeInZone_0']/1000
df['zone1Seconds'] = df['hrTimeInZone_1']/1000
df['zone2Seconds'] = df['hrTimeInZone_2']/1000
df['zone3Seconds'] = df['hrTimeInZone_3']/1000
df['zone4Seconds'] = df['hrTimeInZone_4']/1000
df['zone5Seconds'] = df['hrTimeInZone_5']/1000

df['distanceM'] = df['distance']/100
df['distanceKM'] = df['distance']/100000


df_final = df[
    [
       'date_time',
       'runTimeSeconds',
       'runTimeMinutes',
       'movingTimeSeconds',
        'movingTimeMinutes',
        'zone0Seconds',
        'zone1Seconds',
        'zone2Seconds',
        'zone3Seconds',
        'zone4Seconds',
        'zone5Seconds',
        'distanceM',
        'distanceKM',
        'avgHr',
        'maxHr',
        'minHr',
        'calories',
        'avgRunCadence',
        'elevationGain',
        'locationName',
        'endLongitude',
        'endLatitude'
    ]
]

df_final.to_csv('data/run_summary.csv')

print("CSV file saved successfully")