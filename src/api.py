# from http.client import responses
from typing import Optional, Dict, List

import requests

class HHApi:

    def __init__(self) -> None:
        self.base_url = 'https://api.hh.ru/'
        self.headers = {'User-Agent': 'HH-User-Agent'}

    def get_employer(self, employer_id: str) -> Optional[Dict]:
        """Получение данных о работодателе по его ID"""
        url = f'{self.base_url}employers/{employer_id}'
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        print(f'Получение данных о работодателе "{response.json()['name']}".')
        return response.json() if response.status_code == 200 else None

    def get_vacancies(self, employer_id: str) -> List[Dict]:
        """Получение списка вакансий работодателя по его ID"""
        vacancies = []
        start_page = 0  # первая страница
        end_page = 1  # Конечная страница

        while start_page < end_page:
            params = {
                'employer_id': employer_id,
                'text': 'Программист',
                'area': 55,
                'per_page': 10,
                'page': 0
            }

            response = requests.get(
                f'{self.base_url}vacancies',headers=self.headers,
                params=params)
            response.raise_for_status()
            if response.text.strip():
                data = response.json()
            else:
                data = {}
            vacancies.extend(data['items'])
            end_page = data['pages']
            start_page += 1
        return vacancies
