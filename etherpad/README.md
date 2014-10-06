# info
* Centos6 as base
* runs etherpad-lite
* Asumes some settings.. Take a look at settings.json, and fork this repo if you want something else. Its really just made quick and dirty for a local project :)
* run: docker run -d --link postgres:postgresql -e "TITLE=web title" -e "ADMIN_PW=pass" -e "DEFAULT_PAD_TEXT=start writing" -p 80:8080 xeor/etherpad

# Full example with db
* docker run --name postgres -d postgres
* docker run -i -t --link postgres:postgresql --rm xeor/devbox
  * psql -h $POSTGRESQL_PORT_5432_TCP_ADDR -p 5432 -U postgres -c 'CREATE ROLE pad with LOGIN CREATEDB;'
  * psql -h $POSTGRESQL_PORT_5432_TCP_ADDR -p 5432 -U postgres -c "CREATE DATABASE pad ENCODING 'unicode' TEMPLATE template0;"
  * psql -h $POSTGRESQL_PORT_5432_TCP_ADDR -p 5432 -U postgres -c 'GRANT ALL PRIVILEGES ON DATABASE pad to pad;'
