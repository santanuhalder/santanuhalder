def can_transfer(glucose_data: list, threshold: int) -> bool:
    """
    Method determines whether a patient can be transferred.
    :param glucose_data: input array of glucose data
    :param threshold: glucose threshold
    :return: True if the patient can be transferred -> biggest drop in insulin is less than the threshold
             False if the patient can not be transferred -> biggest frop in insulin is not less than the threshold
    """
    drop = 0
    maxDrop = 0
    for i in range(1, len(glucose_data)):
        if glucose_data[i - 1] > glucose_data[i]:
            maxDrop = max(maxDrop, glucose_data[i - 1] - glucose_data[i])

    if maxDrop < threshold:
        return True
    else:
        return False


glc_data = [89, 93, 92, 91, 92, 90, 94, 104, 103, 102, 106]
print(can_transfer(glc_data, 10))


