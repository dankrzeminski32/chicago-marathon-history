from flask import Blueprint
from src import db
from src.scrapers import history
from src import seeder
from src.services.result_service import ResultService
from src.topfinisher_images import TopFinisherImageRetriever

db_commands_bp = Blueprint("db", __name__)


@db_commands_bp.cli.command("create")
def create():
    db.create_all()

@db_commands_bp.cli.command("seed")
def seed():
    marathons = history.HistoryMarathonScraper().get_marathons()
    marathon_list = list(marathons.values())
    seed = seeder.Seeder()
    seed.populate_table(marathon_list)
    db.session.commit()
    data = history.HistoryAthleteScraper().get_data()
    print(f"LENGTH OF RETRIEVED DATA, {data}")
    seed.populate_athletes_and_results(data)


@db_commands_bp.cli.command("seed-sample")
def seed_sample():
    marathons = history.HistoryMarathonScraper().get_marathons()
    marathon_list = list(marathons.values())
    seed = seeder.Seeder()
    seed.populate_table(marathon_list)
    db.session.commit()
    data = history.HistoryAthleteScraper().get_data(sample=True)
    seed.populate_athletes_and_results(data)
    TopFinisherImageRetriever.get_images()


@db_commands_bp.cli.command("recreate")
def recreate():
    db.drop_all()
    db.create_all()
