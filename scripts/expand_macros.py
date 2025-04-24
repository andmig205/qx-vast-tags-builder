import pandas as pd
from config import ttdSessions, adkSessions, macrosValues
pd.set_option('display.width', 100000)
pd.set_option("display.max_colwidth", 1000000)

def expand_macros(url):
    url = str(url) 
    for key, value in ttdSessions[0].items():
        url = url.replace(f"%%{key}%%", value)
    for key, value in adkSessions[0].items():
        url = url.replace(f"{{{key}}}", value)
    for key, value in macrosValues[0].items():
        url = url.replace(f"[{key}]", value)
    return url
    
def main():
    df = pd.read_csv("tags-list.csv")
    columns = ['tag_local', 'tag_dev', 'tag_stg', 'tag_prod']
    for col in columns:
        df[col] = df[col].apply(expand_macros)
    
    df.to_csv("tags-list-expanded.csv", index=False)
    

if __name__ == "__main__":
    main()