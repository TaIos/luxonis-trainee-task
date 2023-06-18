import logging

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from sreality.persistence import AdvertisementsDao


def _database_contains_no_advertisements() -> bool:
    return AdvertisementsDao().count() == 0


def _run_sreality_scraper_blocking():
    process = CrawlerProcess(get_project_settings())
    process.crawl("sreality")
    process.start()


if __name__ == '__main__':
    if _database_contains_no_advertisements():
        _run_sreality_scraper_blocking()
    else:
        logging.getLogger().warning('Database already contains advertisements, scraper run is aborted.')
