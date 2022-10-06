def saving_calculator(func):
    def wrapper(*args,**kwargs):
        product = func(*args,**kwargs)
        product_price = int(input('How much does your product cost?: '))
        saving_amounts= int(input('How much are you willing to save per month? : '))
        calculated_time = product_price/saving_amounts
        print(f'Saving {saving_amounts} per month you\'ll have your {product} in {calculated_time} months. ')
    return wrapper

@saving_calculator
def producto_ahorrar(producto):
    return producto 
    
    
producto_ahorrar(input('Hi! What are you thinking to buy? : '))

