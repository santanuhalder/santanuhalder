from collections import namedtuple

def max_cost_provider(provider_cost, diagnosis):
    cost = provider_cost[diagnosis]
    provider = max(cost, key=cost.get)
    return provider


Visit = namedtuple("Visit", ["provider_id", "diagnosis_code", "cost"])
visits = [Visit("sinai", "ear_infection", 100), Visit("sinai", "ear_infection", 200),
          Visit("nyu", "ear_infection", 300), Visit("nyu", "bronchitis", 200),
          Visit("nyu", "ear_infection", 200), Visit("sinai", "ear_infection", 300)]
cost_dict = dict()
counter_dict = {}

for i in range(len(visits)):
    provider = visits[i].provider_id
    diagnosis = visits[i].diagnosis_code
    cost = visits[i].cost

    if diagnosis not in cost_dict:
        cost_dict[diagnosis] = {provider: cost}
        counter_dict[diagnosis+provider] = counter_dict.setdefault(diagnosis+provider, 0) + 1
    elif provider not in cost_dict[diagnosis]:
        cost_dict[diagnosis][provider] = cost
        counter_dict[diagnosis+provider] = counter_dict.setdefault(diagnosis+provider, 0) + 1
    else:
        count = counter_dict[diagnosis+provider]
        cost_dict[diagnosis][provider] = ((cost_dict[diagnosis][provider])*count + cost) / (count + 1)
        counter_dict[diagnosis+provider] = count + 1

print(cost_dict)
diagnosis = "ear_infection"
print(max_cost_provider(cost_dict, diagnosis))

