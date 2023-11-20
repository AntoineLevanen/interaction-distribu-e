#!/usr/bin/env -P /usr/bin:/usr/local/bin python3 -B
# coding: utf-8

#
#  main.py
#  chatbot version 1.0
#  Created by Ingenuity i/o on 2023/11/19
#

import sys
import ingescape as igs

import re
import queue
import threading
import time
import nltk
from nltk.chat.util import Chat, reflections
import json

### fonctions pour le chatbot

stop_flag = threading.Event()
queue_entrees = queue.Queue()
queue_sorties = queue.Queue()

chatbot_running = False
output_thread_running = False

# Initialisation de nltk
nltk.download('punkt')

# Définition des patterns et des réponses
patterns = [
    (r'@(.*)', ('Bonjour %1! Comment puis-je vous aider aujourd\'hui? \nEntrez \'aide\' pour vérifier vos actions possibles',)),
    (r'aide', ('\nVous pouvez consulter les informations concernant votre randonnée \nConsulter historique \nModifier une information \nVoir galerie \nConfirmer participation \nQuitter' ,)),
    (r'(.*)',("Action non reconnue (exemple : consulter l'horaire ou consulter historique horaires) ")),
]
# Création du chatbot
chatbot = Chat(patterns, reflections)

def open_informations() :
    # Charger les données existantes depuis le fichier
    try:
        with open('informations.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        # Le fichier n'existe pas encore, initialisez-le avec un dictionnaire vide
        data = {}
        
    return data

# Fonction pour stocker les informations
def stocker_informations(topic, valeur):

    data = open_informations()
    # Vérifier si le topic existe déjà dans les données
    if topic not in data:
        data[topic] = []

    # Ajouter la nouvelle valeur au topic
    data[topic].append(valeur)

    # Écrire les données mises à jour dans le fichier
    with open('informations.json', 'w') as file:
        json.dump(data, file)

# Fonction pour récupérer toutes les valeurs d'un topic
def recuperer_informations(topic):
    try:
        with open('informations.json', 'r') as file:
            data = json.load(file)
            if topic in data:
                return data[topic]
            else:
                return []
    except FileNotFoundError:
        return []
        
def consulter(info,historique) :
    try :
        all_info = recuperer_informations(info)
        mod_info = ""
        
        if historique and all_info != None:
            for i in all_info :
                mod_info = mod_info + "\n"+ i+"\n"
            queue_sorties.put(mod_info)
            
        elif historique == False and all_info != None :
            
            if info == "participants" :
                for i in all_info :
                    mod_info = mod_info + "\n"+ i+"\n"
                queue_sorties.put(mod_info)
                
            else :
                last_info = all_info[-1] if all_info else None
                last_info = info + " par " + last_info
                queue_sorties.put(last_info)
                
        else :
            queue_sorties.put("vous n'avez pas de rando prévue ! ")
            
    except :
        queue_sorties.put("there is no data related to the given topic")
    
def modifier(top,info,user):
    new_info = user+"\n"+ info
    stocker_informations(top, new_info)

    
def confirmer_participation(user):
    #on vérifie que la partici
    
    participants = recuperer_informations("participants")
    confirmee = user in participants
    
    if confirmee :
        queue_sorties.put("vous êtes déjà confirmé")
    
    else :
        stocker_informations("participants", user)
        queue_sorties.put("participation confirmée")

#a faire ?
def open_photos() :
    print("")

def chatbot_principal(queue_entrees, queue_sorties):
    ##récupérer 
    
    while True:
        msg = queue_entrees.get()
        utilisateur_conn,utilisateur_input = msg.split("#")


        if utilisateur_input.lower() == 'exit' or utilisateur_input.lower() == 'quitter':
            queue_sorties.put("Au revoir !")
            break
        else:
            match1 = re.match(r'je veux consulter (.*)', utilisateur_input)
            match2 = re.match(r'consulter (.*)', utilisateur_input)
            match3 = re.match(r'je veux modifier (.*)', utilisateur_input)
            match4= re.match(r'modifier (.*)', utilisateur_input)  
               
               #match5 = re.match(r'consulter historique (.*)', utilisateur_input) 
               
            match6 = re.match(r'voir photos (.*)', utilisateur_input) 
            match7 = re.match(r'voir galerie (.*)', utilisateur_input) 
    
            match8 = re.match(r'confirmer participation', utilisateur_input) 
            match9 = re.match(r'participer', utilisateur_input)

            if match1 or match2:
                info = match2.group(1)
                hist = False
                if "historique" in info:
                    info = info.split(" ")[1]
                    hist = True
                consulter(info, hist)

            elif match3 or match4:
                topic = match4.group(1)
                queue_sorties.put(f"Nouvelle information pour {str(topic)} : ")
                msg = queue_entrees.get()
                utilisateur_conn, new_info = msg.split("#")
                modifier(topic, new_info, utilisateur_conn)
                queue_sorties.put("modification faite !")

            elif match6 or match7:
                open_photos()
                queue_sorties.put("")
            
            elif match8 or match9:
                confirmer_participation(utilisateur_conn)
            else:
                response = chatbot.respond(utilisateur_input)
                queue_sorties.put(response)
                

def get_output():
    while not stop_flag.is_set() : 
        if not queue_sorties.empty():
            output = queue_sorties.get()
            igs.output_set_string("answer",output)
            if output == "Au revoir !" :
                chatbot == False
                output_thread_running = False
                stop_flag.set()
                
                
#inputs
def input_callback(iop_type, name, value_type, value, my_data):
    ### value = user#msg
    queue_entrees.put(value)
    

if __name__ == "__main__":
    
    # Créer la thread pour le traitement asynchrone des entrées
    ##il faut lancer le thread une seul fois - variable globale pour dire si c'est lancé ou pas
    if not chatbot_running :
        thread_entrees = threading.Thread(target=chatbot_principal, args=(queue_entrees, queue_sorties), daemon=True)
        thread_entrees.start()
        thread_entrees.join()

    if not output_thread_running :
        thread_outputs = threading.Thread(target=get_output, args=(queue_sorties,), daemon=True)
        thread_outputs.start()
        thread_outputs.join()

    
    if len(sys.argv) < 4:
        print("usage: python3 main.py agent_name network_device port")
        devices = igs.net_devices_list()
        print("Please restart with one of these devices as network_device argument:")
        for device in devices:
            print(f" {device}")
        exit(0)

    igs.agent_set_name(sys.argv[1])
    igs.definition_set_version("1.0")
    igs.log_set_console(True)
    igs.log_set_file(True, None)
    igs.set_command_line(sys.executable + " " + " ".join(sys.argv))

    igs.input_create("str_input", igs.STRING_T, None)

    igs.output_create("answer", igs.STRING_T, None)

    igs.observe_input("str_input", input_callback, None)

    igs.start_with_device(sys.argv[2], int(sys.argv[3]))

    input()

    igs.stop()

