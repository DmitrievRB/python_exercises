import pytest
from pages.auth_page import AuthPage
def test_authorisation(web_browser):
    page= AuthPage(web_browser)
    page.email.send_keys("grant@gmail.com")
    page.password.send_keys("grant")
    page.btn.click()
    assert page.get_current_url