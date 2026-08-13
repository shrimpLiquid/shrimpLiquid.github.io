import requests

scores = {}
while True:
        try:
                print("jsdioa")
                url = 'http://192.168.1.18/submit'
                myobj = input(":")
                # myobj = "goop"

                x = requests.post(url, json = myobj)

                print(x.text)
        except:
                print("D:")