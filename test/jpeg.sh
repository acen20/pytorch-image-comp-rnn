#!/bin/bash

for i in {00..00..1}; do
  echo JPEG Encoding test/images/$i.bmp
  mkdir -p test/jpeg/$i
  for j in {1..20..1}; do
    convert test/images/$i.bmp -quality $(($j*5)) -sampling-factor 4:2:0 test/jpeg/$i/`printf "%02d" $j`.jpg
  done
done
