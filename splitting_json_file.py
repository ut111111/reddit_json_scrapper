"""operator 2 """
""" after using operator 1 use this file as the format is json so it will take upto 5k posts only """
import json

with open("reddit_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

post_data = data["post_data"]
after_data = data["after_data"]

chunk_size = 1000

for i in range(0, len(post_data), chunk_size):
    chunk = post_data[i:i + chunk_size]

    split_data = {
            "post_data": chunk,
            "after_data": after_data
        }

    filename = f"split_{i // chunk_size + 11}.json"

    with open(filename, "w", encoding="utf-8") as out:
            json.dump(split_data, out, indent=2)

    print(f"Saved {filename}")