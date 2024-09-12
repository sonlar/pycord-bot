import json
import os
keys = ["epic"]
sub_keys = [["timestamp", "discord_timestamp"]]

# Check if Folder "pics" exists
if not os.path.isdir("pics"):
    os.mkdir("pics")

# Check if data.json exists
if not os.path.isfile("data.json"):
    with open("data.json", "w") as f:
        json.dump({}, f)

# Check if epic key exists
with open("data.json", "r") as f:
    data = json.load(f)
for pos,key in enumerate(keys):
    if not key in data:
        data[key] = {}
    for sub_key in sub_keys[pos]:
        if not sub_key in data[key]:
            data[key][sub_key] = ""
    
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

print("check done")
