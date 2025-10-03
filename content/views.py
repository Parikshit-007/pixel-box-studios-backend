from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.core.cache import cache
from django.conf import settings
from .models import (
    Navigation, Hero, ServiceCategory, ServiceItem, Feature, Stat,
    Testimonial, TeamMember, PortfolioProject, AboutContent,
    ContactInfo, ContactFormSubmission, FAQ
)
from .serializers import (
    NavigationSerializer, HeroSerializer, ServiceCategorySerializer,
    ServiceItemSerializer, FeatureSerializer, StatSerializer,
    TestimonialSerializer, TeamMemberSerializer, PortfolioProjectSerializer,
    AboutContentSerializer, ContactInfoSerializer, ContactFormSubmissionSerializer,
    FAQSerializer, ServiceCategoryListSerializer, ServiceItemListSerializer,
    FeaturedTestimonialSerializer, FeaturedTeamMemberSerializer,
    FeaturedPortfolioProjectSerializer
)


class NavigationViewSet(viewsets.ModelViewSet):
    queryset = Navigation.objects.all()
    serializer_class = NavigationSerializer
    
    @action(detail=False, methods=['get'])
    def current(self, request):
        """Get the current navigation configuration"""
        navigation = Navigation.objects.first()
        if navigation:
            serializer = self.get_serializer(navigation)
            return Response(serializer.data)
        return Response({'message': 'No navigation configuration found'}, status=status.HTTP_404_NOT_FOUND)


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
    
    @action(detail=False, methods=['get'])
    def current(self, request):
        """Get the current hero content"""
        hero = Hero.objects.first()
        if hero:
            serializer = self.get_serializer(hero)
            return Response(serializer.data)
        return Response({'message': 'No hero content found'}, status=status.HTTP_404_NOT_FOUND)


class ServiceCategoryViewSet(viewsets.ModelViewSet):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ServiceCategoryListSerializer
        return ServiceCategorySerializer
    
    @action(detail=True, methods=['get'])
    def services(self, request, pk=None):
        """Get services for a specific category"""
        category = self.get_object()
        services = category.services.all()
        serializer = ServiceItemSerializer(services, many=True)
        return Response(serializer.data)


class ServiceItemViewSet(viewsets.ModelViewSet):
    queryset = ServiceItem.objects.all()
    serializer_class = ServiceItemSerializer
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ServiceItemListSerializer
        return ServiceItemSerializer
    
    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Get featured services only"""
        featured_services = ServiceItem.objects.filter(is_featured=True)
        serializer = self.get_serializer(featured_services, many=True)
        return Response(serializer.data)


class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer


class StatViewSet(viewsets.ModelViewSet):
    queryset = Stat.objects.all()
    serializer_class = StatSerializer
    
    def list(self, request):
        """Get all stats with caching"""
        cache_key = 'stats_all'
        cached_data = cache.get(cache_key)
        
        if cached_data is None:
            stats = Stat.objects.all().order_by('order')
            serializer = self.get_serializer(stats, many=True)
            cached_data = serializer.data
            cache.set(cache_key, cached_data, 300)  # Cache for 5 minutes
        
        return Response(cached_data)


class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    
    def get_serializer_class(self):
        if self.action == 'featured':
            return FeaturedTestimonialSerializer
        return TestimonialSerializer
    
    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Get featured testimonials only"""
        cache_key = 'testimonials_featured'
        cached_data = cache.get(cache_key)
        
        if cached_data is None:
            featured_testimonials = Testimonial.objects.filter(is_featured=True).order_by('order')
            serializer = self.get_serializer(featured_testimonials, many=True)
            cached_data = serializer.data
            cache.set(cache_key, cached_data, 300)  # Cache for 5 minutes
        
        return Response(cached_data)


class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
    
    def get_serializer_class(self):
        if self.action == 'featured':
            return FeaturedTeamMemberSerializer
        return TeamMemberSerializer
    
    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Get featured team members only"""
        cache_key = 'team_featured'
        cached_data = cache.get(cache_key)
        
        if cached_data is None:
            featured_members = TeamMember.objects.filter(is_featured=True).order_by('order')
            serializer = self.get_serializer(featured_members, many=True, context={'request': request})
            cached_data = serializer.data
            cache.set(cache_key, cached_data, 300)  # Cache for 5 minutes
        
        return Response(cached_data)


class PortfolioProjectViewSet(viewsets.ModelViewSet):
    queryset = PortfolioProject.objects.all()
    serializer_class = PortfolioProjectSerializer
    lookup_field = 'slug'
    
    def get_serializer_class(self):
        if self.action == 'featured':
            return FeaturedPortfolioProjectSerializer
        return PortfolioProjectSerializer
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
    
    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Get featured portfolio projects only"""
        featured_projects = PortfolioProject.objects.filter(is_featured=True)
        serializer = self.get_serializer(featured_projects, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'], url_path='by-service/(?P<service_id>[^/.]+)')
    def by_service(self, request, service_id=None):
        """Get portfolio projects for a specific service"""
        if service_id:
            projects = PortfolioProject.objects.filter(service_id=service_id)
            serializer = self.get_serializer(projects, many=True)
            return Response(serializer.data)
        return Response({'error': 'Service ID is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['get'], url_path='by-slug')
    def by_slug(self, request, slug=None):
        """Get a single portfolio project by slug"""
        try:
            project = PortfolioProject.objects.get(slug=slug)
            serializer = self.get_serializer(project)
            return Response(serializer.data)
        except PortfolioProject.DoesNotExist:
            return Response({'error': 'Portfolio project not found'}, status=status.HTTP_404_NOT_FOUND)


class AboutContentViewSet(viewsets.ModelViewSet):
    queryset = AboutContent.objects.all()
    serializer_class = AboutContentSerializer
    
    @action(detail=False, methods=['get'])
    def current(self, request):
        """Get the current about content"""
        cache_key = 'about_current'
        cached_data = cache.get(cache_key)
        
        if cached_data is None:
            about = AboutContent.objects.first()
            if about:
                serializer = self.get_serializer(about)
                cached_data = serializer.data
                cache.set(cache_key, cached_data, 300)  # Cache for 5 minutes
            else:
                return Response({'message': 'No about content found'}, status=status.HTTP_404_NOT_FOUND)
        
        return Response(cached_data)


class ContactInfoViewSet(viewsets.ModelViewSet):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer
    
    @action(detail=False, methods=['get'])
    def current(self, request):
        """Get the current contact information"""
        contact_info = ContactInfo.objects.first()
        if contact_info:
            serializer = self.get_serializer(contact_info)
            return Response(serializer.data)
        return Response({'message': 'No contact information found'}, status=status.HTTP_404_NOT_FOUND)


class ContactFormSubmissionViewSet(viewsets.ModelViewSet):
    queryset = ContactFormSubmission.objects.all()
    serializer_class = ContactFormSubmissionSerializer
    
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'create':
            permission_classes = []  # Allow anyone to submit contact forms
        else:
            permission_classes = []  # For now, allow all actions
        return [permission() for permission in permission_classes]
    
    def create(self, request, *args, **kwargs):
        """Create a new contact form submission"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Thank you for your message! We will get back to you soon.',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['patch'])
    def mark_read(self, request, pk=None):
        """Mark a contact form submission as read"""
        submission = self.get_object()
        submission.is_read = True
        submission.save()
        serializer = self.get_serializer(submission)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def unread(self, request):
        """Get unread contact form submissions"""
        unread_submissions = ContactFormSubmission.objects.filter(is_read=False)
        serializer = self.get_serializer(unread_submissions, many=True)
        return Response(serializer.data)


class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    
    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Get featured FAQs only"""
        cache_key = 'faqs_featured'
        cached_data = cache.get(cache_key)
        
        if cached_data is None:
            featured_faqs = FAQ.objects.filter(is_featured=True).order_by('order')
            serializer = self.get_serializer(featured_faqs, many=True)
            cached_data = serializer.data
            cache.set(cache_key, cached_data, 300)  # Cache for 5 minutes
        
        return Response(cached_data)