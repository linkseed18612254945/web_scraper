import json
from weibo_spiders.weibo_user_spider import WeiboUserSpider
from weibo_spiders.weibo_comment_spider import WeiboCommentScrapy
from weibo_spiders.weibo_topic_spider import WeiboTopicScrapy

class WeiboSpiderTool(object):

    def __init__(self, config=None):
        if config is None:
            with open('config.json', 'r') as f:
                config = json.load(f)
        self.config = config
        self.wb_user_spider = WeiboUserSpider(self.config)
        self.wb_comment_spider = WeiboCommentScrapy(self.config)
        self.wb_topic_spider = WeiboTopicScrapy(self.config)

    def get_users_info(self):
        self.wb_user_spider.start()

    def get_wb_comment(self, bid):
        if bid is not None:
            self.wb_comment_spider.wid = bid
        self.wb_comment_spider.start()

    def get_topic_wb(self):
        self.wb_topic_spider.start()

if __name__ == '__main__':
    weibo = WeiboSpiderTool()
    bids = ['JhIm25aWX',
            'JhFMrb03F',
             'JhEWYtG1y',
             'JhzoWFFg5',
             'JhvOd8dkx',
             'JhrBXc7jb',
             'Jhqec60Hf']
    for bid in bids:
        weibo.get_wb_comment(bid)

