# import streamlit as st
# import requests

# BACKEND = "http://127.0.0.1:8000"

# st.title("🤖 Agentic RAG Chatbot (Bedrock Gemma)")

# # Upload PDF
# uploaded_file = st.file_uploader("Upload PDF", type="pdf")

# if uploaded_file:
#     files = {"file": uploaded_file.getvalue()}
#     requests.post(f"{BACKEND}/upload", files=files)
#     st.success("PDF uploaded successfully!")

# # Chat
# if "chat" not in st.session_state:
#     st.session_state.chat = []

# query = st.text_input("Ask something")

# if query:
#     res = requests.get(f"{BACKEND}/chat", params={"query": query})
#     answer = res.json()["response"]

#     st.session_state.chat.append((query, answer))

# # Display chat
# for q, a in st.session_state.chat:
#     st.write(f"**You:** {q}")
#     st.write(f"**Bot:** {a}")



import streamlit as st
import requests

BACKEND = "http://127.0.0.1:8000"

st.title("🤖 Agentic RAG Chatbot (Bedrock Gemma)")

# Upload PDF
uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file:
    files = {
        "file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")
    }

    try:
        res = requests.post(f"{BACKEND}/upload", files=files)

        print("UPLOAD RESPONSE:", res.text)

        if res.status_code == 200:
            st.success("PDF uploaded successfully!")
        else:
            st.error("Upload failed")
            st.text(res.text)

    except:
        st.error("⚠️ Backend not running!")

# Chat memory
if "chat" not in st.session_state:
    st.session_state.chat = []

query = st.text_input("Ask something")

if query:
    try:
        res = requests.get(f"{BACKEND}/chat", params={"query": query})

        print("RAW RESPONSE:", res.text)  # 👈 DEBUG

        if res.status_code != 200:
            st.error("❌ Backend error")
            st.text(res.text)
            answer = "Error"
        else:
            try:
                data = res.json()

                if "response" in data:
                    answer = data["response"]
                else:
                    answer = data.get("error", "Unknown error")

            except:
                st.error("⚠️ Invalid JSON from backend")
                st.text(res.text)
                answer = "Error parsing response"

        st.session_state.chat.append((query, answer))

    except:
        st.error("⚠️ Cannot connect to backend!")

# Display chat
for q, a in st.session_state.chat:
    st.write(f"**You:** {q}")
    st.write(f"**Bot:** {a}")