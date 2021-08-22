FROM python:3.7.10-slim

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY /BAIron /BAIron
COPY /backend /backend
COPY /NLP /NLP

COPY manage.py .
COPY db.sqlite3 .
COPY .env .

COPY shakespeare_sonnets.txt .
COPY ginsberg.txt .
COPY cummings.txt .

EXPOSE 8000

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
RUN python3 manage.py create_admin
RUN python3 manage.py save_poems

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

