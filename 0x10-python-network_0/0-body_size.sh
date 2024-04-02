#!/bin/bash
#script takes in a URL, sends a request to that UR and displays the response
curl -s "$1" | wc -c
