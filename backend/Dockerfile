FROM python:3.10

WORKDIR /backend

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /backend/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /backend/

# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
