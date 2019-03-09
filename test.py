##Just a test to see if key works!
##Also see if database connection works.
from collectCoinData import getLatestCoinData
from updateDatabase import test_graph_connection
#Get key from .env file
import setup
api_key = setup.api_key


def main():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    coinCount = '100'
    conversion = 'USD'
    coinData = getLatestCoinData(api_key, url, coinCount, conversion)
    print('If connection to coinmarketcap api works,',
          'you will see data below: \n', coinData)
    test_graph_connection()


if __name__ == "__main__":
    main()
  