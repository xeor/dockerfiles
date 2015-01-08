Container for https://github.com/tomgi/git_stats

It contain two small things, one nginx server to serve the generated stats, and one script that runs the generation ever X amount of seconds.

## Environment variables
* `generate_every`: Amount of seconds between every git_stats generations. Defaults to 3600 seconds (every 1 hour).
* `GIT_REPO`: uri to a git-repo you want to use, instead of mounting `/data`. Use the same syntax that `git clone` will understand.
* `GIT_REPO_FAIL_RETRY`: Retry initial cloning of repo every X seconds. Default to `10`

## Volumes
* `/data/`: Must be a directory with a .git folder, this is the source git_stats will read from.
* `/www/`: All generated html files will be stored here.
