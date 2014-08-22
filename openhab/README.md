# To get a zwave stick working, add something like this udev rules on the host
echo 'DRIVERS=="usb", ATTRS{manufacturer}=="Silicon Labs", ATTRS{product}=="CP2102 USB to UART Bridge Controller", NAME="zwave", MODE="0666"' > /etc/udev/rules.d/99-zwave.rules
udevadm trigger

# To run
* --privileged and -v mount the zwave device, or use --device (from Docker 1.2>)
* --net="host" if you want upnp stuff or similar. Might be needed
* Configurations needs to be mounted in.

docker run --privileged -i -t --net="host" -P -v /dev/zwave:/dev/zwave -v /path/to/configurations:/srv/configurations xeor/openhab

# group prefixes, just a suggestion, and personal notes :)
* L_ - Location, example L_Living, L_Kitchen
* T_ - Type, example T_Energy, T_Switch
* 
