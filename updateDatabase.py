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
    connection = False
    result = None
    query = "CREATE (n:Person {name:'Bob'})"
    result = run_query(query)
    print('Creation Object:', result)
    result = None
    query2 = "MATCH (n:Person) RETURN n.name AS name"
    result = run_query(query2)
    for record in result:
        print(record["name"])
        if record["name"] == 'Bob':
            connection = True
    return connection


###############################################################################
#                          get_individual_coin_data()                         #
###############################################################################
#   Purpose:                                                                  #
#       1. Will seperate coins stats                                          #
#   Inputs:                                                                   #
#       1. individual coin data from collectCoinData                          #
#       2. Conversion (USD, EURO, ect.)                                       #
#   Output:                                                                   #
#       1. Dictionary of coins stats                                          #
###############################################################################
def get_individual_coin_data(conversion, coin):
    coinDict = {}
    id = coin['id']
    name = coin['name']
    symbol = coin['symbol']
    slug = coin['slug']
    circulating_supply = coin['circulating_supply']
    total_supply = coin['total_supply']
    max_supply = coin['max_supply']
    date_added = coin['date_added']
    num_market_pairs = coin['num_market_pairs']
    tags = coin['tags']
    platform = coin['platform']
    rank = coin['cmc_rank']
    current_price = coin['quote'][conversion]['price']
    volume_24h = coin['quote'][conversion]['volume_24h']
    percent_change_1h = coin['quote'][conversion]['percent_change_1h']
    percent_change_24h = coin['quote'][conversion]['percent_change_24h']
    percent_change_7d = coin['quote'][conversion]['percent_change_7d']
    market_cap = coin['quote'][conversion]['market_cap']
    last_updated = coin['quote'][conversion]['last_updated']
    coinDict.update({'id': id, 'name': name, 'symbol': symbol, 'slug': slug,
                     'circulating_supply': circulating_supply, 
                     'total_supply': total_supply, 'max_supply': max_supply,
                     'date_added': date_added, 
                     'num_market_pairs': num_market_pairs, 'tags': tags,
                     'platform': platform, 'rank': rank,
                     'current_price': current_price, 'volume_24h': volume_24h,
                     'percent_change_1h': percent_change_1h,
                     'percent_change_24h': percent_change_24h,
                     'percent_change_7d': percent_change_7d,
                     'market_cap': market_cap,
                     'last_updated': last_updated
                     })
    return coinDict


###############################################################################
#                           update_coin_database()                            #
###############################################################################
#   Purpose:                                                                  #
#       1. Will add data collected in collectCoinData.py to database          #
#   Inputs:                                                                   #
#       1. Coin data from collectCoinData.py                                  #
#       2. Conversion type (USD, EURO, Ect.)                                  #
###############################################################################
def update_coin_database(coinData, conversion):
    if coinData is None:
        coinData, conversion = collectCoinData.main()
    for coin in coinData:
        coinDict = get_individual_coin_data(conversion, coin)
        #Make sure the coin is already in the database
        query = """MERGE (c:Coin{name:'""" + coinDict['name'] + """'}) RETURN c"""
        run_query(query)
        
        print('Rank:', coinDict['rank'], '|',
              'Name:', coinDict['name'], '|',
              'Price:', coinDict['current_price'], '|',
              'Circulating Supply:', coinDict['circulating_supply'], '|',
              'Volume(24h):', coinDict['volume_24h'], '|',
              'Percent Change(1h):', coinDict['percent_change_1h'], '|',
              'Percent Change(24h):', coinDict['percent_change_24h'], '|',
              'Market Cap:', coinDict['market_cap'], '|',
              'Last Updated:', coinDict['last_updated']
             )
        query = """MERGE (c:Coin{name:'""" + coinDict['name'] + """'}), MERGE(a:Analysis)"""
    return


def main():
    update_coin_database(None, None)
    return 


if __name__ == "__main__":
    main()