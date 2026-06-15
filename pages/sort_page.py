from playwright.sync_api import Page

class Sorting:
    def __init__(self,page):
        self.page = page
        self.sort=page.locator(".product_sort_container")
        self.products = page.locator(".inventory_item_name")

    def sort_page(self,value):
        self.sort.select_option(value)

    def get_first_product(self):
        return self.products.first.text_content()