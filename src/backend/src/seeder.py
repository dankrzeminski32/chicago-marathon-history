from typing import Any
from functools import reduce
from src import db


class Seeder:
    def populate_table(self, data: list[Any]) -> None:
        """populates a table given a list"""
        for obj in data:
            db.session.add(obj)
        db.session.commit()

    def populate_athletes_and_results(self, data: list[tuple["Athlete", "Result"]]):
        """Used this way to get the PK value from athlete to be used in the result table"""
        print(f"STARTING DB POPULATION, list size: {len(data)}")
        for tuple_results in data:
            for tup in tuple_results:
                db.session.add(tup[0])
                db.session.add(tup[1])
        db.session.commit()
