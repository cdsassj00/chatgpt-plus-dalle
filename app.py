import streamlit as st
import openai

openai.api_key = "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"
st.title("지영,세린,승철 아빠가 원하는 그림을 그려준다")

with st.form("form"):
    user_input = st.text_input("Prompt")
    size = st.selectbox("Size", ["1024x1024","512x512","256x256"])
    submit = st.form_submit_button("제출")

if submit and user_input:
    gpt_prompt = [{
        "role":"system",
        "content":"Imagine the detail appereance of the input. Response it shortly."
    }]
    
    gpt_prompt.append({
        "role":"user",
        "content":user_input
    })
    
    with st.spinner("잠시만 기다려주세요"):
        gpt_response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages =gpt_prompt
        )
    
    prompt = gpt_response["choices"][0]["message"]["content"]
    st.write(prompt)
    
    with st.spinner("잠시만 기다려주세요"):
        dalle_response = openai.Image.create(
            prompt = prompt,
            size = size
        )

    st.image(dalle_response["data"][0]["url"])
    
    
