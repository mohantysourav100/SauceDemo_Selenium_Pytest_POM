import time
import pytest

from conftest import driver


@pytest.mark.order("last")
def test_checkoutOverview(overview,json_dataextraction):
    overview.item_totalAmount_validation()
    overview.payment_shippingInfo_validation(json_dataextraction[1]["msg_keywords"])
    overview.click_finish()
    time.sleep(5)
