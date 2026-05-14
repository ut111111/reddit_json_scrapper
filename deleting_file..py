""" operator 3 """
""" use this file to clear the data of main reddit_data.json """


import json

    # Load JSON file
with open("reddit_data.json", "r",encoding="utf-8") as file:
        data = json.load(file)

    # Delete a key
del data["post_data"]

    # Save back to file
with open("reddit_data.json", "w",encoding="utf-8") as file:
        json.dump(data, file, indent=4)