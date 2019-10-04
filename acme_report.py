from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

# IRA's questions: is this still considered part of acme.py's "CLASS"?
# i.e. would doing a super()__init__ constructor here help/make sense?
# or is it entirely new (what frame of mind should I approach this with?)

# would i put the new parameters of price, weight, and flammability... where?
# since it's not in same .py it doesn't make sense for me to do super() here.

# also, will need further reps in using random generators.

def generate_products(num_products=30):
    products = []
    # TODO - your code! Generate and add random products.
    return products


def inventory_report(products):
    pass  # TODO - your code! Loop over the products to calculate the report.


if __name__ == '__main__':
    inventory_report(generate_products())


# from directions:
# name, price, weight, flammability
