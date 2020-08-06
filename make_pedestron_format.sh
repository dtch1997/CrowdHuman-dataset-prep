
USAGE = "source make_pedestron_format.sh DATADIR"
echo $USAGE
DATADIR=$1
echo "Using DATADIR=${DATADIR}"

for ZIPFILE in $DATADIR/CrowdHuman_train*.zip
do
    unzip $ZIPFILE -d $DATADIR
done

unzip $DATADIR/CrowdHuman_val.zip -d $DATADIR/val
mv $DATADIR/val/Images $DATADIR/Images_val
rm -rf $DATADIR/val
rm -rf $DATADIR/*.zip

mkdir $DATADIR/annotations
mv $DATADIR/*.odgt $DATADIR/annotations
rm -rf $DATADIR/*.zip
