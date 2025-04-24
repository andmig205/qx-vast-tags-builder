import pandas as pd
import json
from pathlib import Path

def save_tags(tags, campaign):
    advId = int(campaign["advId"])
    adId = int(campaign["adId"])
    cid = int(campaign["cid"])
    is_wrapper = campaign["is_wrapper"]
    creative = f'{campaign["creative"]}_{cid}_{adId}'
    file = Path("tags-list-abb.csv") 
    df = pd.DataFrame()
    if file.exists():
        df = pd.read_csv("tags-list-abb.csv")
        df["adId"] = df["adId"].astype(int)
        df = df[df["adId"] != int(campaign["adId"])]
    print(tags)
    new_row = {
        "type": "local",
        "adId": adId,
        "creative": creative,
        "tag": tags["local"] 
    }
    row_df = pd.DataFrame(new_row, index=[0]) 
    df = pd.concat([df, row_df], ignore_index=True)
    new_row = {
        "type": "dev",
        "adId": adId,
        "creative": creative,
        "tag": tags["dev"]
    }
    row_df = pd.DataFrame(new_row, index=[0])
    df = pd.concat([df, row_df], ignore_index=True)
    
   
    #df = df.drop_duplicates(subset=["adId"])
    
    df.to_csv("tags-list-abb.csv", index=False)
    
def save_tags_complete(tags, campaign):
    advId = int(campaign["advId"])
    adId = int(campaign["adId"])
    cid = int(campaign["cid"])
    is_wrapper = campaign["is_wrapper"]
    creative = f'{campaign["creative"]}_{cid}_{adId}'
    
    df = pd.read_csv("tags-list.csv")
    df = df[df["adId"] != int(campaign["adId"])]
    new_row = {
        "is_wrapper": is_wrapper, 
        "advId": advId,
        "cid": cid,
        "adId": adId,
        "creative": creative,
        "local": tags["local"],
        "dev": tags["dev"],
        "stg": tags["stg"],
        "prod": tags["prod"]
    }
    
    row_df = pd.DataFrame(new_row, index=[0])
    df = pd.concat([df, row_df], ignore_index=True)
    df = df.drop_duplicates(subset=["adId"])
    
    df.to_csv("tags-list.csv", index=False)
    
def get_campaign(adId):
    path = Path(__file__).parent
    path = path.joinpath('campaigns', 'campaigns.json')
    with open(path, "r") as f:
        content = json.load(f)
    campaign = content[adId]
    return campaign

# append dsp tokens and macros 
def appendTokens_v1(tag, dspTokens, macros = None):
    uriParams = ""
    for macro, value in macros.items():
        uriParams += f"&{macro}={value}"
    for token, value in dspTokens.items():
        uriParams += f"&{token}={value}"
    tag += uriParams
    return tag

def appendTokens(dspTokens, macros = None):
    uriParams = []
    for key, value in macros.items():
        uriParams.append(f"{key}={value}")
    for key, value in dspTokens.items():
        uriParams.append(f"{key}={value}")
    return "&".join(uriParams)