def can_transfer_patient(glucose_data: list, threshold: int, daterange: int) -> bool:
    """
    Method determines whether a patient can be transferred.
    :param glucose_data: input array of glucose data
    :param threshold: glucose threshold
    :return: True if the patient can be transferred -> biggest drop in insulin is less than the threshold
             False if the patient can not be transferred -> biggest frop in insulin is not less than the threshold
    """
    drop = 0
    i, j = 0, 0
    while j - i + 1 < daterange:
        j += 1

    can_transfer = True

    for m in range(j, len(glucose_data)):
        drop = glucose_drop(glucose_data[i:m+1])
        i += 1
        m += 1
        if drop > threshold:
            can_transfer = False
    return can_transfer

def glucose_drop(glucose_data: list) -> int:
    """
    Method determines whether a patient can be transferred.
    :param glucose_data: input array of glucose data
    :param threshold: glucose threshold
    :return: True if the patient can be transferred -> biggest drop in insulin is less than the threshold
             False if the patient can not be transferred -> biggest frop in insulin is not less than the threshold
    """
    drop_ = 0
    maxDrop_ = -float("inf")
    for i in range(1, len(glucose_data)):
        if glucose_data[i - 1] > glucose_data[i]:
            drop_ = glucose_data[i - 1] - glucose_data[i]
            maxDrop_ = max(maxDrop_, drop_)
    return maxDrop_



glc_data = [89, 93, 92, 91, 92, 90, 94, 104, 103, 102, 106]
print(can_transfer_patient(glc_data, 10, 3))


