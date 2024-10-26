# embedding
Showcase how embedding is done in ML model

An embedding is a way of turning data (like words or numbers) into numerical representations that machine learning models can work with. These numerical values are placed in a multi-dimensional space (known as a vector space) based on their similarities.


#Real life analogy for embedding
For a clearer analogy, think of latitude and longitude (a two-dimensional vector) used to pinpoint a location on Earth. Let's say we have data for a few cities in India, like this:
Bareilly: 28.3670° N, 79.4304° E
Rampur: 28.7983° N, 79.0220° E
Nainital: 29.3924° N, 79.4534° E
Pune: 18.5204° N, 73.8567° E
Chennai: 13.0843° N, 80.2705° E

If we wanted to find the two closest cities, the model would easily see that Bareilly and Rampur are closest, based on their latitude and longitude.
Adding one more dimension to Vector
Now, let's add a third dimension, such as population, to the cities' data:
Bareilly: 28.3670° N, 79.4304° E, 903,668
Rampur: 28.7983° N, 79.0220° E, 463,000
Nainital: 29.3924° N, 79.4534° E, 954,605
Pune: 18.5204° N, 73.8567° E, 7,346,000
Chennai: 13.0843° N, 80.2705° E, 12,054,000

Now, if the model has to find the closest city to Bareilly with a similar population, Rampur would no longer be the closest, because its population is much smaller than Bareilly's. Instead, Nainital would be the closest match, considering both location and population.
This is a simple example to show how embeddings and vector spaces work, and how machine learning models search for similarities based on multiple dimensions.


#Prerequisite

Install Python (I'm using 3.12)
Install python-dotenv: To manage environment variables, install the python-dotenv package by running:

pip install python-dotenv
Install langchain-google-genai: Install the Google GenAI integration for Langchain:

pip install langchain-google-genai
Get your API key: https://aistudio.google.com/app/apikey
In Your python project directory, create a file with name .envand add your API key as GOOGLE_API_KEY=YOUR_API_KEY

