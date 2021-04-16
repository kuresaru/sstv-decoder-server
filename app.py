from flask import Flask, request
from sstv import SSTVDecoder
from io import BytesIO

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
                    return None, 204
                bimg = BytesIO()
                img.save(bimg, 'PNG')
                return bimg.getvalue(), 200, {'Content-Type': 'image/png'}
        except:
            pass
    return 'Bad file', 400


if __name__ == '__main__':
    app.run()
