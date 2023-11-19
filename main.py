#!/usr/bin/python3

import os
import threading
import subprocess

def taskOne():
    # os.system("sh /opt/Ingescape-Circle/Ingescape-Circle.sh")
    subprocess.run(['sh /opt/Ingescape-Circle/Ingescape-Circle.sh'])

def taskTwo():
    os.system("sh /opt/Whiteboard/Whiteboard.sh --port 5671")
def taskThree():
    os.system("python3 main_agent/main.py main_agent wlo1 5671")
def taskFour():
    os.system("python3 User/main.py User wlo1 5671")


if __name__ == "__main__":

    thread_01 = threading.Thread(target=taskOne)
    # thread_01.start()

    thread_02 = threading.Thread(target=taskTwo)
    # thread_02.start()

    thread_03 = threading.Thread(target=taskThree)
    thread_03.start()

    thread_04 = threading.Thread(target=taskFour)
    thread_04.start()

    thread_01.join()
    thread_02.join()
    thread_03.join()
    thread_04.join()  