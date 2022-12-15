FROM python:3.8.16-slim
ENV TZ="Europe/Paris"
RUN apt-get update && apt install -y git

RUN git clone https://github.com/Fefel76/IHM_recoCAM.git
WORKDIR IHM_recoCAM/app

RUN mkdir ./log

RUN pip3 install -r requirements.txt
ENV FLASK_APP=main.py

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
