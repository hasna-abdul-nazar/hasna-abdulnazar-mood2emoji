import streamlit as st
from textblob import TextBlob

# Bad words list (basic, kid-safe filter)
BAD_WORDS = ["badword1", "badword2", "inappropriate"]  # Expand as needed

def is_safe_text(text):
    """Check if text contains bad words."""
    words = text.lower().split()
    return not any(word in BAD_WORDS for word in words)

def get_mood_emoji(text):
    """Analyze sentiment and return emoji and explanation."""
    if not is_safe_text(text):
        return "🛑", "Please use appropriate language!"

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    # Adjust for negation: if "not" precedes a negative word, boost polarity
    negative_words = ["tired", "sad", "bad", "angry", "upset", "sick", "hurt", "scared", "worried"]
    words = text.lower().split()
    for i, word in enumerate(words):
        if word == "not" and i + 1 < len(words) and words[i + 1] in negative_words:
            polarity += 0.4  # Boost polarity for "not negative"

    if polarity > 0.1:
        return "😀", "Sounds happy!"
    elif polarity < -0.1:
        return "😞", "Sounds sad!"
    else:
        return "😐", "Sounds neutral."

def main():
    # Custom CSS for kid-friendly styling with animations and floating emojis
    st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 50%, #fecfef 100%);
        color: #333;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        animation: backgroundShift 10s ease-in-out infinite;
        position: relative;
        overflow: hidden;
    }
    .main::before {
        content: '🌟 😊 🎈 🌈 🦄';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        font-size: 2em;
        opacity: 0.1;
        animation: float 20s linear infinite;
        pointer-events: none;
    }
    @keyframes float {
        0% { transform: translateY(100vh); }
        100% { transform: translateY(-100vh); }
    }
    @keyframes backgroundShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    .stTitle {
        color: #ff6b6b;
        font-size: 3em;
        text-align: center;
        text-shadow: 2px 2px #fff;
        animation: titleGlow 2s ease-in-out infinite alternate;
        position: relative;
        z-index: 1;
    }
    @keyframes titleGlow {
        from { text-shadow: 2px 2px #fff; }
        to { text-shadow: 2px 2px #fff, 0 0 10px #ff6b6b; }
    }
    .stTextInput > div > div > input {
        border: 3px solid #4ecdc4;
        border-radius: 20px;
        padding: 10px;
        font-size: 1.2em;
        background-color: #fff;
        transition: border-color 0.3s;
        position: relative;
        z-index: 1;
    }
    .stTextInput > div > div > input:focus {
        border-color: #ff6b6b;
        box-shadow: 0 0 5px #ff6b6b;
    }
    .stButton > button {
        background: linear-gradient(45deg, #ffeaa7, #fab1a0);
        color: #333;
        border: none;
        border-radius: 25px;
        padding: 10px 20px;
        font-size: 1.2em;
        font-weight: bold;
        box-shadow: 0 4px #ccc;
        transition: all 0.3s;
        position: relative;
        overflow: hidden;
        z-index: 1;
    }
    .stButton > button::before {
        content: '🔍';
        position: absolute;
        left: 10px;
        top: 50%;
        transform: translateY(-50%);
    }
    .stButton > button:hover {
        background: linear-gradient(45deg, #fab1a0, #ffeaa7);
        box-shadow: 0 6px #999;
        transform: translateY(-2px) scale(1.05);
    }
    .stCheckbox > div > div > label {
        font-size: 1.2em;
        color: #333;
        position: relative;
        z-index: 1;
    }
    .emoji-output {
        font-size: 4em;
        text-align: center;
        margin: 20px 0;
        animation: emojiBounce 1s ease-in-out;
        position: relative;
        z-index: 1;
    }
    @keyframes emojiBounce {
        0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
        40% { transform: translateY(-10px); }
        60% { transform: translateY(-5px); }
    }
    .explanation {
        font-size: 1.5em;
        text-align: center;
        color: #2d3436;
        background: rgba(255, 255, 255, 0.8);
        padding: 10px;
        border-radius: 15px;
        margin: 10px 0;
        animation: fadeIn 1s ease-in;
        position: relative;
        z-index: 1;
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    .teacher-mode {
        background: rgba(255, 255, 255, 0.9);
        padding: 15px;
        border-radius: 15px;
        border: 2px solid #74b9ff;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        position: relative;
        z-index: 1;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("🌈 Kid-safe Text-Mood Detector 🎈")
    st.write("✨ Share your feelings and discover the emoji! ✨")

    text_input = st.text_input("Your sentence:", placeholder="Type something fun here... 😊")
    submit = st.button("Detect Mood")

    if submit and text_input:
        emoji, explanation = get_mood_emoji(text_input)
        st.markdown(f'<div class="emoji-output">{emoji}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="explanation">{explanation}</div>', unsafe_allow_html=True)

    # Teacher Mode
    teacher_mode = st.checkbox("👩‍🏫 Teacher Mode")
    if teacher_mode:
        st.markdown('<div class="teacher-mode">', unsafe_allow_html=True)
        st.subheader("📚 How the App Works")
        st.code("""
Input Text -> Safety Check -> Sentiment Analysis -> Emoji Output
        """)
        st.write("This app uses TextBlob to analyze the sentiment (mood) of your text!")
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
