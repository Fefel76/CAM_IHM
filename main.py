import time
import logging
from flask import Flask, render_template, request
import requests
from requests.exceptions import HTTPError
from confidentialTapo import privacyTapo
import pickle

logging.basicConfig(level=logging.DEBUG, filename="./log/IHM.log", filemode="w",format='%(asctime)s -- %(funcName)s -- %(process)d -- %(levelname)s -- %(message)s')

logging.info("Flask démarré")
app= Flask(__name__)
pickle.dump("on", open("videos/record.txt", "wb"))
# Variables générales
ListSMS = {"Maribel": "checked", "Biquet": "checked", "Fouine": "checked"}

# fonction api
def call_api(url):
    try:

        response = requests.get(url)
        response.raise_for_status()
        logging.debug("Requête : %s \n Statut : %s \n ", url, response.status_code)

        # Gestion des exceptions
    except HTTPError as http_err:
        logging.error(f'HTTP error occurred: {http_err}')
        return response.status_code
    except Exception as err:
        logging.error(f'Other error occurred: {err}')
        return response.status_code
    else:
        logging.info('Appel réussi de la requête : %s', url)
        return response.status_code, response.content
#Simulateur de l'API de gestion de detection



@app.route("/")
def hello():
    status = getStatus()

    return render_template('index.html', status=status, ListSMS=ListSMS)


@app.route("/detection/status", methods=['GET'])
def getStatus():

    with open('videos/record.txt', 'rb') as f:
        record = pickle.load(f)

    return record


@app.route("/listsms", methods=['GET'])
def listSMS():
    if not(request.args.getlist("sms1")):
        ListSMS["Maribel"]=""
    else:
        ListSMS["Maribel"] = "checked"

    if not(request.args.getlist("sms2")):
        ListSMS["Biquet"]=""
    else:
        ListSMS["Biquet"]="checked"

    if not(request.args.getlist("sms3")):
        ListSMS["Fouine"]=""
    else:
        ListSMS["Fouine"] = "checked"

    logging.debug("Checked", ListSMS)

    status = getStatus()
    return render_template('index.html', status=status, ListSMS=ListSMS)

@app.route("/sms", methods=['GET'])
def getSMS():

    try:
        msg=request.args.get("msg")
    except:
        msg="test par défaut"

    logging.debug("Message reçu :", msg)


    #Maribel
    if ListSMS["Maribel"]=="checked":
        logging.info("Envoi SMS à Maribel : %s", msg)
        call_api("https://smsapi.free-mobile.fr/sendmsg?user=20209358&pass=wIpQpxTkNSSP0P&msg="+msg)

    #Biquet
    if ListSMS["Biquet"] == "checked":
        logging.info("Envoi SMS à Biquet : %s", msg)
        call_api("https://smsapi.free-mobile.fr/sendmsg?user=99937527&pass=pVMGAXaYQLNllS&msg="+msg)

    #Fouine
    if ListSMS["Fouine"] == "checked":
        logging.info("Envoi SMS à Fouine : %s", msg)
        call_api("https://smsapi.free-mobile.fr/sendmsg?user=20226894&pass=HIh0RvwSUqE80x&msg="+msg)

    status = getStatus()
    return render_template('index.html', status=status, ListSMS=ListSMS)


@app.route("/detection/start", methods=['GET'])
def getStart():


    try:
        privacyTapo(False)
    except:
        logging.error("Erreur lors de l'appel fonction privacy de TAPO")

    time.sleep(5)  # décompte de 5 secondes avant activation

    try:

        pickle.dump("on", open("videos/record.txt", "wb"))
    except:
        logging.error("Erreur Pickle pour activer")
    else:
        logging.info("Activation option RECORD")

    call_api("http://localhost:5000/sms?msg=Activation%20des%20caméras")

    status=getStatus()
    return render_template('index.html',status=status, ListSMS=ListSMS)

@app.route("/detection/pause", methods=['GET'])
def getPause():


    try:
        privacyTapo(True)
    except:
        logging.debug("Erreur lors de l'appel fonction privacy de TAPO")

    time.sleep(1)
    try:
        pickle.dump("off", open("videos/record.txt", "wb"))
    except:
        logging.error("Erreur Pickle pour desactiver")
    else:
        logging.info("Désactivation option RECORD")

    call_api("http://localhost:5000/sms?msg=Désactivation%20des%20caméras")

    status = getStatus()
    return render_template('index.html', status=status, ListSMS=ListSMS)

if __name__=='__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)

