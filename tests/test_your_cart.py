import pytest


@pytest.mark.order(before="test_your_information")
def test_yourCart(your_cart,json_dataextraction):
    your_cart.cart_item_validation(json_dataextraction[0]["items"])
    your_cart.cart_checkout()
