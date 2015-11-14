A simple container that uses `taggo` on a mounted volume and config

Note that the folder to store the tags in must exists as well

# mountpoints
* `/data`: Must be mounted where the files should be
* `/taggo.cfg`: Custom mounted, if it doesnt exist, `/data/taggo.cfg` is used, if that doesnt exist, we use a default one (see code).

# variables
* `RUNMODE`: set to one of
  * `inotify`: watch all files in `/data`, or `TAGGO_WATCH` for changes
  * `timer` (default) timermode (every 1 minute, or `TAGGO_INTERVAL` seconds)

