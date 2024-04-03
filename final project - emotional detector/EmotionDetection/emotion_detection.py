import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=input_json, headers=headers)

    #format the response 
    formatted_response = json.loads(response.text) # To convert the response text into a dictionary

    # the formated output is below: ******************
    # {'emotionPredictions': [{'emotion': {'anger': 0.0043339236, 'disgust': 0.00037549555, 'fear': 0.0034732423, 'joy': 0.9947189, 'sadness': 0.012704818}, 'target': '', 'emotionMentions': [{'span': {'begin': 0, 'end': 30, 'text': 'I am so happy I am doing this.'}, 'emotion': {'anger': 0.0043339236, 'disgust': 0.00037549555, 'fear': 0.0034732423, 'joy': 0.9947189, 'sadness': 0.012704818}}]}], 'producerId': {'name': 'Ensemble Aggregated Emotion Workflow', 'version': '0.0.1'}}
    
    if response.status_code == 400:
        output = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }

        return output

    
    # Extract emotion predictions from the response
    emotion_predictions = formatted_response.get('emotionPredictions', []) # get the value, or default empty list '[]

    # Extract emotions and their scores from the first prediction (assuming there is only one)
    emotions = emotion_predictions[0].get('emotion', {})

    # Extract scores for each emotion
    anger_score = emotions.get('anger', 0)
    disgust_score = emotions.get('disgust', 0)
    fear_score = emotions.get('fear', 0)
    joy_score = emotions.get('joy', 0)
    sadness_score = emotions.get('sadness', 0)


    # Determine the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get) # to get the max value from the list

    # Construct the output dictionary
    output = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }

    return output # return the formatted, customized result.


