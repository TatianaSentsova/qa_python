import pytest


from main import BooksCollector


class TestBooksCollector:
    @pytest.fixture(autouse=True)
    def collector(self):
        self.collector = BooksCollector()
        return self.collector

    def test_books_genre_init_state(self):
        assert self.collector.books_genre == {}

    def test_favorites_init_state(self):
        assert self.collector.favorites == []

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_init_genre_list(self, genre):
        assert genre in self.collector.genre and len(self.collector.genre) == 5

    @pytest.mark.parametrize('rating', ['Ужасы', 'Детективы'])
    def test_init_genre_age_rating_list(self, rating):
        assert rating in self.collector.genre_age_rating and len(self.collector.genre_age_rating) == 2

    def test_add_new_book_add_two_books(self, name):
        self.collector.add_new_book(name)
        self.collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(list(self.collector.books_genre)) == 2

    def test_add_new_book_without_genre(self, name):
        self.collector.add_new_book(name)
        assert self.collector.books_genre.get(name) == ''

    @pytest.mark.parametrize('name', ['',
                                      'Самая лучшая и интересная книга в мире!!!',
                                      'Это самая лучшая и интересная книга в мире',
                                      'Это самая лучшая и интересная книга в мире. Часть 2']
                             )
    def test_add_new_book_invalid_length_name(self, name):
        assert not self.collector.add_new_book(name)

    def test_add_new_book_same_name_twice(self, name):
        self.collector.add_new_book(name)
        self.collector.add_new_book(name)
        assert len(list(self.collector.books_genre)) == 1

    def test_set_book_genre(self, name):
        self.collector.add_new_book(name)
        self.collector.set_book_genre(name, 'Ужасы')
        assert self.collector.books_genre[name] == 'Ужасы'

    def test_set_book_genre_non_existent_genre(self, name):
        self.collector.add_new_book(name)
        assert not self.collector.set_book_genre(name, 'Фэнтези')

    def test_set_book_genre_non_existent_book(self):
        assert not self.collector.set_book_genre('Валли', 'Мультфильмы')

    def test_get_book_genre(self, name):
        self.collector.add_new_book(name)
        self.collector.set_book_genre(name, 'Ужасы')
        assert self.collector.get_book_genre(name) == 'Ужасы'

    def test_get_books_with_specific_genre_cartoons(self, new_books):
        for name, genre in new_books:
            self.collector.add_new_book(name)
            self.collector.set_book_genre(name, genre)

        list_cartoons = self.collector.get_books_with_specific_genre('Мультфильмы')
        assert list_cartoons == ['Гадкий я', 'Валли', 'Дамбо']

    def test_get_books_with_specific_genre_non_existent_genre(self, new_books):
        for name, genre in new_books:
            self.collector.add_new_book(name)
            self.collector.set_book_genre(name, genre)
        assert self.collector.get_books_with_specific_genre('Фэнтези') == []

    def test_get_books_with_specific_genre_without_book(self):
        assert self.collector.get_books_with_specific_genre('Комедии') == []

    def test_get_books_genre_five_books(self, new_books):
        for name, genre in new_books:
            self.collector.add_new_book(name)
            self.collector.set_book_genre(name, genre)
        assert len(list(self.collector.get_books_genre())) == 5

    def test_get_books_genre_empty_books_genre(self):
        assert self.collector.get_books_genre() == {}

    def test_get_books_for_children(self, new_books):
        for name, genre in new_books:
            self.collector.add_new_book(name)
            self.collector.set_book_genre(name, genre)
        books_for_children = self.collector.get_books_for_children()
        assert len(books_for_children) == 4 and 'Ребекка' not in books_for_children

    def test_get_books_for_children_empty_books_genre(self):
        assert self.collector.get_books_for_children() == []

    def test_add_book_in_favorites_two_books(self, new_books):
        for name, genre in new_books:
            self.collector.add_new_book(name)
            self.collector.set_book_genre(name, genre)
        for cartoon in ['Валли', 'Дамбо']:
            self.collector.add_book_in_favorites(cartoon)
        assert len(self.collector.favorites) == 2

    def test_add_book_in_favorites_non_existent_book(self):
        assert not self.collector.add_book_in_favorites('Война и мир')

    def test_add_book_in_favorites_same_book_twice(self, name):
        self.collector.add_new_book(name)
        self.collector.add_book_in_favorites(name)
        self.collector.add_book_in_favorites(name)
        assert len(self.collector.favorites) == 1

    def test_delete_book_from_favorites(self, name):
        self.collector.add_new_book(name)
        self.collector.add_book_in_favorites(name)
        self.collector.delete_book_from_favorites(name)
        assert self.collector.favorites == []

    def test_get_list_of_favorites_books(self, name):
        self.collector.add_new_book(name)
        self.collector.add_book_in_favorites(name)
        assert len(self.collector.get_list_of_favorites_books()) == 1

    def test_get_list_of_favorites_book_without_book(self):
        assert self.collector.get_list_of_favorites_books() == []
