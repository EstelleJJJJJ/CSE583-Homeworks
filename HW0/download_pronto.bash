#!/bin/bash

mkdir -p pronto/data
echo "This directory contains Pronto bike-sharing data." > pronto/README.txt
curl -L "https://s3.amazonaws.com/pronto-data/open_data_year_one.zip" -o pronto/data/open_data_year_one.zip
unzip pronto/data/open_data_year_one.zip -d pronto/data
head -n 10 pronto/data/2015_trip_data.csv
