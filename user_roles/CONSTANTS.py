from django.db.models import TextChoices

class GENDER(TextChoices):
    MALE='ML'
    FEMALE='FM'
    OTHERS='OT'


class ROLE(TextChoices):
    CUSTOMER='CST'
    ADMIN='ADM'
    DRIVER='DRV'
    OPERATOR='OPR'
    ATTENDANT='ATD'
    CLEANER='CLN'
    RBACKADMIN='RBA'

class REFER(TextChoices):
    WHATSAPP='WA'
    MOBILE_APP='MA'
    WEB='WB'

class SIGNUP(TextChoices):
    LINKEDIN='LN'
    GMAIL='GM'
    FACEBOOK='FB'
    APPLE_ID='AP'

class PAYMENT_METHOD(TextChoices):
    PAYTM='PTM'
    UPI='UPI'
    CARD='CRD'
    CASH='CSH'
    NETBANKING='NBG'

