from rest_framework import serializers
from wishlist.models import Movie, WishList, StreamPlatform, Reviews


# class MovieSeralizer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     active = serializers.BooleanField()
#
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name", instance.name)
#         instance.description = validated_data.get("description",
#                                                   instance.description)
#         instance.active = validated_data.get("active", instance.active)
#         instance.save()
#         return instance

# def validate(self, data):
#     if data['name'] == data['description']:
#         raise serializers.ValidationError("finish must occur after start")
#     return data


class MovieSeralizer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = '__all__'
        # exclude = ["name"]

    def get_len_name(self, object):
        return len(object.name)
    # # custom serializer field


class ReviewSeralizer(serializers.ModelSerializer):
    # wishlist = WishListSeralizer(many=True, read_only=True)
    class Meta:
        model = Reviews
        fields = '__all__'
        # exclude = ["name"]

class WishListSeralizer(serializers.ModelSerializer):
    reviews = ReviewSeralizer(many=True,read_only=True)
    len_title = serializers.SerializerMethodField()

    class Meta:
        model = WishList
        fields = '__all__'
        # exclude = ["name"]

    def get_len_title(self, object):
        return len(object.title)
    ## custom serializer field


class StreamPlatformSeralizer(serializers.ModelSerializer):
    wishlist = WishListSeralizer(many=True, read_only=True)
    class Meta:
        model = StreamPlatform
        fields = '__all__'
        # exclude = ["name"]
