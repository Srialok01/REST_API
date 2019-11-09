from UTILS.Utils import URL
import requests
import json
import jsonpath


class ListAll:
    global response
    response = requests.get(URL + '/api/users?page=2')

    def SaveGetReq(self):
        assert response.status_code == 200, "response code is invalid"
        with open('C:/Users/ALOK-PC/PycharmProjects/API Automation Framework/DATA/GET_ListAllUsers.txt', 'wb') as f:
            f.write(response.content)

    def GetResponseValidation(self):
        print()
        print(response.content)
        print()
        print("======== Parsing Json Response ========")
        json_response = json.loads(response.text)
        print(json_response)
        print()
        print("========= Fetching all valueS of FirstName using JsonPath =======")
        for i in range(0, 3):
            first_name = jsonpath.jsonpath(json_response, 'data[' + str(i) + '].first_name')
            id = jsonpath.jsonpath(json_response, 'data[' + str(i) + '].id')
            print(f'{i+1}-First name is {first_name[0]} and corresponding id is {id[0]}')


Obj = ListAll()
Obj.SaveGetReq()
Obj.GetResponseValidation()
