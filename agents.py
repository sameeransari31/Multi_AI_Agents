from crewai import Agent
from tools import yt_tool
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()
groq_api_key = os.getenv('GROQ_API_KEY')
llm = ChatGroq(model_name="Llama3-8b-8192",groq_api_key = groq_api_key)

## create a senior blog content researcher 

blog_researcher = Agent(
    role = 'Blog Researcher from Youtube Videos',
    goal = 'get the relevant video transcription for the topic {topic} from the provided Yt channel',
    verbose = True,
    memory = True,
    llm = llm,
    allow_delegation = True,
    backstory = (
       "Expert in understanding videos in AI Data Science , MAchine Learning And GEN AI and providing suggestion" 
    ),
    tools = [yt_tool]
)


## creating a senior blog writer agent with YT tool


blog_writer = Agent(
    role = 'Blog Writer',
    goal = 'Narrate compelling tech stories about the video {topic} from YT video',
    verbose = True,
    memory = True,
    llm = llm,
    allow_delegation = False,
    backstory = (
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools = [yt_tool]
)
