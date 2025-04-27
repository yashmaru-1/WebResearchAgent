class InformationSynthesizer:
    def synthesize(self, data):
        if not data:
            return "No content to synthesize."
        combined_info = "\n\n".join([f"From {item['url']}:\n{item['summary']}" for item in data])
        return combined_info
