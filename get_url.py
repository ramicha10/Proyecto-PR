import requests

try:
    id = input("Enter the policy ID: ")
    # id = "2"
    url = "https://soter-premiar2-dev.herokuapp.com/api/v1/policies/{0}.json".format(id)
    r = requests.get(url)
    print("HTML:\n", r.text)
except:
    print(
        "Invalid URL or some error occured while making the GET request to the specified URL"
    )
