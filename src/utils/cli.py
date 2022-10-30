from flask import Blueprint
from src import db
from src.scrapers import history
from src.utils import seeder

db_commands_bp = Blueprint("db", __name__)

@db_commands_bp.cli.command("create")
def create():
    db.create_all()

@db_commands_bp.cli.command("seed")
def seed():
    scraper = history.HistoryScraper()
    marathons = scraper.getMarathons()
    marathons = list(marathons.values())
    seed = seeder.Seeder(db)
    seed.populate_table(marathons)