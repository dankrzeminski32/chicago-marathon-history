from typing import Any

class Seeder:
    def __init__(self, db):
        self.db = db

    def populate_table(self, data: list[Any]) -> None:
        if self.is_populated():
           pass 
        else:
            for obj in data:
                print(obj)
                self.db.session.add(obj)
            self.db.session.commit()         


    def is_populated(self) -> bool:
        return False 