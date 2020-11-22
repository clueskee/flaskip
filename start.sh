#!/bin/bash
podman build -t flaskip . /
podman run -d --name flaskip -p 5455:80 flaskip
