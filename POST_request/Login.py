from UTILS.Utils import URL
import json
import requests
import jsonpath


class LogIn():
    def UserCreate_Post(self):
        url = URL + '/api/register'
        file = open('C:/Users/ALOK-PC/PycharmProjects/API Automation Framework/DATA/LogIn.txt', 'r')
        read_file = file.read()
        print(read_file)

        print("======== Parsing in JSON format =========")
        json_parse = json.loads(read_file)
        print(json_parse)

        print("========== Posting JSON req ==============")

        response = requests.post(url, json_parse)
        print(response.content)
        print()

        # =========== Asserting status code ==========
        assert response.status_code == 200, "Invalid response code"

        print("========= Parsing json Response ============")
        response_parse = json.loads(response.text)
        print(response_parse)
        print()

        print("========== Retrieving Id details from response =========")
        id = jsonpath.jsonpath(response_parse, 'id')
        print(id[0])


postObj = LogIn()
postObj.UserCreate_Post()
