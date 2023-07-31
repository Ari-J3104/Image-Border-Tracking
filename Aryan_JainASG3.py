import cv2
import numpy as np

"""
# Load the example image
img = cv2.imread('Asg3Image.png')

# Define the colors we will use
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (0, 0, 255)

# Define a variable to hold the selected shape
selected_shape = None

# Define a mouse callback function to capture clicks on the image
def mouse_callback(event, x, y, flags, param):
    global selected_shape
    
    if event == cv2.EVENT_LBUTTONDOWN:
        # Determine which shape was clicked based on the color of the pixel at the mouse coordinates
        color = img[y, x]
        if (color == WHITE).all():
            selected_shape = 'square'

# Create a window to display the image
cv2.namedWindow('Shapes')

# Set the mouse callback function for the window
cv2.setMouseCallback('Shapes', mouse_callback)

while True:
    # Copy the image to a new variable
    display_img = img.copy()
    imgage=display_img.copy()
    
    # Draw a red shape around the selected shape, if one has been selected
    if selected_shape is not None:
        if selected_shape == 'square':
            # Find the contours of the black regions and draw a rectangle around the selected shape
            img_gray = cv2.cvtColor(imgage, cv2.COLOR_BGR2GRAY)
            img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
            edges = cv2.Canny(img_blur, threshold1=100,threshold2=200)
            
            cv2.imshow('image', edges)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            # Find contours in the processed edge image
            contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            
            for contour in contours:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(imgage, (x, y), (x + w, y + h), RED, -1)
      

    # Display the image in the window
    cv2.imshow('Shapes', imgage)
    
    # Wait for a key press
    key = cv2.waitKey(10)
    
    # Exit if the 'q' key is pressed
    if key == ord('q'):
        break

# Clean up and exit
cv2.destroyAllWindows()




MOUSE CLICK X,Y COORDS
"""









def click_event(event, x, y, flags, params):
  
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
  
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)

        """
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x) + ',' +
                    str(y), (x,y), font,
                    1, (255, 0, 0), 2)
        cv2.imshow('image2', img)
        #cv2.waitKey(0)
        """
        
        """
        imgage=img.copy()
        img_gray = cv2.cvtColor(imgage, cv2.COLOR_BGR2GRAY)
        img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
        edges = cv2.Canny(img_blur, threshold1=100,threshold2=200)
            
        cv2.imshow('image', edges)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        # Find contours in the processed edge image
        contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)    
        """
        

        #THIS IS THE RECTANGLE DETECTION SECTION!!!!!
        
        # Load the image
        h,w = img.shape[:2]
        #mask = np.zeros((h+2, w+2), np.uint8)
        # event, (x, y) = cv2.MouseCallbackFlags.EVENT_LBUTTONDOWN, (cv2.MouseCallbackFlags.x, cv2.MouseCallbackFlags.y)
        mask = np.zeros(0)
        img2 = img.copy()
        cv2.floodFill(img, mask, (x,y), (230, 216, 173) ,4)
        img2 = img.copy()

        for i in range(h):
            for j in range(w):
                if(img2[i][j][0] != 255 and img2[i][j][1] != 255 and img2[i][j][2] !=255 and img2[i][j][0] != 230):
                    img2[i][j][0] = 0
                    img2[i][j][1]= 0
                    img2[i][j][2] = 0
                

        cv2.imshow('image3', img2)
        #cv2.waitKey(0)
        

        img3 = img2.copy()
        for i in range(h):
            for j in range(w):
                if(img2[i][j][0] != 230 and img2[i][j][1] != 216 and img2[i][j][2] != 173):
                    img3[i][j][0] = 255
                    img3[i][j][1] = 255
                    img3[i][j][2] = 255

        cv2.imshow('image4', img3)

        for i in range(h):
            for j in range(w):
                if (img3[i][j][0] == 230 and img3[i][j][1] == 216 and img3[i][j][2] == 173):
                    if(img3[i][j+1][0] == 255 and img3[i][j+1][1] == 255 and img3[i][j+1][2] == 255):
                        if(img3[i-1][j][0] == 255 and img3[i-1][j][1] == 255 and img3[i-1][j][2] == 255):
                        
                            print("top right corner")
                            
                            cv2.circle(img3, (j,i), 5, (0,0,255), -1)
                            
                            if(img2[i-1][j][0] == 0 and img2[i-1][j][1] == 0 and img2[i-1][j][2] == 0):
                                print("There exists a blackline above!")
                                
                            if(img2[i][j+1][0] == 0 and img2[i][j+1][1] == 0 and img2[i][j+1][2] == 0):
                                print("There exists a blackline to the right!")
                                for p in range(j,800):
                                    if(img2[i][p][0] == 255):
                                        break
                                    if(img2[i][p][0]==0):
                                        img3[i][p][0] == 0
                                        img3[i][p][1] == 0
                                        img3[i][p][2] == 255
                                        
                                    #ATTEMPT AT MAKING A BLUE LINE 
                                

                            
                        if(img3[i+1][j][0] == 255 and img3[i+1][j][1] == 255 and img3[i+1][j][2] == 255):
                            print("bruh bottom right")
                            cv2.circle(img3, (j,i), 5, (0,0,255), -1)
                    if(img3[i][j-1][0] == 255 and img3[i][j-1][1] == 255 and img3[i][j-1][2] == 255):
                        if(img3[i-1][j][0] == 255 and img3[i-1][j][1] == 255 and img3[i-1][j][2] == 255):
                            print("top left")
                            cv2.circle(img3, (j,i),5,(0,0,255), -1)
                        if(img3[i+1][j][0] == 255 and img3[i+1][j][1] == 255 and img3[i+1][j][2] == 255):
                            print("bottom left")
                            cv2.circle(img3, (j,i), 5,(0, 0, 255),-1)
                            



                            
        cv2.imshow('image4', img3)
        

        
# driver function
if __name__=="__main__":
  
    # reading the image
    img = cv2.imread('Asg3Image.png', 1)


    height, width = img.shape[:2]


    new_width = 800
    new_height = int(height * new_width / width)


    img = cv2.resize(img, (new_width, new_height))



    cv2.namedWindow('testing')
    
    # displaying the image
    cv2.imshow('image1', img)
  
    # setting mouse handler for the image
    # and calling the click_event() function
    cv2.setMouseCallback('image1', click_event)

    # wait for a key to be pressed to exit
    cv2.waitKey(0)
  
    # close the window

cv2.destroyAllWindows()




    
