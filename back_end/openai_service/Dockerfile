FROM python:3.12-slim

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.7.1

RUN groupadd user && useradd --create-home --home-dir /home/user -g user user

# Install system dependencies
RUN apt-get update && apt-get install python3-dev gcc build-essential libpq-dev -y

# Install poetry
RUN pip install "poetry==$POETRY_VERSION"

# Copy the entire project to the working directory
COPY . /home/user/app/

WORKDIR /home/user/app/

# Install dependencies
RUN poetry config virtualenvs.create false
RUN poetry install --with dev --no-root --no-interaction --no-ansi

USER user

# Define the entry point
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
