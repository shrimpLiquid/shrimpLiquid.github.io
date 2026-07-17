import requests

scores = {}

try:
        print("jsdioa")
        url = 'http://192.168.1.78/submit'
        myobj = input(":")
        # myobj = "goop"

        x = requests.post(url, json = myobj)

        print(x.text)
        if myobj == "list":
            scores = eval(x.text)
            print(scores)
except:
        print("D:")