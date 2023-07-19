import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader

"""

"""
def get_pdf_text(pdf_docs):
  text = ""
  for pdf in pdf_docs:
    pdf_reader = PdfReader(pdf)
    #extracts raw text
    for page in pdf_reader.pages:
      text += page.extract_text()
  return text


def get_text_chunks(text):
  pass

def main():
  #load api keys
  load_dotenv()
  #basic configuration of the page
  st.set_page_config(page_title="Chat with multiple PDFs", page_icon=":books:")
  st.header("Chat with multiple PDFs :books:")
  st.text_input("Ask a question about your documents:")

  #create sidebar to upload files
  with st.sidebar:
    st.subheader("Your documents")
    pdf_docs = st.file_uploader("Upload your PDFs here and press on Process", accept_multiple_files=True)
    if st.button("Process"):
      with st.spinner("Processing"):
        raw_text = get_pdf_text(pdf_docs)
        st.write(raw_text)
        

if __name__ == '__main__':
  main()