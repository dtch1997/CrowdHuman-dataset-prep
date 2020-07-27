for ZIPFILE in datasets/CrowdHuman/CrowdHuman_train*.zip
do
    unzip $ZIPFILE -d datasets/CrowdHuman
done

unzip datasets/CrowdHuman/CrowdHuman_val.zip -d datasets/CrowdHuman/val
mv datasets/CrowdHuman/val/Images datasets/CrowdHuman/Images_val
rm -rf datasets/CrowdHuman/val

mkdir datasets/CrowdHuman/annotations
mv datasets/CrowdHuman/*.odgt datasets/CrowdHuman/annotations
