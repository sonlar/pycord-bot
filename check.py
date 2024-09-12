import json
import os

# Check if Folder "pics" exists
if not os.path.isdir("pics"):
    os.mkdir("pics")

# Check if data.json exists
if not os.path.isfile("data.json"):
    with open("data.json"):
        pass
