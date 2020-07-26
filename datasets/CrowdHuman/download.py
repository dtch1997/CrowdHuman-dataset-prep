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
import gdown

GDRIVE_FILE_IDS = {
    'CrowdHuman_train_01.zip': '1XZm5L27eQasrvMq008l6vW8I8ysnavSM',
    'CrowdHuman_train_02.zip': '1KgreKkhPfIiZHkl-x5K7p5LHKsfZss5q',
    'CrowdHuman_train_03.zip': '1Af1rBvQSxOmXphoNNtKzAJyrEeeAF-aV',
    'CrowdHuman_val.zip': '1dRRL6eKE1v_1Kb_R8nZGhTQ0HzYZ-Pss',
    'CrowdHuman_test.zip': '1GYzUB07J35P5Y_DJCwLzJt72x_Mkf9Yl',
    'annotation_train.odgt': '1uBB3psTLteVEP2Wg466DsYVx1eV8LacU',
    'annotation_val.odgt': '151-MHsdCni1izANEuZA3q3Pp7Jwpi-PX'
}

for fname, fid in GDRIVE_FILE_IDS.items():
    print(f"Downloading file {fname}...")
    url = f'https://drive.google.com/uc?id={fid}'
    gdown.download(url, fname, quiet=False)
    
    # It seems that Google drive will block the automatic download if it occurs too quickly. 
    time.sleep(10)
    
