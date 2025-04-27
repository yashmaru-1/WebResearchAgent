import os
import requests
import re
from dotenv import load_dotenv

load_dotenv()

class ResponseGenerator:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        self.model = "gemini-2.0-flash"
        self.endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model}:generateContent"
    
    def clean_and_deduplicate_summary(self, text):
        sentences = re.split(r'(?<=[.!?]) +', text)
        sentences = [s for s in sentences if not re.search(r'https?://\S+|\[\d+\]', s)]
        seen = set()
        unique_sentences = []
        for sentence in sentences:
            cleaned = sentence.strip()
            if cleaned.lower() not in seen and cleaned:
                unique_sentences.append(cleaned)
                seen.add(cleaned.lower())
        return ' '.join(unique_sentences)
   
    def summarize_with_gemini(self, text):
        if not text.strip():
            return "No content to summarize."

        prompt = (
            "You are a world-class professional research agent. "
            "Analyze the provided research content. "
            "Extract all important facts, organize them clearly, and present a complete professional research report.\n\n"
            f"{text}"
        )

        payload = {
            "contents": [{"parts": [{"text": prompt}]}]
        }

        params = {"key": self.api_key}
        response = requests.post(self.endpoint, params=params, json=payload)

        if response.status_code == 200:
            result = response.json()
            raw_summary = result["candidates"][0]["content"]["parts"][0]["text"]
            cleaned_summary = self.clean_and_deduplicate_summary(raw_summary)
            return cleaned_summary
        else:
            return f"Error from Gemini API: {response.text}"

    def generate(self, synthesized_data):
        return synthesized_data
