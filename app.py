import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

# Load model and tokenizer
model_name = "cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Create pipeline
classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

# Label mapping
label_map = {
    "LABEL_0": "Negative",
    "LABEL_1": "Neutral",
    "LABEL_2": "Positive"
}

# Streamlit UI
st.set_page_config(page_title="Sentiment Analyzer", layout="centered")
st.title("🧠 Sentiment Analyzer with BERT")
st.markdown("Enter any sentence and find out if it's **Positive**, **Negative**, or **Neutral**!")

text_input = st.text_area("Enter text:", "")

if st.button("Analyze"):
    if text_input.strip() == "":
        st.warning("Please enter some text to analyze.")
    else:
        with st.spinner("Analyzing..."):
            result = classifier(text_input)[0]
            label = label_map[result["label"]]
            score = round(result["score"] * 100, 2)

        st.success(f"**Sentiment:** {label}")
        st.info(f"**Confidence:** {score} %")
