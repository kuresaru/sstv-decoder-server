SSTV Decoder Server
============

![](https://raw.githubusercontent.com/colaclanth/sstv/master/examples/m1.png)

A slow-scan television decoder that works on audio files over http restful api.

Currently supports the following file types:
* silk v3 (popular in IM)


Currently supports the following modes:
* Martin 1, 2
* Scottie 1, 2, DX
* Robot 36, 72

Installation
------------

```
$ git clone https://github.com/colaclanth/sstv.git

$ python setup.py install
```

Usage
-----

```
$ sstv -d audio_file.wav -o result.png
```

Resources Used
--------------

* SSTV specification/timings - [The Dayton Paper](http://webcache.googleusercontent.com/search?q=cache:GzP65FlYEtwJ:www.barberdsp.com/downloads/Dayton%2520Paper.pdf)
