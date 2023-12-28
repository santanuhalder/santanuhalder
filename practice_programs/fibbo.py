def fibbo(n: int):
	# 0, 1, 1, 2, 3, 5, 8, 13
	memo = {}
	if n <= 1:
		return n
	first_term = fibbo(n-2)
	second_term = fibbo(n-1)
	return first_term + second_term



def fibbo_iter(n):
	if n <= 1:
		return n
	fibbo = [0, 1]
	for i in range(2, n + 1):
		fibbo.append(fibbo[i-2] + fibbo[i-1])
	return fibbo.pop()







# Test the Fibonacci function
result_5 = fibbo(5)
print(f"Fibonacci(5) = {result_5}")  # Expected output: 5

result_7 = fibbo_iter(7)
print(f"Fibonacci(7) = {result_7}")  # Expected output: 13

result_8 = fibbo(8)
print(f"Fibonacci(8) = {result_8}")  # Expected output: 21

result_12 = fibbo(12)
print(f"Fibonacci(12) = {result_12}")  # Expected output: 144

