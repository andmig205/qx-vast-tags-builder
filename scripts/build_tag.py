from urllib.parse import urlparse, parse_qs
from scripts.config import Config
from utils.helpers import save_tags, append_tokens
import re
from typing import Dict, Any, Optional

"""
Build VAST tags by expanding macros, tokens, and GDPR extensions.
"""

# Precompiled regex patterns
GDPR_PATTERN = re.compile(r"\${GDPR}")
GDPR_CONSENT_PATTERN = re.compile(r"\${GDPR_CONSENT_[\d\w]+}")

def extract_gdpr_extensions(query_params: Dict[str, list[str]]) -> str:
    """Extract GDPR-related parameters from query parameters."""
    extensions = ["te=1"]
    for values in query_params.values():
        value = values[0] if values else ""
        if match := GDPR_PATTERN.search(value):
            extensions.append(f"gdpr={match.group()}")
        if match := GDPR_CONSENT_PATTERN.search(value):
            extensions.append(f"gdpr_consent={match.group()}")
    return "&".join(extensions)

def build_url(server_base: str, adv_id: str, cid: str, ad_id: str, tokens: str, gdpr_ext: str) -> str:
    """Construct the final VAST tag URL."""
    return f"{server_base}/{adv_id}/{cid}/{ad_id}?{tokens}&{gdpr_ext}"

def build_tags(campaign: Dict[str, Any]) -> Dict[str, Any]:
    """Generate all environment tags for a given campaign."""
    ad_id = campaign.get("adId")
    adv_id = campaign.get("advId")
    cid = campaign.get("cid")
    dsp = campaign.get("dsp")
    original_tag = campaign.get("originalTag", "")

    parsed_url = urlparse(original_tag)
    query_params = parse_qs(parsed_url.query)

    gdpr_extension = extract_gdpr_extensions(query_params)
    servers = Config.SERVERS
    dsp_tokens = Config.DSP_TOKENS.get(dsp, {})
    macros = Config.MACROS
    tokens_extension = append_tokens(dsp_tokens, macros)

    tags = {
        env: build_url(server, adv_id, cid, ad_id, tokens_extension, gdpr_extension)
        for env, server in servers.items()
    }

    campaign.update(tags)
    return campaign

def main(campaign: Optional[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    """Entry point: build tags if campaign is provided."""
    if campaign is None:
        return None
    return build_tags(campaign)
