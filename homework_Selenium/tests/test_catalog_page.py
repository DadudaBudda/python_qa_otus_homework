from homework_Selenium.pages.catalog_page import CatalogPage as catalog_page


def test_is_top_menu_present(driver, catalog):
    catalog_page().is_top_menu_present()


def test_is_search_input_present(driver, catalog):
    catalog_page().is_search_input_present()


def test_is_sort_by_input_present(driver, catalog):
    catalog_page().is_sort_by_input_present()


def test_is_show_input_present(driver, catalog):
    catalog_page().is_show_input_present()


def test_is_list_view_input_present(driver, catalog):
    catalog_page().is_list_view_input_present()


def test_is_grid_view_input_present(driver, catalog):
    catalog_page().is_grid_view_input_present()


def test_is_side_menu_present(driver, catalog):
    catalog_page().is_side_menu_present()


def test_add_to_compare(driver, catalog):
    catalog_page().add_item_to_compare()
    catalog_page().is_alert_present()
    catalog_page().is_compare_num_equal_to(1)
