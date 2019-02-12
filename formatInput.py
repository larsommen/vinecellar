def doTable(output):
	output.replace("  ", " ")
	output.replace("  ", " ")
	result = "<table>"
	tempArray = output.split("\n")
	for lines in tempArray:
		line = lines.split(" ")
		result += "<tr>"
		for word in line:
			word.replace(" ","")
			if word != "":
				result += "<td>"+word+"</td>"
		result += "</tr>"
	result += "</table>"
	return result
