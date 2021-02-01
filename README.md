# Documentation

This is the progress of working with gstreamer for the first day

necessary tools

* python gstreamer docker, saves you the time to install all the gstreamer stuff on ubuntu
```
FROM ubuntu:18.04

USER root

RUN apt-get update && apt-get -y --no-install-recommends install \
    sudo \
    vim \
    wget \
    build-essential \
    pkg-config \
    python3.6 \
    python3-pip \
    python3.6-dev \
    python3.6-venv \
    python-dev \
    python3-dev


RUN apt-get -y --no-install-recommends install \
    git \
    cmake \
    autoconf \
    automake \
    libtool \
    gstreamer-1.0 \
    gstreamer1.0-dev \
    libgstreamer1.0-0 \
    gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good \
    gstreamer1.0-plugins-bad \
    gstreamer1.0-plugins-ugly \
    gstreamer1.0-libav \
    gstreamer1.0-doc \
    gstreamer1.0-tools \
    gstreamer1.0-x \
    gstreamer1.0-alsa \
    gstreamer1.0-gl \
    gstreamer1.0-gtk3 \
    gstreamer1.0-qt5 \
    gstreamer1.0-pulseaudio \
    python-gst-1.0 \
    libgirepository1.0-dev \
    libgstreamer-plugins-base1.0-dev \
    libcairo2-dev \
    gir1.2-gstreamer-1.0 \
    python3-gi \
    python-gi-dev

```

* then make sure to double check on the tips for displaying contents of docker containers from `ros`
  * `http://wiki.ros.org/docker/Tutorials/GUI`
  * this makes it so windows will appear when using the gstreamer plugins xvimagesink and autovideosink

command to launch `run -it --rm -v ~/:/place --env="DISPLAY" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" --network=host gstreamer /bin/bash`

python code [./rtsp](./rtsp) is someone's basic example of the gstreamer rtsp server. This is the first thing to try running from inside the conttainer

using tcp:
the python ./tcp_server.py needs to be started first

then inside one container run `python3 rtsp_dist_image.py` so that we can start receiving from the tcp server, ad then in another container start a basic rtsp gstreamer client like tamaggos https://github.com/tamaggo/gstreamer-examples
```
gst-launch-1.0 playbin uri=rtsp://localhost:8554/test
```

If not using udp you are at the mercy of message length limits, so understand that for the other examples

```
gst-launch-1.0 -v udpsrc port=20001 ! pngdec ! videoconvert ! imagefreeze ! autovideosink
```
remember if you take away the imagefreeze part it will update when new data comes in.

This can show images sent over udp with the python in [./gstr_send.py](./gstr_send.py)

[./image_send.py](./image_send.py) is just another example of thhis

