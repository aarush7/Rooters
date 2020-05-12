from django.db.models import TextChoices



class FLEX(TextChoices):
    CANCELLABLE = 'CN'
    RESCHEDULABLE ='RS'
    NORMAL='NR'

class PAY(TextChoices):
    SUCCESS = 'SC'
    FAILED = 'FL'
    PARTIALLY_BOOK='PB'


class BOOKING_METHOD(TextChoices):
    WEBAPP='WA'
    PHONEAPP='PA'

class BOOKING_STATUS(TextChoices):
    CONFIRMED='CF'
    CANCELLED='CN'

class GENDER(TextChoices):
    MALE='ML'
    FEMALE='FM'
    OTHERS='OT'

