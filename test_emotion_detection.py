import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):

        test_cases = {
            "statement" : [
                "I am glad this happened",
                "I am really mad about this",
                "I feel disgusted just hearing about this",
                "I am so sad about this",
                "I am really afraid that this will happen"
            ],
            "dominant_emotion" : [
                "joy",
                "anger",
                "disgust",
                "sadness",
                "fear"
            ]

        }

        for statement, dominant_emotion in zip(test_cases["statement"], test_cases["dominant_emotion"]):
            test_resp = emotion_detector(statement)
            self.assertEqual(test_resp["dominant_emotion"],dominant_emotion)

unittest.main()