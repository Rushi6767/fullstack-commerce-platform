from django.db import models


class DemoModel(models.Model):
    # ---- Text fields ----
    char_field = models.CharField(max_length=255)
    text_field = models.TextField()

    # ---- Numeric fields ----
    integer_field = models.IntegerField()
    positive_integer_field = models.PositiveIntegerField()
    float_field = models.FloatField()
    decimal_field = models.DecimalField(max_digits=10, decimal_places=2)

    # ---- Boolean ----
    boolean_field = models.BooleanField(default=False)

    # ---- Date / Time ----
    date_field = models.DateField()
    datetime_field = models.DateTimeField()
    time_field = models.TimeField()

    # ---- Auto fields ----
    auto_now_field = models.DateTimeField(auto_now=True)
    auto_now_add_field = models.DateTimeField(auto_now_add=True)

    # ---- Choice field ----
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('blocked', 'Blocked'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    # ---- File / Media ----
    file_field = models.FileField(upload_to='files/', null=True, blank=True)
    image_field = models.ImageField(upload_to='images/', null=True, blank=True)

    # ---- URL / Email ----
    url_field = models.URLField()
    email_field = models.EmailField()

    # ---- JSON (very important in modern backend) ----
    json_field = models.JSONField(default=dict)

    # ---- Basic metadata ----
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.char_field
    

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Order(models.Model):
    order_number = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.order_number