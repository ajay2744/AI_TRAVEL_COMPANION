from app.clients.tavily import tavily

response = tavily.search(
    query="Mysore Palace history",
    max_results=3
)

print(response)