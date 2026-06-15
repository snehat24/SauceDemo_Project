from playwright.sync_api import Page


class CheckoutPage:

    def __init__(self,page):
        self.page= page
        self.cart=page.locator('#shopping_cart_container')
        self.con=page.get_by_text("Continue Shopping")
        self.checkout=page.get_by_text("Checkout")
        self.firstname=page.get_by_placeholder("First Name")
        self.lastname=page.get_by_placeholder("Last Name")
        self.pincode=page.get_by_placeholder("Zip/Postal Code")
        self.cancel=page.get_by_role('button',name='cancel')
        self.con1=page.locator('#continue')
        self.fin = page.locator('#finish')
        self.home=page.get_by_text("Back Home")
        self.rm = page.get_by_text("Remove")

    def remove(self):
        self.rm.click()

    def open_cart(self):
        self.cart.click()

    def checkout_page(self):
        self.checkout.click()

    def continue_shopping(self):
        self.checkout.click()

    def credentials(self,fname,lname,pin):
        self.firstname.fill(fname)
        self.lastname.fill(lname)
        self.pincode.fill(pin)

    def cancel(self):
        self.cancel.click()

    def finalContinue(self):
        self.con1.click()

    def finish(self):
        self.fin.click()

    def backhome(self):
        self.home.click()