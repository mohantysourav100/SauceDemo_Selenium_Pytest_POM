import time

import pytest


@pytest.mark.order(6)
def test_checkoutComplete(checkout_complete,json_dataextraction):
    checkout_complete.checkout_confirmation(json_dataextraction[1]["msg_keywords"])
    checkout_complete.click_home()
    time.sleep(5)