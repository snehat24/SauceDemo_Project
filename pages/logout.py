from playwright.sync_api import Page

class Logout:

  def __init__(self,page):
    self.page=page
    self.menu=page.locator('#react-burger-menu-btn')
    self.lg=page.locator('#logout_sidebar_link')

  def open_menu(self):
      self.menu.click()

  def logout(self):
      self.lg.click()


