from fastapi import FastAPI
import logging

from langchain import GoogleSearchAPIWrapper
from langchain.chat_models import ChatOpenAI

from gen_ideas import generate_ideas, get_links

app = FastAPI()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

llm = ChatOpenAI(model_name="gpt-3.5-turbo")
search = GoogleSearchAPIWrapper()

@app.get("/")
def healthcheck():
    return {"Status": "OK"}

@app.get("/giftideas/{query}")
async def get_gift_ideas(query: str):
    gift_ideas = generate_ideas(llm, query)
    item_links = [get_links(llm, search, idea) for idea in gift_ideas]

    response = {
        "ideas": [
            {
                "idea": idea,
                "items": details
            } for idea, details in zip(gift_ideas, item_links)
        ]
    }

    return response
