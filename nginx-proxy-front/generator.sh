#!/bin/bash

set -x

nginxconfig="/etc/nginx/conf.d/generated.conf"
tmpfile="${nginxconfig}.tmp"

[[ -e "${tmpfile}" ]] && rm -rf "${tmpfile}"
touch "${tmpfile}"

for i in $(ls  /domains); do
  domain=$(echo ${i} | awk -F_ '{ print $1 }')
  remote=$(echo ${i} | awk -F_ '{ print $2 }')

  ([[ ${domain}} ]] && [[ ${remote} ]]) || continue

  if [[ -e "/domains/${i}/server.pem" ]]; then
    certtype=pem
  else
    certtype=crt
  fi

  # server_name can be a regex, wildcard domain or other, we want to support that. See nginx docs.
  if [[ -e "/domains/${i}/server_name" ]]; then
    server_name=$(cat /domains/${i}/server_name)
  else
    server_name=${domain}
  fi

  # In case we to replace the whole thing
  if [[ -e "/domains/${i}/nginx.conf" ]]; then
    cat /domains/${i}/nginx.conf >> "${tmpfile}"
  else
    cat /nginx.tmpl | sed -e "s@__FOLDER__@${i}@g" -e "s@__CERTTYPE__@${certtype}@g" -e "s@__REMOTE__@${remote}@g" -e "s@__SERVER_NAME__@${server_name}@g" -e "s@__DOMAIN__@${domain}@g" -e "s@__NGINX_EXTRA__@${nginx_extra}@g" >> "${tmpfile}"
  fi
done

mv "${tmpfile}" "${nginxconfig}"

pkill -HUP nginx
