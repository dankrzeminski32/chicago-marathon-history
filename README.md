# Chicago Marathon History

An interactive web tour through the history of The Chicago Marathon.

## Setup

```
docker compose build
```

```
docker compose up -d
```

```
docker compose exec backend flask db seedsample
```

```
docker compose exec backend flask db seed-athlete-images
```

to run test suite:

```
docker compose exec backend pytest
```

Navigate to localhost:3000
