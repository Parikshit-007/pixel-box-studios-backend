from django.core.management.base import BaseCommand
from content.models import ServiceCategory, ServiceItem


class Command(BaseCommand):
    help = 'Add AI and CGI enhanced services'

    def handle(self, *args, **options):
        self.stdout.write('Adding AI and CGI services...')

        # Create AI/CGI category if it doesn't exist
        ai_category, created = ServiceCategory.objects.get_or_create(
            name='AI & CGI Enhanced',
            defaults={
                'description': 'Cutting-edge AI-powered and CGI-enhanced creative solutions that push the boundaries of digital innovation.',
                'icon': 'Sparkles',
                'order': 6
            }
        )
        if created:
            self.stdout.write(f'Created category: {ai_category.name}')
        else:
            self.stdout.write(f'Category already exists: {ai_category.name}')

        # AI/CGI Services
        ai_services = [
            {
                'title': 'AI-Enhanced Animation',
                'description': 'Revolutionary animation workflows powered by artificial intelligence for faster production and enhanced creativity.',
                'features': ['AI Character Generation', 'Automated Rigging', 'Smart Motion Capture', 'AI-Assisted Storyboarding'],
                'icon': 'Sparkles',
                'order': 1,
                'is_featured': True
            },
            {
                'title': 'CGI Visual Effects',
                'description': 'Photorealistic CGI visual effects and compositing that seamlessly blend reality with imagination.',
                'features': ['3D Modeling & Texturing', 'Particle Systems', 'Lighting & Rendering', 'Compositing'],
                'icon': 'Video',
                'order': 2,
                'is_featured': True
            },
            {
                'title': 'AI Content Generation',
                'description': 'Intelligent content creation using AI tools for rapid prototyping and creative ideation.',
                'features': ['AI Text Generation', 'Image Synthesis', 'Video Generation', 'Creative Automation'],
                'icon': 'Zap',
                'order': 3,
                'is_featured': True
            },
            {
                'title': 'Machine Learning Analytics',
                'description': 'Advanced analytics and insights powered by machine learning for data-driven creative decisions.',
                'features': ['Predictive Analytics', 'User Behavior Analysis', 'Performance Optimization', 'ROI Prediction'],
                'icon': 'Target',
                'order': 4,
                'is_featured': False
            },
            {
                'title': 'Virtual Production',
                'description': 'Next-generation virtual production techniques combining real-time rendering with live action.',
                'features': ['Real-time Rendering', 'Virtual Sets', 'Motion Capture Integration', 'Live Compositing'],
                'icon': 'Monitor',
                'order': 5,
                'is_featured': True
            },
            {
                'title': 'AI-Powered Branding',
                'description': 'Intelligent brand identity development using AI to analyze market trends and create unique visual identities.',
                'features': ['AI Logo Generation', 'Brand Analysis', 'Trend Prediction', 'Automated Guidelines'],
                'icon': 'Palette',
                'order': 6,
                'is_featured': False
            }
        ]

        for service_data in ai_services:
            service, created = ServiceItem.objects.get_or_create(
                category=ai_category,
                title=service_data['title'],
                defaults=service_data
            )
            if created:
                self.stdout.write(f'Created service: {service.title}')
            else:
                self.stdout.write(f'Service already exists: {service.title}')

        self.stdout.write(
            self.style.SUCCESS('AI and CGI services added successfully!')
        )
        self.stdout.write('You can now view them in the admin panel under Service Items')


