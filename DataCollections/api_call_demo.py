Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import urllib.request as url
import json
path = "https://data.covid19india.org/states_daily.json"
response = url.urlopen(path)
response
<http.client.HTTPResponse object at 0x000001D535D18340>
data = json.load(response)
type(data)
<class 'dict'>
data.keys()
dict_keys(['states_daily'])
states = data["states_daily"]
type(states)
<class 'list'>
states[0]
{'an': '0', 'ap': '1', 'ar': '0', 'as': '0', 'br': '0', 'ch': '0', 'ct': '0', 'date': '14-Mar-20', 'dateymd': '2020-03-14', 'dd': '0', 'dl': '7', 'dn': '0', 'ga': '0', 'gj': '0', 'hp': '0', 'hr': '14', 'jh': '0', 'jk': '2', 'ka': '6', 'kl': '19', 'la': '0', 'ld': '0', 'mh': '14', 'ml': '0', 'mn': '0', 'mp': '0', 'mz': '0', 'nl': '0', 'or': '0', 'pb': '1', 'py': '0', 'rj': '3', 'sk': '0', 'status': 'Confirmed', 'tg': '1', 'tn': '1', 'tr': '0', 'tt': '81', 'un': '0', 'up': '12', 'ut': '0', 'wb': '0'}
states[1]
{'an': '0', 'ap': '0', 'ar': '0', 'as': '0', 'br': '0', 'ch': '0', 'ct': '0', 'date': '14-Mar-20', 'dateymd': '2020-03-14', 'dd': '0', 'dl': '1', 'dn': '0', 'ga': '0', 'gj': '0', 'hp': '0', 'hr': '0', 'jh': '0', 'jk': '0', 'ka': '0', 'kl': '3', 'la': '0', 'ld': '0', 'mh': '0', 'ml': '0', 'mn': '0', 'mp': '0', 'mz': '0', 'nl': '0', 'or': '0', 'pb': '0', 'py': '0', 'rj': '1', 'sk': '0', 'status': 'Recovered', 'tg': '0', 'tn': '0', 'tr': '0', 'tt': '9', 'un': '0', 'up': '4', 'ut': '0', 'wb': '0'}
states[2]
{'an': '0', 'ap': '0', 'ar': '0', 'as': '0', 'br': '0', 'ch': '0', 'ct': '0', 'date': '14-Mar-20', 'dateymd': '2020-03-14', 'dd': '0', 'dl': '1', 'dn': '0', 'ga': '0', 'gj': '0', 'hp': '0', 'hr': '0', 'jh': '0', 'jk': '0', 'ka': '1', 'kl': '0', 'la': '0', 'ld': '0', 'mh': '0', 'ml': '0', 'mn': '0', 'mp': '0', 'mz': '0', 'nl': '0', 'or': '0', 'pb': '0', 'py': '0', 'rj': '0', 'sk': '0', 'status': 'Deceased', 'tg': '0', 'tn': '0', 'tr': '0', 'tt': '2', 'un': '0', 'up': '0', 'ut': '0', 'wb': '0'}
len(states)
1563
1563 / 3
521.0
states[435]
{'an': '96', 'ap': '10328', 'ar': '93', 'as': '2372', 'br': '3416', 'ch': '57', 'ct': '523', 'date': '06-Aug-20', 'dateymd': '2020-08-06', 'dd': '0', 'dl': '1299', 'dn': '43', 'ga': '191', 'gj': '1034', 'hp': '131', 'hr': '755', 'jh': '708', 'jk': '499', 'ka': '6805', 'kl': '1298', 'la': '3', 'ld': '0', 'mh': '11514', 'ml': '51', 'mn': '124', 'mp': '830', 'mz': '33', 'nl': '82', 'or': '1699', 'pb': '1035', 'py': '188', 'rj': '1151', 'sk': '29', 'status': 'Confirmed', 'tg': '2092', 'tn': '5684', 'tr': '98', 'tt': '62170', 'un': '0', 'up': '4586', 'ut': '369', 'wb': '2954'}
states[-1]
{'an': '0', 'ap': '13', 'ar': '0', 'as': '10', 'br': '0', 'ch': '0', 'ct': '1', 'date': '16-Aug-21', 'dateymd': '2021-08-16', 'dd': '0', 'dl': '0', 'dn': '0', 'ga': '5', 'gj': '0', 'hp': '3', 'hr': '2', 'jh': '0', 'jk': '1', 'ka': '28', 'kl': '142', 'la': '0', 'ld': '0', 'mh': '100', 'ml': '8', 'mn': '6', 'mp': '1', 'mz': '3', 'nl': '4', 'or': '66', 'pb': '2', 'py': '0', 'rj': '0', 'sk': '0', 'status': 'Deceased', 'tg': '3', 'tn': '28', 'tr': '1', 'tt': '438', 'un': '0', 'up': '1', 'ut': '1', 'wb': '9'}
