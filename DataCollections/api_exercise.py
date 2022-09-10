import urllib.request as url
import json
path = "https://data.covid19india.org/states_daily.json"
response = url.urlopen(path)

data = json.load(response)
states = data["states_daily"]

# find out sum of confirmed cases in delhi
confirmed_cases = []
for i in range(len(states)):
    if states[i]["status"] == "Confirmed":
        confirmed_cases.append(states[i])

cases = 0
for i in range(len(confirmed_cases)):
    cases += int(confirmed_cases[i]['dl'])

print("Total confirmed cases in Delhi :",cases)