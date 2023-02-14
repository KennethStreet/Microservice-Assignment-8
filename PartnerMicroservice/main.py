# Written By Kenneth Street
from flask import Flask, render_template, request
import WaveForm
import os

UPLOAD_FOLDER = 'C:/Users/Kenne/Temp'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def root():
    return render_template("index.html")


@app.route("/get_waveform_image", methods=['POST'])
def send_message():
    file = request.files['audio']
    filename = file.filename
    location = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(location)
    img = WaveForm.create_wavefile(location)
    with open(img, "rb") as image:
        f = image.read()
        b = bytearray(f)

    return b


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
