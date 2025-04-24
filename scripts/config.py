config = {
    # Request macros
    "macros": {
        "apidframeworks": "[APIFRAMEWORKS]",
        "breakMaxAds": "[BREAKMAXADS]",
        "breakPosition": "[BREAKPOSITION]",
        "clientua": "[CLIENTUA]",
        "contentCat": "[CONTENTCAT]",
        "contentId": "[CONTENTID]",
        "contentURL": "[CONTENTURI]",
        "deviceua": "[DEVICEUA]",
        "domain": "[DOMAIN]",
        "inventoryState": "[INVENTORYSTATE]",
        "mediaPlayhead": "[MEDIAPLAYHEAD]",
        "omidPartner": "[OMIDPARTNER]",
        "pageURL": "[PAGEURL]",
        "placementType": "[PLACEMENTTYPE]",
        "playBackMethods": "[PLAYBACKMETHODS]",
        "playerCapabilities": "[PLAYERCAPABILITIES]",
        "playerSize": "[PLAYERSIZE]",
    },

    # DSP token maps
    "dspTokens": {
        "TTD_to_Qortex": {
            "%%TTD_ADGROUPID%%": "d_pid",
            "%%TTD_CAMPAIGNID%%": "d_cid",
            "%%TTD_DEALID%%": "d_dealid",
            "%%TTD_IMPRESSIONID%%": "d_impid",
            "%%TTD_PUBLISHERID%%": "d_pubid",
            "%%TTD_SITE%%": "d_siteid",
            "%%TTD_SITE_WITH_PATH%%": "d_bidurl",
            "%%TTD_SUPPLYVENDOR%%": "d_chanid",
        },
        "TTD": {
            "d_bidurl": "%%TTD_SITE_WITH_PATH%%",
            "d_cid": "%%TTD_CAMPAIGNID%%",
            "d_chanid": "%%TTD_SUPPLYVENDOR%%",
            "d_dealid": "%%TTD_DEALID%%",
            "d_impid": "%%TTD_IMPRESSIONID%%",
            "d_pid": "%%TTD_ADGROUPID%%",
            "d_pubid": "%%TTD_PUBLISHERID%%",
            "d_siteid": "%%TTD_SITE%%",
        },
        "ADK": {
            "d_appid": "{app_id}",
            "d_campaign_id": "{campaign_id}",
            "d_domain": "{domain}",
            "d_pageurl": "{page_url}",
            "d_referrer": "{referrer}",
            "d_requestid": "{request_id}",
            "d_siteid": "{site_id}",
            "d_timestamp": "{timestamp}",
        },
        "Xandr": {
            "d_appid": "${EXT_APP_ID}",
            "d_creative": "${CREATIVE_ID}",
            "d_dealid": "${DEAL_ID}",
            "d_pid": "${PUBLISHER_ID}",
            "d_pubid": "${PUBLISHER_ID}",
            "d_referrer": "${REFERER_URL_ENC}",
            "d_siteid": "${SITE_ID}",
            "d_timestamp": "${TIMESTAMP}",
        },
    },

    # Environments
    "servers": {
        "dev": "https://dev-iva-tag.qortex.ai/ivavast",
        "local": "http://127.0.0.1:8000/ivavast",
        "prod": "https://iva-tag.qortex.ai/ivavast",
        "stg": "https://stg-iva-tag.qortex.ai/ivavast",
    },

}

# Sessions
ttdSessions = [
    {
        "TTD_ADGROUPID": "pid_33",
        "TTD_CAMPAIGNID": "cid_11",
        "TTD_DEALID": "dealid_44",
        "TTD_IMPRESSIONID": "impression_55",
        "TTD_PUBLISHERID": "pubid_22",
        "TTD_SITE": "SITE_ID_00",
        "TTD_SITE_WITH_PATH": "ompid_66",
        "TTD_SUPPLYVENDOR": "Supply_vendor",
    }
]

adkSessions = [
    {
        "app_id": "adk_app_id_22",
        "campaign_id": "adk_cid_33",
        "domain": "adk_domain_77",
        "page_url": "adk_page_url_88",
        "referrer": "adk_referrer_44",
        "request_id": "adk_request_id_55",
        "site_id": "adk_siteid_11",
        "timestamp": "adk_timestamp_66",
    }
]

macrosValues = [
    {
        "APIFRAMEWORKS": "2,3,4",
        "BREAKPOSITION": "1",
        "MEDIAPLAYHEAD": "00%3A05%3A21.123",
        "OMIDPARTNER": "ias.com-omid",
    }
]
mediaFileNode = '<MediaFile id="{id}" delivery="{delivery}" type="{type}" bitrate="{bitrate}" width="{width}" height="{height}" scalable="{scalable}" maintainAspectRatio="{maintainAspectRatio}"><![CDATA[{assetURI}]]></MediaFile>'
