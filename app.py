from flask import Flask, current_app
import numpy as np
from PIL import Image
import py360convert
import pyvirtualcam


fileToOpen = "bezge.jpg"
equirectanguler = np.array(Image.open(fileToOpen))
app = Flask(__name__, static_folder="static")
h_angle = 0
v_angle = -20
zoom = 1
v_fov = 66/zoom
h_fov = 44/zoom


@app.route('/')
def index():
    return current_app.send_static_file('index.html')


@app.route('/move-x/<angle>')
def cam_horizontal(angle):
    global h_angle
    h_angle += int(angle)
    updateCamera()
    return 'Current h angle: {0}'.format(h_angle)


@app.route('/move-y/<angle>')
def cam_vertical(angle):
    global v_angle
    v_angle += int(angle)
    updateCamera()
    return 'Current y angle: {0}'.format(v_angle)


@app.route('/zoom/<zoomAmount>')
def cam_zoom(zoomAmount):
    global zoom, v_fov, h_fov
    zoom = float(zoomAmount)
    v_fov = 66/zoom
    h_fov = 44/zoom
    updateCamera()
    return 'Current Zoom amount: {0}'.format(zoomAmount)


cam = pyvirtualcam.Camera(width=1920, height=1080, fps=25)
print(f'{cam.device} is using as output')


def updateCamera():
    img = py360convert.e2p(equirectanguler, (v_fov, h_fov),
                           h_angle, v_angle, (1080, 1920), 0, "bilinear")
    cam.send(img)


updateCamera()
