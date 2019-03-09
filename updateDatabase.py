#This script will add the collected data to the database

#Import needed Scripts
from utilities import graph_connection, run_query



###############################################################################
#                          test_graph_connection():                           #
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


def main():
    test_graph_connection()
    return 
    
if __name__ == "__main__":
    main()