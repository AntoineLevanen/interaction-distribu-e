import os
import sys, getopt
import threading
import argparse

def taskOne(python_i, device, port):
    os.system(f"{python_i} main_agent/main.py main_agent {device} {port}")
    
def taskTwo(python_i, device, port):
    os.system(f"{python_i} User/main.py User {device} {port}")


if __name__ == "__main__":
    
    try: # get args
        python = sys.argv[1]
        device = sys.argv[2]
        port = sys.argv[3]
    except: # display the help message
        print("Help : add your python exe file path, your wi-fi device and the choose port, finally the number of user")
        print("example : python3 main.launch.py python3 wlo1 5670 1")
        sys.exit(1)

    # launch the main_agent in a thread
    thread_01 = threading.Thread(target=taskOne, args=(python, device, port))
    thread_01.start()


    # launch 1 or more User agents in separated thread
    try:
        for _ in range(int(sys.argv[4])):
            thread_02 = threading.Thread(target=taskTwo, args=(python, device, port))
            thread_02.start()
    except:
        print("Can't add multiple User agent")
        sys.exit(2)

    thread_01.join()
    thread_02.join()  