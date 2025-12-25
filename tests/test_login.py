import pytest
from pages.login_page import Login

@pytest.mark.order("first")
def test_login(driver, baseurl,credentials):
    login = Login(driver)
    login.site_load(baseurl)
    login.login(credentials["username"],credentials["password"])
    #assert "wrong_url" in driver.current_url, "Login Failed - URL doesn't match"

