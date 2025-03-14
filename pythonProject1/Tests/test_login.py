import pytest
from Pages.Login_page import LoginPage

@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        login_page.open("https://opensource-demo.orangehrmlive.com/")

        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login()

        assert login_page.is_dashboard_displayed(), "Dashboard not displayed after login"
