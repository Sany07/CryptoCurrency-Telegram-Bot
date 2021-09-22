from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'


currency = input()

parameters = {
#   'start':'1',
#   'limit':'5000',
#   'convert':'USD'
'slug':currency
}


    
# Makes symbolstr into a list for later for loop
# symbol_list=symbolstr.split(',')

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'Your Api Key',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    if response:
        res = json.loads(response.text)
        resp = res['data']['1']
        print(resp['name'],'\n',resp['quote']['USD']['price']) 

    else:
        print('Not Found\n Type proper name')

except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
