from accounts.serializers import *
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')


class ShoppingSearchSerializer(serializers.Serializer):
    categories = CategorySerializer(many=True)


# for shopping page
class ShoppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commodity
        fields = ('title', 'amount', 'image')


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ('title', 'description')


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ('title',)


class ShoppingDetailSerializer(serializers.ModelSerializer):
    features = FeatureSerializer(many=True)
    shops = ShopSerializer(many=True)
    class Meta:
        model = Commodity
        fields = ('title', 'amount', 'image', 'features', 'shops')


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')
