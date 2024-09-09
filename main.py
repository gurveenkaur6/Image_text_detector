import cv2
import matplotlib.pyplot as plt
import easyocr



# read the image
image_path = "images/American_highway_exit_sign.png"
image= cv2.imread(image_path, cv2.IMREAD_COLOR)

# initialise the text detector
reader = easyocr.Reader(['en'])

# detect the text on the image
results = reader.readtext(image)
for t in results:
    
    print(results)

# draw bbox and text