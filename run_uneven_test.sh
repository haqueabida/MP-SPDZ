echo "running uneven QSI, MOE, bitonic merge"
Scripts/mascot.sh quadratic_set_intersection >> 32_992.txt
Scripts/mascot.sh merge_odd_even >> 32_992.txt
Scripts/mascot.sh bitonic_merge_uneven >> 32_992.txt
