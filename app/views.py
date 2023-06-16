from rest_framework.response import Response 
from rest_framework.decorators import api_view

from transformers import AutoTokenizer, AutoModelForSequenceClassification
tokenizer = AutoTokenizer.from_pretrained("aXhyra/presentation_sentiment_31415")
model = AutoModelForSequenceClassification.from_pretrained("aXhyra/presentation_sentiment_31415")


@api_view(['GET'])
def ApiOverView(request):
    api_enpoints = {
        'POST /analyze': 'sentiment analysis'
    }
    return Response(api_enpoints)



@api_view(['POST'])
def Analyze(request):
    text = request.data.get('text')
    if text and len(text) > 0:
        inputs = tokenizer(text, return_tensors="pt")
        preds = model(inputs['input_ids'])

        labels = ['negative', 'neutral', 'positive']
        preds = labels[preds.logits.argmax().item()]

        return Response({'sentiment': preds})
    return Response({'message': 'provide a text', 'status_code': 400}, status=400)

