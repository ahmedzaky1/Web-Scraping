# Web Scraping

creates a Streamlit web application that allows users to enter a URL. It then uses CrewAI and the OpenAI API to scrape data from the website and potentially summarize it (summarization logic might not be implemented yet). The scraped data is displayed in the app.

## Libs

- **streamlit** :: This library is used to create web applications in Python. It allows you to create interactive elements like text boxes and buttons.

- **crewai** :: This library is used to create a framework for building large language models (LLMs) and their interactions.

- **langchain_openai** :: This library provides an interface to interact with OpenAI's GPT-3 model through the Chat API.

- **crewai_tools** ::  This library (likely custom-made) offers tools for CrewAI, potentially including the ScrapeWebsiteTool class.

- **dotenv** ::  This library helps you load environment variables from a .env file.


## Steps Of Project.

#### 1) Activate Environment

```python
$ conda activate web-scraping
```

#### 2) Install Libs

```python
$ pip install -r requirements.txt
```

#### 3) Generate API KEY

```python
loads an API key from a .env file using load_dotenv and os.getenv.
```

#### 4) Running the application

```python
$ streamlit run app.py
```

#### 4) URL : https://www.ibm.com/topics/artificial-intelligence

