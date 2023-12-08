from django.db import models
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=150)

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        return Customer.objects.get(email = email)