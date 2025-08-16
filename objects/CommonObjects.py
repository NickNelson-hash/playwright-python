from playwright.sync_api import Page, Locator


class CommonObjects:
    page:Page
    def __init__(self,page:Page):
        self.page = page
        self.add_new_record = page.get_by_role("button",name="Add record")

    def drop_down(self,name:str)->Locator:
        return self.page.get_by_role("combobox", name=name)

    def link(self,name:str)->Locator:
        return self.page.get_by_role("link", name=name).nth(1)

    def created_data_bread_crumb(self,first_name:str)->Locator:
        return self.page.locator("//li[contains(@class,'breadcrumb') and text()='"+first_name+"']")

    def tab_menu(self,name:str)->Locator:
        return self.page.get_by_role("link", name=name).nth(1)

    def pencil_edit_icon(self,field_name:str)->Locator:
        return self.page.locator("//label[text()='"+field_name+"']/../following-sibling::td//*[@title='Edit']")

    def toggle_panel(self,name:str)->Locator:
        return self.page.locator("//*[text()='"+name+"']/parent::div[contains(@class,'panel__header')]")

    def drop_down_option(self,option:str)->Locator:
        return self.page.get_by_role("option", name=option)

    def button(self,name:str)->Locator:
        return self.page.get_by_role("button", name=name)


    def input_box(self,name:str)->Locator:
        return self.page.locator("//input[@title='"+name+"']")