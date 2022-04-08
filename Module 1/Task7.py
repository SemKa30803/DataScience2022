results = {
    'vk': {'revenue': 103, 'cost': 98},
    'yandex': {'revenue': 179, 'cost': 153},
    'facebook': {'revenue': 103, 'cost': 110},
    'adwords': {'revenue': 35, 'cost': 34},
    'twitter': {'revenue': 11, 'cost': 24},
}

for i in results:
    # print (i)
    results[i]['ROI'] = round((results[i]['revenue'] / results[i]['cost'] - 1) * 100 * 100) / 100
print(results)
