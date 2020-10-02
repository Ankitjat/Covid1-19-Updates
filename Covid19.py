import requests
import json
from sys import exit

try:
    data = requests.get("https://api.covid19api.com/summary")
except Exception as e:
    exit("Please check Your Internet Connection")

data=json.loads(data.text)
country = True
while country:
    country = input("Enter Country : ")
    for x in data['Countries']:
        if x['Country'].casefold() != country.casefold():
            continue
        else:
            for key, val in x.items():
                print(f"{key:<15}:{val}")
            break
    else:
        print(country,"not Found")
    print("{:=^100}\n".format("{ For Exit Press Enter }"))
