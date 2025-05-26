#!/bin/bash
docker build -t rsa_challenge:latest .
docker run -d -p 5555:1337 rsa_challenge:latest
