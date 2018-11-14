import scrapy
import logging

from scrapy.utils.log import configure_logging

configure_logging(install_root_handler=False)
logging.basicConfig(
    filename='log.txt',
    format='%(levelname)s: %(message)s',
    level=logging.INFO
)

BASE_URL = "https://www.fifaindex.com/de/players/{}/"
VERSIONS = {
    '13': 'fifa13_10',
    '14': 'fifa14_13',
    '15': 'fifa15_14',
    '16': 'fifa16_73',
    '17': 'fifa17_173',
    '18': 'fifa18_278',
    '18wc': 'fifa18wc_271',
    '19': ''
}

class Player(scrapy.Item):
    id = scrapy.Field()
    overall = scrapy.Field()
    potential = scrapy.Field()
    name = scrapy.Field()
    position = scrapy.Field()
    age = scrapy.Field()
    team = scrapy.Field()
    nation = scrapy.Field()

class FifaSpider(scrapy.Spider):
    name = 'fifaspider'
    #start_urls = [BASE_URL.format(v) for v in [15, 16, 17, 18, 19]]
    start_urls = [BASE_URL.format(VERSIONS['15'])]

    def get_url(self, version):
        return FifaSpider.base_url.format(version)

    def parse(self, response):
        sel = scrapy.Selector(response)
        items = sel.xpath('//table/tbody/tr')

        for item in items:
            player = Player()

            text_attrs = item.xpath('.//text()').extract()
            player['overall'] = text_attrs[0]
            player['potential'] = text_attrs[1]
            player['name'] = text_attrs[2]
            player['position'] = ' '.join(text_attrs[3:-2])
            player['age'] = text_attrs[-2]

            player['id'] = item.xpath('.//@data-playerid').extract()[0]
            player['nation'] = item.xpath('.//td[@data-title="Nationalität"]/a/@title').extract()[0]
            #player['team'] = item.xpath('.//td[@data-title="Team"]/a/@title').extract()[0]
            team = item.xpath('.//td[@data-title="Team"]/a/@title').extract()
            player['team'] = team[0] if len(team) > 0 else ''

            #self.logger.info(player)
            #self.logger.info(player.items())
            yield player

        for next_page in response.css('li.page-item > a'):
            yield response.follow(next_page, self.parse)
