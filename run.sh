#!/bin/bash

docker build -t fyp-image .

docker run --name fyp-container -d -v $(pwd)/src:/code/src fyp-image