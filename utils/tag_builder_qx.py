from config import mediaFileNode, config
from pathlib import Path
from utils.helpers import get_campaign, append_tokens, save_tags

"""
Generates Qortex ad tag without wrapping 3P tag.

Not currently in use

"""

def save_template(content, fileName):
    path = Path(__file__).parent.parent
    path = path.joinpath('ad-server', 'templates', 'qxads', fileName)
    with open(path, "w") as f:
        f.write(content)

def build_vast(campaign):
    #vastTemplate = "QX_VAST_Template.xml"
    adMediaFiles, clickThroughURI, adId, advId, cid, vastTemplate = campaign["mediaFiles"], campaign["clickThroughURI"], campaign["adId"], campaign["advId"], campaign["cid"], campaign["vastTemplate"]
    with open(f'templates/{vastTemplate}') as f:
        xml = f.read()
    
    mediaNodes = []
    for mediaFile in adMediaFiles:
        node = mediaFileNode.format(**mediaFile)
        mediaNodes.append(node)
    
    template_values = {
        "adId": adId,
        "advId": advId,
        "campaignId": cid,
        "clickThroughURI": clickThroughURI,
        "mediaFiles": "\n".join(mediaNodes)
        
    }
    xml = xml.format(**template_values)
    output_name = f"{advId}_{cid}_{adId}.xml"
    save_template(xml, output_name) 
    return None

def build_tags(campaign):
    adId, advId, cid, dsp, rtype = campaign["adId"], campaign["advId"], campaign["cid"], campaign["dsp"], campaign["rtype"]
    servers = config["servers"]
    dspTokens = config["dspTokens"][dsp]
    macros = config["macros"]
    tokensExtension = append_tokens(dspTokens, macros)
    
    def build_url(server):
        return f"{server}/{advId}/{cid}/{adId}?rtype={rtype}{tokensExtension}"
    
    # generate tags variations 
    tags = {
        "local": build_url(servers["local"]),
        "dev": build_url(servers["dev"]),
        "stage": build_url(servers["stg"]),
        "prod": build_url(servers["prod"]),
    }
        
    save_tags(tags, campaign)
    return
    
def main(adId):
    campaign = get_campaign(adId)
    if campaign is None: 
        return
    build_tags(campaign)
    build_vast(campaign)
    
if __name__ == "__main__":
    main("95218031")