from rest_framework import serializers
from .models import (
    Navigation, Hero, ServiceCategory, ServiceItem, Feature, Stat,
    Testimonial, TeamMember, PortfolioProject, PortfolioGalleryImage, AboutContent,
    ContactInfo, ContactFormSubmission, FAQ
)


class NavigationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Navigation
        fields = '__all__'


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = '__all__'


class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = '__all__'


class ServiceCategoryListSerializer(serializers.ModelSerializer):
    services_count = serializers.SerializerMethodField()
    
    class Meta:
        model = ServiceCategory
        fields = ['id', 'name', 'description', 'icon', 'order', 'services_count']
    
    def get_services_count(self, obj):
        return obj.services.count()


class ServiceItemSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = ServiceItem
        fields = '__all__'


class ServiceItemListSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = ServiceItem
        fields = ['id', 'title', 'description', 'features', 'icon', 'order', 'is_featured', 'category_name']


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = '__all__'


class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        fields = '__all__'


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'


class FeaturedTestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['id', 'name', 'role', 'company', 'review', 'photo', 'rating', 'order']


class TeamMemberSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    
    class Meta:
        model = TeamMember
        fields = '__all__'
    
    def get_image(self, obj):
        if obj.image_upload:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.image_upload.url)
        return obj.image


class FeaturedTeamMemberSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    
    class Meta:
        model = TeamMember
        fields = ['id', 'name', 'role', 'bio', 'image', 'social_links', 'order']
    
    def get_image(self, obj):
        if obj.image_upload:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.image_upload.url)
        return obj.image


class PortfolioGalleryImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    
    class Meta:
        model = PortfolioGalleryImage
        fields = ['id', 'image', 'caption', 'order']
    
    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image_upload:
            return request.build_absolute_uri(obj.image_upload.url)
        return obj.image_url


class PortfolioProjectSerializer(serializers.ModelSerializer):
    media_url = serializers.SerializerMethodField()
    service_name = serializers.CharField(source='service.title', read_only=True)
    gallery_images = PortfolioGalleryImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = PortfolioProject
        fields = '__all__'
    
    def get_media_url(self, obj):
        request = self.context.get('request')
        if obj.media_upload:
            return request.build_absolute_uri(obj.media_upload.url)
        return obj.media_url


class FeaturedPortfolioProjectSerializer(serializers.ModelSerializer):
    media_url = serializers.SerializerMethodField()
    service_name = serializers.CharField(source='service.title', read_only=True)
    
    class Meta:
        model = PortfolioProject
        fields = ['id', 'title', 'slug', 'description', 'media_url', 'media_type', 'tags', 'client', 'project_url', 'service_name', 'order']
    
    def get_media_url(self, obj):
        request = self.context.get('request')
        if obj.media_upload:
            return request.build_absolute_uri(obj.media_upload.url)
        return obj.media_url


class AboutContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutContent
        fields = '__all__'


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = '__all__'


class ContactFormSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactFormSubmission
        fields = '__all__'
        read_only_fields = ['timestamp', 'is_read']


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'
