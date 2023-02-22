# Chicago Marathon History

An interactive web tour through the history of The Chicago Marathon.

## Setup

First, Make sure you remove '-example' from ./src/backend/.env-example after configuring it with your own variables.

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
