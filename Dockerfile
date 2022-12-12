FROM python:3.8.16-slim
ENV TZ="Europe/Paris"
RUN apt-get update
RUN apt install -y git

RUN git clone https://github.com/Fefel76/IHM_recoCAM.git

WORKDIR IHM_recoCAM

RUN pip3 install -r requirements.txt

RUN groupadd -r user && useradd -r -g user user && RUN chown -R user:user *
USER user

WORKDIR app

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
CMD ["/bin/bash"]