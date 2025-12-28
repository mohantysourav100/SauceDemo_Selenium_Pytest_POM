import pytest


@pytest.mark.order(4)
def test_yourinformation(your_info,user_details):
    your_info.fill_yourDetails(user_details["first_name"],user_details["last_name"],user_details["zip_code"])
    your_info.click_Continue()
