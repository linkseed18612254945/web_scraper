import os
import pandas as pd
import tqdm
from nlp_toolbox import NLPTools
comment_dir = r'C:\Users\51694\PycharmProjects\web_scraper\comment\yongzhou'
comments_ids = os.listdir(comment_dir)
nlp = NLPTools()
for wid in tqdm.tqdm(comments_ids):
    comments = pd.read_csv(os.path.join(comment_dir, wid))
    sentiments = nlp.sentiment_predict(comments['评论内容'])
    comments['senta_sentiments'] = sentiments
    comments.to_csv(os.path.join(comment_dir, wid))