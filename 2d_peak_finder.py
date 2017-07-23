"""
2D Peak Finder: This code finds out the 2D peak in a given matrix/ 2D array.
Algorithm: 1) Find mid column, find the index of max element in that row.
		   2) Compare with adjacent elements, then run the same logic recursively
		   		i) on left half of array, if array[i,j] < array[i,j-1]
		   		ii) on right half of array, if array[i,j] < array[i,j+1]
		   		iii) return array [i,j], if (i), (ii) fails.
		   		Note: (i,j) -> location of the global max in the middle column.

"""

import numpy as np
import time
start_time = time.time()

# Input 2D array.
twoDInput = np.matrix([
	[ 4,  5,  6,  7,  8,  7,  6,  5,  4,  3,  2],
	[ 5,  6,  7,  8,  9,  8,  7,  6,  5,  4,  3],
	[ 6,  7,  8,  9, 10,  9,  8,  7,  6,  5,  4],
	[ 7,  8,  9, 10, 11, 10,  9,  8,  7,  6,  5],
	[ 8,  9, 10, 11, 12, 13, 14,  9,  8,  7,  6],
	[ 7,  8,  9, 10, 11, 10,  9,  8,  7,  6,  5],
	[ 6,  7,  8,  9, 10,  9, 85,  7,  6,  5,  4],
	[ 5,  6,  7,  8,  9,  8,  7,  6,  5,  4,  3],
	[ 4,  5,  6,  7,  8,  7,  6,  5,  4,  3,  2],
	[ 3,  4,  5,  6,  7,  6,  5,  4,  3,  2,  1],
	[ 2,  3,  4,  5,  6,  5,  4,  3,  2,  1,  1]
])

# Helper function to find the size of 2D array.
# @param - 2D array.
def findSize (input):
	return np.shape(input)

# Helper function to find the middle column in a 2D array.
# @param - 2D array.
def findMidCol(input):
	if input is not None:
		inputSize = findSize(input)
		return inputSize[1]//2
	else:
		return -1

# Helper function to find the row index of element with max value.
# @param - Single column matrix.
def findMaxIndex(colInput):
	if colInput is not None:
		return np.argmax(colInput)
	else:
		return -1

# Recursive function to find the peak in a 2D array.
# @param - 2D array.
def peakFinder(input):
	(r,c) = findSize(input)
	midCol = findMidCol(input)
	if midCol != -1:
		# row index of max element of mid column.
		i = findMaxIndex(input[:,midCol])
	# If columns of input array is 1, return the max element as peak.
	if (c == 1):
		return np.amax(input)
	# If columns of input array is 2, just compare with available adjacent element.
	elif (c == 2):
		if (input[i,midCol] < input[i,midCol-1]):
			return peakFinder(input[:,midCol-1])
		else:
			return input[i,midCol]
	# peak finder logic for column length > 2.
	else:
		if (input[i,midCol] < input[i,midCol-1]):
			return peakFinder(input[:,:midCol])
		elif (input[i,midCol] < input[i,midCol+1]):
			return peakFinder(input[:,midCol:])
		else:
			return input[i,midCol]

def main(input):
	# Check if array is empty
	if (input is None):
		return print("Input Matric is Empty. A peak can't be found!")
	# Check if the array has only 1 element.
	elif findSize(input) == (1,1):
		return input[0,0]
	else:
		return peakFinder(input)

peakValue = main(twoDInput)
print("Peak found in the input, value is: "+str(peakValue))
print("--- %s seconds ---" % (time.time() - start_time))