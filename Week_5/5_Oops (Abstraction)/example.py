from abc import ABC, abstractmethod

# ---------------------------------------------------------------
# 1. ABSTRACT BASE CLASS EXAMPLE: Payment
# ---------------------------------------------------------------
# Payment is an "abstract base class" (ABC). It can't be instantiated
# directly — it exists only to be inherited from, and it forces every
# subclass to implement its own version of pay().


class Payment(ABC):
    def __init__(self, payer_name):
        # Every payment method needs to know who is paying.
        self.payer_name = payer_name

    @abstractmethod
    def pay(self, amount):
        # No implementation here — this is a contract. Any subclass
        # of Payment MUST override this method, or Python will refuse
        # to let you create an instance of it.
        pass

    def print_receipt(self, amount, method):
        # A normal (non-abstract) method — shared by all subclasses,
        # so we don't have to repeat this print statement everywhere.
        print(f"{self.payer_name} paid {amount} via {method}")


# ---------------------------------------------------------------
# Concrete subclasses — each provides its own pay() implementation
# ---------------------------------------------------------------

class CreditCardPayment(Payment):
    def pay(self, amount):
        if amount > 0:
            print(f"Processing credit card payment of {amount}")
            # Reuses the shared print_receipt() method from Payment
            self.print_receipt(amount, "credit card")
        else:
            print("Invalid amount")


class PayPalPayment(Payment):
    def pay(self, amount):
        if amount > 0:
            print(f"Processing PayPal payment of {amount}")
            self.print_receipt(amount, "PayPal")
        else:
            print("Invalid amount")


class UPIPayment(Payment):
    def pay(self, amount):
        if amount > 0:
            print(f"Processing UPI payment of {amount}")
            self.print_receipt(amount, "UPI")
        else:
            print("Invalid amount")


# --- Test the payment classes ---
payment1 = CreditCardPayment('Uday')
payment1.pay(5000)
# Output:
# Processing credit card payment of 5000
# Uday paid 5000 via credit card

payment2 = PayPalPayment('Satish')
payment2.pay(2600)
# Output:
# Processing PayPal payment of 2600
# Satish paid 2600 via PayPal

payment3 = UPIPayment('Arun')
payment3.pay(490)
# Output:
# Processing UPI payment of 490
# Arun paid 490 via UPI


# ---------------------------------------------------------------
# 2. INHERITANCE + super() EXAMPLE: BankSupport
# ---------------------------------------------------------------
# BankSupport is a regular (non-abstract) base class this time.
# Subclasses can either fully override respond() or extend it
# using super().

class BankSupport:
    def __init__(self, customer_name):
        self.customer_name = customer_name

    def respond(self):
        print(f"Hello {self.customer_name}, welcome to SBI bank support.")


class CardSupport(BankSupport):
    def respond(self):
        # This COMPLETELY overrides the parent's respond() —
        # the parent's greeting is never printed here.
        print(f"Hello {self.customer_name}, I see you are having trouble with your card.")


customer1 = CardSupport('Aditi')
customer1.respond()
# Output:
# Hello Aditi, I see you are having trouble with your card.


class ATMSupport(BankSupport):
    def respond(self):
        # super().respond() calls BankSupport's original respond()
        # first, THEN adds its own extra message. This is how you
        # extend a parent method instead of replacing it entirely.
        super().respond()
        print(f"Hello {self.customer_name}, welcome to SBI ATM support.")


customer2 = ATMSupport('Ravi')
customer2.respond()
# Output:
# Hello Ravi, welcome to SBI bank support.
# Hello Ravi, welcome to SBI ATM support.


# ---------------------------------------------------------------
# 3. DEFAULT ARGUMENTS EXAMPLE: Billing
# ---------------------------------------------------------------
# discount=None is a default parameter — if the caller doesn't pass
# a discount, it defaults to None and the "if" branch runs instead.
#
# NOTE (bug, kept as-is from the original notebook):
# The line below does "discounted_amount = amount = discount",
# which just sets BOTH discounted_amount and amount equal to the
# discount value itself — it does NOT subtract the discount from
# amount. The intended logic was probably:
#     discounted_amount = amount - discount
# As written, calling generate_bill(1000, 200) prints "200", not "800".

class Billing:
    def generate_bill(self, amount, discount=None):

        if discount is None:
            print(f"Total amount: {amount}")

        else:
            discounted_amount = amount = discount  # <- bug: no subtraction happens
            print(f'Amount after {discount} discount {discounted_amount}')


bill = Billing()

bill.generate_bill(1000, 200)
# Output: Amount after 200 discount 200   (bug — should be 800)

bill.generate_bill(2500)
# No discount passed -> discount stays None -> "if" branch runs
# Output: Total amount: 2500


# ---------------------------------------------------------------
# 4. VARIABLE-LENGTH ARGUMENTS EXAMPLE: ShoppingCart
# ---------------------------------------------------------------
# *items lets add_items() accept any number of positional arguments,
# which Python collects into a tuple called items.

class ShoppingCart:
    def __init__(self):
        self.cart = []  # cart starts empty and PERSISTS across calls

    def add_items(self, *items):
        # extend() appends every item from the tuple into self.cart
        self.cart.extend(items)
        print(f"Items added to cart {self.cart}")


cart1 = ShoppingCart()

cart1.add_items('Laptop')
# Output: Items added to cart ['Laptop']

cart1.add_items('Laptop', 'Headphones')
# self.cart is NOT reset between calls, so this adds on top of
# what's already there.
# Output: Items added to cart ['Laptop', 'Laptop', 'Headphones']

cart1.add_items('Laptop', 'Headphones', 'Charger')
# Same reused cart again — items keep accumulating/duplicating.
# Output: Items added to cart ['Laptop', 'Laptop', 'Headphones', 'Laptop', 'Headphones', 'Charger']