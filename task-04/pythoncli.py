from pip._vendor import requests
date=input('Enter date')
ide=int(input("Enter ID"))
l=['spirit','curiosity','opportunity']
for rover in l:
	response=requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date="+date+"&api_key=15AprzMowARDYrOCuDzi6jvvZJuQ5S4xGoqcoaSG")
	fil=response.json()["photos"]
	for i in fil:
		if i['id']==ide:
			imag=i['img_src']
print(imag,'\nDisplaying...')
import numpy as np
import urllib.request as url
import cv2
def openimg(i):
	resp = url.urlopen(i)
	image = np.asarray(bytearray(resp.read()), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)
	return image
image = openimg(imag)
cv2.imshow("Image", image)
cv2.waitKey(0)
print("Finished.")
