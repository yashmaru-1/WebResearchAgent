import sys
import os
import asyncio
import streamlit as st
from dotenv import load_dotenv



sys.path.append(os.path.join(os.path.dirname(__file__), '../agent'))

from research_agent import ResearchAgent
from web_crawler import WebCrawler
from query_analyzer import QueryAnalyzer
from search_tool import SearchTool
from content_analyzer import ContentAnalyzer
from synthesizer import InformationSynthesizer
from news_aggregator import NewsAggregator
from response_generator import ResponseGenerator

load_dotenv()

search_tool = SearchTool()
query_analyzer = QueryAnalyzer()
content_analyzer = ContentAnalyzer()
synthesizer = InformationSynthesizer()
web_crawler = WebCrawler()
news_aggregator = NewsAggregator()
response_generator = ResponseGenerator()

agent = ResearchAgent(
    search_tool=search_tool,
    query_analyzer=query_analyzer,
    content_analyzer=content_analyzer,
    synthesizer=synthesizer,
    web_crawler=web_crawler,
    news_aggregator=news_aggregator,
    response_generator=response_generator
)

st.set_page_config(page_title="Smart Research Assistant", page_icon="🧠", layout="wide")

st.markdown("""
    <div style="text-align: center;">
        <h1>Smart Research Assistant</h1>
        <p style="font-size:18px; color: #6c757d;">Generate complete professional research reports instantly</p>
    </div>
""", unsafe_allow_html=True)

st.divider()

query = st.text_input(
    "Enter your research topic",
    placeholder="e.g., Impact of AI on education, Gujarat latest news",
    key="query_input"
)



def get_website_name(url):
    try:
        domain = url.split("//")[-1].split("/")[0].replace("www.", "")
        name = domain.split(".")[0]
        return name.capitalize()
    except:
        return "Website"

if query:
    with st.spinner("Researching and generating report..."):
        try:
            result = asyncio.run(agent.process_query(query))
            if isinstance(result, tuple) and len(result) == 2:
                summary, sources = result
                st.success("Research completed")

                col1, col2 = st.columns((2, 1))
                with col1:
                    st.subheader("Research Report")
                    st.markdown(summary)
                with col2:
                    st.subheader("Sources")
                    if sources:
                        for link in sources:
                            site_name = get_website_name(link)
                            st.markdown(f"[{site_name}]({link})", unsafe_allow_html=True)
                    else:
                        st.info("No sources found.")

                
            else:
                st.error("Unexpected backend output format.")
        except Exception as e:
            st.error(f"Error occurred: {str(e)}")
else:
    st.info("Enter a research topic to start.")
