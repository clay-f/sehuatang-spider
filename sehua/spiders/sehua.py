import scrapy
from sehua.items import SehuaItem


class SeHua(scrapy.Spider):
    name = "sehua"
    start_urls = [
        "https://rewrfsrewr.xyz/forum-95-1.html"
    ]

    def parse(self, response):
        table_list = response.css("div#threadlist table#threadlisttableid tbody[id^='normalthread']")
        for item in table_list:

            author = item.css("td.by a::text").get()
            if 'linzjian' == author:
                sehua_item = SehuaItem()
                sehua_item['author'] = author
                sehua_item['url'] = response.urljoin(item.css('tr a[class*=xst]::attr(href)').get())
                yield sehua_item
        next_page = response.css("span#fd_page_bottom div.pg a.nxt::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)