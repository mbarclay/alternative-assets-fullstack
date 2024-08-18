# use an official python runtime as a parent image
FROM python:3.12.4-slim

# install poetry
RUN pip install poetry

# set the working directory in the container
WORKDIR /app

# copy pyproject.toml, poetry.lock and the source code to the working directory
COPY pyproject.toml poetry.lock config.py settings.toml ./
COPY src ./src

# disable virtualenv creation by poetry and install dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# make port 8080 available to the world outside this container
EXPOSE 8080

# run the fastapi app using uvicorn when the container launches.
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]