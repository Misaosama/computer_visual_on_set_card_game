#!/usr/bin/env python3
import cv2
import numpy as np
import time
import os
import Cards

if __name__ == "__main__":
	image = cv2.imread('image/image2.webp')
	
	img = Cards.preprocess_image(image)
	
	
	
	# Find and sort the contours of all cards in the image (query cards)
	cnts_sort, cnt_is_card = Cards.find_cards(img)
	print(cnt_is_card )
	if len(cnts_sort) != 0:
		# Initialize a new "cards" list to assign the card objects.
		# k indexes the newly made array of cards.
		cards = []
		k = 0
	
		# For each contour detected:
		for i in range(len(cnts_sort)):
			if (cnt_is_card[i] == 1):
				cv2.drawContours(image,cnts_sort[i],-1,(0,0,255),3)
				cards.append(Cards.preprocess_card(cnts_sort[i], image))

		for i in range(len(cards)):
			cv2.imshow('{}'.format(i), cards[i].warp)
			cv2.waitKey(10)
			input("Press Enter to continue...")
	
	# Output img with window name as 'image' 
	cv2.imshow('image', img)
	cv2.waitKey(10)
	input("Press Enter to continue...")
	cv2.imshow('image', image)
	
	# Maintain output window utill 
	# user presses a key 
	cv2.waitKey(10)         
	
	# Destroying present windows on screen 
	cv2.destroyAllWindows()
	