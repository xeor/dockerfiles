NOT DONE

An own Sentry container for my own needs (ie, some small hacks, see below). For a general Sentry container, it looks like https://github.com/slafs/sentry-docker is the one to use.. :)

# info
* Forced use of postgresql as a db.
* Added `HTTP_USER` automatic login.

# volumes
* `/data`: Everything (including the config we create is here. So if you have your own custom config. Call it `sentry.conf.py` and place it in this directory.

# environment variables
Most of the options in sentry.conf is configuratble. Take a look in `sentry.conf.py` and what is in `config(...)` to see all of them. Here is the most important ones..
Some of the items is prefixed with `_` to dodge name-conflicts if you link the database as `db`

* `_DB_NAME`: Default is `sentry`
* `_DB_USER`: Default is `sentry`
* `_DB_PASS`: Default is `sentry`
* `_DB_HOST`: Default is `db` (so use `--link yourpostgresqlcontainer:db` when linking :) )
* `_DB_PORT`: Default is `5432`
* `REDIS_HOST`: Default is `redis`
* `BROKER_URL`: Default is `redis://redis:6379`
* `SENTRY_URL`: Default is `http://localhost:8080` (no trailing slash!)
* `EMAIL_HOST`: Default is `smtp.gmail.com`
* `EMAIL_HOST_PASSWORD`: Default is emtpy
* `EMAIL_HOST_USER`: Default is empty
* `EMAIL_PORT`: Default is `587`
* `EMAIL_USE_TLS`: Default is `True`
* `SERVER_EMAIL`: Default is `sentry@localhost`

