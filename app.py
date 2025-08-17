import gradio as gr
import os
from translator import translate_text

# Make sure API key is read from environment variable set in Hugging Face Secrets
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

def run_translation(input_text, target_language, style, tone):
    if not input_text.strip():
        return "Please enter some text."
    try:
        return translate_text(input_text, target_language, style, tone)
    except Exception as e:
        return f"Error: {str(e)}"

with gr.Blocks(title="🌍 Hackathon Translator") as demo:
    gr.Markdown("# 🌍 Multilingual Stylistic Translator")
    gr.Markdown("Translate text into another language with your chosen style and tone.")

    with gr.Row():
        input_text = gr.Textbox(label="Input Text", lines=4, placeholder="Enter text here...")

    with gr.Row():
        target_language = gr.Textbox(label="Target Language (e.g., Spanish, French)")

    with gr.Row():
        style = gr.Dropdown(choices=["formal", "casual", "poetic", "sarcastic"], value="formal", label="Style")
        tone = gr.Dropdown(choices=["neutral", "friendly", "serious", "humorous"], value="neutral", label="Tone")

    output_text = gr.Textbox(label="Translated Text", lines=4)

    translate_btn = gr.Button("Translate")
    translate_btn.click(fn=run_translation, inputs=[input_text, target_language, style, tone], outputs=output_text)

demo.launch()


