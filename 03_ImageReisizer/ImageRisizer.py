
import cv2 


# How to load an image in openCV
# src = cv2.imread("Photo.jpg", cv2.IMREAD_COLOR)
# src = cv2.imread(r"C:\Users\Rohit\Desktop\MyProjects\Python Crash Course- COH\Python Projects\03_ImageReisizer\Photo.jpg", cv2.IMREAD_COLOR)


# Creating GUI window to display an image on screen
# first Parameter is windows title (should be in string format)
# Second Parameter is image array

# if src is None:
#     print("Image not found or path is incorrect.")
# else:
#     cv2.imshow("MY ART", src)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()


# --------- Python Project 3: Image Resizer ------------

# configurable Parameters
source = "C:/Users/Rohit/Desktop/MyProjects/Python Crash Course- COH/Python Projects/03_ImageReisizer/Photo.jpg"
destination = 'newImage.png'
scale_percent = 80


src = cv2.imread(source, cv2.IMREAD_UNCHANGED)




# percent of original size
new_width = int(src.shape[1] * scale_percent / 100)
new_height = int(src.shape[0] * scale_percent / 100)
# dim = (width, height)
 
# resize image
output = cv2.resize(src, (new_width, new_height))

cv2.imwrite(destination, output)
cv2.waitKey(0)

