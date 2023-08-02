from pages.search_page import SearchPage
from pages.image_page import ImagePage


class TestSearchPage:

    def test_search(self, driver):
        search_page = SearchPage(driver, 'https://ya.ru/')
        search_page.open()
        search_page.search_and_submit()
        suggest = search_page.check_table_suggest()
        search_page.enter_click()
        resul_search = search_page.check_search()
        link = search_page.check_first_link()
        assert suggest == True, 'Таблица с подсказками не появилась'
        assert resul_search == True, 'Страница с результатом поиска не появилась'
        assert link == 'tensor.ru', 'Первая ссылка не ведёт на сайт tensor.ru'

    def test_search2(self, driver):
        image_page = ImagePage(driver, 'https://ya.ru/')
        image_page.open()
        image_page.search_imnge()
        url = image_page.check_url()
        category_name, search_row = image_page.first_category_image()
        first_image = image_page.open_first_image()
        first_id_image1, id_image2 = image_page.next_image()
        last_id_image = image_page.prev_image()
        assert url == 'https://yandex.ru/images/', 'Вы не перешли на страницу с картинками'
        assert category_name == search_row, 'Поиск не соответствует выбранной картинке'
        assert first_image == True, 'Окно с картинкой не открывается!'
        assert first_id_image1 != id_image2, 'Картинка не cменилась на следующую'
        assert last_id_image == first_id_image1, 'Первое изображение не вернулось'
