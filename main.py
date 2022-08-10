from random import shuffle


repeats = 10000
n_total = 100


def generate_boxes(n_total):
	boxes = list(range(n_total))
	shuffle(boxes)
	return boxes


def the_shower_experience(prisoner, boxes, n_total):
	box_value = prisoner
	for _ in range(n_total//2):
		box_value = boxes[box_value]
		if prisoner == box_value:
			return True
	return False


def get_successes(prisoners, boxes, n_total):
	results = []
	for prisoner in prisoners:
		results.append(the_shower_experience(prisoner, boxes, n_total))
	return results


def compute_pbb(repeats, n_total):
	prisoners = list(range(n_total))
	wins = 0
	for _ in range(repeats):
		if sum(get_successes(prisoners, generate_boxes(n_total), n_total)) == n_total:
			wins += 1
	return wins / repeats


print(compute_pbb(repeats, n_total))
