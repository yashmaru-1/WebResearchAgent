import aiohttp
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()

class WebCrawler:
    async def crawl(self, urls):
        content = []
        for url in urls:
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(url, timeout=10) as res:
                        soup = BeautifulSoup(await res.text(), "lxml")
                        title = soup.find('h1') or soup.find('title')
                        paragraphs = soup.find_all('p')
                        text = " ".join([p.text for p in paragraphs])
                        content.append({"url": url, "title": title.text if title else "No title", "text": text})
            except Exception as e:
                content.append({"url": url, "text": f"Error fetching: {str(e)}"})
        return content
