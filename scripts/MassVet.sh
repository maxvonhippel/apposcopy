find /home/yu/research/benchmarks/fse -name '*.apk' | while read line; do
    echo "Processing file '$line'"
    python MassVet.py $line
done
