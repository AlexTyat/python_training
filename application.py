from selenium import webdriver

class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)



    def open_home_page(self):
        wd = self.wd
        # open home page
        wd.get("http://localhost/addressbook/group.php")

    def login(self, username, password):
        wd = self.wd
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_groups_page(self):
        wd = self.wd
        # open groups page
        wd.find_element_by_link_text("groups").click()

    def create_group(self, group):
        wd = self.wd
        # init groups creation
        wd.find_element_by_name("new").click()
        # fill up group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()

    def return_to_groups_page(self):
        wd = self.wd
        # return to groups page
        wd.find_element_by_link_text("groups").click()

    def logout(self):
        wd = self.wd
        # logout
        wd.find_element_by_link_text("Logout").click()

    def destroy(self):
        self.wd.quit()