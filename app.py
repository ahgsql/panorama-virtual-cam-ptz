from flask import Flask
import numpy as np
from PIL import Image
import py360convert
import pyvirtualcam


fileToOpen = "bezge.jpg"
equirectanguler = np.array(Image.open(fileToOpen))
app = Flask(__name__)
h_angle = 0
v_angle = -20
zoom = 1
v_fov = 66/zoom
h_fov = 44/zoom


@app.route('/')
def index():
    return '<a href="https://github.com/ahgsql/panorama-virtual-cam-ptz">Github</a>'


@app.route('/move-x/<angle>')
def cam_horizontal(angle):
    global h_angle
    h_angle += int(angle)
    updateCamera()
    return 'Hello from Server'


@app.route('/move-y/<angle>')
def cam_vertical(angle):
    global v_angle
    v_angle += int(angle)
    updateCamera()
    return 'Hello from Server'


@app.route('/zoom/<zoomAmount>')
def cam_zoom(zoomAmount):
    global zoom, v_fov, h_fov
    zoom = float(zoomAmount)
    v_fov = 66/zoom
    h_fov = 44/zoom
    updateCamera()
    return 'Hello from Server'


cam = pyvirtualcam.Camera(width=640, height=360, fps=25)
print(f'{cam.device} is using as output')


def updateCamera():
    img = py360convert.e2p(equirectanguler, (v_fov, h_fov),
                           h_angle, v_angle, (360, 640), 0, "bilinear")
    cam.send(img)
    cam.sleep_until_next_frame()
