# Chicago Marathon History

An interactive web tour through the history of The Chicago Marathon.

## Setup

First, Make sure you remove '-example' from both .env-example and config-example.py after configuring them.

Then,

```
docker compose build
```

```
docker compose up -d
```

```
docker compose exec backend flask db seed-sample
```

to run test suite:

```
docker compose exec backend pytest
```

Navigate to localhost:3000
