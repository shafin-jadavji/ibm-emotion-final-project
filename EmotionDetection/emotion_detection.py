import requests
import json

# The URL for the emotion detection service provided by the Watson NLP service.
EMOTION_DETECTION_URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
# Timeout value for the API request
TIMEOUT_IN_SECONDS = 10

# Function to perform emotion detection on the provided text
def emotion_detector(text_to_analyse):

    # Constructing the request payload in the expected format
    payload = { "raw_document": { "text": text_to_analyse } }

    # Custom header specifying the model ID for the emotion detection service
    requests_header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    try:    
        # Sending a POST request to the emotion detection API
        response = requests.post(EMOTION_DETECTION_URL, json=payload, headers=requests_header, timeout=TIMEOUT_IN_SECONDS)
    
    except requests.exceptions.RequestException as e:
        # Handling any request-related exceptions
        print(f"Request error: {e}")
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
    
    if response.status_code == 200:
        # Parsing the JSON response from the API
        formatted_response = json.loads(response.text)

        # Extract the required set of emotions, including anger, disgust, fear, joy and sadness, along with their scores.
        emotions = {
            'anger': formatted_response['emotionPredictions'][0]['emotion']['anger'],
            'disgust': formatted_response['emotionPredictions'][0]['emotion']['disgust'],
            'fear': formatted_response['emotionPredictions'][0]['emotion']['fear'],
            'joy': formatted_response['emotionPredictions'][0]['emotion']['joy'],
            'sadness': formatted_response['emotionPredictions'][0]['emotion']['sadness']
        }

        # Determine the dominant emotion based on the maximum score among the emotions
        dominant_emotion = max(emotions, key=emotions.get)
        
        return {**emotions, 'dominant_emotion': dominant_emotion}
    
    else:
        # Handling all non-200 status codes
        print(f"Request failed with status code {response.status_code}")
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }