''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

#Intialize Flask
app = Flask("Emotion Detection")

@app.route("/")
def get_index():
    ''' This code renders the home page for the emotion detection
    '''
    return render_template("index.html")

@app.route("/emotionDetector")
def get_emotion():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using demotion_detector()
        function. The output returned shows the emotion and its confidence 
        score for the provided text.
    '''
    text_to_analyze = request.args.get("textToAnalyze")
    resp = emotion_detector(text_to_analyze)

    if resp["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return f"""For the given statement, the system response is
    'anger': {resp['anger']},
    'disgust': {resp['disgust']},
    'fear': {resp['fear']},
    'joy': {resp['joy']}, and
    'sadness': {resp['sadness']}.
    The dominant emotion is {resp["dominant_emotion"]}"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
