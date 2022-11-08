from src import init_app
from config import DevConfig,TestConfig

app = init_app(DevConfig)

if __name__ == "__main__":
    app.run(host='0.0.0.0')