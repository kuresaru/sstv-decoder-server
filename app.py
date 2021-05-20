import os
from flask import Flask, request
from sstv import SSTVDecoder
from io import BytesIO
import tempfile
import subprocess

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


@app.route('/', methods=['POST'])
def decode():
    f = request.files.get('file')
    if f:
        try:
            baudio = f.stream
            with SSTVDecoder(baudio) as sstv:
                img = sstv.decode()
                if img is None:  # No SSTV signal found
                    return '', 204
                bimg = BytesIO()
                img.save(bimg, 'PNG')
                return bimg.getvalue(), 200, {'Content-Type': 'image/png'}
        except:
            pass
    return '', 204


@app.route('/silk', methods=['POST'])
def silk():
    f = request.files.get('file')
    if f:
        tmp_slk = tempfile.mktemp() + '.slk'
        tmp_pcm = tempfile.mktemp() + '.pcm'
        with open(tmp_slk, "wb") as fw:
            data = f.read()
            fw.write(data)
        pret = subprocess.Popen(
            f"./decoder {tmp_slk} {tmp_pcm} -quiet".split(' ')).wait()
        os.unlink(tmp_slk)
        if pret == 0:
            bimg = None
            with SSTVDecoder(open(tmp_pcm, "rb"), slkraw=True) as sstv:
                img = sstv.decode()
                if img is None:  # No SSTV signal found
                    return '', 204
                bimg = BytesIO()
                img.save(bimg, 'PNG')
            os.unlink(tmp_pcm)
            if bimg:
                return bimg.getvalue(), 200, {'Content-Type': 'image/png'}
    return '', 204


if __name__ == '__main__':
    app.run(host="0.0.0.0")
