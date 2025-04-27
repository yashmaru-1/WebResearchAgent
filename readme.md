# Web Research Assistant

An intelligent web research agent that automatically searches, crawls, analyzes, and synthesizes information from the internet to generate a professional research report.

## Features

- Web search and crawling for latest articles
- News aggregation for trending topics
- Content analysis and extraction
- Research document synthesis
- Summarization using Gemini AI API
- Professional, complete research report generation
- Download research report as PDF
- Clean and simple Streamlit-based frontend

---

## Architecture Overview

```
[User Query]
    ↓
[Query Analyzer] → Determine intent (news or research)
    ↓
[Search Tool] OR [News Aggregator] → Fetch URLs
    ↓
[Web Crawler] → Extract full content from URLs
    ↓
[Content Analyzer] → Clean and structure raw content
    ↓
[Information Synthesizer] → Merge extracted data
    ↓
[Response Generator (Gemini AI)] → Analyze deeply and generate report
    ↓
[Streamlit Frontend] → Display Final Report + Download as PDF
```

---

## Project Structure

```
WEBRESEARCHAGENT/
├── agent/
│   ├── content_analyzer.py
│   ├── news_aggregator.py
│   ├── query_analyzer.py
│   ├── research_agent.py
│   ├── response_generator.py
│   ├── search_tool.py
│   ├── synthesizer.py
│   └── web_crawler.py
├── app/
│   └── frontend.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## How to Run Locally

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/smart-research-assistant.git
    cd smart-research-assistant
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables:
    - Create a `.env` file based on `.env.example`
    - Add your API keys:
      ```bash
      GEMINI_API_KEY=your_gemini_api_key
      SERPAPI_API_KEY=your_serpapi_api_key
      ```

4. Run the application:
    ```bash
    streamlit run app/frontend.py
    ```

5. Open your browser and enjoy the Smart Research Assistant.

---

## Tech Stack

- Python 3.9+
- Streamlit
- SerpApi
- Google Gemini API
- aiohttp
- BeautifulSoup
- fpdf

---

## License

This project is licensed for educational and assignment purposes only.

---

## Credits

Yash Maru