import pytest


from main import BooksCollector


@pytest.fixture(scope='function')
def name():
    return 'Гордость и предубеждение и зомби'


@pytest.fixture(scope='function')
def new_books():
    return [('Гадкий я', 'Мультфильмы'),
            ('1 + 1', 'Комедии'),
            ('Ребекка', 'Детектив'),
            ('Валли', 'Мультфильмы'),
            ('Дамбо', 'Мультфильмы')]
