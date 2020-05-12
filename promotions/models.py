from django.db import models
import uuid

# Create your models here.
class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class voucher(models.Model):
    voucher_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    voucher_code=models.CharField(max_length=50,blank=False)
    voucher_discount=models.FloatField(blank=False)
    max_discount=models.IntegerField(blank=False)
    from_date=models.DateTimeField(blank=False)
    to_date=models.DateTimeField(blank=False)
