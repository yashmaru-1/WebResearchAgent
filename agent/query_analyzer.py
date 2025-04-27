class QueryAnalyzer:
    def analyze(self, query):
        keywords = query.lower().split()
        if "news" in keywords or "latest" in keywords:
            intent = "news"
        else:
            intent = "research"
        return intent, keywords
