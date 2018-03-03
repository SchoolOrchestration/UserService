# userservice
A service to handle user management

## Start Up

```bash
docker-compose up -d
```

## Run tests

```bash
 docker-compose run --rm web python manage.py test
```

## Run code coverage

```bash
docker-compose -f docker-compose.test.yml up sut
```

## Deploy

```
sh ./deploy.sh {staging|production}
```