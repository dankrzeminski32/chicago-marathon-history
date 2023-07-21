![chimarathonhistory1](https://user-images.githubusercontent.com/76189617/224878590-305afa46-36c2-4300-854b-fa8c68b9dd56.png)
![chimarathonhistory2](https://user-images.githubusercontent.com/76189617/224878609-8f4e9358-278b-427a-a9a4-33e8fe99cd9c.png)
![chimarathonhistory3](https://user-images.githubusercontent.com/76189617/224878616-08c5d47f-736b-4d60-84c2-8e7a974fe578.png)


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
docker compose exec backend flask db seed
```

to run test suite:

```
docker compose exec backend pytest
```

Navigate to localhost:3000
