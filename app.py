import streamlit as st
import pickle

# Loading your trained model
model = pickle.load(open('model.pkl', 'rb'))


st.set_page_config(page_title="Spam Message Detector", page_icon="📧", layout="centered")

st.title("📧 Spam Message Detector")
st.markdown(
    """
    ### 🚀 Check if a message is **Spam** or **Not Spam**
    Enter a message in the text box below, and the app will predict whether it's spam!
    """
)

# Sidebar 
st.sidebar.title("About the App")
st.sidebar.info(
    """
    This application uses a **Machine Learning Model** to classify messages as:
    - **Spam** (e.g., promotional or malicious messages).
    - **Not Spam** (e.g., legitimate messages).
    
    The model was trained on a dataset of text messages using techniques like **TF-IDF** and **Random Forest Classifier**.
    """
)

# Input 
st.markdown("### Input Your Message Below:")
user_input = st.text_area("Type or paste your message here", height=150)

# make prediction
if st.button("🔍 Analyze Message"):
    if user_input.strip() != "":
       
        prediction = model.predict([user_input])[0]

        
        if prediction == "spam":  
            st.error("⚠️ This message is classified as **Spam**.")
            st.markdown("💡 **Tip**: Avoid interacting with spam messages and never click on suspicious links!")
        else:
            st.success("✅ This message is classified as **Not Spam**.")
            st.markdown("🛡️ **Good News**: This seems like a legitimate message.")

    else:
        st.warning("⚠️ Please enter a valid message to analyze.")

# Footer
st.markdown("---")
st.markdown(
    """
    #### 🤖 **App Features:**
    - **Real-time Predictions**: The app analyzes your message instantly.
    - **Interactive Design**: Clear results with helpful tips.
    - **Built Using**: [Streamlit](https://streamlit.io/) and Python.

    💡 *Have feedback or ideas for improvement? Feel free to share!*  
    """
)