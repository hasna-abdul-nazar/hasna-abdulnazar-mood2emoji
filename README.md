# Kid-safe Text-Mood Detector

A simple web app built with Streamlit and TextBlob that analyzes the mood of a short sentence and returns a kid-friendly emoji with a one-line explanation. Suitable for students aged 12–16.

## What the Project Does

This app takes user input (a short sentence), checks for inappropriate language, analyzes the sentiment using TextBlob, and outputs an emoji (😀 for happy, 😐 for neutral, 😞 for sad) along with a brief explanation. It includes a "Teacher Mode" to show a simple diagram of how the app works.

Kids learn about:
- Basic programming concepts like input/output and conditionals.
- Introduction to natural language processing (sentiment analysis).
- Importance of safety and appropriateness in digital tools.

## Setup and Run Instructions

1. Ensure you have Python 3.9+ installed.
2. Clone or download this repository.
3. Navigate to the project directory: `cd mood2emoji`
4. Install dependencies: `pip install -r requirements.txt`
5. Run the app: `streamlit run app.py`
6. Open the provided local URL in your browser.

## How You'd Teach It in 60 Minutes

1. **Introduction (10 min):** Discuss emotions and how computers can "understand" text. Show examples of positive, negative, and neutral sentences.
2. **Demo (10 min):** Run the app and demonstrate input/output. Explain sentiment analysis simply.
3. **Code Walkthrough (20 min):** Go through app.py line-by-line, explaining functions like `get_mood_emoji` and safety checks.
4. **Hands-on Activity (15 min):** Have students modify the bad words list or add a new emoji. Test changes.
5. **Wrap-up (5 min):** Discuss real-world applications and ethics of AI.

## Known Limitations

- Uses basic TextBlob for sentiment; may not handle sarcasm or complex emotions accurately.
- Bad words filter is simple and hardcoded; not comprehensive.
- No advanced NLP models to keep it lightweight and kid-friendly.
- App is local-only; for sharing, deploy to Streamlit Cloud.

## Credits

- TextBlob for sentiment analysis.
- Streamlit for the web framework.
