import os
import requests
import time
from base64 import b64encode

DID_API_KEY = os.getenv("DID_API_KEY") 

def generate_avatar_video(script_text: str):

    url = "https://api.d-id.com/clips"
    
    auth_str = f"{DID_API_KEY}:"
    encoded_auth = b64encode(auth_str.encode()).decode()

    payload = {
        "script": {
            "type": "text",
            "input": script_text,
            "provider": {
                "type": "microsoft",
                "voice_id": "en-US-JennyNeural"
            }
        },
        "presenter_id": "v2_public_Amber@0zSz8kflCN", 
        "config": {
            "result_format": "mp4",
            "fluent": True, # Ensures smooth lip-sync
            "driver_expressions": {
                "expressions": [
                    {"start_frame": 0, "expression": "neutral", "intensity": 1}
                ]
            }
        }
    }

    headers = {
        "Authorization": f"Basic {encoded_auth}",
        "Content-Type": "application/json",
        "accept": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    data = response.json()
    clip_id = data["id"]
    
    print(f"Video queued successfully. ID: {clip_id}")

    max_retries = 30
    for i in range(max_retries):
        status_url = f"{url}/{clip_id}"
        status_res = requests.get(status_url, headers=headers)
        status_data = status_res.json()
        
        if status_data.get("status") == "done":
            return {
                "video_id": clip_id,
                "status": "completed",
                "video_url": status_data.get("result_url"), 
                "metadata": status_data.get("metadata")
            }
        elif status_data.get("status") == "failed":
            raise Exception("D-ID Video Generation Failed.")
        
        print(f"Processing... (attempt {i+1}/{max_retries})")
        time.sleep(5) # Wait 5 seconds between checks

    return {"video_id": clip_id, "status": "still_processing"}