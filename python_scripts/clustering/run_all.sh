for file in $(find configs -name '*.yaml')
do
    python3 _clustering.py $file
done
