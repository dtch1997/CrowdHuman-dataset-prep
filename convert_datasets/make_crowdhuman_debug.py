# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 03:32:12 2020

@author: Daniel Tan
"""
import os
import json
from PIL import Image
import argparse
import pathlib
import shutil

parser = argparse.ArgumentParser(description="Convert the ODGT annotations to COCO format")
parser.add_argument("--datadir", default="Pedestron/datasets/CrowdHuman", 
                    help="The directory where CrowdHuman dataset is saved."
                    "Expected to contain: \n "
                    "- Images/all_train_images.jpg \n"
                    "- Images_val/all_val_images.jpg \n"
                    "- annotations/annotations*.odgt")
parser.add_argument("--debug-size", default=100,
                    help="The number of images to use in the debug dataset")
parser.add_argument("--savedir", default="Pedestron/datasets/CrowdHuman_debug",
                    help="Te directory where debug dataset should be saved")

def make_parent(path: pathlib.Path):
    parent = path.parent
    if parent.exists() and parent.is_dir():
        return
    else:
        parent.mkdir(parents=True, exist_ok=True)

def make_debug(data_dir:    pathlib.Path,
               save_dir:    pathlib.Path,
               debug_size:  int,
               split:       str="train"):
    assert split in ["train", "val"]
    json_path = pathlib.Path("annotations") / f"{split}.json"
    with open(data_dir / json_path, 'r') as jsonfile:
        json_dict = json.load(jsonfile)
    
    img_dir = "Images" if split == "train" else "Images_val"
    # Copy the images over
    images = json_dict['images'][:debug_size]
    print(f"Creating a debug {split} dataset of size {debug_size}")
    
    for img in images:
        # Copy the image file
        img_path = data_dir / img_dir / img['file_name']
        img_savepath = save_dir / img_dir / img['file_name']
        print(f"Copying {img_path} to {img_savepath}")
        image = Image.open(str(img_path))
        make_parent(img_savepath)
        image.save(str(img_savepath), "JPEG")
    img_ids = [image['id'] for image in images]
    
    assert len(img_ids) == debug_size
    for idx in img_ids:
        # img_id is 1-indexed
        assert 1 <= idx <= debug_size
    
    # Select relevant annotations
    annotations = []
    for ann in json_dict['annotations']:
        if ann['image_id'] < debug_size:
            annotations.append(ann)
    
    # Create new json dict
    new_json_dict = {'images': images, 
                     'annotations': annotations,
                     'categories': json_dict['categories']}
    json_savepath = save_dir / json_path
    print(f"Saving annotations to {json_savepath}")
    make_parent(json_savepath)
    with open(json_savepath, 'w') as jsonfile:
        json.dump(new_json_dict, jsonfile)
    

def main():
    args = parser.parse_args()
    make_debug(pathlib.Path(args.datadir), pathlib.Path(args.savedir), args.debug_size, split="train")
    make_debug(pathlib.Path(args.datadir), pathlib.Path(args.savedir), args.debug_size, split="val")
    
if __name__ == "__main__":
    main()
    

        
    

    