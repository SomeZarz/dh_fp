@echo off
REM Build the Docker image
docker build -t dh-image .

REM Run the Docker container
docker run --name dh-container -d -v "%cd%\src:/code/src" dh-image

echo Script finished.
