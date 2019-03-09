# CryptoAnalysis Project

### Table of Contents
**[Project Setup](#project-setup)**<br>


## Project Setup
1. Clone Project
2. First Set Up Account through [coinmarketcap](https://coinmarketcap.com/api/documentation/v1/#section/Introduction) to get API key
3. With the setup key obtained in step 1 of setup create a .env file and add key to it
```
API_KEY=09dsadaf2-9d31-412d-45b4-eadsf0bbd19
```
4. Installing Necessary Project Packages <br />
Optional: **[Installing and Using Virtualenv](#installing-and-using-virtualenv)**
5. Setup Database to store history **[Database Setup](#database-setup)**
6. Run test.py in your chosen shell to ensure setup was successful

### Installing and Using Virtualenv
-----------------------------------
If you just want to install packages...
```
pip install -r requirements.txt
```
This is optional, using virtualenv to isolate your development enviorment.
If you would like to skip this just install the packages in requirements.txt <br/>
See [Documentation](https://virtualenv.pypa.io/en/latest/) <br />
In your command prompt in root project folder...
```
pip install virtualenv
virtualenv venv
cd venv
cd scripts
activate
cd..
cd..
pip install -r requirements.txt
```

### Database Setup
------------------
This project utilizes a Neo4j Database Hosted through [GrapheneDB](https://www.graphenedb.com/)
1. Create an account
2. Create a graph
3. Create a user for the graph
4. Using the info from above steps add the following to you .env file
```
GRAPHENE_HOST=https://hobby-fldasjflsadjfdasfasdfdd.dbs.graphenedb.com:24780/db/data/cypher
GRAPHENE_BOLT=bolt://hobby-fldasjflsadjfdasfasdfdd.dbs.graphenedb.com:24786
GRAPHENE_USER=userNameFromCreatedUser
GRAPHENE_PASS=passwordFromCreatedUser
```
Host and Bolt are under the Connection Tab
