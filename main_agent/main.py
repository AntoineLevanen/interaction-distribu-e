#!/usr/bin/env -P /usr/bin:/usr/local/bin python3 -B
# coding: utf-8

#
#  main.py
#  main_agent version 1.0
#  Created by Ingenuity i/o on 2023/11/18
#

import sys
import ingescape as igs

def processMessage(message : str) -> str:
    """
    Take a message formated like this "hour # user name # message"
    and reformat it to be print on the whiteboard

    # print(message)
    split_message = message.split("#")
    # print(split_message)
    return str(split_message[0] + "\n" + split_message[1] + " : " + split_message[2])"""
    return message


def parameter_callback(iop_type, name, value_type, value, my_data):
    pass
    # add code here if needed

def service_callback(sender_agent_name, sender_agent_uuid, service_name, arguments, token, my_data):
    """
    Service called by agent to send message to whiteboard
    arguments : list, [0]: data type, [1]: data
    """
    # check if service called is the right one

    print("argument list : ", arguments)

    if arguments[0] == '0': # add a user message
        print("send a message")
        igs.output_set_string("user_message", processMessage(arguments[1]))

    elif arguments[0] == '1': # add an image on the white board
        # print("display an image")
        image = str(arguments[1])
        igs.service_call("Whiteboard", "addImageFromUrl", (image, 250, 250), "")

    elif arguments[0] == '2': # add a note on the whiteboard
        # print("display a text note")
        igs.service_call("Whiteboard", "addText", (str(arguments[1]), 100, 150, "blue"), "")


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
    igs.log_set_console(True)
    igs.log_set_file(True, None)
    igs.set_command_line(sys.executable + " " + " ".join(sys.argv))

    igs.parameter_create("message_counter", igs.INTEGER_T, None)
    igs.parameter_create("max_message_displayed", igs.INTEGER_T, None)
    igs.parameter_create("clear_displayed_message", igs.BOOL_T, None)

    igs.output_create("user_message", igs.STRING_T, None)

    igs.observe_parameter("message_counter", parameter_callback, None)
    igs.observe_parameter("max_message_displayed", parameter_callback, None)
    igs.observe_parameter("clear_displayed_message", parameter_callback, None)

    igs.service_init("waitMessage", service_callback, None)
    igs.service_arg_add("waitMessage", "user_name", igs.STRING_T)
    igs.service_arg_add("waitMessage", "user_message", igs.STRING_T)

    igs.start_with_device(sys.argv[2], int(sys.argv[3]))

    input()

    igs.stop()