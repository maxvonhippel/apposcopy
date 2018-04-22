echo APK location:  $1
find $1 -name '*.apk' | while read line; do
    echo "Processing file '$line'"
    python MassVet.py $line
done
