import cv2
image=cv2.imread("mens shirts2.jpg",1)
cv2.line(image,(0,0),(800,800),(255,0,0),5)
cv2.rectangle(image,(210,210),(550,550),(0,255,0),2)
cv2.circle(image,(100,100),100,(0,0,255),-1)
cv2.circle(image,(615,615),100,(0,0,255),-1)
cv2.circle(image,(615,100),100,(0,0,255),-1)
cv2.circle(image,(100,615),100,(0,0,255),-1)
font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(image,"hello",(220,400),font,4,(10,56,167))
cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()