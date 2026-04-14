import requests
import os
import time
import random
from datetime import datetime

# ODOT Camera URL
BASE_URL = "https://www.tripcheck.com/roadcams/cams/ORE22%20at%20Cordon%20Rd%20EB_pid4547.jpg"

def download_images():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    print("Starting collection session...")

    for i in range(5):
        # Cache-buster to force a fresh image
        image_url = f"{BASE_URL}?{random.random()}"
        
        try:
            response = requests.get(image_url, headers=headers, timeout=10)
            if response.status_code == 200:
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filename = f"traffic_{timestamp}.jpg"
                
                with open(filename, 'wb') as f:
                    f.write(response.content)
                print(f"Captured {i+1}/5: {filename}")
            else:
                print(f"Failed capture {i+1}. Status: {response.status_code}")
        except Exception as e:
            print(f"Error during capture {i+1}: {e}")
        
        # Wait 4 minutes between captures
        if i < 4:
            print("Waiting 4 minutes...")
            time.sleep(240)

if __name__ == "__main__":
    download_images()
