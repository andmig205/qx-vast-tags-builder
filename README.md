# Qortex VAST Tag Builder

Internal tool for managing ad campaigns and generating VAST tags for the Qortex ad server.

## 📁 Campaigns

Campaigns are stored in the file:

`campaigns/campaigns.json`

This is a JSON dictionary where each key is an `adId`, and each value contains metadata about a campaign.

### 🔧 Campaign Entry Structure

```json
{
  "123456": { 
    "advName": "Advertiser Name",
    "advId": "ADV001",
    "cid": "CMP001",
    "adId": "123456",
    "creative": "Creative Long Name",
    "tag_owner": "IAS",
    "vast_version": "4.2",
    "vast_wrapper": true,
    "vpaid": false,
    "omid": true,
    "is_wrapper": true,
    "rtype": "1",
    "dsp": "TTD",
    "adDuration": "30",
    "originalTag": "https://3p-tag-url.com/vast",
    "mediaFiles": [
      {
        "id": "video_001",
        "delivery": "progressive",
        "type": "video/mp4",
        "bitrate": 2000,
        "width": 640,
        "height": 360,
        "scalable": true,
        "maintainAspectRatio": true,
        "assetURI": "https://cdn.example.com/video.mp4"
      }
    ]
  }
}
```

## ⚙️ Tag Generation & Deployment Flow

1. **Update `campaigns.json`**  
   Edit or extend `campaigns/campaigns.json` to include new campaigns or update existing ones.

2. **Run the tag generation script**  
   Run the bulk tag builder:

   ```bash
   python scripts/tag_builder_bulk.py
   ```

   This will output a CSV file with generated Qortex VAST tags to:

   ```
   dist/ctags-list-abb.csv
   ```

3. **Upload `campaigns.json` to S3**  
   Replace the object at:

   ```
   https://s3.dualstack.us-east-1.amazonaws.com/dev-iva.qortex.ai/iva-server-assets/campaigns/campaigns.json
   ```

   with the new version of `campaigns/campaigns.json`.

4. **Purge ad server cache**  
   Use the following API endpoint to apply the update on the server:

   ```
   https://dev-iva-tag.qortex.ai/api/purge/
   ```

   This will reload the new campaigns into the ad-serving system.

## 🧱 Project Structure

```
campaigns/      → JSON campaign definitions  
dist/           → Output CSV files  
docs/           → Internal documentation notes  
scripts/        → Entry-point Python scripts  
utils/          → Shared helper modules (e.g. macro expansion)
```

## 📝 Dependencies

Install dependencies in a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```


