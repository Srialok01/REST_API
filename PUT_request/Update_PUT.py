from UTILS.Utils import URL
import requests
import json
import jsonpath


class UpdateUsr():
    def Updateuse(self):
        url = URL + "/api/users/2"
        file = open('C:/Users/ALOK-PC/PycharmProjects/API Automation Framework/DATA/PUT Req.txt', 'r')
        file_read = file.read()
        print(file_read)

        print("############ Parsing the file into json format ############")

        json_parse = json.loads(file_read)
        print(json_parse)
        print()

        print("################ Posting the request #####################")
        response = requests.put(url, json_parse)
        print(response.content)
        print()

        assert response.status_code == 200, " Invalid status code "

        print("############## Parsing response in json ##############")
        response_parse = json.loads(response.text)
        print(response_parse)
        print()

        print("############## Finding the value of UpdatedAt ############")

        updated_time = jsonpath.jsonpath(response_parse, 'updatedAt')
        print(updated_time[0])
uptObj = UpdateUsr()
uptObj.Updateuse()