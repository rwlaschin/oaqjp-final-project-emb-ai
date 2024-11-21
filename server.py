"""
Uses WatsonX to provide sentiment analysis
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """
    Displays index page
    """
    return render_template("index.html")

@app.route('/emotionDetector', methods=['GET'])
def post_emotion_detector():
    """
    Fetches response from sentiment analysis and returns formated response
    """
    text = request.args.get('textToAnalyze')
    print('arg', text)

    response = emotion_detector(text)
    print(response)

    if response.get("dominant_emotion") is None:
        response_str = 'Invalid text!  Please try again!'
    else:
        response_str = 'For the given statement, the system response is ' + \
            ', '.join([
                f"'{key}': {value}" for (key,value) in response.items()
                    if key != 'dominant_emotion'
                ]) + \
            f". The dominant emotion is <strong>{response['dominant_emotion']}</strong>."

    return response_str, 200

if __name__ == '__main__':
    app.run(port=5000,debug=True)
