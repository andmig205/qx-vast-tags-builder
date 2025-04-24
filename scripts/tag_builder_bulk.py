import json
import pandas as pd
from pathlib import Path
from tag_builder import main as wrapper_builder
# from tag_builder_qx import main as qx_tag_builder
# from expand_macros import main as expand_macros

def get_campaigns():
    path = Path(__file__).parent
    path = path.joinpath('campaigns', 'campaigns.json')
    
    with open(path, "r") as f:
        campaigns = json.load(f)
    return campaigns 

def writeFiles(df):
    df.to_csv("campaigns_updated.csv")

    df = df[["adId", "advName", "creative", "tag_owner", "vast_version", "vast_wrapper", "omid", "vpaid","local","dev", "stage","prod"]]
    ouput_lines = []
    for row in df.itertuples(index=True, name="Row"):
        ouput_lines.append("")
        ouput_lines.append("******************************")
        ouput_lines.append("")
        ouput_lines.append(f"Ad ID: {row.adId}")
        ouput_lines.append(f"Advertiser: {row.advName}")
        ouput_lines.append(f"Original tag owner: {row.tag_owner}")
        ouput_lines.append(f"Creative: {row.creative}")
        ouput_lines.append(f"VAST version: {row.vast_version}")
        ouput_lines.append(f"VAST Wrapper: {row.vast_wrapper}")
        ouput_lines.append(f"Implements OMID: {row.omid}")
        ouput_lines.append(f"Implements VPAID: {row.vpaid}")
        ouput_lines.append("")
        ouput_lines.append("Tags")
        ouput_lines.append(f"    local: {row.local}")
        ouput_lines.append(f"    dev: {row.dev}")
        ouput_lines.append(f"    stage: {row.stage}")
        ouput_lines.append(f"    production: {row.prod}")
        # print("******************************")
        # print(f"Ad ID: {row.adId}")
        # print(f"Advertiser: {row.advName}")
        
        # print(f"Original tag owner: {row.tag_owner}")
        # print(f"Creative: {row.creative}")
        # print(f"VAST version: {row.vast_version}")
        # print(f"VAST Wrapper: {row.vast_wrapper}")
        # print(f"Implements OMID: {row.omid}")
        # print(f"Implements VPAID: {row.vpaid}")
        # print("Tags")
        # print(f"\tlocal: {row.local}")
        # print(f"dev: {row.dev}")
        # print(f"stage: {row.stage}")
        # print(f"production: {row.prod}")

    with open("distribution.txt", "w") as file:
        file.writelines(line + "\n" for line in ouput_lines)

def build_tags(campaigns): 
    df = None
    for key, value in campaigns.items():
        if value["is_wrapper"]:
            tags = wrapper_builder(key)
            tagDF = pd.DataFrame(tags, index=[0])
            if df is None:
                df = tagDF
                
            else:
                df = pd.concat([df, tagDF], ignore_index=True)
    print(df.columns) 
    writeFiles(df)
    
def main():
    campaigns = get_campaigns()
    build_tags(campaigns)
    # expand_macros()
    

if __name__ == "__main__":
    main()