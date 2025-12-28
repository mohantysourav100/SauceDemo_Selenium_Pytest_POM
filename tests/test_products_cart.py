import pytest


@pytest.mark.order(2)
def test_itemCart(product_cart,json_dataextraction):
    product_cart.add_product_toCart(json_dataextraction[0]["items"])
    product_cart.product_count_validation()
    product_cart.navigate_toCart()