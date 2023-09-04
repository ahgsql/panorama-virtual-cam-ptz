# Panorama Virtual Cam with PTZ

PVCP is Python based application that allows you to load an equirectangular image, convert it to a perspective image, and push this image into a live virtual camera driver using UnityCapture. It also provides a web interface powered by Flask to control the camera's angle and zoom.

## Project Goal

The goal of this project is to enable users to transform equirectangular images into perspective images and stream them as a virtual camera feed. This can be useful for various applications, including virtual reality experiences or projects that rely on ptz cameras.

I need this kind of virtual camera for my fire-dedection system.

## Mechanism

1.  **Image Conversion**: The application loads an equirectangular image (specified in the `fileToOpen` variable) and converts it into a perspective image using the `py360convert` library.
2.  **Virtual Camera**: It utilizes the `pyvirtualcam` library to create a virtual camera with specified dimensions (width, height, fps) and sends the converted perspective image to this virtual camera.
3.  **Web Interface**: The application provides a Flask-based web interface to control the camera's horizontal and vertical angles as well as zoom. It listens on specified routes to adjust these parameters.

## Flask Routes

- **Root Route ("/")**:

  - Description: This route serves as a basic indicator that the server is running.
  - Usage: Visit this route to check if the server is operational.

- **Horizontal Camera Movement ("/move-x/angle")**:

  - Description: Adjusts the horizontal angle of the virtual camera.
  - Usage: Access this route with a specified angle to move the camera horizontally.
  - 
    http://127.0.0.1:5000/move-x/4

- **Vertical Camera Movement ("/move-y/angle")**:
  - Description: Adjusts the vertical angle of the virtual camera.
  - Usage: Access this route with a specified angle to move the camera vertically.
  - 
    http://127.0.0.1:5000/move-y/-2
    
- **Zoom Control ("/zoom/zoomAmount")**:
  - Description: Changes the zoom level of the virtual camera.
  - Usage: Access this route with a specified zoom amount to control the camera's zoom.
    http://127.0.0.1:5000/zoom/1.3

## PTZ (Pan-Tilt-Zoom) Feature

- **Pan (Horizontal Angle)**: You can adjust the horizontal angle of the virtual camera using the `/move-x/<angle>` route.
- **Tilt (Vertical Angle)**: You can adjust the vertical angle of the virtual camera using the `/move-y/<angle>` route.
- **Zoom**: You can control the zoom level of the virtual camera using the `/zoom/<zoomAmount>` route.

## Usage

1. Install Unity Capture
   Visit https://github.com/schellingb/UnityCapture#installation for more information
2. Clone this repository

   `git clone https://github.com/yourusername/panorama-virtual-cam-ptz.git`

3. Install the required dependencies:

   `pip install -r requirements.txt`

4. Run the application:

   `flask run`

5. Access the web interface to control the virtual camera.
