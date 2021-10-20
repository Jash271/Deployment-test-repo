from flask import Flask, request, jsonify
from YouGlance import spy
import json
from requests import get, post
import time
import os
from flask_cors import CORS
app = Flask(__name__)
CORS(app)



@app.route('/')
def index():
    return "YouGlance API"

@app.route("/youglance/get_unique_entities",methods = ['POST'])
def get_unique_entities():
    data = json.loads(request.data)
    video_id = data['video_id']
    obj = spy(video_id)
    k = obj.generate_df()
    unique = obj.get_unique_ents()
    print(unique)
    return {
        "unique_ents": unique,
    }


"""
@app.get("/youglance/wild_card")
def wild_card_search(item:Item,status_code=status.HTTP_200_OK):
    print(item.query)
    df=pd.DataFrame(item.df)
    print(df.head())
    return {
        'Text':'Ok'
    }
    
"""


@app.route("/youglance/wild_card",methods = ['POST'])
def wild_card():
    data = json.loads(request.data)
    video_id = data['video_id']
    query = data['query']
    obj = spy(video_id)
    k = obj.generate_df()
    m = obj.wildcard_search(query)
    return {
        "wild_card": m,
    }
    

@app.route("/youglance/search_by_ents",methods = ['POST'])
def search_by_ents():
    data = json.loads(request.data)
    video_id = data['video_id']
    query = data['query']
    print(query)
    l = [query]
    obj = spy(video_id)
    k = obj.generate_df()
    m = obj.search_by_ents(l)
    print(m)
    return {
        "search_by_ents": m,
    }

    

@app.route("/youglance/sentiment",methods = ['POST'])
def get_sentiment():
    data = json.loads(request.data)
    video_id = data['video_id']

    obj = spy(video_id)
    obj.generate_df()
    k = obj.sentiment_analysis((-0.2, 0.2))
    d = {
        "Negative": k["Negative"],
        "Positive": k["Positive"],
        "Neutral": k["Neutral"],
        "label_stats": dict(obj.show_label_stats()),
    }
    return d
