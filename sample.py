# 必要モジュールのインポート
import os
import streamlit as st
import requests
import openai

API_KEY = st.secrets.OpenAI.API_KEY


openai.api_key = API_KEY

def text_summary(prompt):
    # 分析の実施
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    temperature=0.8,
    max_tokens=100,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["あなた:", "高橋:"]
    )

    # 分析結果の出力
    return response["choices"][0]["text"].replace('\n','')
prompt="高橋君は"
return_text=text_summary(prompt)
print(return_text)
