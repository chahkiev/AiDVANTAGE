FROM python:3-slim
LABEL author="Chahkiev Magomed"

RUN apt-get update && apt-get install -y \
    git \
    vim

WORKDIR /home/AiDVANTAGE
ADD . .

RUN pip3 install -r requirements.txt  && \
    python3 manage.py makemigrations && \
    python3 manage.py makemigrations DiseaseDetector && \
    python3 manage.py migrate

# ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:8000"]