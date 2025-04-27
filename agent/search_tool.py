import os
import requests
from dotenv import load_dotenv

load_dotenv()

class SearchTool:
    def __init__(self):
        self.api_key = os.getenv("SERP_API_KEY")
        self.base_url = "https://serpapi.com/search"

    def search(self, query):
        params = {
            "q": query,
            "api_key": self.api_key,
            "engine": "google"
        }
        response = requests.get(self.base_url, params=params)
        data = response.json()

        results = []
        if "organic_results" in data:
            for result in data["organic_results"]:
                results.append({
                    "title": result.get("title"),
                    "link": result.get("link"),
                    "snippet": result.get("snippet")
                })
        return results
