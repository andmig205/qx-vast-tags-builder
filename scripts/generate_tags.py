import json
from pathlib import Path
from scripts.build_tag import main as build_tag
from scripts.distribute_tags import distribute_tags

"""
Builds and distributes ad tags from campaign definitions.
"""

CAMPAIGNS_PATH = Path(__file__).parent.parent / 'campaigns' / 'campaigns.json'

def get_campaigns() -> dict:
    """Load campaigns from JSON file."""
    with CAMPAIGNS_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)

def build_tags(campaigns: dict) -> None:
    """Build tags for wrapper campaigns and distribute them."""
    tags_list = [
        build_tag(campaign)
        for campaign in campaigns.values()
        if campaign.get("is_wrapper")
    ]
    distribute_tags(tags_list)

def main() -> None:
    """Main execution flow."""
    campaigns = get_campaigns()
    build_tags(campaigns)
