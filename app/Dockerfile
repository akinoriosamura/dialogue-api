FROM tiangolo/uvicorn-gunicorn-fastapi:python3.6

ENV LISTEN_PORT 5231
ENV PORT 5231
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

EXPOSE 5231

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    wget build-essential gcc zlib1g-dev git  \
    vim \
    libsm6 \
    libxrender1 \
    libxext6

# workdirの指定
WORKDIR /app

# 依存Pythonライブラリ一覧コピー
COPY . .

# install pipenv
RUN pip install -U pip && \
    pip install pipenv && \
    pipenv install --system

WORKDIR /app/ParlAI

RUN python setup.py develop

WORKDIR /app
