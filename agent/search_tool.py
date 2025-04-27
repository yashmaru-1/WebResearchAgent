from serpapi import GoogleSearch
import os
from dotenv import load_dotenv

load_dotenv()

class SearchTool:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("SERPAPI_API_KEY")
    
    def search(self, query):
        search = GoogleSearch({
            "q": query,
            "api_key": self.api_key
        })
        results = search.get_dict()
        return results.get("organic_results", [])
