from playwright.sync_api import Page

class AddToCart:
  def __init__(self,page):
     self.page= page
     self.add=page.get_by_text("Add to cart")

  def add_to_cart(self):
      self.add.first.click()


