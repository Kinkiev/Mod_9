# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json


class TestSpyderPipeline:
    quotes = []
    authors = []

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if "fullname" in adapter.keys():
            self.authors.append(
                {
                    "fullname": adapter["fullname"],
                    "date_born": adapter["date_born"],
                    "location_born": adapter["location_born"],
                    "bio": adapter["bio"],
                }
            )
        if "quote" in adapter.keys():
            self.quotes.append(
                {
                    "keywords": adapter["keywords"],
                    "author": adapter["author"],
                    "quote": adapter["quote"],
                }
            )
        return

    def close_spider(self, spider):
        with open("quotes.json", "w", encoding="utf-8") as fd:
            json.dump(self.quotes, fd, ensure_ascii=False)
        with open("authors.json", "w", encoding="utf-8") as fd:
            json.dump(self.authors, fd, ensure_ascii=False)
