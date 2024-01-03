def is_palindrome(n):
	s = str(n)
	return s == s[::-1]


def get_pals():
	pals = []

	for x in range(999, 100, -1):
		for y in range(999, 100, -1):
			if is_palindrome(x*y):
				pals.append(x*y)
	return pals

def main():
	print(max(get_pals()))