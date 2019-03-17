FROM node:alpine as vue_builder

WORKDIR /app

COPY central-ui/package.json package.json

RUN npm install

COPY central-ui/ .

RUN npm run build

# =========================================== #

FROM python:3.6.4

WORKDIR /app

RUN pip install pipenv

COPY Pipfile .

COPY Pipfile.lock .

RUN pipenv install --system --deploy

COPY . .

COPY --from=vue_builder /app/dist .
