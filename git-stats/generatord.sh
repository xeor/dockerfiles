#!/bin/bash

[[ -d /www ]] || (mkdir /www && chown nginx: /www)

while true; do
  if [[ $GIT_REPO ]]; then
    cd /data
    git pull
  fi
  /usr/local/bin/git_stats generate -p /data -o /www/
  sleep ${generate_every:-3600}
done
