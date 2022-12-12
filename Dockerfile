FROM python:3.8.16-slim
ENV TZ="Europe/Paris"
RUN apt-get update
RUN apt install -y git

WORKDIR IHM_recoCAM
RUN git clone https://github.com/Fefel76/IHM_recoCAM.git



RUN pip3 install -r requirements.txt

WORKDIR app

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
CMD ["/bin/bash"]