#!/usr/bin/env -P /usr/bin:/usr/local/bin python3 -B
# coding: utf-8

#
#  main.py
#  test_agent_01 version 1.0
#  Created by Ingenuity i/o on 2023/11/18
#

import sys
import ingescape as igs

#inputs
def input_callback(iop_type, name, value_type, value, my_data):
    # call main_agent service here
    arguments_list = (value_type, value)
    igs.service_call("main_agent", "waitMessage", arguments_list, "")

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
    igs.definition_set_description("""test main_agent services""")
    igs.log_set_console(True)
    igs.log_set_file(True, None)
    igs.set_command_line(sys.executable + " " + " ".join(sys.argv))

    igs.input_create("text", igs.STRING_T, None)

    igs.observe_input("text", input_callback, None)

    igs.output_create("whiteboard_message", igs.STRING_T, None)

    igs.start_with_device(sys.argv[2], int(sys.argv[3]))

    input()

    igs.stop()

