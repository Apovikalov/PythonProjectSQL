import requests

params = {
    'text': 'Программист',
    'area': 55,
    'per_page': 10,
    'page': 0
}
response = requests.get("https://api.hh.ru/vacancies", params=params)
if response.text.strip():
    data = response.json()
else:
    data = {}

print(response)

with open("hh_response.html", "wb") as file:
    file.write(response.content)

for vacancy in data['items']:
    print(f"ID: {vacancy['id']}")
    print(f"Название: {vacancy['name']}")
    print(f"Компания: {vacancy['employer']['name']}")
    print(f"Зарплата: {vacancy.get('salary', 'Не указана')}")
    print('-' * 50)
