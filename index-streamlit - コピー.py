from google.cloud import vision
from googletrans import Translator
import os
import streamlit as st
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "C:\\API-json\\my-vision-ai-311301-b2d880e50e9b.json"

def img_trans(content):
    # image.jpgを開いて読み込む


    # vision APIが扱える画像データにする
    image = vision.Image(content=content)

    # ImageAnnotatorClientのインスタンスを生成
    annotator_client = vision.ImageAnnotatorClient()

    response_data = annotator_client.label_detection(image=image)

    labels = response_data.label_annotations

    translator = Translator()
    st.write('----RESULT----')
    for label in labels:
        J_description = translator.translate(label.description, dest='ja')
        st.write(label.description, ':', J_description.text, ':', round(label.score * 100, 2), '%')
    st.write('----RESULT----')



st.title('画像解析アプリ')

st.header('概要')
st.write('こちらはGoogle Cloud Visionを利用した画像解析アプリです。リンクは下記です。')
st.markdown('<a href="https://cloud.google.com/vision/docs?hl=ja">', unsafe_allow_html=True)

upload_file = st.file_uploader('ファイルのアップロード', type=['jpg'])

if upload_file is not None:
    content = upload_file.read()
    st.subheader('ファイル詳細')
    file_details = {'FileName': upload_file.name, 'FileType': upload_file.type, 'FileSize': upload_file.size}
    st.write(file_details)
    st.image(upload_file,caption='アップロードされた画像',use_column_width=True)

    st.subheader('画像の解析')
    if st.button('開始'):
        comment = st.empty()
        comment.write('解析を開始します')
        img_trans(content=content)
        comment.write('解析が完了しました')



