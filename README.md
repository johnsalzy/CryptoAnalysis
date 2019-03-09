# CryptoAnalysis Project

### Table of Contents
**[Project Setup](#project-setup)**<br>


## Project Setup 
1. Clone Project
2. First Set Up Account API to get API key -https://coinmarketcap.com/api/documentation/v1/#section/Introduction
3. Install/Activate virtualenv **[Installing and Using Virtualenv](#venv-setup)**
4. With the setup key obtained in step 1 of setup create a .env file and add key to it
```
API_KEY=09dsadaf2-9d31-412d-45b4-eadsf0bbd19
```
6. Run test.py in your chosen shell to ensure that it works








### Installing and Using Virtualenv
-----------------------------------
This is optional, using virtualenv to isolate your development enviorment.
If you would like to skip this just install the packages in requirements.txt
See Documentation: https://virtualenv.pypa.io/en/latest/
In your command prompt in root project folder...
```
pip install virtualenv
virtualenv venv
cd venv
cd scripts
activate
cd..
cd..
pip install -r requirements.txt\
```
