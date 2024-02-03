# It is a LLM based app in which user can provide video and pdf or text document and then chat with it.


```
Libraries and tools used  
- Langchain with openai is used for embeddings  also it used for text preprocessing   
- FAISS is used for creating and storing vector database
- RetrivalQA chain is used for question answering to vector db
- Also you can provide the video to extract text (English) and then concatenate it with the pdf vector db .
```


### Sample Image
![Sample Image of the Chat BOT ](https://github.com/Shivam-a0621/Chat_Video_PDF/blob/main/image.png?raw=false)https://github.com/Shivam-a0621/Chat_Video_PDF/blob/main/image.png?raw=false)

## Process
```
-Created a document loader from langchain.document_loader
-A pipeline to read the text from the video and save it in a text file
-Implemented Vectorstor for fast retrival and answering
-Using gradio created a chat bot to querry the loaded document
```
