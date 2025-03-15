from education.models import Education

CART_SESSION_ID = 'cart'


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        education_ids = self.cart.keys()
        educations = Education.objects.filter(id__in=education_ids)
        cart = self.cart.copy()
        for education in educations:
            cart[str(education.id)]["education"] = education

        for item in cart.values():
            item['total_price'] = int(item['price']) * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, education, quantity):
        education_id = str(education.id)
        if education_id not in self.cart:
            self.cart[education_id] = {'quantity': 0, 'price': str(education.price)}
        self.cart[education_id]['quantity'] += quantity
        self.save()

    def remove(self, education):
        education_id = str(education.id)
        if education_id in self.cart:
            del self.cart[education_id]
            self.save()

    def save(self):
        self.session.modified = True

    def get_total_price(self):
        return sum(int(item['price']) * item['quantity']for item in self.cart.values())

    def clear(self):
        del self.session[CART_SESSION_ID]
        self.save()

