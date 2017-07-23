""" 1D peak finder - 
Version 1: 1) Scan through the list, compare adjacent element(s) for each element.
		   2) If number, i > i-1, i > i+1 => 'i' is the peak.

Version 2:  1) Find middle number 'i', compare with adjacent elements, return if it is the peak.
			2) a) If i<i-1, consider left half to the middle element and run step1.
			   b) If i<i+1, consider right half to the middle element and run step1.
			   c) Else 'i' is peak.

Results:
1) listSize = 100,000
	version1 run time - 0.0781 Sec
	version2 run time - 0.0001 Sec

2) listSize = 10,00,000
	version1 run time - 0.781 Sec
	version2 run time - 0.0468 Sec
"""
import time
start_time = time.time()
#inputList = input("Enter list numbers:")
inputList = [1,2,3,4,5,6,7,8,9,10,11,12,11,14,15,16,17,18,19,20,21,22,23,24,25]

# Peak finder, version 1 - Basic iterative algorithm.
def peak_finder_v1(inputList, listLen):
	if (inputList):
		for index in range(listLen):
			if (index != listLen-1 and index != 0) and (inputList[index] > inputList[index-1]) \
					and (inputList[index]>inputList[index+1]):
				return inputList[index]
			elif (index == listLen-1 and inputList[index] > inputList[index-1]):
				return inputList[index]

def peak_finder_v1_main(inputList):
	listLen = len(inputList)
	if listLen == 0:
		return print("List is Empty. Cannot find the peak.")
	elif listLen == 1:
		return inputList[0]
	else:
		return peak_finder_v1(inputList, listLen)


""" version2: Optimized solution using recursive approach.
"""
# Helper function to find the list length.
def findListLen(inputList):
	return len(inputList)

# Helper function to find the middle index.
def findMidPoint(inputList):
	if inputList is not None:
		return findListLen(inputList)//2
	else:
		return -1

# Peak finder function - Version2 - Iterative solution.
def peak_finder_v2 (inputList):
	midPoint = findMidPoint(inputList)
	if findListLen(inputList) == 1 or midPoint == 0:
		return inputList[0]
	elif findListLen(inputList) == 2:
		if inputList[midPoint] < inputList[midPoint-1]:
			return inputList[midPoint-1]
		else:
			return inputList[midPoint]
	else:
		if inputList[midPoint] < inputList[midPoint-1]:
			return peak_finder_v2(inputList[:midPoint])
		elif inputList[midPoint] < inputList[midPoint+1]:
			return peak_finder_v2(inputList[midPoint:])
		else:
			return inputList[midPoint]

def peak_finder_v2_main(inputList):
	listLen = findListLen(inputList)
	if listLen == 0:
		return print("Input list is empty. A peak can't be found.")
	elif listLen == 1:
		return inputList[0]
	else:
		return peak_finder_v2(inputList)

peak_val = peak_finder_v2_main(inputList)
print("Peak found in the list, value:"+str(peak_val))
print("--- %s seconds ---" % (time.time() - start_time))