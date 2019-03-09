from neo4j.v1 import GraphDatabase, basic_auth
#Go up a directory to import setup.py file
import setup

username = setup.graphene_user
password = setup.graphene_pass
db_host = setup.graphene_host
db_bolt = setup.graphene_bolt


def graph_connection():
    """
    Will establish a connection with the Neo4j graph database
    Database hosted though grapheneDB
    """
    driver = GraphDatabase.driver(db_bolt, auth=basic_auth(username, password))
    return driver


def run_query(query):
    """
    Purpose:
        Will run a query on through the bolt connection of the graph
    Input:
        One query
    Output:
        Response to query(if any)
    """
    driver = GraphDatabase.driver(db_bolt, auth=basic_auth(username, password))
    session = driver.session()
    result = session.run(query)
    session.close()
    return result