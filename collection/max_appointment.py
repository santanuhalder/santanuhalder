def maxAppointment(appointments):
    appts = {}
    for i in range(len(appointments)):
        appts[appointments[i]] = appts.setdefault(appointments[i], 0) + 1
    max_day = max(appts, key=appts.get)
    days = [key for key in appts if appts[key] == appts[max_day]]
    return days


arr1 = [14, 14, 2, 1, 3]
arr2 = [14, 14, 2, 2, 1, 1, 3, 3, 3]
print(maxAppointment(arr2))


