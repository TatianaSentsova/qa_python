import pytest


from main import BooksCollector


import data


class TestBooksCollector:
    def test_books_genre_init_state(self, collector):
        assert collector.books_genre == {}

    def test_favorites_init_state(self, collector):
        assert collector.favorites == []

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_init_genre_list(self, collector, genre):
        assert genre in collector.genre and len(collector.genre) == 5

    @pytest.mark.parametrize('rating', ['Ужасы', 'Детективы'])
    def test_init_genre_age_rating_list(self, collector, rating):
        assert rating in collector.genre_age_rating and len(collector.genre_age_rating) == 2

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book(data.name)
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(list(collector.books_genre)) == 2

    def test_add_new_book_without_genre(self, collector):
        collector.add_new_book(data.name)
        assert collector.books_genre.get(data.name) == ''

    @pytest.mark.parametrize('name', ['',
                                      'Самая лучшая и интересная книга в мире!!!',
                                      'Это самая лучшая и интересная книга в мире',
                                      'Это самая лучшая и интересная книга в мире. Часть 2']
                             )
    def test_add_new_book_invalid_length_name(self, collector, name):
        collector.add_new_book(name)
        assert name not in list(collector.books_genre)

    def test_add_new_book_same_name_twice(self, collector):
        collector.add_new_book(data.name)
        collector.add_new_book(data.name)
        assert len(list(collector.books_genre)) == 1

    def test_set_book_genre(self, collector):
        collector.add_new_book(data.name)
        collector.set_book_genre(data.name, 'Ужасы')
        assert collector.books_genre[data.name] == 'Ужасы'

    def test_set_book_genre_non_existent_genre(self, collector):
        collector.add_new_book(data.name)
        collector.set_book_genre(data.name, 'Фэнтези')
        assert collector.books_genre[data.name] == ''

    def test_set_book_genre_non_existent_book(self, collector):
        collector.set_book_genre('Валли', 'Мультфильмы')
        assert ('Валли', 'Мультфильмы') not in collector.books_genre.items()

    def test_get_book_genre(self, collector):
        collector.add_new_book(data.name)
        collector.set_book_genre(data.name, 'Ужасы')
        assert collector.get_book_genre(data.name) == 'Ужасы'

    def test_get_books_with_specific_genre_cartoons(self, collector):
        for name, genre in data.new_books:
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)

        list_cartoons = collector.get_books_with_specific_genre('Мультфильмы')
        assert list_cartoons == ['Гадкий я', 'Валли', 'Дамбо']

    def test_get_books_with_specific_genre_non_existent_genre(self, collector):
        for name, genre in data.new_books:
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)
        assert collector.get_books_with_specific_genre('Фэнтези') == []

    def test_get_books_with_specific_genre_without_book(self, collector):
        assert collector.get_books_with_specific_genre('Комедии') == []

    def test_get_books_genre_five_books(self, collector):
        for name, genre in data.new_books:
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)
        assert len(list(collector.get_books_genre())) == 5

    def test_get_books_genre_empty_books_genre(self, collector):
        assert collector.get_books_genre() == {}

    def test_get_books_for_children(self, collector):
        for name, genre in data.new_books:
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)
        books_for_children = collector.get_books_for_children()
        assert len(books_for_children) == 4 and 'Ребекка' not in books_for_children

    def test_get_books_for_children_empty_books_genre(self, collector):
        assert collector.get_books_for_children() == []

    def test_add_book_in_favorites_two_books(self, collector):
        for name, genre in data.new_books:
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)
        for cartoon in ['Валли', 'Дамбо']:
            collector.add_book_in_favorites(cartoon)
        assert len(collector.favorites) == 2

    def test_add_book_in_favorites_non_existent_book(self, collector):
        collector.add_book_in_favorites('Война и мир')
        assert 'Война и мир' not in collector.favorites

    def test_add_book_in_favorites_same_book_twice(self, collector):
        collector.add_new_book(data.name)
        collector.add_book_in_favorites(data.name)
        collector.add_book_in_favorites(data.name)
        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book(data.name)
        collector.add_book_in_favorites(data.name)
        collector.delete_book_from_favorites(data.name)
        assert collector.favorites == []

    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book(data.name)
        collector.add_book_in_favorites(data.name)
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_get_list_of_favorites_book_without_book(self, collector):
        assert collector.get_list_of_favorites_books() == []
