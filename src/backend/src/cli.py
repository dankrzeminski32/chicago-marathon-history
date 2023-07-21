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
    db.create_all()
    marathons = history.MarathonParticipantCountScraper().get_marathons()
    seed = seeder.Seeder()
    seed.populate_table(marathons)
    db.session.commit()
    print("FINISHED POPULATING MARATHONS")
    data = history.AthleteResultScraper().parse_for_athletes_and_results()
    print(f"LENGTH OF RETRIEVED DATA, {len(data)}")
    seed.populate_athletes_and_results(data)
    TopFinisherImageRetriever.get_images()


@db_commands_bp.cli.command("recreate")
def recreate():
    db.drop_all()
    db.create_all()


@db_commands_bp.cli.command("seed-athlete-images")
def seedAthleteImages():
    TopFinisherImageRetriever.get_images()
