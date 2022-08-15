# 必要モジュールのインポート
import os
from dotenv import load_dotenv
import streamlit as st
import requests
import openai


#st.header("チャットボット_高橋")
# .envファイルの内容を読み込見込む
load_dotenv()

# os.environを用いて環境変数を表示させます
#print(os.environ['API_KEY'])
st.header(test)


openai.api_key = os.environ['API_KEY']

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
