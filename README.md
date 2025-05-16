# 🧠 Sentiment Analysis with BERT (Streamlit Application)

## 📌 Project Overview

This **Sentiment Analysis with BERT** project is a web application built using **Streamlit** and **Hugging Face Transformers**. It allows users to analyze the sentiment of any given text using a pre-trained BERT model.

## 🚀 Features

* User-friendly interface for sentiment analysis.
* Real-time sentiment prediction using a pre-trained BERT model (Twitter-RoBERTa).
* Classification into three sentiment categories:

  * **Positive**
  * **Negative**
  * **Neutral**
* Display of confidence score for predictions.

## 💡 Technologies Used

* **Frontend:** Streamlit (Python)
* **Natural Language Processing:** Hugging Face Transformers, BERT (Twitter-RoBERTa Model)
* **Model:** cardiffnlp/twitter-roberta-base-sentiment

## ⚡ Project Structure

* `app.py`: Main Streamlit application file.

## 💡 How to Run the Project

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/Sentiment-Analysis-BERT.git
   cd Sentiment-Analysis-BERT
   ```
2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Application:**

   ```bash
   streamlit run app.py
   ```

## 📚 Usage

* Enter any text in the input box.
* Click the **Analyze** button.
* View the predicted sentiment and confidence score.

## ⚡ How It Works

* The application uses a pre-trained BERT model (Twitter-RoBERTa) from Hugging Face.
* It classifies text into one of three categories: Positive, Negative, or Neutral.
* The confidence score shows the model's certainty for the prediction.
