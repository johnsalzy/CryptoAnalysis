#This script will add the collected data to the database

#Import needed Scripts
from utilities import graph_connection, run_query
import collectCoinData


###############################################################################
#                          test_graph_connection()                            #
###############################################################################
#   Purpose:                                                                  #
#       1. Will ensure a node can be added to Neo4j DB                        #
#       2. Will also make sure you can query the database                     #
###############################################################################
def test_graph_connection():
    result = None
    query = "CREATE (n:Person {name:'Bob'})"
    result = run_query(query)
    print('Creation Object:', result)
    result = None
    query2 = "MATCH (n:Person) RETURN n.name AS name"
    result = run_query(query2)
    for record in result:
        print(record["name"])
    return


###############################################################################
#                           update_coin_database()                            #
###############################################################################
#   Purpose:                                                                  #
#       1. Will add data collected in collectCoinData.py to databas           #
#   Inputs:                                                                   #
#       1. Coin data from collectCoinData.py                                  #
###############################################################################
def update_coin_database(coinData, conversion):
    if coinData is None:
        coinData, conversion = collectCoinData.main()
    for coin in coinData:
        #Get data from coins to put into database
        id = coin['id']
        name = coin['name']
        circulating_supply = coin['circulating_supply']
        max_supply = coin['max_supply']
        rank = coin['cmc_rank']
        current_price = coin['quote'][conversion]['price']
        volume_24h = coin['quote'][conversion]['volume_24h']
        percent_change_1h = coin['quote'][conversion]['percent_change_1h']
        percent_change_24h = coin['quote'][conversion]['percent_change_24h']
        percent_change_7d = coin['quote'][conversion]['percent_change_7d']
        market_cap = coin['quote'][conversion]['market_cap']

        print('Rank:', rank, '|',
              'Name:', name, '|',
              'Price:', current_price, '|',
              'Circulating Supply:', circulating_supply, '|',
              'Volume(24h):', volume_24h, '|',
              'Percent Change(1h):', percent_change_1h, '|',
              'Percent Change(24h):', percent_change_24h, '|',
              'Market Cap:', market_cap
              )
    return


def main():
    update_coin_database(None, None)
    
    return 
    
if __name__ == "__main__":
    main()