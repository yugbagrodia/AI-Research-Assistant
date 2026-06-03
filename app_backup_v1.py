import streamlit as st
from pypdf import PdfReader
import os
from dotenv import load_dotenv
import google.generativeai as genai

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="📚",
    layout="wide"
)

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

with st.sidebar:

    st.title("📚 AI Research Assistant")

    st.markdown("---")

    st.write(
        "Upload research papers and analyze them using Gemini AI."
    )

    st.markdown("---")

    st.subheader("Features")

    st.write("✅ Summary")
    st.write("✅ Contributions")
    st.write("✅ Limitations")
    st.write("✅ Future Work")
    st.write("✅ Paper Chat")

if "analysis" not in st.session_state:
    st.session_state.analysis = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "paper_text" not in st.session_state:
    st.session_state.paper_text = ""


def extract_section(text, start, end=None):

    try:
        start_index = text.index(start) + len(start)

        if end:
            end_index = text.index(end)
            return text[start_index:end_index].strip()

        return text[start_index:].strip()

    except ValueError:
        return "Section not found."


st.title("📚 AI Research Assistant")

st.markdown(
    """
    Analyze research papers using Gemini AI.
    
    Generate:
    - Summary
    - Key Contributions
    - Limitations
    - Future Work
    - Interactive Q&A
    """
)

st.caption(
    "Upload research papers, generate insights, and chat with the paper."
)

uploaded_file = st.file_uploader(
    "Upload a Research Paper",
    type=["pdf"]
)

if uploaded_file:

    st.success("PDF uploaded successfully!")

    st.write("File Name:", uploaded_file.name)
    st.write("File Size:", uploaded_file.size, "bytes")

    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text

    st.session_state.paper_text = text

    st.write("Total Pages:", len(reader.pages))
    st.write("Total Characters Extracted:", len(text))

    st.subheader("Preview")
    st.write(text[:500])

    model = genai.GenerativeModel("gemini-2.5-flash")

    if st.button("Generate Analysis"):

        with st.spinner("Analyzing paper..."):

            response = model.generate_content(
                f"""
                Analyze the following research paper.

                Return your response in the exact format:

                SUMMARY:
                <summary>

                KEY CONTRIBUTIONS:
                <bullet points>

                LIMITATIONS:
                <bullet points>

                FUTURE WORK:
                <bullet points>

                Paper:

                {text[:10000]}
                """
            )

            st.session_state.analysis = response.text

if st.session_state.analysis:

    analysis = st.session_state.analysis

    summary = extract_section(
        analysis,
        "SUMMARY:",
        "KEY CONTRIBUTIONS:"
    )

    contributions = extract_section(
        analysis,
        "KEY CONTRIBUTIONS:",
        "LIMITATIONS:"
    )

    limitations = extract_section(
        analysis,
        "LIMITATIONS:",
        "FUTURE WORK:"
    )

    future_work = extract_section(
        analysis,
        "FUTURE WORK:"
    )

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "Summary",
            "Contributions",
            "Limitations",
            "Future Work"
        ]
    )

    with tab1:
        st.write(summary)

    with tab2:
        st.write(contributions)

    with tab3:
        st.write(limitations)

    with tab4:
        st.write(future_work)

    st.divider()

    st.subheader("Ask Questions About This Paper")

    question = st.text_input(
        "Enter your question"
    )

    if st.button("Ask Question"):

        with st.spinner("Thinking..."):

            model = genai.GenerativeModel("gemini-2.5-flash")

            response = model.generate_content(
                f"""
                You are helping a student understand a research paper.

                Research Paper:

                {st.session_state.paper_text[:10000]}

                Question:

                {question}

                Answer clearly and accurately.
                """
            )

            st.session_state.chat_history.append(
                {
                    "question": question,
                    "answer": response.text
                }
            )

    if st.session_state.chat_history:

        st.subheader("Conversation")

        for chat in reversed(st.session_state.chat_history):

            st.markdown(
                f"**Question:** {chat['question']}"
            )

            st.markdown(
                f"**Answer:** {chat['answer']}"
            )

            st.divider()