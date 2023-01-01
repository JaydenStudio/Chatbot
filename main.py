import os
import math
import webbrowser
import time
print("Tips: Enter help to start the help process")
while True:
    msg = input("chat>")
    if msg == "" or msg == "Hello!" or msg == "hello!" or msg == "Hello" or msg == "hello" or msg == "Hi" or msg == "hi" or msg == "hi!" or msg == "Hi!":
        print("[bot]Hello!I'm a bot")
    elif msg == "e" or msg == "E":
        print(f"[bot]{math.e}")
    elif msg == "Pi" or msg == "pi" or msg == "pI":
        print(f"[bot]{math.pi}")
    elif msg == "help" or msg == "Help":
        os.system("start python help.py")
    elif msg == "Github" or msg == "github":
        webbrowser.open("http://github.com/")
    elif msg == "google" or msg == "Google":
        webbrowser.open("http://google.com")
    elif msg == "sleep" or msg == "Sleep":
        slps = input("[bot]sleep second:")
        try:
            time.sleep(int(slps))
        except ValueError:
            print("[bot]ValueError")
    elif msg == "What is github" or msg == "what is Github" or msg == "what is Github" or msg == "What is Github?" or msg == "What is github?" or msg == "What is Github?":
        print("[bot]GitHub is a web-based hosting service for version control using Git. It is mostly used for computer code. It offers all of the distributed version control and source code management (SCM) functionality of Git as well as adding its own features. It provides access control and several collaboration features such as bug tracking, feature requests, task management, and wikis for every project.")
    elif msg == "What is base64?" or msg == "what is base64?":
        print("[bot]Base64 is a type of encoding that is used to represent binary data in an ASCII string format. It is often used to encode binary data such as images, audio, and video files so that they can be transferred over the internet. It is also used to store passwords and other sensitive information in a secure format.")
    elif msg == "bye" or msg == "Bye":
        print("[bot]Bye~")
        exit()
    else:
        print("[bot]Sorry,I understand you.")