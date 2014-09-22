A version that uses the same idea as `https://github.com/drone/drone/blob/master/Dockerfile`, but:
* Downloads the fresh version from git, not adding from local repo
* Hardcode/changes the path of the gitlab url to be /git/. This is a bug in the official version and cannot be changed in it..
