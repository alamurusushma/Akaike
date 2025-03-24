import gradio as gr
from utils import extract_bing_news, text_to_speech, analyze_sentiment

def get_news(company_name):
    """Fetch news, perform analysis, and generate TTS"""
    articles = extract_bing_news(company_name)
    comparison = {"comparative_analysis": [analyze_sentiment(a["summary"]) for a in articles]} if articles else {}

    if articles:
        combined_text = " ".join([a["summary"] for a in articles if a["summary"]])
        audio_file = text_to_speech(combined_text) if combined_text.strip() else None
        return {"articles": articles, **comparison}, audio_file

    return {"error": "No news found for the given company."}, None

gradio_ui = gr.Interface(
    fn=get_news,
    inputs=gr.Textbox(label="Enter Company Name"),
    outputs=[gr.JSON(), gr.Audio()],
    title="News Analysis",
    description="Enter a company name and click 'Submit' to analyze news and sentiment.",
)

if __name__ == "__main__":
    gradio_ui.launch()