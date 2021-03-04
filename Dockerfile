FROM python:3.8
COPY requirements.txt /
RUN pip install -r requirements.txt
COPY views_time_caster/* /views_time_caster/
WORKDIR /views_time_caster
CMD ["gunicorn","-k","uvicorn.workers.UvicornWorker","--bind","0.0.0.0:80","app:app"]
