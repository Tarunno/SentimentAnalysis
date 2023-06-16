# Semtiment Analysis API
A web api that got single endpoint /analyze which acccpts POST request with a payload that contains the text which is to be analyzed by the classification model.

### Api documentation: https://documenter.getpostman.com/view/13756354/2s93shz9q9
<br/>

# Model
I have used a BERT based model which was provide pretrained from aXhyra/presentation_sentiment_31415 in Hugginface. Which is a fine-tuned version of distilbert-base-uncased on the tweet_eval dataset. It achieves the following results on the evaluation set:
- Loss: 1.0860
- F1: 0.7983

# Insturctions
- Clone the repository https://github.com/Tarunno/SentimentAnalysis
- Create a virtual environment
- In that venv Install requirements.txt
- Run the server
- Let the pretrained model to be downloaded
- Restart the server

# Endpoint 
- POST /analyze  payload(raw/json)={"text": "I love programming"} 