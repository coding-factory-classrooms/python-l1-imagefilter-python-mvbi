import cv2

def VideoCapture(video):
  """
  Capture every frame from a video file
  :param video:  Video file to capture
  """
  
  vidcap = cv2.VideoCapture(f'video/{video}')
  success, image = vidcap.read()
  count = 0

  while success:
    img = "img/frame%d" % count + '.jpg'
    cv2.imwrite(img, image)     # save frame as JPEG file
    success, image = vidcap.read()
    print('Read a new frame: ', success)
    count += 1