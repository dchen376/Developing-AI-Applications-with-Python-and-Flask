"""
This module implements a Flask application for emotion detection.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector  # import this method

app = Flask(__name__)

@app.route('/emotionDetector')
def emotion_detector_route():
    """
    Handle the emotion detection route.

    Retrieves the text to analyze from the query parameters 
    and returns the emotion detection result.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return "Error: Text to analyze not provided", 400

    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return format_response(result)


def format_response(result):
    """
    Format the emotion detection result into a human-readable format.

    Args:
        result (dict): The emotion detection result.

    Returns:
        str: A formatted string describing the emotion detection result.
    """
    output = "For the given statement, the system is "
    output += ", ".join(f"'{emotion}': {score}"
    for emotion, score in result.items()
    if emotion != 'dominant_emotion')
    output += f". The dominant emotion is {result['dominant_emotion']}."
    return output


@app.route('/')
def index():
    """
    Render the index HTML page.
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5003)
