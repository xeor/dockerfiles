A simple nginx container that reads 1 nginx.conf file that you need to mount. If it changes, nginx will reload.

# run 
docker run -i -t -p 80:80 -v $PWD/nginx.conf:/nginx.conf xeor/nginx-simple

