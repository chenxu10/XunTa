from collections import defaultdict

def findsubstring(strr):
	count = 0
	start = 0
	min_len = len(strr)
	distinct_count = len(set([x for x in strr]))
	curr_count = defaultdict(int)

	for j in range(len(strr)): # j in end pointer
		curr_count[strr[j]] += 1 #[aabcbdbca]  {"a":1,"b":2}
		if curr_count[strr[j]] == 1:
			count += 1

		if count == distinct_count:
			while curr_count[strr[start]] > 1:
				if curr_count[strr[start]] > 1:
					curr_count[strr[start]] -= 1
				start += 1

			len_window = j - start + 1
			if min_len > len_window:
				min_len = len_window
				start_index = start

	return str(strr[start_index:start_index + min_len])

if __name__ == "__main__":
	assert(findsubstring("aabcbcdbca")=="dbca")
	print(findsubstring("aabcbcdbca")=="dbca")
