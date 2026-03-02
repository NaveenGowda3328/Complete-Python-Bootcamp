import requests # pip install requests

query = "artificial intelligence"
api = "d8e05cc4a0464a5db399a0f99f242d3d"

url = f" https://newsapi.org/v2/everything?q={query}&from=2025-08-04&sortBy=popularity&apiKey={api}"

print(url)
c = requests.get(url)

#Error of code.