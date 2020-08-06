"""
A short script for automatically downloading the CrowdHuman dataset. 
The original dataset is available here: https://www.crowdhuman.org/
File ID are obtained as follows: 
    1. Go to CrowdHuman website (linked above)
    2. Scroll to "download" button and click
    3. Click on Google drive link
    4. Click "Download file"
    5. In the URL, there is some part which looks like ...?file_id=XXXX
    6. The FILE_ID is the XXXX part. 

FAQ:
    Q: I got an error "Permission denied. Maybe you need to change permission over..."?
    A: See https://github.com/wkentaro/gdown/issues/43. This is likely because Google Drive restricts downloads of large files to prevent swamping their network. Try again later, or manually download the dataset. 
"""

import time
import os
import argparse
import pathlib

parser = argparse.ArgumentParser(description="Download CrowdHuman dataset from Google Drive")
parser.add_argument("--datadir", default="Pedestron/datasets/CrowdHuman")
parser.add_argument("--service-account", default="cred.json")

GDRIVE_FILE_IDS = {
    'CrowdHuman_train_01.zip': '10JWSJs-bfRIccCwSSpwZDKo2fmBZQD-k',
    'CrowdHuman_train_02.zip': '1LXYNBLh0s3d37h7NNi-GI72lYKPr06BR',
    'CrowdHuman_train_03.zip': '1zNJDsXZy7seY9iPzbcjgHyRp_eCLM63m',
    'CrowdHuman_val.zip': '1x6B7TlWO8yhAA_zAgTBV83MjkImA3GKR',
    # 'CrowdHuman_test.zip': '1GYzUB07J35P5Y_DJCwLzJt72x_Mkf9Yl',
    'annotation_train.odgt': '1A7FhvTf9M8R7lzgWganFUPSwcuAQNfbT',
    'annotation_val.odgt': '1U1K2Q1-iVwzOPImTMtSkngYGKSe13OsJ'
}

def main():
    args = parser.parse_args()
    for fname, fid in GDRIVE_FILE_IDS.items():
        path = pathlib.Path(args.datadir) / fname
        print(f"Downloading file {fname} to {path}")
        os.system(f"gdrive --service-account {args.service_account} download {fid}")
    
if __name__ == "__main__":
    main()
