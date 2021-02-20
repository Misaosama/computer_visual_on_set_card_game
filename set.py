#!/usr/bin/env python3
import numpy as np

'''
The meaning of 4 dimensions of the vector
+----------------------------------------------------+
|0 => number:	1,			2,			3		 	 |
|1 => shape:	diamond	 	oval 		squiggle	 |
|2 => color: 	red	 		green	  	purple	 	 |
|3 => shading: 	solid 		striped 	open 	 	 |
+----------------------------------------------------+
'''

## return true if all three elements are different
def triple_xor(e1, e2, e3):
	return e1 != e2 and e2 != e3 and e1 != e3

## return true if all three elements are the same
def triple_eq(e1, e2, e3):
	return e1 == e2 and e2 == e3

## return true if three cards can make a set
def is_a_set(v1, v2, v3):
	count = 0
	for i in range(4):
		if triple_eq(v1[i], v2[i], v3[i]) or triple_xor(v1[i], v2[i], v3[i]):
			count += 1
	return count == 4

## find all sets of an array of cards
def find_sets(arr):
	res = []
	if len(arr) < 3:
		return res
	for i in range(len(arr)):
		for j in range(i+1, len(arr)):
			for k in range(j+1, len(arr)):
				if is_a_set(arr[i], arr[j], arr[k]):
					res.append((i+1, j+1, k+1)) # increase index by one so non-programmer can easily understand
	return res

if __name__ == "__main__":
	print(is_a_set([3,2,1,1] ,[2,1,2,2], [1,3,3,3])) ## true
	print(is_a_set([2,2,2,3] ,[2,1,2,2], [2,3,2,1])) ## true
	print(is_a_set([2,2,2,1] ,[2,1,2,2], [2,3,2,1])) ## false
	
	print(find_sets([[3,2,1,1] ,[2,1,2,2], [1,3,3,3]]))
	
	print(find_sets([ [1,3,2,3], [3,3,3,3], [2,1,3,3], [1,1,1,1], [3,3,3,1], [1,2,3,2], [1,1,2,2], [2,3,1,2], [3,2,2,1], [3,1,3,1], [2,1,2,1], [1,3,2,1]]))