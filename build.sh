#!/bin/bash

for i in ${@}; do
  cmd=$(cat "${i}/dockerfiles.conf" 2> /dev/null | grep -E "^build=" | awk -F= '{ print $NF }')
  [[ ${cmd} ]] || continue
  echo " * Doing ${i}"
  ${cmd} 2> /dev/null
  echo
  sleep 1
done

