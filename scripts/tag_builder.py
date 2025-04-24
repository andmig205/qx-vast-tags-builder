from urllib.parse import quote, urlparse, parse_qs
from config import config
from helpers import save_tags, get_campaign, appendTokens
import re

"""
1) build tag with macros/tokens
2) expand macros and tokens for testing
"""
def buildTags(campaign):
    adId, advId, cid, dsp, originalTag, creative  = campaign["adId"], campaign["advId"], campaign["cid"], campaign["dsp"], campaign["originalTag"], campaign["creative"] 
    parsed_url = urlparse(originalTag)
    query_params = parse_qs(parsed_url.query)
    gdpr_consent_pattern = r"\${GDPR_CONSENT_[\d\w]+}"
    gdpr_pattern = r"\${GDPR}"
    gdrp_extension = ["te=1"]
    for key, value in query_params.items():
        match = re.search(gdpr_pattern, value[0])
        if match:
            gdrp_extension.append(f"gdpr={match.group()}")
            
        match = re.search(gdpr_consent_pattern, value[0])
        if match:
            gdrp_extension.append(f"gdpr_consent={match.group()}")
    gdrp_extension = "&".join(gdrp_extension)
    servers = config["servers"]
    dspTokens = config["dspTokens"][dsp]
    macros = config["macros"]
    tokens_extension = appendTokens(dspTokens, macros)
    
    def build_url(server):
        return f"{server}/{advId}/{cid}/{adId}?{tokens_extension}&{gdrp_extension}"
    # generate tags variations 
    tags = {
        "local": build_url(servers["local"]),
        "dev": build_url(servers["dev"]),
        "stage": build_url(servers["stg"]),
        "prod": build_url(servers["prod"]),
    }

    campaign.update(tags)
    
    return campaign

def main(adId):
    campaign = get_campaign(adId) 
    if campaign is None:
        return
    
    tags = buildTags(campaign)
    return tags
    # print(tags)
    # save_tags(tags, campaign)

if __name__ == "__main__":
    main("17422960")

