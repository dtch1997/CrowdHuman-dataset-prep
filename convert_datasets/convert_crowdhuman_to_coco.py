import os
import json
from PIL import Image
import argparse
import pathlib

parser = argparse.ArgumentParser(description="Convert the ODGT annotations to COCO format")
parser.add_argument("--datadir", default="Pedestron/datasets/CrowdHuman", 
                    help="The directory where CrowdHuman dataset is saved."
                    "Expected to contain: annotations/annotations*.odgt")
parser.add_argument("--overwrite", action="store_true"
                    help="If set, overwrites any existing files in the datadir")

def load_file(fpath):
    assert os.path.exists(fpath)  # assert() raise-if-not
    with open(fpath, 'r') as fid:
        lines = fid.readlines()
    records = [json.loads(line.strip('\n')) for line in lines]  # str to list
    return records

def crowdhuman2coco(odgt_path, json_path, img_dir):
    records = load_file(odgt_path)
    json_dict = {"images": [], "annotations": [], "categories": []}  
    START_B_BOX_ID = 1  
    image_id = 1  
    bbox_id = START_B_BOX_ID
    image = {}  
    annotation = {}  
    categories = {}  
    record_list = len(records)  
    print(f"Converting annotations of {record_list} images...")
    
    for i in range(record_list):
        file_name = records[i]['ID'] + '.jpg'  
        print(f"Processing file {file_name}...")
        im = Image.open(str(img_dir / file_name))
        image = {'file_name': file_name, 'height': im.size[1], 'width': im.size[0],
                 'id': image_id}  
        json_dict['images'].append(image)  

        gt_box = records[i]['gtboxes']
        gt_box_len = len(gt_box)  
        for j in range(gt_box_len):
            category = gt_box[j]['tag']
            if category not in categories:  
                new_id = len(categories) + 1  
                categories[category] = new_id
            category_id = categories[category]  
            fbox = gt_box[j]['fbox']  
            ignore = 0  
            if "ignore" in gt_box[j]['head_attr']:
                ignore = gt_box[j]['head_attr']['ignore']
            if "ignore" in gt_box[j]['extra']:
                ignore = gt_box[j]['extra']['ignore']
            
            annotation = {'area': fbox[2] * fbox[3], 'iscrowd': ignore, 'image_id':  
                image_id, 'bbox': fbox, 'hbox': gt_box[j]['hbox'], 'vbox': gt_box[j]['vbox'],
                          'category_id': category_id, 'id': bbox_id, 'ignore': ignore}
            json_dict['annotations'].append(annotation)

            bbox_id += 1  
        image_id += 1  
    for cate, cid in categories.items():
        cat = {'supercategory': 'none', 'id': cid, 'name': cate}
        json_dict['categories'].append(cat)
        
    with open(json_path, 'w') as json_fp:
        json.dump(json_dict, json_fp)


if __name__ == '__main__':
    args = parser.parse_args()
    train_odgt_path = pathlib.Path(args.datadir) / 'annotations' / 'annotation_train.odgt'
    train_json_path = pathlib.Path(args.datadir) / 'annotations' / 'train.json'
    train_img_dir = pathlib.Path(args.datadir) / 'Images'
    crowdhuman2coco(train_odgt_path, train_json_path, train_img_dir)
    
    val_odgt_path = pathlib.Path(args.datadir) / 'annotations' / 'annotation_val.odgt'
    val_json_path = pathlib.Path(args.datadir) / 'annotations' / 'val.json'
    val_img_dir = pathlib.Path(args.datadir) / 'Images_val'
    crowdhuman2coco(val_odgt_path, val_json_path, val_img_dir)
    