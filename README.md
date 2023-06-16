# Semtiment Analysis API
A web API that got a single endpoint /analyze which accepts POST request with a payload that contains the text which is to be analyzed by the classification model.

### Api documentation: https://documenter.getpostman.com/view/13756354/2s93shz9q9
<br/>

# Model
I have used a BERT-based model which was provided pre trained from aXhyra/presentation_sentiment_31415 in Hugginface. Which is a fine-tuned version of distilbert-base-uncased on the tweet_eval dataset. It achieves the following results on the evaluation set:
- Loss: 1.0860
- F1: 0.7983

# Insturctions
- Clone the repository https://github.com/Tarunno/SentimentAnalysis
- Create a virtual environment
- In that venv Install requirements.txt
- Run the server
- Let the pre-trained model to be downloaded
- Restart the server

# Endpoint 
- POST /analyze  payload(raw/json)={"text": "I love programming"}

# Exception handling
- Invalid endpoints (404)
- Invalid HTTP request method (405)
- Empty payload (400)
- Server error (500) <br/>
Each of the exceptions provides custom response messages.
