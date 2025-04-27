class ContentAnalyzer:
    def analyze(self, crawled_data):
        analyzed = []
        for item in crawled_data:
            if 'text' in item and len(item['text']) > 100:
                analyzed.append({
                    "url": item['url'],
                    "summary": item['text']
                })
        return analyzed
