import json
import spacy
import streamlit as st

# Load spaCy model with word vectors
nlp = spacy.load("en_core_web_md")

# Load FAQs
with open("faq.json") as f:
    faqs = json.load(f)["faqs"]

def get_response(user_input):
    user_input = user_input.lower()  # Convert user input to lowercase
    doc = nlp(user_input)
    # This threshold 
    highest_similarity = 0.8
    best_response = "I'm sorry, I cannot answer this question."

    # print("similarity")
    for faq in faqs:
        faq_question = faq["question"].lower()  # Convert FAQ question to lowercase
        faq_doc = nlp(faq_question)
        similarity = doc.similarity(faq_doc)
        # print(similarity)
        if similarity > highest_similarity:
            highest_similarity = similarity
            best_response = faq["answer"]

    return best_response

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'processing' not in st.session_state:
    st.session_state.processing = False

# Streamlit app
st.title("Customer Support Chatbot")
multi = '''
Here are some topics you can ask about:
- Return policy
- Order tracking
- Shipping information
- Payment methods
- Customer support

'''

with st.expander("**Hi, ask me anything related to our policies and services!**"):
    st.markdown(multi)

# Display chat history
st.subheader("Chat History")
chat_container = st.container()

# Create a form to handle user input
with st.form(key='chat_form', clear_on_submit=True):
    user_input = st.text_input("You:")
    submit_button = st.form_submit_button(label='Send')

# Handle user input from text box
if submit_button and user_input and not st.session_state.processing:
    st.session_state.processing = True
    with st.spinner('Processing...'):
        response = get_response(user_input)
        # Append user query and response to chat history
        st.session_state.chat_history.append(f"You: {user_input}")
        st.session_state.chat_history.append(f"Bot: {response}")
    st.session_state.processing = False

st.write("Frequently Asked Questions:")
faq_buttons = [st.button(faq['question'], key=f"faq_{i}") for i, faq in enumerate(faqs[:5])]

# Checking if any FAQ button is clicked
for i, faq_button in enumerate(faq_buttons):
    if faq_button and not st.session_state.processing:
        st.session_state.processing = True
        user_input = faqs[i]['question']
        with st.spinner('Processing...'):
            response = get_response(user_input)
            # Appending user query and response to chat history
            st.session_state.chat_history.append(f"You: {user_input}")
            st.session_state.chat_history.append(f"Bot: {response}")
        st.session_state.processing = False


# Display chat history in the container
with chat_container:
    # Display chat history
    for chat in st.session_state.chat_history:
        st.write(chat)
    # for role, message in st.session_state.chat_history:
    #     if role == "You":
    #         st.markdown(f"**You:** {message}")
    #     else:
    #         st.markdown(f"**Bot:** {message}")

# Automatically scroll to the bottom of the chat
st.markdown('<script>window.scrollTo(0,document.body.scrollHeight);</script>', unsafe_allow_html=True)