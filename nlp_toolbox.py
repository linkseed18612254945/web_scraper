from senta import Senta
from snownlp import SnowNLP

class NLPTools(object):
    def __init__(self):
        self.senta = Senta()
        self.senta.init_model(model_class="ernie_1.0_skep_large_ch", task="sentiment_classify", use_cuda=False)

    def sentiment_predict(self, texts, kernel='senta'):
        if isinstance(texts, str):
            texts = [texts]
        if kernel == 'senta':
            sentiments = [x[1] for x in self.senta.predict(texts)]
        else:
            sentiments = ['positive' if SnowNLP(text).sentiments > 0.5 else 'negative' for text in texts]
        return sentiments


if __name__ == '__main__':
    nlp = NLPTools()
    res = nlp.sentiment_predict('冷水滩公安局确实实至名归，擅长破冷水', kernel='snow')
    print(res)
