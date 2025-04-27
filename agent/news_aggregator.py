from search_tool import SearchTool

class NewsAggregator:
    def __init__(self):
        self.search_tool = SearchTool()

    async def fetch_news(self, query):
        search_results = self.search_tool.search(query)
        news = [{"url": result.get("link", ""), "summary": result.get("title", "")} for result in search_results if "title" in result]
        return news
