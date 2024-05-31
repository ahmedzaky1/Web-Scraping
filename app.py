import streamlit as st
from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI
from crewai_tools import ScrapeWebsiteTool
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
api_key = os.getenv('API_KEY')
Model = 'gpt-3.5-turbo'
llm = ChatOpenAI(model=Model, api_key=api_key)

def scrape_website(url):
    web_scrape_tool = ScrapeWebsiteTool(website_url=url)
    web_scraper_agent = Agent(
        role='Web Scraper',
        goal='Effectively Scrape data on the websites for your company',
        backstory='''You are expert web scraper, your job is to scrape all the data for 
                    your company from a given website.
                    ''',
        tools=[web_scrape_tool],
        verbose=True,
        llm=llm
    )

    web_scraper_task = Task(
        description='Scrape all the data on the site so your company can use for decision making.',
        expected_output='All the content of the website.',
        agent=web_scraper_agent,
        output_file='data.txt'
    )

    crew = Crew(
        agents=[web_scraper_agent],
        tasks=[web_scraper_task],
        verbose=2,
    )

    result = crew.kickoff()
    return result

st.title('Web Scraping and Summarization with OpenAI')

url = st.text_input('Enter the URL to scrape')
if st.button('Scrape and Summarize'):
    with st.spinner('Scraping the website...'):
        result = scrape_website(url)
        st.success('Scraping completed!')

    st.subheader('Scraped Data')
    st.write(result)
