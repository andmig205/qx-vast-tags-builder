import re
from config import config

def parseMacros(tag, dsp):
    urlParams = ""
    dspTokens = config["dspTokens"]
    if dsp == "TTD":
        pattern = r"%%[\w_]+%%"
        macros = re.findall(pattern, tag)
        qxParams = dspTokens["TTD_to_Qortex"]
        # for key, value in qxParams.items():
        #     print(f"Key: {key}, Value: {value}")
        
        # urlParams = []
        # for macro in macros:
        #     param = qxParams.get(macro)
        #     if(param):
        #         urlParams.append(f"{qxParams.get(macro)}={macro}")

        urlParams = "&".join([f"{qxParams[macro]}={macro}" for macro in macros if qxParams.get(macro)])

   
    return urlParams
        
def main():
    tag = "https://unified.adsafeprotected.com/v2/2227577/82662558?mon=82662559&omidPartner=[OMIDPARTNER]&apiframeworks=[APIFRAMEWORKS]&bundleId=%%TTD_SITE%%&mode=strict&ias_dspID=9&ias_campId=%%TTD_CAMPAIGNID%%&ias_pubId=%%TTD_PUBLISHERID%%&ias_chanId=%%TTD_SUPPLYVENDOR%%&ias_placementId=%%TTD_ADGROUPID%%&bidurl=%%TTD_SITE_WITH_PATH%%&ias_dealId=%%TTD_DEALID%%&ias_xappb=%%TTD_SITE%%&adsafe_par&ias_impId=v4~~%%TTD_IMPRESSIONID%%&originalVast=https://ad.doubleclick.net/ddm/pfadx/N553.3848558MATTERKIND/B32665665.404189740;sz=0x0;ord=[timestamp];dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;dc_tdv=1;dcmt=text/xml;dc_sdk_apis=[APIFRAMEWORKS];dc_omid_p=[OMIDPARTNER];dc_vast=3;gdpr=${GDPR};gdpr_consent=${GDPR_CONSENT_755};dc_mpos=[BREAKPOSITION];ltd="

    urlParams = parseMacros(tag, "TTD")
    print(urlParams)


if __name__ == "__main__":
    main()