import cv2
import matplotlib.pyplot as plt
import easyocr
import bbox



# read the image
image_path = "images/American_highway_exit_sign.png"
image= cv2.imread(image_path, cv2.IMREAD_COLOR)

# initialise the text detector
reader = easyocr.Reader(['en'])

# detect the text on the image
# This method returns a list of results, where each result includes the bounding box, detected text, and confidence score
results = reader.readtext(image)

# draw bbox and text
for t in results:
    print(t)
    bbox, text, score = t

    top_left, top_right,bottom_right,bottom_left = bbox

    # pixels can only be whole numbers
    top_left = tuple(map(int,top_left)) 
    bottom_right = tuple(map(int, bottom_right))

    # drawing a green rectangle on the image
    cv2.rectangle(image, top_left, bottom_right, (0,255,0), 5)

    cv2.putText(image, text, (top_left[0], top_left[1] - 10) , cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,255), 2)

# need to convert from bgr to rgb to match the color of the source/original image
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()
