FROM python:3.7.3

WORKDIR /app

COPY . .

RUN conda env create -f environment.yml
RUN conda activate poc_to_prod_env

EXPOSE 5000

CMD ["python", "app.py" ]
