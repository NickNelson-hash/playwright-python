from playwright.sync_api import Page, Locator


class CommonObjects:
    page:Page
    def __init__(self,page:Page):
        self.page = page
        self.add_new_record = page.get_by_role("button",name="Add record")

    def drop_down(self,name:str)->Locator:
        return self.page.get_by_role("combobox", name=name)

    def drop_down_option(self,option:str)->Locator:
        return self.page.get_by_role("option", name=option)

    def button(self,name:str)->Locator:
        return self.page.get_by_role("button", name=name)


    def input_box(self,name:str)->Locator:
        return self.page.locator("//input[@title='"+name+"']")