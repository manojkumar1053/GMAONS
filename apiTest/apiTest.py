import requests

apiUrl = "http://interview.wpengine.io/v1/accounts/"
allowedMethods = requests.get(apiUrl)

# for i in range(2000, 2101):
#     json_body = {
#         "account_id": i,
#         "status": "awesome",
#         "created_on": "2020-10-10"
#     }
#     response1 = requests.post(apiUrl, data=json_body)
#     print(response1.content)


#
# checkOptions = requests.options(apiUrl)
# print(allowedMethods.status_code)
# checkPost = requests.post(apiUrl+"-9")
# print(allowedMethods.status_code)


for i in range(8888, 8899):
    json_body = {
        "account_id": i,
        "status": "awesome",
        "created_on": "2020-10-10"
    }
    response1 = requests.post(apiUrl, data=json_body)
    print(response1.status_code)
    print(response1.content)
    print(response1.headers)
#print(response1.content)
