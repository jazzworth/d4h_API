from numpy.core.numeric import NaN
import numpy as np
import pandas as pd
import datetime
import re

# open the working copy of member data from old DB and assign to dataframe
df = pd.read_csv('members_02012022.csv', parse_dates=['orientation_date'])

# create new df to perform series manipulations
df_import = df

# create new Series to concantonate original with dtype str
df_import['Address'] = pd.Series(dtype='string')
df_import['Name'] = pd.Series(dtype='string')
df_import['Position'] = pd.Series(dtype='string')

# addding all the new emergency contact fields
df_import['Emergency Contact 1 Name'] = pd.Series(dtype='string')
df_import['Emergency Contact 1 Relation'] = pd.Series(dtype='string')
df_import['Emergency Contact 1 Phone'] = pd.Series(dtype='string')
df_import['Emergency Contact 1 Alt. Phone'] = pd.Series(dtype='string')
df_import['Emergency Contact 2 Name'] = pd.Series(dtype='string')
df_import['Emergency Contact 2 Relation'] = pd.Series(dtype='string')
df_import['Emergency Contact 2 Phone'] = pd.Series(dtype='string')
df_import['Emergency Contact 2 Alt. Phone'] = pd.Series(dtype='string')

# concatonate original name and address fields
df_import['Address'] = df_import['addr1'] + ', ' + df_import['addr2']
df_import['Name'] = df_import['first_name'] + ' ' + df_import['last_name']

# convert missions to Status
df_import['Status'] = df_import['missions'].apply(
    lambda x: 'Operational' if x == 'Y' else 'Non-Operational')

# rename the old headers
df_import = df_import.rename(columns={

    'email': 'Email',
    'orientation_date': 'Join Date',
    'home_phone': 'Home Phone',
    'work_phone': 'Work Phone',
    'cell_phone': 'Mobile Phone',
    'call_sign': "Call Sign",
    'memb_id': "Reference",
    'comment': 'Comment'

})

# convert the phone so to strings for parsing
df_import['Home Phone'] = pd.Series(df_import['Home Phone'], dtype="string")
df_import['Work Phone'] = pd.Series(df_import['Home Phone'], dtype="string")
df_import['Mobile Phone'] = pd.Series(df_import['Home Phone'], dtype="string")

# remove all characters save for digits as the d4h template requires
df_import['Home Phone'] = df_import['Home Phone'].str.replace('\D+',  '')
df_import['Work Phone'] = df_import['Work Phone'].str.replace('\D+',  '')
df_import['Mobile Phone'] = df_import['Mobile Phone'].str.replace('\D+',  '')

# prepend 505 to numbers less than 10 after adding dummy values
df_import['Work Phone'] = df_import['Work Phone'].fillna(
    '5555555555').replace("", '5555555555')
df_import['Home Phone'] = df_import['Home Phone'].fillna(
    '5555555555').replace("", '5555555555')
df_import['Mobile Phone'] = df_import['Mobile Phone'].fillna(
    '5555555555').replace("", '5555555555')
df_import['Mobile Phone'] = np.where(df_import['Mobile Phone'].str.len(
) < 10, '505' + df_import['Mobile Phone'], df_import['Mobile Phone'])
df_import['Work Phone'] = np.where(df_import['Work Phone'].str.len(
) < 10, '505' + df_import['Work Phone'], df_import['Work Phone'])
df_import['Home Phone'] = np.where(df_import['Home Phone'].str.len(
) < 10, '505' + df_import['Home Phone'], df_import['Home Phone'])


# convert Join Date to a date after handling 0s and NaN entries
df_import['Join Date'] = df_import['Join Date'].replace('0000-00-00', np.nan)
df_import['Join Date'] = df_import['Join Date'].fillna('1900-01-01')
df_import['Join Date'] = pd.to_datetime(df_import['Join Date'], yearfirst=True)

# delete old series
del (df_import['addr1'],
     df_import['addr2'],
     df_import['first_name'],
     df_import['last_name'],
     df_import['url'],
     df_import['fax'],
     df_import['birth'],
     df_import['emerg_cont'],
     df_import['phone_tree'],
     df_import['nonmember'],
     df_import['alt_phone'],
     df_import['pager'],
     df_import['missions'])

# correct column order
columns = [
    'Name',
    'Join Date',
    'Status',
    'Position',
    'Email',
    'Reference',
    'Home Phone',
    'Mobile Phone',
    'Work Phone',
    'Address',
    'Emergency Contact 1 Name',
    'Emergency Contact 1 Relation',
    'Emergency Contact 1 Phone',
    'Emergency Contact 1 Alt. Phone',
    'Emergency Contact 2 Name',
    'Emergency Contact 2 Relation',
    'Emergency Contact 2 Phone',
    'Emergency Contact 2 Alt. Phone',
    'Call Sign',
    'Comment'
]

# change column order to match the template
df_import = df_import[['Name',
                       'Join Date',
                       'Status',
                       'Position',
                       'Email',
                       'Reference',
                       'Home Phone',
                       'Mobile Phone',
                       'Work Phone',
                       'Address',
                       'Emergency Contact 1 Name',
                       'Emergency Contact 1 Relation',
                       'Emergency Contact 1 Phone',
                       'Emergency Contact 1 Alt. Phone',
                       'Emergency Contact 2 Name',
                       'Emergency Contact 2 Relation',
                       'Emergency Contact 2 Phone',
                       'Emergency Contact 2 Alt. Phone',
                       'Call Sign',
                       'Comment'
                       ]]

# write json to csv
df_import.to_csv('output_members' + str(datetime.datetime.now()
                                        ) + '.csv', index=False, encoding='utf-8')
