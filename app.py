import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

def getLlamaResponse(input_text, no_words):
    llm =CTransformers(model = 'models/llama-2-7b-chat.ggmlv3.q8_0.bin', model_type= 'llama', config= {'max_new_tokens': 256, 'temperature': 0.01})

    #Prompt Template
    template= """
        Write a blog on topic {input_text}
        within {no_words} words.

            """
    
    prompt = PromptTemplate(input_variables= [ "input_text", 'no_words'], template= template)

    response=llm(prompt.format( input_text = input_text, no_words=no_words))
    print(response)
    return response

st.set_page_config(page_title="Generate Blogs", page_icon ="🧜",layout = 'centered', initial_sidebar_state='collapsed' )
st.header("Generate Blogs 🧜")
input_text = st.text_input("Enter the topic")

col1, col2 = st.columns([5,5])

with col1:
    no_words=st.text_input('No. of Words')


submit= st.button("Generate")

if submit:
    st.write(getLlamaResponse(input_text, no_words))
 

