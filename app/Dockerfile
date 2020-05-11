FROM tiangolo/uvicorn-gunicorn-fastapi:python3.6

RUN apt-get update

# workdirの指定
WORKDIR /app

# 依存Pythonライブラリ一覧コピー
COPY . .

# install pipenv
RUN pip install -U pip && \
    pip install pipenv && \
    pipenv install --system

# WORKDIR /app/ParlAI
# 
# RUN python setup.py develop
# 
# WORKDIR /app
