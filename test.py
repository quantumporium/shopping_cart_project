# good structure for an pytest test
from app import shopping_cart

def check_if_checkout_give_the_right_value():
    '''
    '''
    arrange_array = [15,7, 10] # arrange
    shopping_cart_array = shopping_cart.checkout(arrange_array) # act
    assert shopping_cart_array == (31.99, 2.8, 34.79), "this check if the function checkout in shopping_cart work well."
  
check_if_checkout_give_the_right_value()