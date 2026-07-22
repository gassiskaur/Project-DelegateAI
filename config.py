#configuration file for project 

import os 
from dotenv import load_dotenv
from openai import OpenAI
from elevenlabs import ElevenLabs 

load_dotenv()

#read api keys  
OPENAI_API_KEY= os.getenv("OPENAI_API_KEY")
ELEVENLABS_API_KEY=os.getenv("ELEVENLABS_API_KEY")
ELEVANLABS_AGENT_ID=os.getenv("ELEVANLABS_AGENT_ID")
ELEVANLABS_PHONE_NUMBER_ID=os.getenv("ELEVANLABS_PHONE_NUMBER_ID")
MONGODB_USERNAME=os.getenv("MONGODB_USERNAME=")
MONGODB_PASSWORD= os.getenv("MONGODB_PASSWORD")
MONGODB_CLUSTER=os.getenv("MONGODB_CLUSTER")
MONGODB_URI=f"mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@{MONGODB_CLUSTER}"

# Initialize the Clients
openai_client = OpenAI(api_key=OPENAI_API_KEY)
elevenlabs_client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
