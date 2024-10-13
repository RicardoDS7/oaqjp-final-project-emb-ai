import requests
import json

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(URL, json=payload, headers=headers)

    #JSON Formatted Response
    response_json = json.loads(response.text)

    #Handle Error 400
    if response.status_code == 400:
        result = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
        }

        return result

    #Emotion Scores
    anger_score = response_json["emotionPredictions"][0]["emotion"]["anger"]
    disgust_score = response_json["emotionPredictions"][0]['emotion']['disgust']
    fear_score = response_json["emotionPredictions"][0]['emotion']['fear']
    joy_score = response_json["emotionPredictions"][0]['emotion']['joy']
    sadness_score = response_json["emotionPredictions"][0]['emotion']['sadness']

    #Find Dominant Emotion
    # Extracting the 'emotion' dictionary
    emotion_values = response_json["emotionPredictions"][0]['emotion']

    # Finding the key with the maximum value
    dominant_emotion = max(emotion_values, key=emotion_values.get)   

    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion

    }
    return result