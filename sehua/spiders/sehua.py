import scrapy


class SeHua(scrapy.Spider):
    name = "sehua"
    start_urls = [
        "https://rewrfsrewr.xyz/forum-95-1.html"
    ]

    def parse(self, response):
        table_list = response.css("div#threadlist table#threadlisttableid tbody[id^='normalthread']")
        for item in table_list:
            author = item.css("td.by a::text").get()
            if '为之生而为之死' == author:
                self.logger.info("author: %s, url: %s", author, response.url)
        next_page = response.css("span#fd_page_bottom div.pg a.nxt::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)