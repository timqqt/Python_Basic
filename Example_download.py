# import os
# from urllib.request import urlretrieve
# os.makedirs('./img/', exist_ok=True)
# img_url = "https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png"
# urlretrieve(img_url, './img/image1.png')
import requests
img_url = "https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png"
r = requests.get(img_url, stream=True)
with open('./img/image3.png', 'wb') as f:
    for chunk in r.iter_content(chunk_size=32):
        f.write(chunk)