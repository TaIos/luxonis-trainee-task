from sreality.items import FlatItem

from sreality.persistence import AdvertisementsDao, Advertisements


class PostgresFlatItemPersistPipeline:

    def __init__(self):
        self.advertisementsDao = AdvertisementsDao()

    def process_item(self, item, spider):
        self._persist_item_to_database(item)
        return item

    def _persist_item_to_database(self, item: FlatItem):
        self.advertisementsDao.save(Advertisements(
            name=item['name'],
            image_url=item['image_url'],
            scraped_hash_id=item['scraped_hash_id']))
