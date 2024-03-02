from .cart import Cart

#Context processcor 
def cart(request):
    #Return default data from cart
    return {'cart': Cart(request)}