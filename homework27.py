import requests
# 1. Отримайте поточний статус війни як англійською, так і українською мовою.
# 2. Отримайте останню статистику по війні
# 3. Отримайте статистику за 2 різні дні (виберіть дату самостійно).

# Task 1
responce_one_eng = requests.get('https://russianwarship.rip/api/v2/war-info/status/en')

print('\n')
print(responce_one_eng.json().get('data').get('description'))

responce_one_ua = requests.get('https://russianwarship.rip/api/v2/war-info/status/ua')

print('\n')
print(responce_one_ua.json().get('data').get('description'))

# Task 2
responce_two = requests.get('https://russianwarship.rip/api/v2/statistics/latest')

print('\n')
print(responce_two.json().get('data'))

# Task 3 
responce_three_0516 = requests.get('https://russianwarship.rip/api/v2/statistics/2022-05-16')

print('\n')
print(responce_three_0516.json().get('data'))
responce_three_0603 = requests.get('https://russianwarship.rip/api/v2/statistics/2022-06-03')

print('\n')
print(responce_three_0603.json().get('data'))