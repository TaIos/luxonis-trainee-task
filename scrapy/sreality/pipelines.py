import os
from configparser import ConfigParser

from sreality.items import FlatItem
from sreality.psql import connect


def retrieve_db_secrets() -> dict:
    return {
        'user': os.environ['POSTGRES_USER'],
        'password': os.environ['POSTGRES_PASSWORD'],
        'database': os.environ['POSTGRES_DB'],
        'host': os.environ['POSTGRES_HOST'],
        'port': os.environ['POSTGRES_PORT']
    }

class PostgresFlatItemPersistPipeline:

    def __init__(self):
        self.conn, self.cur = connect(retrieve_db_secrets())

    def process_item(self, item, spider):
        self._persist_item_to_database(item)
        return item

    def _persist_item_to_database(self, item: FlatItem):
        # TODO sanitize or use some ORM framework/client
        self.cur.execute(f""" 
        insert into advertisements(id, name, image_url, scraped_hash_id)
        values(DEFAULT,'{item['name']}', '{item['image_url']}', '{item['scraped_hash_id']}')""")
        self.conn.commit()

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()

    @staticmethod
    def _read_and_validate_config(path: str) -> ConfigParser:
        cfg = ConfigParser(allow_no_value=True)
        cfg.read(path)
        if not cfg.has_section('postgresql'):
            raise ValueError(f'Invalid config file [{path}], no section [postgresql]')
        return cfg
