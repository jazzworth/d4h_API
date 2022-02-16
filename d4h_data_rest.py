import requests
import os
import datetime
import time
import json
import numpy as np
import pandas as pd
from pandas.io.json import json_normalize
import pprint


class Api_calls:

    # initialize object with object attributes
    def __init__(self):

        # required data for header and REST function
        self.api_token = 'your own api token goes here'
        self.header = {'Authorization': 'Bearer ' + self.api_token}
        self.server_url = 'https://api.d4h.org/v2/team/'

    # function to retrieve custom fields

    def getCustomFields(self):

        # url for REST object as specified in the d4h api docs
        api_url = self.server_url + 'custom-fields'

        # make the call to the api. Using this call to test status code in stead of direct convert to json
        r = requests.get(api_url, headers=self.header)

        # test for success status code
        if r.status_code in range(200, 299):

            # use json decoder to serialize data to json
            json_output_temp = r.json()

            # create dataframe normailized on the 'data' key
            df = pd.json_normalize(json_output_temp, 'data', errors='ignore')

            # write json to csv
            df.to_csv('output_custom_fields_' + str(datetime.datetime.now()
                                                    ) + '.csv', index=False, encoding='utf-8')

    # function to retrieve a list of tasks

    def getTasks(self):

        # url for REST object as specified in the d4h api docs
        api_url = self.server_url + 'tasks'

        # make the call to the api. Using this call to test status code in stead of direct convert to json
        r = requests.get(api_url, headers=self.header)

        # test for success status code
        if r.status_code in range(200, 299):

            # use json decoder to serialize data to json
            json_output_temp = r.json()

            # create dataframe normailized on the 'data' key
            pprint.pprint(json_output_temp)
            df = pd.json_normalize(json_output_temp, 'data', errors='ignore')

            # #write json to csv
            df.to_csv('output_tasks' + str(datetime.datetime.now()) +
                      '.csv', index=False, encoding='utf-8')

    # function to retrieve a list of members

    def getMembers(self):

        # url for REST object as specified in the d4h api docs
        api_url = self.server_url + 'members'

        # make the call to the api. Using this call to test status code in stead of direct convert to json
        r = requests.get(api_url, headers=self.header)

        # test for success status code
        if r.status_code in range(200, 299):

            # use json decoder to serialize data to json
            json_output_temp = r.json()

            # create dataframe normailized on the 'data' key
            pprint.pprint(json_output_temp)
            df = pd.json_normalize(json_output_temp, 'data', errors='ignore')

            # #write json to csv
            df.to_csv('output_members' + str(datetime.datetime.now()
                                             ) + '.csv', index=False, encoding='utf-8')

    # function to retrieve a list of exercises

    def getExercises(self):

        # url for REST object as specified in the d4h api docs
        api_url = self.server_url + 'exercises'

        # make the call to the api. Using this call to test status code in stead of direct convert to json
        r = requests.get(api_url, headers=self.header)

        # test for success status code
        if r.status_code in range(200, 299):

            # use json decoder to serialize data to json
            json_output_temp = r.json()

            # create dataframe normailized on the 'data' key
            pprint.pprint(json_output_temp)
            df = pd.json_normalize(json_output_temp, 'data', errors='ignore')

            # #write json to csv
            df.to_csv('output_exercises' + str(datetime.datetime.now()
                                               ) + '.csv', index=False, encoding='utf-8')

    # function to retrieve a list of exercises
    def getActivites(self):

        # url for REST object as specified in the d4h api docs
        api_url = self.server_url + 'activities'

        # make the call to the api. Using this call to test status code in stead of direct convert to json
        r = requests.get(api_url, headers=self.header)

        # test for success status code
        if r.status_code in range(200, 299):

            # use json decoder to serialize data to json
            json_output_temp = r.json()

            # create dataframe normailized on the 'data' key
            pprint.pprint(json_output_temp)
            df = pd.json_normalize(json_output_temp, 'data', errors='ignore')

            # #write json to csv
            df.to_csv('output_activities' + str(datetime.datetime.now()
                                                ) + '.csv', index=False, encoding='utf-8')

     # function to retrieve a list of exercises
    def getIncidents(self):

        # url for REST object as specified in the d4h api docs
        api_url = self.server_url + 'incidents'

        # make the call to the api. Using this call to test status code in stead of direct convert to json
        r = requests.get(api_url, headers=self.header)

        # test for success status code
        if r.status_code in range(200, 299):

            # use json decoder to serialize data to json
            json_output_temp = r.json()

            # create dataframe normailized on the 'data' key
            pprint.pprint(json_output_temp)
            df = pd.json_normalize(json_output_temp, 'data', errors='ignore')

            # #write json to csv
            df.to_csv('output_incidents' + str(datetime.datetime.now()
                                               ) + '.csv', index=False, encoding='utf-8')

    # function to add a task from a csv file

    def postTasks(self):

        # url for REST object as specified in the d4h api docs
        api_url = self.server_url + 'tasks'

        # temp_data = {"ref":"testupload107","date_due":"2021-02-23","member_id":86587,"description":"This is a task that was uploaded via the api"}

        # read in the csv
        data = pd.read_csv('upload_task.csv')

        # convert the data to json and create json file for use and records
        data.to_json('temp_data.json', orient='records', lines=True)

        # loop through lines (records) and POST with open automatically closes the file when finished
        with open('temp_data.json') as f:
            for line in f:
                json_lines = json.loads(line)
                task_request = requests.post(
                    api_url, json=json_lines, headers=self.header)
                print(json_lines)
                print(task_request.text)

    # function to add an exercise from a csv file

    def postExercises(self):

        # url for REST object as specified in the d4h api docs
        api_url = self.server_url + 'exercises'

        # read in the csv
        data = pd.read_csv('upload_exercise.csv')

        # convert the data to json and create json file for use and records
        data.to_json('temp_data.json', orient='records', lines=True)

        # loop through lines (records) and POST with open automatically closes the file when finished
        with open('temp_data.json') as f:
            for line in f:
                json_lines = json.loads(line)
                task_request = requests.post(
                    api_url, json=json_lines, headers=self.header)
                print(json_lines)
                print(task_request.text)

# function to add an incident from a csv file
    def postIncidents(self):

        # url for REST object as specified in the d4h api docs
        api_url = self.server_url + 'incidents'

        # read in the csv
        data = pd.read_csv('upload_incident.csv')

        # convert the data to json and create json file for use and records
        data.to_json('temp_data.json', orient='records', lines=True)

        # loop through lines (records) and POST with open automatically closes the file when finished
        with open('temp_data.json') as f:
            for line in f:
                json_lines = json.loads(line)
                task_request = requests.post(
                    api_url, json=json_lines, headers=self.header)
                print(json_lines)
                print(task_request.text)

# function to add an incident from a csv file
    def postEvents(self):

        # url for REST object as specified in the d4h api docs
        api_url = self.server_url + 'events'

        # read in the csv
        data = pd.read_csv('upload_event.csv')

        # convert the data to json and create json file for use and records
        data.to_json('temp_data.json', orient='records', lines=True)

        # loop through lines (records) and POST with open automatically closes the file when finished
        with open('temp_data.json') as f:
            for line in f:
                json_lines = json.loads(line)
                task_request = requests.post(
                    api_url, json=json_lines, headers=self.header)
                print(json_lines)
                print(task_request.text)

    # TODO create file agnostic iterator for POST in methods

    def iterateJson(self):
        data = pd.read_csv('upload_task.csv')
        data.to_json('temp_data.json', orient='records', lines=True)
        with open('temp_data.json') as f:
            for line in f:
                temp_data = json.loads(line)
                time.sleep(5)
                print(temp_data)


output_object = Api_calls()
# output_object.outputCustomFields()
# output_object.getTasks()
# output_object.postTasks()
# output_object.iterateJson()
# output_object.getMembers()
# output_object.getExercises()
# output_object.getIncidents()
# output_object.getActivites()
# output_object.postExercises()
# output_object.postIncidents()
# output_object.postEvents()
