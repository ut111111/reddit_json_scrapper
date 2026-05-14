
'''operator 1'''

'''this script is the main first understand before trying as they are not proessional 
use this and respect the rate limit it is used only for leanring purpose not intended to use for 
personal scrapping  '''
import requests
import time
import json
import random
from pathlib import Path




url = "https://www.reddit.com/r/subreddit_name/.json"

file_path = Path("reddit_data.json")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

params = {
    "limit" : "25",
    "after" : None
}


meta_data_list = []
after_list = []

# try:
#     if params["after"] is None:
#         if file_path.exists():
#             with open ("reddit_data.json","r",encoding="utf-8") as f:
#                 data = json.load(f)
#                 if data["after_data"][-1] is None:
#                      params["after"] = data["after_data"][-2]
#                 elif data["after_data"][-2] is None:
#                      params["after"] = data["after_data"][-3]
#                 elif data["after_data"][-3] is None:
#                      print ("data repeating")
                
#                 else:    
#                  params["after"] = data["after_data"][-1]


# except:
#     pass


i = 0

while True:

        res = requests.get(url,headers=headers,params=params).json()

        meta_data = res["data"]["children"]


        after = res["data"]["after"]
        

        for content in meta_data: 

            json_dict = {}    

            title = content["data"]["title"]
            json_dict["title"] = title
                
            label = content["data"]["link_flair_text"]
            json_dict["label"] = label

            post = content["data"]["selftext"]
            json_dict["post"] = post

            upvote = content["data"]["ups"]
            json_dict["upvote"] = upvote

            meta_data_list.append(json_dict)
            
                
        
        params["after"] = after
        


        after_list.append(after)



        print(f"page {i} scraping ")

        if i == 2 :
            break

        i +=1
        
        time.sleep(random.uniform(5,20))





final_data = {}

final_data["post_data"] = meta_data_list
final_data["after_data"] = after_list

if file_path.exists(): 
        with open ("reddit_data.json","r",encoding="utf-8") as f:
            data = json.load(f)
            if len(data) == 0:
                   old_data = {
                    "post_data": [],
                    "after_data": []
                    }
            else:
                old_data = data
else:
        old_data = {
            "post_data": [],
            "after_data": []
        }

for i in old_data:
        old_data[i].extend(final_data[i])
        

with open ("reddit_data.json","w",encoding="utf-8") as f:
        json.dump(old_data,f,indent = 4,ensure_ascii = False)
        
        
