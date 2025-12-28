import pytest

@pytest.mark.smoke
@pytest.mark.order(3)
def test_yourCart(your_cart,json_dataextraction):
    your_cart.cart_item_validation(json_dataextraction[0]["items"])
    your_cart.cart_checkout()
