from flask import Blueprint
from src.backend import db
from src.backend.scrapers import history
from src.backend import seeder
from src.backend.services.result_service import ResultService
from src.backend.topfinisher_images import TopFinisherImageRetriever

db_commands_bp = Blueprint("db", __name__)


@db_commands_bp.cli.command("create")
def create():
    db.create_all()

@db_commands_bp.cli.command("seed")
def seed():
    marathons = history.MarathonParticipantCountScraper().get_marathons()
    seed = seeder.Seeder()
    seed.populate_table(marathons)
    db.session.commit()
    print("FINISHED POPULATING MARATHONS")
    data = history.AthleteResultScraper().parse_for_athletes_and_results()
    print(f"LENGTH OF RETRIEVED DATA, {len(data)}")
    seed.populate_athletes_and_results(data)


@db_commands_bp.cli.command("recreate")
def recreate():
    db.drop_all()
    db.create_all()


@db_commands_bp.cli.command("seed-athlete-images")
def seedAthleteImages():
    TopFinisherImageRetriever.get_images()
