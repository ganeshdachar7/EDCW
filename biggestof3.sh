#!/bin/bash

echo "Enter numbers separated by space:"
read -a nums

# Sort numbers in descending order
sorted=($(printf "%s\n" "${nums[@]}" | sort -nr))

echo "Third biggest number is: ${sorted[2]}"
