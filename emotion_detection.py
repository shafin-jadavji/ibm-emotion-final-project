import requests
import json

# The URL for the emotion detection service provided by the Watson NLP service.
EMOTION_DETECTION_URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

# Function to perform emotion detection on the provided text
def emotion_detector(text_to_analyse):

    # Constructing the request payload in the expected format
    payload = { "raw_document": { "text": text_to_analyse } }

    # Custom header specifying the model ID for the emotion detection service
    requests_header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the emotion detection API
    response = requests.post(EMOTION_DETECTION_URL, json=payload, headers=requests_header, timeout=10)
    
    formatted_response = json.loads(response.text)

    return  formatted_response