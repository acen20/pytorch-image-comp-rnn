#!/bin/bash

for i in {00..1..1}; do
  echo BMP Encoding test/images/$i.png
  mkdir -p test/bmp/$i
  for j in {1..20..1}; do
    convert test/images/$i.bmp -quality $(($j*5)) -sampling-factor 4:2:0 test/bmp/$i/`printf "%02d" $j`.bmp
  done
done
