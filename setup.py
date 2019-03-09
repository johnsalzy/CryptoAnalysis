import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

api_key = os.environ.get("API_KEY")
graphene_host = os.environ.get("GRAPHENE_HOST")
graphene_bolt = os.environ.get("GRAPHENE_BOLT")
graphene_user = os.environ.get("GRAPHENE_USER")
graphene_pass = os.environ.get("GRAPHENE_PASS")