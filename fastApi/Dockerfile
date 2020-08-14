FROM tiangolo/uvicorn-gunicorn:python3.7

RUN mkdir /fastApi

COPY requirements.txt /fastApi

WORKDIR /fastapi

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /fastApi

WORKDIR /fastApi/Gender

EXPOSE 8000

#CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]
CMD uvicorn main:app --host 0.0.0.0 --port $PORT
#Run en local docker-compose
#CMD uvicorn main:app --host 0.0.0.0 --port 8000