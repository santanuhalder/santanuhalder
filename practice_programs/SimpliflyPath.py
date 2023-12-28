def simplifyPath(path):
	path_list = path.split('/')
	res = list()
	for char in path_list:
		if (char == '' or char == '.') or (char == '..' and not res):
			pass
		elif char == '..':
			res.pop()
		else:
			res.append(char)
	return '/' + '/'.join(res)


input_path = "/a//b////c/d//././/.."
solution = simplifyPath(input_path)
# solution1 = simplifyPath_new(input_path)
print(solution)



