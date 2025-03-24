# Akaike
# News Analysis and Text-to-Speech App

This project fetches the latest news about a company from Bing News, analyzes the sentiment, extracts key topics, and converts the summary into speech (in english). The app is built using **Gradio** for the UI, **BeautifulSoup** for web scraping, **TextBlob** for sentiment analysis, and **gTTS** for text-to-speech.

## Features
- Fetches news articles from Bing News based on a company name.
- Extracts article summaries and performs sentiment analysis.
- Identifies key topics from the article text.
- Converts the summary to Hindi speech using gTTS.
- Displays results in a simple Gradio UI.

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/news-analysis-tts.git
   cd news-analysis-tts
