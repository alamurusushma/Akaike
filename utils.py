import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from gtts import gTTS
import os

def extract_bing_news(company_name):
    """Scrapes Bing News search results."""
    search_url = f"https://www.bing.com/news/search?q={company_name}"
    response = requests.get(search_url, headers={'User-Agent': 'Mozilla/5.0'})

    if response.status_code != 200:
        print(f"Bing News fetch failed: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    articles = []

    for item in soup.find_all("a", {"class": "title"}, limit=5):
        title = item.text.strip()
        news_url = item["href"]
        summary = extract_summary(news_url)

        articles.append({
            "title": title,
            "summary": summary,
            "sentiment": analyze_sentiment(summary),
            "topics": extract_topics(summary),
            "url": news_url
        })

    return articles

def extract_summary(news_url):
    """Extracts a summary from the news article."""
    try:
        response = requests.get(news_url, headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code != 200:
            return "No summary available"

        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        summary = " ".join(p.text.strip() for p in paragraphs[:3])
        return summary if summary else "No summary available"
    except Exception as e:
        return "Error extracting summary"

def analyze_sentiment(text):
    """Analyzes the sentiment of the text."""
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

def extract_topics(text):
    """Extracts simple topics from the text."""
    words = text.split()
    return list(set(words[:5]))  # Simple topic extraction using first few words

def text_to_speech(text, filename="output.mp3"):
    """Converts text to speech in Hindi and saves it as an MP3 file."""
    try:
        tts = gTTS(text=text, lang="hi")  # Set language to Hindi
        tts.save(filename)
        return filename
    except Exception as e:
        print("Error generating speech:", e)
        return None