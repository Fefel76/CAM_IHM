FROM python:3.8.16-slim
ENV TZ="Europe/Paris"
RUN apt-get update && apt install -y git

RUN git clone https://github.com/Fefel76/IHM_recoCAM.git
WORKDIR IHM_recoCAM/app

RUN pip3 install -r requirements.txt

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
