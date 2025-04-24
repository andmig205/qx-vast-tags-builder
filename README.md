## Campaigns and Tags Generation

### Campaigns

Currently, campaigns are stored in the `qx-iva-video\tags\campaigns\campaigns.json` directory. The campaigns are organized as a `JSON` structure, which is an object/dictionary.

Each dictionary `key` is an `adId`. The value of the property is:

```
"[adId value]": { 
    "advName": "[advertiser name]",
    "advId": "[advId value]", 
    "cid": "[campaign id value]",
    "adId": "[adId value]",
    "creative": "[long name]",
    "tag_owner": "[3P tag owner :: ex: IAS]",
    "vast_version": "[VAST version of 3P tag]",
    "vast_wrapper": [true/false :: flags if Qortex tag is VAST Wrapper],
    "vpaid": [ture/false :: flags if Qortex VPAID is used],
    "omid": [true/false :: flags if Qortex OMID is used],
    "is_wrapper": [true/false :: flags if the ad is direct or uses Qortex wrapping either VAST Wrapper or VPAID],
    "rtype": "[integer :: response type : refer to config.py on the server]",
    "dsp": "[DSP name]",
    "adDuration": "[ad duration value :: should be aligned with 3P VAST AdDuration node value]",
    "originalTag": "[false/URL :: 3P tag URL]",
    "mediaFiles": [optional :: array of video files to include in VAST response. Used for pure VAST ads only.]
}
```
#### MediaFiles array element structure

```
{
    "id": "[video asset id]",
    "delivery": "progressive",
    "type": "[mime type :: ex. video/mp4]",
    "bitrate": [integer :: ex. 2000],
    "width": [integer],
    "height": [integer],
    "scalable": "[true/false]",
    "maintainAspectRatio": "[true/false]",
    "assetURI": "[full address]"
},

```

### Tag generation and deployment flow

1. Update campaigns.json.
2. Run `qx-iva-video\tags\tag_builder_bulk.py` script.
3. Script generates Qortex tags and stores them in  `qx-iva-video\tags\ctags-list-abb.csv` file.
4. Update S3 `https://s3.dualstack.us-east-1.amazonaws.com/dev-iva.qortex.ai/iva-server-assets/campaigns/campaigns.json` with the new `campaigns.json`.
5. Run `https://dev-iva-tag.qortex.ai/api/purge/`. The script will update campaigns.json on the ad server. This makes all campaigns available for serving.

