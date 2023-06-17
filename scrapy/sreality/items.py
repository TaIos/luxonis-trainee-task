from scrapy import Item, Field


class FlatItem(Item):
    name = Field()
    image_url = Field()
    scraped_hash_id = Field()
