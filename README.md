![image](https://user-images.githubusercontent.com/63831913/218657948-7a87cc93-6a87-4af9-a388-83074c4a4acb.png)


Communication Contract


How to REQUEST DATA
The Endpoint is 'http://127.0.0.1:5000/get_waveform_image'
The Method is POST
You pass the audio file you want to get a waveform image of by attaching that image to the files header within requests.

How to RECEIVE DATA
The response will be an HTTP Response and you can convert the ByteArray in requests.Content to get your image 

Example:

import requests
import io
import PIL.Image as Image


def main():
    url = 'http://127.0.0.1:5000/get_waveform_image'
    audiofile = 'C:/Users/Kenne/Downloads/StarWars3.wav'
    with open(audiofile, 'rb') as fobj:
        response = requests.post(url, files={'audio': fobj})
        image = Image.open(io.BytesIO(response.content))
        image.save('C:/Users/Kenne/Temp/Images/Image/foo.png')


if __name__ == '__main__':
    main()
