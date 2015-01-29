#!/bin/bash

set -x

nginxconfig="/etc/nginx/conf.d/generated.conf"
tmpfile="${nginxconfig}.tmp"

[[ -e "${tmpfile}" ]] && rm -rf "${tmpfile}"
touch "${tmpfile}"

for i in $(ls  ./domains); do
  domain=$(echo ${i} | awk -F_ '{ print $1 }')
  remote=$(echo ${i} | awk -F_ '{ print $2 }')

  ([[ ${domain}} ]] && [[ ${remote} ]]) || continue

  cat nginx.tmpl | sed -e "s@__FOLDER__@${i}@g" -e "s@__REMOTE__@${remote}@g" -e "s@__DOMAIN__@${domain}@g" >> "${tmpfile}"
done

mv "${tmpfile}" "${nginxconfig}"

pkill -HUP nginx
