from dotenv import load_dotenv
import os

#1.Load environment variable and access api Key
load_dotenv()
apikey = os.getenv("GOOGLE_API_KEY")

#2. Create object of  GoogleGenerativeAIEmbeddings
# using embedding model embedding-001 provided by Google
from langchain_google_genai import GoogleGenerativeAIEmbeddings
objEmbeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

#3. Generate embedding for given text
#embed_query() returns embedding in form of List of floats
listOfEmbeddingInNumericForm = objEmbeddings.embed_query("hello, world!")

#4.print all embeddings
for embedding in listOfEmbeddingInNumericForm:
    print(embedding)