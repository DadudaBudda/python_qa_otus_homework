"""1. Настроить Selenium для запуска тестов
2. Написать фикстуру для запуска трех разных браузеров (ie, firefox, chrome) в полноэкранном режиме с опцией headless.
Выбор браузера должен осуществляться путем передачи аргумента командной строки pytest. По завершению работы тестов должно
осуществляться закрытие браузера.
3. Добавить опцию командной строки, которая указывает базовый URL opencart.
4. Написать тест, который открывает основную страницу opencart (http://<ip_or_fqdn>/opencart/) и проверяет, что мы
находимся именно на странице приложения opencart.
5. Написать тесты проверяющие наличие элементов на разных страницах приложения opencart.
Реализовать минимум пять тестов (одни тест = одна страница приложения)
Какие элементы проверять определить самостоятельно, но не меньше 5 для каждой страницы.
Покрыть нужно:
Главную /
Каталог /index.php?route=product/category&path=20
Карточку товара /index.php?route=product/product&path=57&product_id=49
Страницу логина /index.php?route=account/login
Страницу логина в админку /admin/
6. К существующим тестам добавить явные ожидания элементов.
7. Реализовать 2 тестовых сценария на раздел администратора
7.1 Добавить проверку логина и разлогина раздела.
7.2 Добавить проверку перехода к разделу с товарами, что появляется таблица с товарами."""


def test_open_page(driver, url):
    driver.get(url)
    assert driver.title == 'Your Store'




def test_is_slideshow_present():
    main_page.is_slideshow_present()


def test_is_featured_products_present(main_page):
    main_page.is_featured_products_present()


def test_is_brend_carousel_present(main_page):
    main_page.is_brend_carousel_present()


def test_is_top_menu_present(main_page):
    main_page.is_top_menu_present()


def test_is_search_input_present(main_page):
    main_page.is_search_input_present()


def test_alert_add_to_fav_not_logged_in(main_page):
    main_page.add_featured_to_fav(1)
    main_page.is_alert_present()


def test_add_item_to_cart_item_num(main_page):
    main_page.add_featured_to_cart()
    main_page.is_items_num_in_cart_equal_to(1)
    main_page.is_alert_present()