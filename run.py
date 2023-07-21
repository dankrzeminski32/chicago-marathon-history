from src.backend import init_app
from config import TestConfig
import asyncio
from src.backend.cli import seedsample


app = init_app(TestConfig)

if __name__ == "__main__":
    with app.app_context():
        asyncio.run(seedsample())
