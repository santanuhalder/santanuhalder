def maxAppointment(arr, n):
    appointments = dict()
    for i in range(len(arr)):
        appointments[arr[i]] = appointments.setdefault(arr[i], 0) + 1
    max_value = 0
    max_key = 0
    for key, value in appointments.items():
        if value >= max_value:
            max_value = value
            max_key = key
    return max_key


arr = [4, 24, 23, 24, 22, 5, 5, 4, 4, 3]
arr.sort()
k = 3
print(maxAppointment(arr, k))
