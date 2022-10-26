from typing import Any
from scrapers import history


history.HistoryScraper().populate_db()

class Seeder:
    def __init__(self, db):
        self.db = db

    def populate_table(self, table: str, data: list[Any]) -> None:
        if self.is_populated(table):
            pass #don't populate
        else:
            pass #populate db

    def is_populated(self, table: str) -> bool:
        pass 