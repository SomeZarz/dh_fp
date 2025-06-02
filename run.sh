#!/bin/bash

docker build -t dh-image .

docker run --name dh-container -d -v $(pwd)/src:/code/src dh-image