from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

class TestSentimentAnalysis(unittest.TestCase):
    def test_sentiment_analyzer(self):
        res1 = sentiment_analyzer('I love working with Python')
        self.assertEqual(res1["label"] , 'SENT_POSITIVE')

        res2 = sentiment_analyzer('I hate working with Python')
        self.assertEqual(res2["label"] , 'SENT_NEGATIVE')

        res3 = sentiment_analyzer('I am neutral on Python')
        self.assertEqual(res3["label"] ,'SENT_NEUTRALL)

if __name__ == "__main__":
    unittest.main()


