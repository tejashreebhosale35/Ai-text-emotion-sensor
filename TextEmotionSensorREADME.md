# 🧠 AI Text Emotion Sensor

An intelligent emotion analysis application built with Streamlit and Large Language Models (LLMs). The system analyzes user-provided text and generates an emotional profile by measuring the intensity of six core emotions: Joy, Anger, Sadness, Fear, Surprise, and Love.

The application provides visual emotion breakdowns, identifies the dominant emotion, and offers a brief psychological interpretation of the text.

## 🚀 Features

* Real-time emotion detection from text
* Analysis of six core emotions:

  * Joy 😊
  * Anger 😡
  * Sadness 😢
  * Fear 😨
  * Surprise 😲
  * Love ❤️
* Emotion intensity scoring (0–100%)
* Dominant emotion identification
* Psychological insight generation
* Interactive Plotly visualization
* Streamlit-based user interface
* Powered by Groq's LLM infrastructure

## 🛠️ Technology Stack

* Python
* Streamlit
* LangChain
* Groq API
* Plotly Express
* Pandas
* JSON
* python-dotenv

## 📂 Project Structure

AI-Text-Emotion-Sensor/

├── EmotionSensor.py

├── SecretKey.env

├── README.md

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/tejashreebhosale35/Ai-text-emotion-sensor.git

cd Ai-text-emotion-sensor
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure API Key

Create a file named:

```text
SecretKey.env
```

Add:

```env
GROQ_API_KEY=your_api_key_here
```

## ▶️ Running the Application

```bash
streamlit run app.py
```

The application will launch in your browser.

## 📊 How It Works

1. User enters text into the input box.
2. The text is sent to a Large Language Model through Groq.
3. The model evaluates six emotional dimensions.
4. A structured JSON response is generated.
5. The application:

   * Extracts emotion scores
   * Determines the dominant emotion
   * Produces a psychological interpretation
   * Displays an interactive chart

## 📈 Example Input

```text
I just found out I passed my programming exam! I can't believe it, I'm so relieved but still shocked!
```

## 📋 Example Output

```json
{
  "scores": {
    "Joy": 92,
    "Anger": 2,
    "Sadness": 1,
    "Fear": 15,
    "Surprise": 80,
    "Love": 20
  },
  "dominant_emotion": "Joy",
  "explanation": "The text reflects strong happiness and relief with a significant element of surprise. The overall emotional tone is highly positive and celebratory."
}
```

## 🎯 Applications

* Mental wellness monitoring
* Journaling analysis
* Customer feedback evaluation
* Educational projects
* Human-computer interaction research
* Emotion-aware chatbot systems

## 🔒 Disclaimer

This application provides AI-generated emotional interpretations and should not be considered a psychological diagnosis or professional mental health assessment. Results may vary depending on context and language complexity.

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

## 👨‍💻 Author

Your Name

Built with Streamlit, LangChain, Groq, and Plotly.
