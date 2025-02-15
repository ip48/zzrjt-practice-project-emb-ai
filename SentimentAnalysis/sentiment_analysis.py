import requests
import json

def sentiment_analyzer(text_to_analyse):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    print(f"Inna: {text_to_analyse}")
    input = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = input, headers=header)
    res_json = json.loads(response.text)
    #print(f"Inna: {res_json}")
    label = res_json['documentSentiment']['label']
    score = res_json['documentSentiment']['score']
    return {'label': label, 'score': score}
