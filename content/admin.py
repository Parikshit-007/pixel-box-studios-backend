from django.contrib import admin
from .models import (
    Navigation, Hero, ServiceCategory, ServiceItem, Feature, Stat,
    Testimonial, TeamMember, PortfolioProject, PortfolioGalleryImage, AboutContent,
    ContactInfo, ContactFormSubmission, FAQ
)


@admin.register(Navigation)
class NavigationAdmin(admin.ModelAdmin):
    list_display = ['has_logo', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Logo Options', {
            'fields': ('logo_image', 'logo_url'),
            'description': 'Upload a logo image OR provide a logo URL. If both are provided, uploaded image takes priority.'
        }),
        ('Menu Links', {
            'fields': ('menu_links',),
            'description': 'Enter menu links as JSON array. Example: [{"name": "Home", "href": "/"}, {"name": "Services", "href": "/services"}]'
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def has_logo(self, obj):
        return bool(obj.logo_image or obj.logo_url)
    has_logo.boolean = True
    has_logo.short_description = 'Has Logo'


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ['title', 'cta_text', 'has_video', 'has_portrait_video', 'has_image', 'has_logo', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Hero Content', {
            'fields': ('title', 'subtitle')
        }),
        ('Landscape Video (Desktop/Laptop - 16:9)', {
            'fields': ('hero_video', 'video_url'),
            'description': 'Upload a landscape video file (16:9 aspect ratio) OR provide a video URL. Used for desktop and landscape displays.'
        }),
        ('Portrait Video (Mobile Portrait - 9:16)', {
            'fields': ('hero_video_portrait', 'video_url_portrait'),
            'description': 'Upload a portrait video file (9:16 aspect ratio) OR provide a video URL. Used for mobile portrait displays.'
        }),
        ('Hero Image (Alternative to Video)', {
            'fields': ('hero_image', 'image_url'),
            'description': 'Upload an image OR provide image URL. Use this as alternative to video. Image takes priority if both video and image are provided.'
        }),
        ('Company Logo', {
            'fields': ('logo_upload', 'logo_url'),
            'description': 'Upload company logo OR provide logo URL. Used for navbar and favicon.'
        }),
        ('Call to Action', {
            'fields': ('cta_text', 'cta_link')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def has_portrait_video(self, obj):
        return bool(obj.hero_video_portrait or obj.video_url_portrait)
    has_portrait_video.boolean = True
    has_portrait_video.short_description = 'Portrait Video'
    
    def has_video(self, obj):
        return bool(obj.hero_video or obj.video_url)
    has_video.boolean = True
    has_video.short_description = 'Has Video'
    
    def has_image(self, obj):
        return bool(obj.hero_image or obj.image_url)
    has_image.boolean = True
    has_image.short_description = 'Has Image'
    
    def has_logo(self, obj):
        return bool(obj.logo_upload or obj.logo_url)
    has_logo.boolean = True
    has_logo.short_description = 'Has Logo'


class ServiceItemInline(admin.TabularInline):
    model = ServiceItem
    extra = 0
    fields = ['title', 'description', 'icon', 'order', 'is_featured']
    ordering = ['order']


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'created_at', 'updated_at']
    list_editable = ['order']
    readonly_fields = ['created_at', 'updated_at']
    inlines = [ServiceItemInline]
    
    fieldsets = (
        ('Category Information', {
            'fields': ('name', 'description', 'icon', 'order')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(ServiceItem)
class ServiceItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'order', 'is_featured', 'created_at']
    list_filter = ['category', 'is_featured']
    list_editable = ['order', 'is_featured']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Service Information', {
            'fields': ('category', 'title', 'description', 'icon', 'order', 'is_featured')
        }),
        ('Features', {
            'fields': ('features',),
            'description': 'Enter features as JSON array. Example: ["Feature 1", "Feature 2", "Feature 3"]'
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'order', 'created_at']
    list_editable = ['order']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Feature Information', {
            'fields': ('title', 'description', 'icon', 'order')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = ['title', 'number', 'suffix', 'order', 'created_at']
    list_editable = ['number', 'suffix', 'order']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Statistic Information', {
            'fields': ('title', 'number', 'suffix', 'order')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'rating', 'is_featured', 'order', 'created_at']
    list_filter = ['rating', 'is_featured']
    list_editable = ['rating', 'is_featured', 'order']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Customer Information', {
            'fields': ('name', 'role', 'company')
        }),
        ('Photo Options', {
            'fields': ('photo_image', 'photo'),
            'description': 'Upload photo OR provide photo URL. If both are provided, uploaded image takes priority.'
        }),
        ('Testimonial Content', {
            'fields': ('review', 'rating', 'order', 'is_featured')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'is_featured', 'order', 'created_at']
    list_filter = ['is_featured']
    list_editable = ['is_featured', 'order']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Team Member Information', {
            'fields': ('name', 'role', 'bio', 'order', 'is_featured')
        }),
        ('Photo Options', {
            'fields': ('image_upload', 'image'),
            'description': 'Upload photo OR provide photo URL. If both are provided, uploaded image takes priority.'
        }),
        ('Social Links', {
            'fields': ('social_links',),
            'description': 'Enter social links as JSON object. Example: {"linkedin": "https://linkedin.com/in/username", "twitter": "https://twitter.com/username"}'
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


class PortfolioGalleryImageInline(admin.TabularInline):
    model = PortfolioGalleryImage
    extra = 1
    fields = ['image_upload', 'image_url', 'caption', 'order']
    ordering = ['order']


@admin.register(PortfolioProject)
class PortfolioProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'client', 'service', 'media_type', 'is_featured', 'order', 'created_at']
    list_filter = ['media_type', 'is_featured', 'service']
    list_editable = ['is_featured', 'order']
    readonly_fields = ['slug', 'created_at', 'updated_at']
    search_fields = ['title', 'description', 'client']
    inlines = [PortfolioGalleryImageInline]
    
    fieldsets = (
        ('Project Information', {
            'fields': ('title', 'slug', 'description', 'client', 'service', 'project_url', 'order', 'is_featured')
        }),
        ('Detailed Content (For Detail Page)', {
            'fields': ('detailed_description', 'challenge', 'solution', 'results'),
            'classes': ('collapse',),
            'description': 'Optional detailed content for portfolio detail page'
        }),
        ('Main Media', {
            'fields': ('media_upload', 'media_url', 'media_type'),
            'description': 'Upload main media file OR provide media URL. If both are provided, uploaded file takes priority.'
        }),
        ('Tags', {
            'fields': ('tags',),
            'description': 'Enter tags as JSON array. Example: ["Animation", "3D", "Character Design"]'
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('service')


@admin.register(PortfolioGalleryImage)
class PortfolioGalleryImageAdmin(admin.ModelAdmin):
    list_display = ['portfolio_project', 'caption', 'order', 'created_at']
    list_filter = ['portfolio_project']
    list_editable = ['order']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Gallery Image', {
            'fields': ('portfolio_project', 'image_upload', 'image_url', 'caption', 'order')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(AboutContent)
class AboutContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('About Information', {
            'fields': ('title', 'description')
        }),
        ('Company Story', {
            'fields': ('story',)
        }),
        ('Vision & Mission', {
            'fields': ('vision', 'mission')
        }),
        ('Values', {
            'fields': ('values',),
            'description': 'Enter company values as JSON array. Example: ["Innovation", "Quality", "Customer Focus"]'
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['email', 'phone', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('phone', 'email', 'address')
        }),
        ('Social Links', {
            'fields': ('social_links',),
            'description': 'Enter social links as JSON object. Example: {"facebook": "https://facebook.com/company", "instagram": "https://instagram.com/company"}'
        }),
        ('Business Hours', {
            'fields': ('business_hours',),
            'description': 'Enter business hours as JSON object. Example: {"monday": "9:00 AM - 6:00 PM", "tuesday": "9:00 AM - 6:00 PM"}'
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(ContactFormSubmission)
class ContactFormSubmissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'is_read', 'timestamp']
    list_filter = ['is_read', 'timestamp']
    list_editable = ['is_read']
    readonly_fields = ['timestamp']
    search_fields = ['name', 'email', 'subject', 'message']
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'phone', 'company')
        }),
        ('Message', {
            'fields': ('subject', 'message')
        }),
        ('Status', {
            'fields': ('is_read', 'timestamp')
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).order_by('-timestamp')


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'order', 'is_featured', 'created_at']
    list_editable = ['order', 'is_featured']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('FAQ Content', {
            'fields': ('question', 'answer')
        }),
        ('Display Settings', {
            'fields': ('order', 'is_featured')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


# Customize admin site
admin.site.site_header = "Pixel Box Studio Admin"
admin.site.site_title = "Pixel Box Studio Admin"
admin.site.index_title = "Welcome to Pixel Box Studio Administration"