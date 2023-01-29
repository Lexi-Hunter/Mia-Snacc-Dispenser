# Web streaming code modified from: http://picamera.readthedocs.io/en/latest/recipes2.html#web-streaming

import io
import picamera
import logging
import socketserver
import RPi.GPIO as GPIO
from threading import Condition
from http import server
import time

ControlPins = [7, 11, 13, 15]

GPIO.setmode(GPIO.BOARD)

GPIO.setup(37, GPIO.OUT)
GPIO.output(37, 0)

for pin in ControlPins:
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, 0)

seq = [
    [1,1,0,0],
    [0,1,1,0],
    [0,0,1,1],
    [1,0,0,1]
]

def refill():
    for i in range(30):
        time.sleep(2)
        giveTreat(refill=True)

def giveTreat(refill=False):
    GPIO.output(37,1)
    time.sleep(0.5)
    GPIO.output(37,0)

    if not refill:
        #Flash light
        for i in range(3):
            GPIO.output(37,1)
            time.sleep(0.5)
            GPIO.output(37,0)
            time.sleep(0.5)
    #Spin backwards briefly
    for i in range(10):
        for seq_step in seq[::-1]:
            for index, val in enumerate(seq_step):
                GPIO.output(ControlPins[index], val)
                time.sleep(0.002)
    #Spin forwards
    for i in range(32+10):
        for seq_step in seq:
            for index, val in enumerate(seq_step):
                GPIO.output(ControlPins[index], val)
                time.sleep(0.002)
    for pin in ControlPins:
        GPIO.output(pin,0)
    
    if not refill:
        time.sleep(5)

PAGE="""\
<html>
<head>
<style>
.button {
  background-color: #4CAF50; /* Green */
  border: none;
  color: white;
  padding: 15px 64px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 60px;
  margin: 4px 2px;
  cursor: pointer;
  width: 100%;
  height: 13%
}

h1 {
  font-size: 80;
}

img {
  width: 100%;
  height: auto;
}


</style>
<title>Mia Snack Dispenser</title>
</head>
<body>
<center><h1>Mia Snack Dispenser</h1></center>
<center><img src="stream.mjpg" width="320" height="240"></center>
<center><a href="/on" target="_parent"><button class="button">Give dog snacc</button></a></center>
</body>
</html>
"""

class StreamingOutput(object):
    def __init__(self):
        self.frame = None
        self.buffer = io.BytesIO()
        self.condition = Condition()

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            # New frame, copy the existing buffer's content and notify all
            # clients it's available
            self.buffer.truncate()
            with self.condition:
                self.frame = self.buffer.getvalue()
                self.condition.notify_all()
            self.buffer.seek(0)
        return self.buffer.write(buf)

class StreamingHandler(server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(301)
            self.send_header('Location', '/index.html')
            self.end_headers()
            
        elif self.path == '/index.html':
            content = PAGE.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(content))
            self.end_headers()
            
            self.wfile.write(content)
        elif self.path == '/stream.mjpg':
            self.send_response(200)
            self.send_header('Age', 0)
            self.send_header('Cache-Control', 'no-cache, private')
            self.send_header('Pdaragma', 'no-cache')
            self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
            self.end_headers()

            try:
                while True:
                    with output.condition:
                        output.condition.wait()
                        frame = output.frame
                    self.wfile.write(b'--FRAME\r\n')
                    self.send_header('Content-Type', 'image/jpeg')
                    self.send_header('Content-Length', len(frame))
                    self.end_headers()
                    self.wfile.write(frame)
                    self.wfile.write(b'\r\n')
                    # Turn Green light on
                    #GPIO.output(37,1)

            except Exception as e:
                logging.warning(
                    'Removed streaming client %s: %s',
                    self.client_address, str(e))
                # Turn green light off
                #GPIO.output(37,0)
        elif self.path == '/on':
            giveTreat()
            content = PAGE.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(content))
            self.end_headers()
            self.wfile.write(content)

        elif self.path == '/refill':
            refill()
            content = PAGE.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(content))
            self.end_headers()
            self.wfile.write(content)

        else:
            self.send_error(404)
            self.end_headers()

class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
    allow_reuse_address = True
    daemon_threads = True

with picamera.PiCamera(resolution='320x240', framerate=24) as camera:
    output = StreamingOutput()
    #Uncomment the next line to change your Pi's Camera rotation (in degrees)
    #camera.rotation = 90
    camera.start_recording(output, format='mjpeg')
    try:
        address = ('', 8000)
        server = StreamingServer(address, StreamingHandler)
        server.serve_forever()
    finally:
        camera.stop_recording()
        GPIO.cleanup()
