#!/bin/bash
# causes the server to respond with a message containing You got me!
curl -sL -X PUT -H  0.0.0.0:5000/catch_me -d "user_id=98"
