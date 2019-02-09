def findAvg(string):

	avg = 0
	sumTotal = 0
	number = 0

	with open(string , "r") as thisfile:
		for line in thisfile:
			number += 1
			sumTotal += float(line)
	thisfile.close()
	avg = sumTotal/number
	return round(avg, 1);

def findMin(string):

	minVal = 100
	with open(string , "r") as thisfile:
                for line in thisfile:
                        if (float(line) < minVal):
				minVal = float(line)
        thisfile.close()
	return round(minVal, 1);

def findMax(string):

        maxVal = 0
        with open(string , "r") as thisfile:
                for line in thisfile:
                        if (float(line) > maxVal):
                                maxVal = float(line)
        thisfile.close()
        return round(maxVal, 1);

def getStats(string):
	avg = str(findAvg(string))
	minimum = str(findMin(string))
	maximum = str(findMax(string))
	return avg, minimum, maximum;

