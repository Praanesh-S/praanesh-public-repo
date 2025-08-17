def build_prompt(text, language, style, tone):
    return f"""
Translate the following text into {language}, keeping the original meaning, but adjust the style to "{style}" and the tone to "{tone}".

Make sure to preserve idiomatic expressions where possible, and rewrite in a way that fits the target culture and voice.


Text:
\"\"\"{text}\"\"\"
"""