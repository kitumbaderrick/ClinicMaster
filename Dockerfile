FROM python:slim-bullseye

WORKDIR /ClinicMaster

COPY requirements.txt  requirements.txt 

RUN pip install --upgrade pip

RUN pip install -r requirements.txt 

COPY . .

CMD ["python" ,"manage.py","runserver","0.0.0.0:8000"]