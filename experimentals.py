'''This file is is experimental have some ai coded script 
may work for the intended task but better to use your own scripts for data filtering
and analysis'''



# from collections import Counter
# import json

# # Load your JSON file
# with open("reddit_data.json", "r", encoding="utf-8") as f:
#     data = json.load(f)

# # Replace this path if needed
# ids = data["after_data"]

# # Remove null values (None in Python)
# ids = [x for x in ids if x is not None]

# # Count occurrences
# counter = Counter(ids)

# # Repeated items only
# repeated = {k: v for k, v in counter.items() if v > 1}

# # Stats
# total = len(ids)
# unique = len(counter)
# duplicates_count = total - unique

# print(f"Total IDs: {total}")
# print(f"Unique IDs: {unique}")
# print(f"Repeated entries: {duplicates_count}")
# print(f"Unique repeated IDs: {len(repeated)}")

# print("\nRepeated IDs:")
# for k, v in repeated.items():
#     print(f"{k} -> {v} times")


# trash
# from collections import defaultdict
# import json
# import glob

# post_locations = defaultdict(list)

# files = glob.glob(
#     r"C:\Users\Aatanki\Documents\python_projects\data_reddit\*.json"
# )

# for file in files:
#     with open(file, "r", encoding="utf-8") as f:
#         data = json.load(f)

#         for idx, item in enumerate(data["post_data"]):

#             post_text = item.get("post", "").strip()

#             if post_text:
#                 post_locations[post_text].append(
#                     (file, idx)
#                 )

# # Print duplicates
# for text, locations in post_locations.items():

#     if len(locations) > 1:

#         print("\nDUPLICATE FOUND")
#         print("Repeated:", len(locations), "times")

#         print("\nLocations:")

#         for loc in locations[:10]:
#             print(loc)

#         print("\nPreview:")
#         print(text[:300])

#         print("=" * 100)

# this will tell where it first copied
# import json
# import glob

# seen = {}

# files = glob.glob(
#     r"C:\Users\Aatanki\Documents\python_projects\data_reddit\*.json"
# )

# total = 0

# for file in files:

#     with open(file, "r", encoding="utf-8") as f:
#         data = json.load(f)

#         for idx, item in enumerate(data["post_data"]):

#             total += 1

#             post_text = item.get("post", "").strip()

#             if not post_text:
#                 continue

#             if post_text in seen:

#                 print("\nFIRST DUPLICATE FOUND")
#                 print("Current File:", file)
#                 print("Current Index:", idx)

#                 print("\nOriginally Seen At:")
#                 print(seen[post_text])

#                 print("\nGlobal Position:", total)

#                 print("\nPreview:")
#                 print(post_text[:300])

#                 exit()

#             else:
#                 seen[post_text] = (file, idx)




# this one tell all the duplicates in folder


# import json
# import glob

# seen = set()

# files = glob.glob(
#     r"C:\Users\Aatanki\Documents\python_projects\data_reddit\*.json"
# )

# total = 0
# duplicates = 0

# for file in files:

#     with open(file, "r", encoding="utf-8") as f:
#         data = json.load(f)

#         for item in data["post_data"]:

#             total += 1

#             post_text = item.get("post", "").strip()

#             if not post_text:
#                 continue

#             if post_text in seen:
#                 duplicates += 1

#             else:
#                 seen.add(post_text)

#     print(
#         f"{file} | "
#         f"Total Seen: {total} | "
#         f"Unique: {len(seen)} | "
#         f"Duplicates: {duplicates}"
#     )


# from collections import Counter
# import json

# with open("reddit_data.json", "r", encoding="utf-8") as f:
#     data = json.load(f)

# posts = data["post_data"]

# ids = [post["title"] for post in posts]

# counter = Counter(ids)

# duplicates = {k: v for k, v in counter.items() if v > 1}

# print(duplicates)