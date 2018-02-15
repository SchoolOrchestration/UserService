# userservice
A service to handle user management

| Requirement|Maturity|
| ---|---|
| Deployment|Staging|
| API Docs|Yes|
| Test Coverage |[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/de05583a37504c7ba0e18afbf9afefd1)](https://www.codacy.com?utm_source=github.com&utm_medium=referral&utm_content=vumatel/userservice&utm_campaign=Badge_Coverage)|
| Codacy|[![Codacy Badge](https://api.codacy.com/project/badge/Grade/de05583a37504c7ba0e18afbf9afefd1)](https://www.codacy.com?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=vumatel/userservice&amp;utm_campaign=Badge_Grade)|
| CI |Yes|
| Sentry|Yes|
| Status Cake|Yes|

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