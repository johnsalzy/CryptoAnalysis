#This script will collect coin data about the coins that we care about

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

#Get key from .env file
import setup
api_key = setup.api_key


###############################################################################
#                             getLatestCoinData():                            #
#   Takes three inputs:                                                       #
#       api_key - Key needed to gain access to API see README.md              #
#       query_url -  Address that is being quiried                            #
#       limit - Number of coins data is being returned about                  #
#   One output:                                                               #
#       data: Returns a list of coins and their stats                         #
###############################################################################
def getLatestCoinData(key, query_url, limit):
    data = None
    url = query_url
    parameters = {
        'start': '1',
        'limit': limit,
        'convert': 'USD',
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': key,
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
    return data


###############################################################################
#                             sortCoinData():                                 #
#   Takes two inputs:                                                         #
#       coinData - Data obtained from getLatestCoinData()                     #
#       caredList - A list of coins we want the stats about                   #
#   One output:                                                               #
#       Returns a list of cared about coins and their stats                   #
###############################################################################
def sortCoinData(coinData, caredList):
    sortedCoinData = []
    print(coinData['status'], '\n')
    for coin in coinData['data']:
        if coin['id'] in caredList:
            sortedCoinData.append(coin)
    return sortedCoinData


def main():
    #caredList = [Bitcoin, Ethereum, XRP, Litecoin, EOS, Bitcoin Cash, Binance,
    #             Tether, Stellar, TRON, Bitcoin SV, Cardano, Monero, IOTA, 
    #             DASH, Maker, NEO, Ethereum Classic, NEM]
    caredList = [1, 1027, 52, 2, 1756, 1831, 1839, 825, 512, 1958, 3602, 2010,
                 328, 1720, 131, 1518, 1376, 1321, 873]
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    coinCount = '100'
    coinData = getLatestCoinData(api_key, url, coinCount)
    sortedCoinData = sortCoinData(coinData, caredList)
    
    return sortCoinData
    
if __name__ == "__main__":
    main()