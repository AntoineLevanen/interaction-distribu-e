#!/usr/bin/env -P /usr/bin:/usr/local/bin python3 -B
# coding: utf-8

#
#  main.py
#  main_agent version 1.0
#  Created by Ingenuity i/o on 2023/11/18
#

import sys
import ingescape as igs

def parameter_callback(iop_type, name, value_type, value, my_data):
    pass
    # add code here if needed

def service_callback(sender_agent_name, sender_agent_uuid, service_name, arguments, token, my_data):
    """
    Doc :
    """
    # check if service called is the right one
    if isinstance(arguments[0], str):
        igs.output_set_string("user_message", arguments[1])


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

