from typing import Any
from src.backend import db


class Seeder:
    def populate_table(self, data: list[Any]) -> None:
        """populates a table given a list"""
        for obj in data:
            print(obj)
            db.session.add(obj)
        db.session.commit()

    def populate_athletes_and_results(self, data: list[tuple["Athlete", "Result"]]):
        """Used this way to get the PK value from athlete to be used in the result table"""
        print(f"STARTING DB POPULATION, list size: {len(data)}")
        for list in data:
            for index, tup in enumerate(list):
                db.session.add(tup[0])
                db.session.commit()
                tup[1].athlete_id = tup[0].id
                db.session.add(tup[1])
            db.session.commit()
