* FlexGet container for general use
* flexget.com
* Start with something like: `docker run -d -v $PWD/config.yml:/config.yml xeor/flexget`
  * I didnt add flexget to xeor/flexget yet, since I havent tested it and think its ready.. Just clone this git repo and build with `docker build .` if you want to try it

# usage
* Mount in your config.yml file.
  * flexget will reload when you change this file..
* Mount up the folders that you want your data in, based on your config.yml. Example -v your_data:/data
