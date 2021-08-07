# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import logging
import pyodbc
import datetime


class SehuaPipeline:
    def __init__(self):
        self.cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=scrapy;UID=sa;PWD=.')
        self.cursor = self.cnxn.cursor()

    def process_item(self, item, spider):
        try:
            logging.info("author: %s, url: %s", item['author'], item['url'])
            self.cursor.execute(r"insert into sehua(title, [url], created_at) values(?, ?, ?)", item['author'],
                                item['url'], datetime.datetime.now())
            self.cursor.commit()
        except Exception as e:
            print(e)
        return item
