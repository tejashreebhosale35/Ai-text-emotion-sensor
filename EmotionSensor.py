import os
import json
import streamlit as st
import pandas as pd
import plotly.express as px
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

# 1. Page Layout & Authentication Setup
st.set_page_config(page_title="AI Emotion Sensor", page_icon="🧠", layout="centered")
st.title("🧠 AI Text Emotion Sensor")
st.write("Analyze sentences or paragraphs to detect emotional distribution using advanced LLMs.")

load_dotenv("SecretKey.env")

if "GROQ_API_KEY" not in os.environ:
    st.error("🔑 GROQ_API_KEY is missing from SecretKey.env!")
    st.stop()

# 2. Initialize Low-Temperature ChatGroq Client for Stable Parsing
llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.1)

# 3. Create Strict Structured Prompt Template
emotion_prompt = PromptTemplate.from_template(
    "You are an expert sentiment analyzer and psychologist. Analyze the primary emotions in the text provided.\n\n"
    "Text to analyze: \"{text}\"\n\n"
    "Instructions:\n"
    "1. Evaluate the intensity score for these 6 core emotions: Joy, Anger, Sadness, Fear, Surprise, Love.\n"
    "2. Each emotion must be given a value from 0 to 100 representing its intensity in the text.\n"
    "3. Provide a brief 1-2 sentence overall psychological analysis explanation summarizing the dominant mood.\n"
    "4. Return the response strictly as a valid, raw JSON object with no markdown text wrapping or formatting. Use this precise layout:\n"
    "{{\n"
    "  \"scores\": {{\n"
    "    \"Joy\": 0,\n"
    "    \"Anger\": 0,\n"
    "    \"Sadness\": 0,\n"
    "    \"Fear\": 0,\n"
    "    \"Surprise\": 0,\n"
    "    \"Love\": 0\n"
    "  }},\n"
    "  \"dominant_emotion\": \"Emotion Name\",\n"
    "  \"explanation\": \"Your text analysis summary here.\"\n"
    "}}\n"
    "JSON Output:"
)

chain_emotion = emotion_prompt | llm | StrOutputParser()

# 4. User Interface Inputs
user_text = st.text_area(
    "Type or paste your text here:",
    placeholder="e.g., I just found out I passed my programming exam! I can't believe it, I'm so relieved but still shocked!",
    height=150
)

# Visual mapping dictionary for aesthetic accents
emotion_emojis = {
    "Joy": "😊 Joy",
    "Anger": "😡 Anger",
    "Sadness": "😢 Sadness",
    "Fear": "😨 Fear",
    "Surprise": "😲 Surprise",
    "Love": "❤️ Love"
}

if st.button("Analyze Emotion Profile 🚀", type="primary"):
    if not user_text.strip():
        st.warning("Please enter some text to analyze first!")
    else:
        with st.spinner("Decoding underlying emotional variables..."):
            try:
                # Step A: Run AI evaluation chain
                raw_response = chain_emotion.invoke({"text": user_text})
                
                # Sanitize response string to protect JSON conversions
                clean_json_str = raw_response.strip('"` \n\r\t')
                data = json.loads(clean_json_str)
                
                # Step B: Extract response fields
                scores = data["scores"]
                dominant = data["dominant_emotion"]
                explanation = data["explanation"]
                
                st.success("Analysis Complete!")
                
                # Step C: Render Layout Blocks
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("📊 Emotion Breakdown")
                    # Structure dictionary into a Pandas DataFrame for chart plotting
                    df = pd.DataFrame({
                        "Emotion": list(scores.keys()),
                        "Intensity (%)": list(scores.values())
                    })
                    
                    # Generate a beautiful, interactive horizontal bar graph via Plotly Express
                    fig = px.bar(
                        df, 
                        x="Intensity (%)", 
                        y="Emotion", 
                        orientation="h",
                        color="Intensity (%)",
                        color_continuous_scale="Viridis",
                        range_x=[0, 100]
                    )
                    fig.update_layout(showlegend=False, height=300, margin=dict(l=0, r=0, t=10, b=10))
                    st.plotly_chart(fig, use_container_width=True)

                with col2:
                    st.subheader("💡 Sensor Summary")
                    # Dynamically append emoji badge for visual pop
                    emoji_badge = emotion_emojis.get(dominant, dominant)
                    
                    st.markdown(f"**Dominant Emotion:** `{emoji_badge}`")
                    st.info(f"**Psychological Insight:**\n{explanation}")
                    
            except Exception as e:
                st.error(f"Failed to process analysis. The framework returned an unparseable payload.")
                with st.expander("Debug Details"):
                    st.write(e)
