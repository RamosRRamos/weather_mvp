# Wheather Playlist

## Project description

This project is a simple Django application that provides a REST API 
to manage weather data and generate playlists based on the weather conditions. 
The application uses Weather API to fetch weather data and the OpenIA API to generate playlists.

## Prototype goals

- Create simple APIs. with 2 microservices
- Focus on usability and essential functionalities.
- Use a “gateway” using Django for this purpose.


## Use Cases

### 1. User Registration
**Actor**: Visitor  
**Description**:  To obtain a personalized music playlist based on the temperature in your city.

**Main Flow**:
1. The user accesses the service's API, providing the name of their city as a parameter.
2. The service consults a third-party service to obtain the current temperature of the city entered.
3. Based on the temperature obtained:
   - If the temperature is above 25ºC, the service searches for songs in the Pop genre in a database or streaming service.
   - If the temperature is between 10ºC and 25ºC, the service searches for songs in the Rock genre.
   - If the temperature is below 10ºC, the service searches for songs in the Classical genre.
4. The service returns a playlist containing the songs selected according to temperature.
5. The user receives the playlist and can enjoy it.

**Alternate Flows**:

1. City not found: If the city entered is not found in the third-party service, the service returns an error message indicating that the city is invalid. (Implemented as needed)
2. Temperature service unavailable: If the third-party service is unavailable, the service returns an error message stating that it was not possible to obtain the city's temperature. (Implemented as needed)
3. No music found: If no music is found for the genre corresponding to the temperature, the service returns a message stating that there is no music available at the moment. (Implemented as needed)


## Core Technologies

1. **Backend**: Django (Python framework)
2. **Database**:
   - Primary: Choose one from SQLite, Postgres (based on project needs - consider scalability, features)
   - Secondary (optional): Redis (for caching, real-time messaging)
3. **Distributed Task Queue**: Celery (for asynchronous tasks)
4. **Message Broker**: Redis (coordinates communication between services)

## Development Environment

1. **Dependency Management**: Poetry (Python package manager)
2. **Containerization**: Docker (for packaging and deployment)
3. **Testing**:
   - Unit Testing:
     - Backend: Django Test Framework / pytest
   - Integration Testing: (Implemented as needed)
   - End-to-End Testing: (Implemented as needed) 
4. **CI/CD**: GitHub Actions (for automated builds, testing, and deployment)
5. **Deployment**: Cloud provider of choice (Heroku, AWS, GCP)
6. **Monitoring**: Sentry (error tracking) (optional) (Implemented as needed)
7. **Logging**: Django logging framework (centralized logging) (Implemented as needed)


## Backend

- **Framework**: Django (Python)
- **REST API Framework**: Django REST Framework (DRF)
- **OpenAPI Schema Generation**: drf-spectacular
- **Django Code Upgrade**: django-upgrade
- **Unique Correlation ID**: django-guid (Implemented as needed)
- **Database**: PostgreSQL (psycopg)
- **Error Monitoring**: Sentry (sentry-sdk) (Implemented as needed)
- **Environment Variables**: python-decouple
- **Background Worker Tasks**: Celery
- **Security**:
  - Content-Security-Policy: django-csp
  - Permissions-Policy: django-permissions-policy 
  - Brute Force Attack Prevention: django-defender (Implemented as needed)
- **Static Asset Serving**:
  - WhiteNoise


## Security

- Django security features (built-in protection)
- django-defender for blocking brute force attacks against login
- Implement essential security practices: CORS, CSRF protection, JWT authentication, HTTPS

## Developer Tools

- **Documentation**: Swagger or ReDoc (for API reference)
- **Version Control**: Git (source code management)
- **Code Review**: Pull requests on a platform like GitHub
- **Code Quality**: Linters/formatters (Ruff, Pylint, Flake8, ESLint, Black)
- **Static Code Analysis**: Bandit (Python security linter)
- **IDE**: PyCharm, WebStorm
- **Project Management**: GitHub Projects

## Communication and Collaboration

- **Communication tools**: (Implemented as needed)
- **Version control platform**: GitHub

## License

MIT License (permissive open-source license)


# Project Prerequisites and Setup for Development

This section outlines the prerequisites and setup steps for the project's development environment.  
If you don't use a container manager, you need to follow all the steps, 
some of which can be skipped if you do use a container manager.

## Python and pip Installation

- Check if Python 3.12 is installed on your system by running `python --version` or `python3 --version` in the terminal.
- If Python 3.12 is not installed, download it from the official website: [Python.org](https://www.python.org/).
- Pip, the Python package manager, is usually installed automatically with Python. 
- Verify its installation by running `pip --version` in the terminal. 
- If not installed, you can install it following the instructions in the official Python documentation.

## Poetry Installation

- Poetry is a dependency manager and packaging tool for Python projects. 
- Install Poetry by following the instructions in the official documentation: 
- [Poetry Installation](https://python-poetry.org/docs/#installation).
- After installation, verify Poetry's installation by running `poetry --version` in the terminal.

## Docker Installation

- Docker is a platform for developing, shipping, and running applications with containers. 
- Install Docker by following the instructions on the official website: 
- [Docker Installation](https://docs.docker.com/get-docker/).
- After installation, verify Docker's installation by running `docker --version` in the terminal.

## Database Configuration

- Depending on the chosen database (SQLite or PostgreSQL), you may need to install and configure it separately.
- For SQLite, no additional installation is usually required as it is a built-in library in Python.
- For PostgreSQL, follow the installation instructions in the official documentation: 
- [PostgreSQL Downloads](https://www.postgresql.org/download/).

## Redis Installation (Optional)

- If you choose to use Redis as a secondary database.
- Follow the installation instructions in the official documentation: [Redis Quick Start](https://redis.io/topics/quickstart).
- After installation, verify Redis's installation by running `redis-server --version` in the terminal.


Make sure that all the prerequisites are correctly installed and working 
before proceeding with the configuration and execution of the project.


If you are unable to configure the project, open an issue to explain why.

# Running the Project

- To make it easier to run the project we use the commands in the Makefile, and docker to make the environment easier.

## Setup

- To start the project we will use the settings contained in the .examples files 
- ### We start with .env.example

  If you are using Linux or Mac use the following command:

- for weather_api_service
  - `cp backend/weather_api_service/.env.example backend/weather_api_service/.env`
- for openai_service
  - `cp backend/openai_service/.env.example backend/openai_service/.env`
- for main_service
  - `cp backend/main_service/.env.example backend/main_service/.env`

  If you are using Windows use the following command:


- for weather_api_service
  - `copy backend\weather_api_service\.env.example backend\weather_api_service\.env` 
- for openai_service
  - `copy backend\openai_service\.env.example backend\openai_service\.env`
- for main_service
  - `copy backend\main_service\.env.example backend\main_service\.env` 

- ### Now we'll create our local django project settings.

  With local.py.example, these settings are not traced by github

  If you are using Linux or Mac use the following command:
- for weather_api_service
  - `cp backend/weather_api_service/settings/local.py.example`
- for openai_service
  - `cp backend/openai_service/settings/local.py.example` 
- for main_service  
  - `cp backend/main_service/settings/local.py.example` 

  If you are using Windows use the following command:
- for weather_api_service
  - `copy backend\weather_api_service\settings\local.py.example` 
- for openai_service
  - `copy backend\openai_service\settings\local.py.example`
- for main_service
  - `copy backend\main_service\settings\local.py.example` 

## With Docker Compose and Make File:

If you use windows, you can use the linux sub-system to help you with this task

Feel free to contribute by creating poetrys runs to fill in the Makefile commands and unify the systems.

- To start, open a new terminal in the project directory
- Run de make command to the initial setup: `make docker_setup`
- Run de make command to run the project: `make docker_up`


> [!NOTE]
> When you run make docker_up, Docker spawns several containers needed for the application to work, 
> including containers for the  backend and database. 
> Each of these containers will have its own port to communicate with the host.


🔥🔥🔥 Now you can access the project at http://localhost:8000 in your browser. 🔥🔥🔥


### Docker Compose Documentation:

This docker-compose.yml file defines and configures the services required to run an application composed of several interdependent microservices using Docker containers. The primary services include a PostgreSQL database, a RabbitMQ broker, a Redis result store, and three microservices (WeatherService, OpenIAService, and MainService) along with their respective Celery workers.

## Services

### 1. db

   - Image: postgres:alpine
   - Function: Database service using PostgreSQL.
   - Environment:
     - POSTGRES_USER: Database username (in this case, mini_blog).
     - POSTGRES_PASSWORD: Database password.
     - POSTGRES_DB: Name of the database to be created (in this case, mini_blog).
   - Ports:
     - 5432:5432: Mapping of the default PostgreSQL port.
   - Volumes:
     - dbdata:/var/lib/postgresql/data:delegated: Data persistence for PostgreSQL to ensure data is not lost when the container restarts.
  
### 2. broker

   - Image: rabbitmq:alpine
   - Function: Message broker service using RabbitMQ, responsible for managing the task queue for Celery.
   - Ports:
     - 5672:5672: The default port used by RabbitMQ for communication with Celery.

### 3. result

   - Image: redis:alpine
   - Function: Result store service using Redis, used to store the results of Celery tasks.
   - Ports:
     - 6379:6379: The default port of Redis.
   
### 4. weatherservice

   - Build:
     - Dockerfile: Dockerfile
     - Context: ./back_end/weather_api_service
   - Function: Main service providing the weather forecast API.
   - Ports:
     - 8801:8000: Port mapping where 8801 is the host port and 8000 is the container port.
   - Volumes:
     - ./back_end/weather_api_service:/home/user/app/: Synchronizes the local directory with the container directory.
   - Env File:
     - ./back_end/weather_api_service/.env: Environment variables configuration file.
   - Depends On:
     - db, broker, result: Specifies that the service depends on the db, broker, and result services to be running.
   
### 5. weatherservice_celery

   - Build:
     - Dockerfile: Dockerfile
     - Context: ./back_end/weather_api_service
   - Function: Celery worker for the WeatherService, responsible for processing background tasks.
   - Command:
     - celery --app=weather_api_service worker --loglevel=info: Command to start the Celery worker.
   - Volumes:
     - ./back_end/weather_api_service:/home/user/app/
   - Env File:
     - ./back_end/weather_api_service/.env
   - Depends On:
     - db, broker, result
     
### 6. openiaservice

   - Build:
     - Dockerfile: Dockerfile
     - Context: ./back_end/openai_service
   - Function: Main service providing the API for interacting with OpenAI.
   - Ports:
     - 8802:8000: Port mapping where 8802 is the host port and 8000 is the container port.
   - Volumes:
     - ./back_end/openai_service:/home/user/app/
   - Env File:
     - ./back_end/openai_service/.env
   - Depends On:
     - db, broker, result
     
### 7. openiaservice_celery
   - Build:
     - Dockerfile: Dockerfile
     - Context: ./back_end/openai_service
   - Function: Celery worker for the OpenIAService, responsible for processing background tasks.
   - Command:
     - celery --app=openai_service worker --loglevel=info
   - Volumes:
     - ./back_end/openai_service:/home/user/app/
   - Env File:
     - ./back_end/openai_service/.env
   - Depends On:
     - db, broker, result
     
### 8. mainservice
   - Build:
     - Dockerfile: Dockerfile
     - Context: ./back_end/main_service
   - Function: Main service providing the core API for the application.
   - Ports:
     - 8803:8000: Port mapping where 8803 is the host port and 8000 is the container port.
   - Volumes:
     - ./back_end/main_service:/home/user/app/
   - Env File:
     - ./back_end/main_service/.env
   - Depends On:
     - db, broker, result
     
### 9. mainservice_celery
   - Build:
     - Dockerfile: Dockerfile
     - Context: ./back_end/main_service
   - Function: Celery worker for the MainService, responsible for processing background tasks.
   - Command:
     - celery --app=main_service worker --loglevel=info
   - Volumes:
     - ./back_end/main_service:/home/user/app/
   - Env File:
     - ./back_end/main_service/.env
   - Depends On:
     - db, broker, result
   - Volumes
     - dbdata
       - Name: weather_mvp_dbdata
       - Function: Volume to store PostgreSQL database data, ensuring data persistence.


## Without Docker and Make File: (for each service)

### Setup Backend (for each service)

- To start, open a new terminal in the project directory
- Run the following command to install the dependencies: `poetry install`
- Activate the virtual environment: `poetry shell`
- Go to the backend directory: `cd backend`

### Run Backend (for each service)

- Create the migrations: `poetry run python manage.py makemigrations`
- Apply the migrations: ` poetry run python manage.py migrate`
- Generate a superuser: `poetry run python manage.py createsuperuser`
- Run the following command to start the backend server: `poetry run python manage.py runserver`


### Setup Celery (for each service)

- To start, open a new terminal in the project directory
- Run the following command to start the celery worker: `celery -A mini_blog worker -l info`

### Setup Redis (for each service)

- Make sure you have Redis installed on your system.
- To start, open a new terminal in the project directory
- Run the following command to start the redis server: `redis-server --port 6379`
- If you have a password set for your Redis server, you can provide it using the --requirepass option.
- For example: `redis-server --port 6379 --requirepass your_password`



### Testing (for each service)

- To run the tests, you can use the following command: `poetry run pytest`
- This command will run the tests in the project and display the results in the terminal.
- You can also run specific tests by providing the path to the test file or test case you want to run.
- For example: `poetry run pytest backend/(service)/tests/test_views.py`
- This command will run the tests in the test_views.py file and display the results in the terminal.
- To use django test runner, you can use the following command: `poetry run python manage.py test --keepdb --parallel`
- This command will run the tests in the project using the Django test runner and display the results in the terminal.
- You can use make to run the tests in the project: `make test` you need to pass a path to the module you want to test.
- Example: `make test someapp.tests.test_views`
- You can use another make command to run the tests in the project: `make test_all_modules` you not need to 
- pass a path to the module you want to test.

### API Schema and Client Generation (Implemented as needed)
- You can utilize the DRF-Spectacular tool to generate an OpenAPI schema from our Django Rest Framework (DRF) API. 
- This schema serves as the foundation for various tasks such as generating client code and creating comprehensive API documentation.
- You can access the API documentation pages at the following URLs:
- Swagger UI: http://localhost:8000/api/schema/swagger-ui/
- ReDoc: http://localhost:8000/api/schema/redoc/


## Project references

- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [React](https://reactjs.org/)
- [Poetry](https://python-poetry.org/)
- [Docker](https://www.docker.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [Redis](https://redis.io/)
- [Celery](https://docs.celeryproject.org/en/stable/)
- [Swagger](https://swagger.io/)
- [ReDoc](https://redoc.ly/)
- [DRF-Spectacular](https://drf-spectacular.readthedocs.io/en/latest/)
- [Django Guid](https://github.com/snok/django-guid)
- [Django CSP](https://django-csp.readthedocs.io/en/latest/)
- [Django Permissions Policy](https://github.com/adamchainz/django-permissions-policy)
- [Django Defender](https://github.com/jazzband/django-defender)
- [WhiteNoise](https://whitenoise.readthedocs.io/en/latest/)
- [GitHub Actions](https://docs.github.com/en/actions)
- [Sentry](https://sentry.io/)
- [Bandit](https://bandit.readthedocs.io/en/latest/)
- [PyCharm](https://www.jetbrains.com/pycharm/)
- [WebStorm](https://www.jetbrains.com/webstorm/)
- [GitHub Projects](https://docs.github.com/en/issues/organizing-your-work-with-project-boards/about-project-boards)
- [MIT License](https://opensource.org/licenses/MIT)
- [Ruff](https://ruff.readthedocs.io/en/latest/)

### Book references and articles

- [Zen of Python](https://www.python.org/dev/peps/pep-0020/)
- [Clean Code](https://www.amazon.com.br/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882)
- [Clean Architecture](https://www.amazon.com.br/Clean-Architecture-Craftsmans-Software-Structure/dp/0134494164)
- [TDD](https://www.amazon.com.br/Test-Driven-Development-Kent-Beck/dp/0321146530)
- [Refactoring](https://www.amazon.com.br/Refactoring-Improving-Design-Existing-Code/dp/0134757599)
- [Design Patterns](https://www.amazon.com.br/Design-Patterns-Elements-Reusable-Object-Oriented/dp/0201633612)
- [PMBOK](https://www.pmi.org/pmbok-guide-standards/foundational/pmbok)


# Feel free to contribute to this article. 🗿
