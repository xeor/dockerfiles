# Info

This is a simple image for getting zabbix up and running. Nothing special.

To get the database setup, you might need to go into the container after it have started and run;

    psql -h db -U postgres postgres < /usr/share/doc/zabbix-server-pgsql-2.4.7/postgresql/schema.sql
    psql -h db -U postgres postgres < /usr/share/doc/zabbix-server-pgsql-2.4.7/postgresql/images.sql
    psql -h db -U postgres postgres < /usr/share/doc/zabbix-server-pgsql-2.4.7/postgresql/data.sql

As you can see, database needs to be linked as `db`, and we are using postgres.
