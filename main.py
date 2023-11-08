# get AI21_API_KEY. Use https://studio.ai21.com/account/account
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import AlephAlpha
from dotenv import load_dotenv
import os

# Load the environment variables from the .env file
load_dotenv()

API_KEY = os.getenv('API_KEY')

template = """Q: {question}

A:"""

prompt = PromptTemplate(template=template, input_variables=["question"])

llm = AlephAlpha(
    model="luminous-extended",
    maximum_tokens=20,
    stop_sequences=["Q:"],
    aleph_alpha_api_key=API_KEY,
)

llm_chain = LLMChain(prompt=prompt, llm=llm)
question = "What is AI?"
output = llm_chain.run(question)

print(output)
