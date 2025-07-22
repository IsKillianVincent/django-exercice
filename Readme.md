# Django Exercice

Un projet Django pour gérer des factures, avec filtres, actions admin, tests, Bootstrap, et middleware personnalisé.

## Installation

```bash
git clone https://github.com/IsKillianVincent/django-exercice.git
cd django-exercice
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
python manage.py tests
