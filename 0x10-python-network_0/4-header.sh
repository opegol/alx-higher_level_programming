#!/bin/bash
# sends a GET request to the URL and sets a header variable
curl -sH "X-School-User-Id: 98" "$1"
