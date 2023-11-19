import os
import threading
import subprocess

def taskOne():
    # os.system("sh /opt/Ingescape-Circle/Ingescape-Circle.sh")
    subprocess.run(['sh /opt/Ingescape-Circle/Ingescape-Circle.sh'])
def taskTwo():
    os.system("sh /opt/Whiteboard/Whiteboard.sh --port 5670")

def taskThree():
    os.system("python main_agent/main.py main_agent Wi-Fi 5670")
    
def taskFour():
    os.system("python User/main.py User Wi-Fi 5670")


if __name__ == "__main__":

    #thread_01 = threading.Thread(target=taskOne)
    # thread_01.start()

    #thread_02 = threading.Thread(target=taskTwo)
    # thread_02.start()

    thread_03 = threading.Thread(target=taskThree)
    thread_03.start()

    thread_04 = threading.Thread(target=taskFour)
    thread_04.start()

    #thread_01.join()
    #thread_02.join()
    thread_03.join()
    thread_04.join()  