DATADIR="Pedestron/datasets/CrowdHuman"

for ZIPFILE in $DATADIR/CrowdHuman_train*.zip
do
    unzip $ZIPFILE -d $DATADIR
done

unzip $DATADIR/CrowdHuman_val.zip -d $DATADIR/val
mv $DATADIR/val/Images $DATADIR/Images_val
rm -rf $DATADIR/val

mkdir $DATADIR/annotations
mv $DATADIR/*.odgt $DATADIR/annotations
