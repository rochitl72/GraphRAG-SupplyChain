from langchain_huggingface import HuggingFaceEndpoint
import os


from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from arango import ArangoClient

# 🔹 Set up ArangoDB Connection
ARANGO_URL = "http://localhost:8529"
USERNAME = "root"
PASSWORD = "openSesame"
DB_NAME = "supply_chain_db"

client = ArangoClient(hosts=ARANGO_URL)
db = client.db(DB_NAME, username=USERNAME, password=PASSWORD)

# 🔹 Set up OpenAI API for AI-Powered Queries
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"  # 🔴 Replace with your actual API Key
import os
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

llm = HuggingFaceEndpoint(
    endpoint_url="https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct",
    max_new_tokens=256,
    temperature=0.7
)




# 🔹 Prompt Template for AI Queries
template = PromptTemplate(
    input_variables=["query"],
    template="Analyze the supply chain database and answer: {query}"
)

chain = LLMChain(llm=llm, prompt=template)

# 🔹 Function to Query the Supply Chain Graph
def query_graph(user_query):
    # Convert user query into an AQL (ArangoDB Query)
    if "suppliers of" in user_query.lower():
        company = user_query.split("suppliers of")[-1].strip()
        aql_query = f"""
        FOR v, e IN 1..1 ANY 'nodes/{company}' GRAPH 'supply_chain_graph'
        RETURN v
        """
    else:
        aql_query = "FOR n IN nodes RETURN n"

    # Execute AQL Query
    cursor = db.aql.execute(aql_query)
    results = [doc for doc in cursor]

    # Pass Results to AI for Analysis
    ai_response = chain.run(query=user_query)
    
    return {"query_result": results, "ai_analysis": ai_response}

# 🔹 Run Example Query
if __name__ == "__main__":
    user_input = input("Enter your supply chain query: ")
    response = query_graph(user_input)
    print("🔍 Query Result:", response["query_result"])
    print("🧠 AI Analysis:", response["ai_analysis"])
