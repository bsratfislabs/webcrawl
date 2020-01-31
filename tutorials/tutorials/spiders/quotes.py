import scrapy
from ..items import TutorialsItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    page_num = 2
    start_urls = [
        'http://quotes.toscrape.com/page/1/'
        # 'https://www.amazon.in/s?bbn=1389401031&rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1389401031%2Cp_n_date_first_available_absolute%3A1318487031&dc&fst=as%3Aoff&qid=1580363870&rnid=1318486031&ref=lp_1389401031_nr_p_n_date_first_avail_0'
    ]

    def parse(self, response):
        items = TutorialsItem()

        all_div_quotes = response.css('div.quote')
        for quote in all_div_quotes:
            items['title'] = quote.css('span.text::text').extract()
            items['author'] = quote.css('.author::text').extract()
            items['tags'] = quote.css('.tag::text').extract()
            yield items

        next_page = 'http://quotes.toscrape.com/' + str(self.page_num) + '/'
        if self.page_num < 10:
            self.page_num += 1
            yield response.follow(next_page, callback=self.parse)
