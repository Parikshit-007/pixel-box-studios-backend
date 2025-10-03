from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    NavigationViewSet, HeroViewSet, ServiceCategoryViewSet, ServiceItemViewSet,
    FeatureViewSet, StatViewSet, TestimonialViewSet, TeamMemberViewSet,
    PortfolioProjectViewSet, AboutContentViewSet, ContactInfoViewSet,
    ContactFormSubmissionViewSet, FAQViewSet
)

router = DefaultRouter()
router.register(r'navigation', NavigationViewSet)
router.register(r'hero', HeroViewSet)
router.register(r'service-categories', ServiceCategoryViewSet)
router.register(r'services', ServiceItemViewSet)
router.register(r'features', FeatureViewSet)
router.register(r'stats', StatViewSet)
router.register(r'testimonials', TestimonialViewSet)
router.register(r'team', TeamMemberViewSet)
router.register(r'portfolio', PortfolioProjectViewSet)
router.register(r'about', AboutContentViewSet)
router.register(r'contact-info', ContactInfoViewSet)
router.register(r'contact-form', ContactFormSubmissionViewSet)
router.register(r'faqs', FAQViewSet)

urlpatterns = [
    path('', include(router.urls)),
]



