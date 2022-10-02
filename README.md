[![Maintainability](https://api.codeclimate.com/v1/badges/970c251839c68d938c5c/maintainability)](https://codeclimate.com/github/Elgismarus/postable/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/970c251839c68d938c5c/test_coverage)](https://codeclimate.com/github/Elgismarus/postable/test_coverage)

# postable

Sample Django REST API application for usage of [postalcode](https://github.com/Elgismarus/postalcode) package.

# Compatibility

| Name | Version |
| --- | --- |
| Python | 3.10.6 |
| Django | 4.1.1 |
| pytest | 7.1.3 |

# Dependencies

## Prod

### Django

Django was chosen to be closer to the real stack. It speeds up the development of web applications.

### djangorestframework

In combinaison of Django, this allowed to develop the REST API faster.

### PostalCode

Use the custom package `Postalcode` created previously to validate postal code provided through the API.

## Development

### pytest-django

For running Django tests.

### Coverage

Get coverage data to ensure enough test coverage of the web application.


# Deployment

This application can be containize with Docker. It makes it easier to deploy as part of an orchestration tool like Docker Swarm or Kubernetes, so the application can be easily spawned and, therefore, provide higher availablity in the event of load (Horizontal Scaling).

## Build image

_Docker installation is required._

1. Open Terminal
1. Clone project
1. `cd` into project root directory
1. Run `docker build -t <TAG> .`

This will create the image which can be published on DockerHub or any private repository.

`<TAG>` must be replaced with a name of your choosing (e.g. `postable:0.0.1`)

Example:

```
docker build -t postable:0.0.1 .
```

## Run a application container

_Docker installation is required._


1. Open Terminal
1. Clone project
1. `cd` into project root directory
1. Run `docker run --name <NAME> -p <PORT>:8080 <TAG>`


Example:
```
docker run --name postable-prod-1 -p 8000:8000 postable:0.0.1
```


| Variable | Description |
| --- | --- |
| `<NAME>` | Name of the container. If not provided, a random name is assigned |
| `<PORT>` | Expose local port to application. If not provided, random port will be assigned (usually done when high availability is required when multiple environments need to be spawned) |
| `<TAG>` | Name used to build the image (previous step) |


# Local Server

Run the server locally with `python manage.py runserver`

# Testing

Test suites can be run from VSCode through the test explorer UI (already included in the devcontainer setup mentioned below) or via CLI as detailed below:

1. Open Terminal
1. Clone project
1. `cd` into project root directory
1. Open and build project in VSCode (`code .`)
1. Run `pytest`

# Contribute easily with VSCode

This project has been built with VSCode in a devcontainer. This allows for development environment consistency across engineers and eases onboarding and setup. This avoids frustration when the environment version changes and the required programming languages and/or dependencies must be installed on the local machine.

1. Open Terminal
1. Clone project
1. `cd` into project root directory
1. Type `code .`
1. In VSCode, `ctrl+P` and select `Remote container: Rebuild Container`

It usually takes some time the first time to build (download images/container). Once built, you will have all the VSCode plugins required and be able to work on the project. The test explorer is a good tool for debugging and running specific tests visually.
