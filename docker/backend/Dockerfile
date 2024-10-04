FROM python:3.11

ENV DJANGODIR=/backend

RUN mkdir $DJANGODIR

WORKDIR $DJANGODIR

COPY pyproject.toml /$DJANGODIR/
COPY backend /$DJANGODIR
COPY questions /$DJANGODIR/questions

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-root