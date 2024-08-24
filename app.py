#fastapi
from fastapi import FastAPI
#langserv
import uvicorn
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langserve import add_routes
#essay prompt
e_prompt=ChatPromptTemplate.from_messages(
    [
        ("system","listen to user carefull"),("user","give me essay of 100 words on topic{topic}")
        ]
    )
#poem
p_prompt=ChatPromptTemplate.from_template(
    """
        write poem on 50 words on topic{topic}    
    """
)
model=Ollama(model="llama2")
app=FastAPI(server="langservr",version=1.0)
add_routes(
    app,
    e_prompt|model,
    path="/essay"
)
add_routes(
    app,
    p_prompt|model,
    path="/poem"
)
uvicorn.run(app,host="localhost",port=8000)
