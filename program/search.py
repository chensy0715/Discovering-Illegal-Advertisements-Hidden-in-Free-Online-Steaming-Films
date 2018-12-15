from selenium import webdriver
import pytesseract
from PIL import Image
import numpy as np
import pyautogui
import imutils
import cv2
import time

test = open("list1.txt")
temp = []

#read file list


while True:
	line = test.readline()
	print(line)
	temp.append(line)
#	print(line)
	if not line: 
		break
		
test.close()
print(temp)


#i = 0
#j = 1


length = len(temp)

b = webdriver.Chrome()

# first three minutes
file_n = 0
file_name = 'extracted_text_'


#only one-time screeshot

#while(1):
#	
#	# take screenshot
#	image = pyautogui.screenshot(region=(0,0,2560,400))
#	image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
#	screenshot = str(i) + ".jpg"
#	cv2.imwrite(screenshot, image)
#
#	# OCR detection
#	text = pytesseract.image_to_string(screenshot, lang='chi_sim')
#	f = open(file_name+str(file_n)+'.txt', 'a')
#	f.write(text)
#	f.close()
#	
#	i+=1
#	time.sleep(3)
#	if(i==60):
#		break
#	else:
#		continue




#i = 0
#j = 1
k = 0
i = 0
j = 1

while(k<length -1):
	temp1 = temp[k]
	print(temp1)
#	b = webdriver.Chrome()
	b.get(temp[k])
	content = b.find_element_by_class_name('ytp-fullscreen-button')
	
	content.click()
#	time.sleep(20)
#	i += 1
	time.sleep(10)
	
	
#screenshot and OCR detection in the beginning	
	
	j = 1
	
	while(1):
		
#		image = pyautogui.screenshot(region=(0,0,2560,400))
#		image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
#		cv2.imwrite(str(j)+ ".jpg", image)	
#		time.sleep(10)
		
		# take screenshot
#		image = pyautogui.screenshot(region=(0,0,2560,400))
		image = pyautogui.screenshot(region=(0,0,2560,1000))
		image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
		screenshot = str(i) + ".jpg"
#		screenshot = "/Users/shengyuchen/Desktop/sample/"+ str(i) + ".jpg"
		cv2.imwrite(screenshot, image)
		
		# OCR detection
#		text = pytesseract.image_to_string(screenshot, lang='chi_sim')
#		f = open(file_name+str(k)+'.txt', 'a')
##		f = open("/Users/shengyuchen/Desktop/sample/"+file_name+str(k)+'.txt', 'a')
#		f.write(text)
#		f.close()
#		time.sleep(5)
		
		i+=1
		j+=1
		time.sleep(5)
		if(j==10):
			break
		else:
			continue
		
#screenshot and OCR dection in the middle	
		
	b.get(temp[k])
	content = b.find_element_by_class_name('ytp-fullscreen-button')
	
	content.click()
	

	time.sleep(10)	
	time.sleep(20)
	j = 1
	
	
	while(1):
		# take screenshot
#		image = pyautogui.screenshot(region=(0,0,2560,400))
		image = pyautogui.screenshot(region=(0,0,2560,1000))
		image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
		screenshot = str(i) + ".jpg"
#		screenshot = "/Users/shengyuchen/Desktop/sample/"+ str(i) + ".jpg"
		cv2.imwrite(screenshot, image)

		# OCR detection
#		text = pytesseract.image_to_string(screenshot, lang='chi_sim')
#		f = open(file_name+str(k)+'.txt', 'a')
##		f = open("/Users/shengyuchen/Desktop/sample/"+file_name+str(k)+'.txt', 'a')
#		f.write(text)
#		f.close()
		
		i+=1
		j+=1
		time.sleep(5)
		if(j==10):
			break
		else:
			continue
			
			
#if need to add more screeshot section in 2/3 
		
#	b.get(temp[k])
#	content = b.find_element_by_class_name('ytp-fullscreen-button')
#	
#	content.click()
#	
#
#	time.sleep(10)	
#	time.sleep(20)
#	j = 1
#	
#	
#	while(1):
#		# take screenshot
##		image = pyautogui.screenshot(region=(0,0,2560,400))
#		image = pyautogui.screenshot(region=(0,0,2560,1000))
#		image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
#		screenshot = str(i) + ".jpg"
##		screenshot = "/Users/shengyuchen/Desktop/sample/"+ str(i) + ".jpg"
#		cv2.imwrite(screenshot, image)
#
#		# OCR detection
#		text = pytesseract.image_to_string(screenshot, lang='chi_sim')
#		f = open(file_name+str(k)+'.txt', 'a')
##		f = open("/Users/shengyuchen/Desktop/sample/"+file_name+str(k)+'.txt', 'a')
#		f.write(text)
#		f.close()
#		
#		i+=1
#		j+=1
#		time.sleep(5)
#		if(j==10):
#			break
#		else:
#			continue
#		
		
		
#screenshot and OCR dectection in the end	
	
	time.sleep(20)
	j = 1
	b.get(temp[k])
	content = b.find_element_by_class_name('ytp-fullscreen-button')
	
	content.click()
	time.sleep(10)
		
	while(1):
			# take screenshot
#		image = pyautogui.screenshot(region=(0,0,2560,400))
		image = pyautogui.screenshot(region=(0,0,2560,1000))
		image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
		screenshot = str(i) + ".jpg"
#		screenshot = "/Users/shengyuchen/Desktop/sample/1.jpg"
#		screenshot = "/Users/shengyuchen/Desktop/sample/"+ str(i) + ".jpg"
		cv2.imwrite(screenshot, image)

		# OCR detection
#		text = pytesseract.image_to_string(screenshot, lang='chi_sim')
#		f = open(file_name+str(k)+'.txt', 'a')
##		f = open("/Users/shengyuchen/Desktop/sample/"+file_name+str(k)+'.txt', 'a')
#		f.write(text)
#		f.close()
			
		i+=1
		j+=1
		time.sleep(5)
		if(j==10):
			break
		else:
			continue	
	
	
	
	
	time.sleep(10)
	k+=1
	
	
	
	
	






