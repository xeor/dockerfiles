This uses the upstream taggo pip package but got some additional niceness to it when it comes to automatic runs..
See https://taggo.readthedocs.io/en/latest/

Start the container with environment variables like `CRON_TAGGO_0` with the format `* * * * *|run ....`

  * CRON_TAGGO_n where n is a number, start at 0, have as many as you want.
  * We take care automaticly that only 1 of each number is running at a time. Example, if one of your job is running every minute and it takes more than a minute to finish. It wont start the 2nd time.
  * The environment variable is split in 2 by a `|`. The first param is a cron, the 2nd is the parameters sent to the `taggo` command.

