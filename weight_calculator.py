def calculate():
	""" convert raw weight value into weight on either side from 45lb 25lb 10lb 5lb 2.5lb plates """
	input_weight = input("What weight are you working with?")
	input_weight = int(input_weight)
	working_weight = (input_weight - 45)/2
	plates = {45: 0 , 25: 0, 10: 0, 5: 0, 2.5: 0}
	for plate in plates:
		while working_weight//plate > 0:
			plates[plate] += 1
			working_weight = working_weight - plate

	print(plates, input_weight)
	for i in plates:
		print(i, ":", plates[i])



if __name__ == "__main__":
	calculate()