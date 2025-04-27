class ResearchAgent:
    def __init__(self, search_tool, query_analyzer, content_analyzer, synthesizer, web_crawler, news_aggregator, response_generator):
        self.search_tool = search_tool
        self.query_analyzer = query_analyzer
        self.content_analyzer = content_analyzer
        self.synthesizer = synthesizer
        self.web_crawler = web_crawler
        self.news_aggregator = news_aggregator
        self.response_generator = response_generator

    async def process_query(self, query):
        intent, keywords = self.query_analyzer.analyze(query)

        if intent == 'news':
            news_results = await self.news_aggregator.fetch_news(query)
            urls = [item["url"] for item in news_results if item["url"]]
        else:
            search_results = self.search_tool.search(query)
            urls = [result["link"] for result in search_results if "link" in result]

        if not urls:
            return "No search results found.", []

        crawled_data = await self.web_crawler.crawl(urls)
        analyzed_content = self.content_analyzer.analyze(crawled_data)
        research_document = self.prepare_research_document(analyzed_content)
        final_summary = self.response_generator.summarize_with_gemini(research_document)

        return final_summary, urls

    def prepare_research_document(self, analyzed_content):
        document = "Research Document\n\n"
        for idx, item in enumerate(analyzed_content, start=1):
            document += f"Section {idx} - Source: {item['url']}\n"
            document += f"{item['summary']}\n\n"
        return document
