import requests

question = requests.get('https://opentdb.com/api.php?amount=10&category=18&type=boolean')
question.raise_for_status()
question_data = question.json()['results']
