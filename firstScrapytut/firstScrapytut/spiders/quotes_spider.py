import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'quotes'

    start_urls = [

        'http://quotes.toscrape.com'
    ]



    def parse(self, response):


       all_div_quotes = response.css('div.quote')


       for i in  all_div_quotes:


           title = i.css('span.text::text').extract()
           author = i.css('.author::text').extract()

           tags= i.css('.tag::text').extract()


           yield {

               'title' : title,
               'author' : author,
               'tags' : tags

           }

