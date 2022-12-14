FROM mypython
#FROM python:3.8.16-slim
#ENV TZ="Europe/Paris"
#RUN apt-get update && apt install -y git

RUN git clone https://github.com/Fefel76/CAM_IHM.git
WORKDIR CAM_IHM
EXPOSE 5001
#création des répertoires
RUN mkdir ./log && mkdir ./videos && mkdir ./conf

RUN pip3 install -r requirements.txt
ENV FLASK_APP=main.py

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5001"]
