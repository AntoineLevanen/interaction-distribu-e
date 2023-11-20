#!/usr/bin/env -P /usr/bin:/usr/local/bin python3 -B
# coding: utf-8

#
#  main.py
#  controler version 1.0
#  Created by Ingenuity i/o on 2023/11/19
#

import sys
import ingescape as igs

def process_information(message:str) : #"hour # user name # message"
    hour,user, msg = message.split("#")

#inputs
def input_callback(iop_type, name, value_type, value, my_data):
    hour,user,msg = process_information(value)
    
    #première sortie -> pour aller au whiteboard 
    igs.output_set_string("processed_str", user+ " à "+ hour + " : "+msg)
    
    #deuxième sortie : on va envoyer au chatbot la msg pour la traiter
    igs.output_set_string("chatbot_str", user+"#"+msg)
    

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("usage: python3 main.py agent_name network_device port")
        devices = igs.net_devices_list()
        print("Please restart with one of these devices as network_device argument:")
        for device in devices:
            print(f" {device}")
        exit(0)

    igs.agent_set_name(sys.argv[1])
    igs.definition_set_version("1.0")
    igs.definition_set_description("""recevoir le message utilisateur et le traiter pour le chatbot
""")
    igs.log_set_console(True)
    igs.log_set_file(True, None)
    igs.set_command_line(sys.executable + " " + " ".join(sys.argv))

    igs.input_create("raw_str", igs.STRING_T, None)

    igs.output_create("processed_str", igs.STRING_T, None) #changer
    igs.output_create("chatbot_str", igs.STRING_T, None) #changer

    igs.observe_input("raw_str", input_callback, None)

    igs.start_with_device(sys.argv[2], int(sys.argv[3]))

    input()

    igs.stop()

