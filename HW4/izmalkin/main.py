import streamlit as st

from transformers import pipeline

# Load the sentiment analysis model
pipe = pipeline('sentiment-analysis', model='nlptown/bert-base-multilingual-uncased-sentiment')

# Create the Streamlit application
def main():
    st.title("Sentiment Analysis")
    
    # Create a text input form
    text = st.text_input("Enter your text:", key="text_input")
    st.markdown(f'<style>div.stTextInput > div > div > input{{color: black !important;}}</style>', unsafe_allow_html=True)
    # Process the input text using the pipeline
    if st.button("Analyze"):
        result = pipe(text)
        
        # Display the sentiment analysis result
        st.markdown(f"<p style='font-weight: bold; color: white;'>Sentiment: {result[0]['label']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-weight: bold; color: white;'>Score: {result[0]['score']}</p>", unsafe_allow_html=True)


# Run the application
if __name__ == "__main__":
    main()
