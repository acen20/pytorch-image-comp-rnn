#!/bin/bash

LSTM=test/lstm_ssim.csv
JPEG=test/jpeg_ssim.csv

echo -n "" > $LSTM
for i in {00..00..1}; do
  echo Processing test/decoded/kodim$i
  for j in {00..15..1}; do
    echo -n `python3 metric.py -m ssim -o test/images/$i.bmp -c test/decoded/$i/$j.png`', ' >> $LSTM
  done
  echo "" >> $LSTM
done

echo -n "" > $JPEG
for i in {00..00..1}; do
  echo Processing test/jpeg/kodim$i
  for j in {01..20..1}; do
    echo -n `python3 metric.py -m ssim -o test/images/$i.bmp -c test/jpeg/$i/$j.jpg`', ' >> $JPEG
  done
  echo "" >> $JPEG
done
