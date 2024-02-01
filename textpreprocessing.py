from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import ConversationalRetrievalChain
from langchain.chains.conversation.memory import ConversationBufferMemory
import moviepy.editor as mp
import speech_recognition as sr



text_split= CharacterTextSplitter(
    separator='\n',
    chunk_size=2000,
    chunk_overlap=200,
    length_function=len,
    )


def creat_text(path):
    pdf= PdfReader(path)
    raw_txt=""
    for i,pages in enumerate(pdf.pages):
        text= pages.extract_text()
        if text:
            raw_txt+=text
    return raw_txt


def video_to_text(path):
    video= mp.VideoFileClip(path)
    # Extract the audio from the video
    audio_file = video.audio
    audio_file.write_audiofile("movies.wav")
    # Initialize recognizer
    r = sr.Recognizer()
    # Load the audio file
    with sr.AudioFile("movies.wav") as source:
        data = r.record(source)

    # Convert speech to text
    text = r.recognize_google(data)

    return text


def text_split(text):
    return text_split.split_text(text)



    
    



        