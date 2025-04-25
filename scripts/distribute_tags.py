from typing import List, Dict, Optional
from pathlib import Path
import pandas as pd

"""
Writes tags into files for external distribution:
1. CSV file containing all tags and their variations.
2. TXT file in a readable human-friendly format.
"""

# Fields to export
EXPORT_COLUMNS = [
    "adId", "advName", "creative", "tag_owner", "vast_version",
    "vast_wrapper", "omid", "vpaid", "local", "dev", "stage", "prod"
]

DIST_DIR = Path(__file__).parent.parent / 'dist'
DIST_DIR.mkdir(exist_ok=True)  # Ensure the directory exists

def write_csv(df: pd.DataFrame) -> None:
    """Write the tags DataFrame into a CSV file."""
    path = DIST_DIR / 'tags.csv'
    df.to_csv(path, columns=EXPORT_COLUMNS, index=False)

def write_dist_txt(df: pd.DataFrame) -> None:
    """Write the tags DataFrame into a readable TXT file."""
    path = DIST_DIR / 'distribution.txt'
    output_lines = []

    for row in df.itertuples(index=False, name="Row"):
        output_lines.extend([
            "",
            "******************************",
            "",
            f"Ad ID: {row.adId}",
            f"Advertiser: {row.advName}",
            f"Original tag owner: {row.tag_owner}",
            f"Creative: {row.creative}",
            f"VAST version: {row.vast_version}",
            f"VAST Wrapper: {row.vast_wrapper}",
            f"Implements OMID: {row.omid}",
            f"Implements VPAID: {row.vpaid}",
            "",
            "Tags",
            f"    local: {row.local}",
            f"    dev: {row.dev}",
            f"    stage: {row.stage}",
            f"    production: {row.prod}",
        ])

    with open(path, "w", encoding="utf-8") as file:
        file.write("\n".join(output_lines))

def distribute_tags(tags: Optional[List[Dict]] = None) -> None:
    """Main entry point to distribute tags into CSV and TXT formats."""
    if not tags:
        return

    df = pd.DataFrame(tags)
    write_csv(df)
    write_dist_txt(df)
