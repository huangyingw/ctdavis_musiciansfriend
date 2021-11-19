from scrapy import Spider
from scrapy.loader import ItemLoader
from quotes_spider.items import QuotesSpiderItem

class QuotesSpider(Spider):
    name = 'quotes'

    start_urls = ['https://rewrfsrewr.xyz/forum.php?mod=forumdisplay&fid=103&filter=typeid&typeid=481']

    def parse(self, response):
        movie_name = response.xpath("//*[contains(.,'影片名称')]/text()").re(r'影片名称.*：(.*)')
        movie_name = [x.strip() for x in movie_name]
        torrents = response.xpath('//*[contains(@href, ".torrent")]/@href').getall()
        magnets = response.xpath("//*[contains(.,'magnet')]/text()").re(r'(magnet:.*)&.*') or response.xpath("//*[contains(.,'magnet')]/text()").re(r'(magnet:.*)')
        actress = response.xpath("//*[contains(.,'出演女优')]/text()").re(r'出演女优.*：(.*)')
        actress = [x.strip() for x in actress]
        mosaic = response.xpath("//*[contains(.,'是否有码')]/text()").re(r'是否有码.*：(.*)')
        mosaic = [x.strip() for x in mosaic]
        size = response.xpath("//*[contains(.,'影片大小')]/text()").re(r'影片大小.*：(.*)')
        size = [x.strip() for x in size]
        if torrents or magnets:
            item = ItemLoader(QuotesSpiderItem())
            item.add_value('title', response.xpath("//span[@id='thread_subject']/text()").get())
            item.add_value('movie_name', movie_name)
            item.add_value('actress', actress)
            item.add_value('mosaic', mosaic)
            item.add_value('size', size)
            item.add_value('torrents', torrents)
            item.add_value('magnets', magnets)
            item.add_value('link', response.url)
            yield item.load_item()
        for href in response.css('a[href*="thread-"][onclick="atarget(this)"]::attr(href)').getall():
            yield scrapy.Request(response.urljoin(href), self.parse)
        for href in response.css('a[href*="forum.php?mod=viewthread"]::attr(href)').getall():
            yield scrapy.Request(response.urljoin(href), self.parse)
        next_page = response.xpath("//a[contains(text(), '下一页')]/@href").get()
        if next_page:
            yield response.follow(next_page, self.parse)
