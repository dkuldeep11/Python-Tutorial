"""This is a sorting module, which contains following sorts:
- bubble
- selection
- insertion
- merge
- quick
"""

def bubble(A):
	for i in range(len(A)-2, -1, -1):
		for j in range(0, i+1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]

	return A
	#TC = O(n^2)

def selection(A):
	for i in range(0, len(A)-1):
		min = i
		for j in range(i+1,len(A)):
			if A[j] < A[min]:
				min = j
		A[i], A[min] = A[min], A[i]

	return A
	#TC = O(n^2)
	
def insertion(A):
	for i in range(1, len(A)):
		for j in range(i, 0, -1):
			if A[j] < A[j-1]:
				A[j], A[j-1] = A[j-1], A[j]
			else:
				break
	return A
	#TC = O(n^2)

def merge_sort(A):
	return merge_sort_call(A, 0, len(A)-1)
	
def merge_sort_call(A, l, h):
	if l == h:
		return A

	mid =  int((l+h)/float(2))
	A = merge_sort_call(A, l, mid)
	A = merge_sort_call(A, mid+1, h)
	A = merge(A, l, mid, h)

	return A

def merge(A, l, mid, h):
	aux = [n for n in A]
	k = l
	i = l
	j = mid+1
	while i <= mid and j <= h:

		if A[i] <= A[j]:
			aux[k] = A[i]
			k = k + 1
			i = i + 1
		else:
			aux[k] = A[j]
			k = k + 1
			j = j + 1

	while i <= mid:
		aux[k] = A[i]
		k = k + 1
		i = i + 1
	
	while j <= h:
		aux[j] = A[j]
		k = k + 1
		j = j + 1

	return aux


def quick_sort(A):
	return q_sort(A, 0, len(A)-1)

def q_sort(A, l, h):
	if l >= h:
		return

	p = partition(A, l, h)
	q_sort(A, l, p-1)
	q_sort(A, p+1, h)

def partition(A, l, h):
	k = l
	i = l+1
	j = h
	while i < j:
		
		while A[i] <= A[k]:
			i = i + 1
	
		while A[j] > A[k]:
			j = j - 1

		if i < j:
			A[i], A[j] = A[j], A[i]

	A[k], A[j] = A[j], A[k]
	return j

def main():
	A = [40, 60, 20, 30, 15, 20, 35, 55]

	#bubble
	print A
	print "bubble..."
	A = bubble(A)
	print A

	A = [40, 60, 20, 30, 15, 20, 35, 55]
	#selection
	print "\n", A
	print "selection..."
	A = selection(A)
	print A
	
	A = [40, 60, 20, 30, 15, 20, 35, 55]
	#insertion
	print "\n", A
	print "insertion..."
	A = insertion(A)
	print A
	
	A = [40, 60, 20, 30, 15, 20, 35, 55]
	#merge sort
	print "\n", A
	print "merge sort ..."
	A = merge_sort(A)
	print A

	
	A = [40, 60, 20, 30, 15, 20, 35, 55]
	#quick sort
	print "\n", A
	print "quick sort ..."
	quick_sort(A)
	print A

if __name__ == "__main__":
	main()
