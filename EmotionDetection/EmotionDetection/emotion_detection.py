"""
Uses WatsonX to provide sentiment analysis
"""

import requests
import json
import http

def format_output(emotion_data):
    """ Formats watsonx response """
    predictions = emotion_data.get("emotionPredictions",[])[0]
    emotion_response = predictions.get("emotion")
    dominant_emotion = { "name": None, "value": None}

    for (key,value) in emotion_response.items():
        if dominant_emotion["value"] is None or value >= dominant_emotion["value"]:
            dominant_emotion["name"] = key
            dominant_emotion["value"] = value

    emotion_response["dominant_emotion"] = dominant_emotion["name"]
    return emotion_response
    

def emotion_detector(text_to_analyze):
    """ 
        Runs sentiment analysis and formats the response
        returns: 
            200, valid text string and object
            400, invalid text string and Null object
    """

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    body = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=body, headers=headers)
    if response.status_code == 200:
        response_json = response.json()
        # print('response', response_json)
        return format_output(response_json)
    elif response.status_code == 400:
        return { "anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None, "dominant_emotion": None}
    else:
        raise http.HTTPError(response.status_code, response.text)

def pprint(data):
    """ 
        Helper to format json object
    """
    print(json.dumps(data, indent=2))

if __name__ == "__main__":
    pprint(emotion_detector("A dog's loyalty teaches us the true meaning of unconditional love."))
    pprint(emotion_detector("The quietness of the house speaks volumes of a dog's absence."))
    pprint(emotion_detector("Dogs bring so much love and companionship into our lives."))

