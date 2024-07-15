# qa_python

1) Тестирование конструктора класса BooksCollector:
    - test_book_collection_books_genre_true 
    - test_book_collection_favorites_true 
    - test_book_collection_genre_true
    - test_book_collection_genre_age_rating_true
2) Тестирование метода добавления новой книги add_new_book:
    - test_add_new_book_add_two_books - добавление 2-х книг
    - test_add_new_book_add_without_genre_true - проверка, что книга добавляется со значением жанра ввиде пустой строки
    - test_add_new_book_invalid_length_name - негативные проверки длины названия книги: 0, 41, 42 и 51 символ
    - test_add_new_book_same_name_twice - негативная проверка добавления 2-х книг с одним и тем же названием
3) Тестирование метода set_book_genre (установка жанра книге):
    - test_set_book_genre_true - позитивная проверка установки книге жанра
    - test_set_book_genre_non_existent_genre - негативная проверка установки жанра книге не из списка self.genre
    - test_set_book_genre_for_book_not_from_collector - негативная проверка для установке жанра книге, которую не добавляли в self.books_genre
4) Тестирование метода вывода списка книг с определённым жанром get_books_with_specific_genre:
    - test_get_books_with_specific_genre_cartoons_true - позитивная проверка вывода книг в жанре "Мульфильмы"
    - test_get_books_with_specific_genre_non_existent_genre - негативная проверка вывода списка с жанром не из списка self.genre 
    - test_get_books_with_specific_genre_without_book - негативная проверка вывода списка, когда не добавлено ни одной книги в self.books_genre
5) Тестирование метода получения словаря books_genre:
    - test_get_books_genre_from_five_books - получение словаря c 5 книгами
    - test_get_books_genre_with_empty_books_genre - получение пустого словаря
6) Тестирование метода получения списка книг, подходящего детям, get_books_for_children:
    - test_get_books_for_children - получения списка книг, подходящего детям
    - test_get_books_for_children_with_empty_books_genre - получение пустого списка
7) Тестирование метода добавления книг в Избранное add_book_in_favorites:
    - test_add_book_in_favorites_two_different_books - добавление двух разных книг в Избранное (self.favorites)
    - test_add_book_in_favorites_for_book_not_from_collector - негативная проверка добавления книги не из self.books_genre в Избранное
    - test_add_book_in_favorites_for_same_book_twice - негативная проверка добавления одной и той же книги в Избранное
8) Тестирование метода удаления книги из Избранных книг delete_book_from_favorites:
   - test_delete_book_from_favorites - удаление книги из Избранное
9) Тестирование метода получения списка Избранных книг get_list_of_favorites_books:
   - get_list_of_favorites_book_from_one_book - получения списка избранных книг, состоящего из одной книги
   - get_list_of_favorites_book_without_book - получение пустого списка избранных книг
