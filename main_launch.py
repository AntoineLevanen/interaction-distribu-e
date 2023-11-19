import os
import sys, getopt
import threading
import argparse

def taskOne(python_i, device, port):
    os.system(f"{python_i} main_agent/main.py main_agent {device} {port}")
    
def taskTwo(python_i, device, port):
    os.system(f"{python_i} User/main.py User {device} {port}")


if __name__ == "__main__":
    

    try:
        python = sys.argv[1]
        device = sys.argv[2]
        port = sys.argv[3]
    except:
        print("Help : add your python exe file path, your wi-fi device and the choose port")
        print("example : python3 main.launch.py python3 wlo1 5670")
        sys.exit(1)


    

    

    thread_01 = threading.Thread(target=taskOne, args=(python, device, port))
    thread_01.start()

    thread_02 = threading.Thread(target=taskTwo, args=(python, device, port))
    thread_02.start()

    thread_01.join()
    thread_02.join()  