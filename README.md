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

```shell
docker run -d -p 5000:5000 kuresaru/sstv-decoder-server
```

Build from source
-----------------

```shell
docker build -t kuresaru/sstv-decoder-server .
```

Usage
-----

```shell
# for wav/mp3/ogg ...etc
curl -s "localhost:5000" -X POST -F "file=@test.wav" -o test.png
# for silk v3
curl -s "localhost:5000/silk" -X POST -F "file=@test.slk" -o test.png
```

Resources Used
--------------

* SSTV specification/timings - [The Dayton Paper](http://webcache.googleusercontent.com/search?q=cache:GzP65FlYEtwJ:www.barberdsp.com/downloads/Dayton%2520Paper.pdf)
* [SSTV Decoder](https://github.com/colaclanth/sstv)
* [Silk V3 Decoder](https://github.com/kn007/silk-v3-decoder)
