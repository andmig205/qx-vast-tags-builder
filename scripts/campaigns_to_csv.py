import json
from pathlib import Path
import pandas as pd

def main():
    path = Path(__file__).parent
    origin = path.joinpath('campaigns', 'campaigns.json')

    dest = path.joinpath('campaigns', 'campaigns.csv')

    with open(origin, "r") as f:
        campaigns = json.load(f)


    df = pd.DataFrame.from_dict(campaigns, orient="index")

    df.to_csv(dest, index=False)

    # print(df)

if __name__ == "__main__":
    main()



