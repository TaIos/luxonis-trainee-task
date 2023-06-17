from sreality.items import FlatItem

from scrapy import Spider


class SrealitySpider(Spider):
    name = "sreality"

    start_urls = [
        f'https://www.sreality.cz/api/cs/v1/estates?category_main_cb=1&category_type_cb=1&per_page=100&sort=0&page={i}'
        for i in range(1, 6)
    ]

    def parse(self, response):
        return map(SrealitySpider._parse_flat, response.json()['_embedded']['estates'])

    @staticmethod
    def _parse_flat(flat):
        return FlatItem(
            name=flat['name'],
            image_url=flat['_links']['images'][0]['href'],
            scraped_hash_id=flat['hash_id'])
