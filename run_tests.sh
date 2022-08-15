echo "running QSI, MOE, BitM"
Scripts/mascot.sh quadratic_set_intersection >> 512_512.txt
Scripts/mascot.sh merge_odd_even >> 512_512.txt
Scripts/mascot.sh bitonic_merge >> 512_512.txt
