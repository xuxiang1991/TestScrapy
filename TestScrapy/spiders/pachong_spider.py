import scrapy
from TestScrapy.items import TestscrapyItem
import sys


class MySpider(scrapy.Spider):
    """
    name:scrapy唯一定位实例的属性，必须唯一
    allowed_domains：允许爬取的域名列表，不设置表示允许爬取所有
    start_urls：起始爬取列表
    start_requests：它就是从start_urls中读取链接，然后使用make_requests_from_url生成Request，
                    这就意味我们可以在start_requests方法中根据我们自己的需求往start_urls中写入
                    我们自定义的规律的链接
    parse：回调函数，处理response并返回处理后的数据和需要跟进的url
    log：打印日志信息
    closed：关闭spider
    """
    # 设置name
    name = "spidertieba"
    # 设定域名
    allowed_domains = ["cs090.com"]
    # 填写爬取地址
    start_urls = [
        "http://bbs.cs090.com/forum-12-1.html",
    ]
    # USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'
    # 编写爬取方法
    # .//div[contains(@class,"threadlist_author pull_right")]//span[contains(@class,"frs-author-name-wrap")]/a/text()'
    def parse(self, response):
        print(response)
        for line in response.xpath('//table/tbody/tr'):
            # 初始化item对象保存爬取的信息
            item = TestscrapyItem()
            # 这部分是爬取部分，使用xpath的方式选择信息，具体方法根据网页结构而定
            item['title'] = line.xpath(
                './/th[@class="common" or @class="new"]/a/text()').extract()
            item['author'] = line.xpath(
                './/td[@class="by"][1]/cite/a/text()').extract()
            item['num'] = line.xpath(
                './/td[@class="num"]/a/text()').extract()
            item['time'] = line.xpath(
                './/td[@class="by"]/em/span/text()').extract()
            yield item
