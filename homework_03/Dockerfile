FROM python:3.9-buster
RUN pip install poetry
WORKDIR /app/
COPY poetry.lock pyproject.toml /app/
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi
COPY main.py /app/
EXPOSE 8000
CMD ["uvicorn", "--host=0.0.0.0", "main:app"]
