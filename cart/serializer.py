from rest_framework import serializers

class CouponSerializer(serializers.Serializer):
      TYPE=(
        ('fixed','fixed'),
        ('percent','percent')
      )
      name=serializers.CharField(max_length=100)
      coupon_type=serializers.ChoiceField(choices=TYPE)
      coupon_valu=serializers.IntegerField()
      cart_value=serializers.IntegerField()
      exfail_date=serializers.DateTimeField()
      active=serializers.BooleanField(default=True)
      