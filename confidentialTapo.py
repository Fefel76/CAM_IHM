from pytapo import Tapo
import logging
import os


def privacyTapo(enabled):

    try:
        user = os.environ.get('USER_CAM')
        password = os.environ.get('PWD_CAM')
        logging.info("++++++++++++++++++++++++recup env")
    except:
        logging.error("Erreur de récupération des variables d'environnements ")

    user='biquet.auger'
    password='kali3460'

    cam1 = "192.168.1.17"  # ip of the camera, example: 192.168.1.52
    cam2 = "192.168.1.15"  # ip of the camera, example: 192.168.1.52
    cam3 = "192.168.1.16"  # ip of the camera, example: 192.168.1.52


    try:
        garage = Tapo(cam2, "admin", password)
    except:
        logging.error("Erreur de connexion sur la caméra TAPO du Garage : @IP = %s et login=%s", cam2, user)

    try:
        piscine = Tapo(cam3, "admin", password)
    except:
        logging.error("Erreur de connexion sur la caméra de la Piscine")

    try:
        salon = Tapo(cam1, user, password)
    except:
        logging.error("Erreur de connexion sur la caméra du Salon")

    try:
        logging.debug("Etat Caméra du Garage : %s",garage.getBasicInfo())
        logging.debug("Etat Caméra de la Piscine : %s",piscine.getBasicInfo())
        logging.debug("Etat Caméra du Salon : %s",salon.getBasicInfo())
    except:
       logging.warning("Avertissement sur récupération état des caméras")


    if (enabled):
        try:
            garage.setPrivacyMode(True)

        except:
            logging.error("Erreur lors du passage en mode confidentiel de la caméra GARAGE")
        try:
            piscine.setPrivacyMode(True)
        except:
            logging.error("Erreur lors du passage en mode confidentiel de la caméra PISCINE")
        try:
            salon.setPrivacyMode(True)
        except:
            logging.error("Erreur lors du passage en mode confidentiel de la caméra SALON")
    else:
        try:
            garage.setPrivacyMode(False)
        except:
            logging.error("Erreur lors du passage en mode non onfidentiel de la caméra GARAGE")
        try:
            piscine.setPrivacyMode(False)
        except:
            logging.error("Erreur lors du passage en mode nonconfidentiel de la caméra PISCINE")
        try:
            salon.setPrivacyMode(False)
            logging.info("Salon prêt !")
        except:
            logging.error("Erreur lors du passage en mode non confidentiel de la caméra SALON")


