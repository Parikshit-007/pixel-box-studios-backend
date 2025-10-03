from django.core.management.base import BaseCommand
from content.models import (
    Navigation, Hero, ServiceCategory, ServiceItem, Feature, Stat,
    Testimonial, TeamMember, PortfolioProject, AboutContent, ContactInfo
)


class Command(BaseCommand):
    help = 'Populate the database with sample data for Pixel Box Studio'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')

        # Create Navigation
        navigation, created = Navigation.objects.get_or_create(
            defaults={
                'logo_url': 'https://via.placeholder.com/200x60/6366f1/ffffff?text=Pixel+Box+Studio',
                'menu_links': [
                    {"name": "Home", "href": "/"},
                    {"name": "Services", "href": "/services"},
                    {"name": "About Us", "href": "/about"},
                    {"name": "Portfolio", "href": "/portfolio"},
                    {"name": "Contact", "href": "/contact"}
                ]
            }
        )
        if created:
            self.stdout.write('✓ Created Navigation')

        # Create Hero
        hero, created = Hero.objects.get_or_create(
            defaults={
                'title': 'IMMERSIVE',
                'subtitle': 'We craft stunning animations and data-driven digital marketing campaigns that blur the line between imagination and reality.',
                'cta_text': 'Get Started',
                'cta_link': '/contact',
                'video_url': 'https://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_1mb.mp4'
            }
        )
        if created:
            self.stdout.write('✓ Created Hero')

        # Create Service Categories and Items
        animation_category, created = ServiceCategory.objects.get_or_create(
            name='Animation & Motion Graphics',
            defaults={
                'description': 'Stunning 2D/3D animations, motion graphics, and visual storytelling that captivate audiences.',
                'icon': 'Play',
                'order': 1
            }
        )
        if created:
            self.stdout.write('✓ Created Animation Category')

        marketing_category, created = ServiceCategory.objects.get_or_create(
            name='Digital Marketing',
            defaults={
                'description': 'Data-driven digital marketing campaigns, social media strategies, and content creation.',
                'icon': 'Sparkles',
                'order': 2
            }
        )
        if created:
            self.stdout.write('✓ Created Marketing Category')

        brand_category, created = ServiceCategory.objects.get_or_create(
            name='Brand Identity',
            defaults={
                'description': 'Complete brand identity packages, logo design, and visual systems.',
                'icon': 'Palette',
                'order': 3
            }
        )
        if created:
            self.stdout.write('✓ Created Brand Category')

        # Create Service Items
        services_data = [
            {
                'category': animation_category,
                'title': '3D Animation',
                'description': 'Cutting-edge 3D animations that bring your vision to life with photorealistic detail and fluid motion.',
                'features': ['Character Animation', 'Product Visualization', 'Architectural Renders'],
                'icon': 'Video',
                'order': 1,
                'is_featured': True
            },
            {
                'category': animation_category,
                'title': 'Motion Graphics',
                'description': 'Dynamic motion graphics that captivate audiences and communicate complex ideas with visual clarity.',
                'features': ['Logo Animation', 'Explainer Videos', 'UI/UX Animation'],
                'icon': 'Palette',
                'order': 2,
                'is_featured': True
            },
            {
                'category': marketing_category,
                'title': 'Digital Marketing',
                'description': 'Data-driven marketing strategies that amplify your brand\'s reach and drive measurable results.',
                'features': ['Social Media Campaigns', 'Content Strategy', 'Performance Analytics'],
                'icon': 'Megaphone',
                'order': 1,
                'is_featured': True
            },
            {
                'category': brand_category,
                'title': 'Brand Identity',
                'description': 'Comprehensive brand identity solutions that establish your unique presence in the market.',
                'features': ['Logo Design', 'Brand Guidelines', 'Visual Systems'],
                'icon': 'Zap',
                'order': 1,
                'is_featured': True
            }
        ]

        for service_data in services_data:
            service, created = ServiceItem.objects.get_or_create(
                category=service_data['category'],
                title=service_data['title'],
                defaults=service_data
            )
            if created:
                self.stdout.write(f'✓ Created Service: {service.title}')

        # Create Features
        features_data = [
            {
                'title': 'Animation & Motion Graphics',
                'description': 'Stunning 2D/3D animations, motion graphics, and visual storytelling that captivate audiences and bring your brand to life.',
                'icon': 'Play',
                'order': 1
            },
            {
                'title': 'Digital Marketing',
                'description': 'Data-driven digital marketing campaigns, social media strategies, and content creation that drive engagement and conversions.',
                'icon': 'Sparkles',
                'order': 2
            },
            {
                'title': 'Brand Identity',
                'description': 'Complete brand identity packages, logo design, and visual systems that create memorable and impactful brand experiences.',
                'icon': 'Palette',
                'order': 3
            }
        ]

        for feature_data in features_data:
            feature, created = Feature.objects.get_or_create(
                title=feature_data['title'],
                defaults=feature_data
            )
            if created:
                self.stdout.write(f'✓ Created Feature: {feature.title}')

        # Create Stats
        stats_data = [
            {'title': 'Projects Completed', 'number': 150, 'suffix': '+', 'order': 1},
            {'title': 'Happy Clients', 'number': 75, 'suffix': '+', 'order': 2},
            {'title': 'Years Experience', 'number': 8, 'suffix': '+', 'order': 3},
            {'title': 'Team Members', 'number': 12, 'suffix': '+', 'order': 4}
        ]

        for stat_data in stats_data:
            stat, created = Stat.objects.get_or_create(
                title=stat_data['title'],
                defaults=stat_data
            )
            if created:
                self.stdout.write(f'✓ Created Stat: {stat.title}')

        # Create Testimonials
        testimonials_data = [
            {
                'name': 'Sarah Johnson',
                'role': 'Marketing Director',
                'company': 'TechCorp Solutions',
                'review': 'Pixel Box Studio transformed our brand with incredible animations and marketing campaigns. Their creativity and attention to detail is unmatched.',
                'photo': 'https://via.placeholder.com/100x100/6366f1/ffffff?text=SJ',
                'rating': 5,
                'order': 1,
                'is_featured': True
            },
            {
                'name': 'Michael Chen',
                'role': 'CEO',
                'company': 'InnovateLab',
                'review': 'The team at Pixel Box Studio delivered exceptional results for our product launch. Their motion graphics brought our vision to life perfectly.',
                'photo': 'https://via.placeholder.com/100x100/10b981/ffffff?text=MC',
                'rating': 5,
                'order': 2,
                'is_featured': True
            }
        ]

        for testimonial_data in testimonials_data:
            testimonial, created = Testimonial.objects.get_or_create(
                name=testimonial_data['name'],
                company=testimonial_data['company'],
                defaults=testimonial_data
            )
            if created:
                self.stdout.write(f'✓ Created Testimonial: {testimonial.name}')

        # Create Team Members
        team_data = [
            {
                'name': 'Alex Rodriguez',
                'role': 'Creative Director',
                'bio': 'With over 10 years in animation and design, Alex leads our creative vision and ensures every project exceeds expectations.',
                'image': 'https://via.placeholder.com/300x300/6366f1/ffffff?text=AR',
                'social_links': {'linkedin': 'https://linkedin.com/in/alexrodriguez', 'twitter': 'https://twitter.com/alexrodriguez'},
                'order': 1,
                'is_featured': True
            },
            {
                'name': 'Emma Thompson',
                'role': 'Lead Animator',
                'bio': 'Emma specializes in 3D character animation and brings characters to life with incredible attention to detail and personality.',
                'image': 'https://via.placeholder.com/300x300/10b981/ffffff?text=ET',
                'social_links': {'linkedin': 'https://linkedin.com/in/emmathompson', 'instagram': 'https://instagram.com/emmathompson'},
                'order': 2,
                'is_featured': True
            }
        ]

        for member_data in team_data:
            member, created = TeamMember.objects.get_or_create(
                name=member_data['name'],
                defaults=member_data
            )
            if created:
                self.stdout.write(f'✓ Created Team Member: {member.name}')

        # Create Portfolio Projects
        portfolio_data = [
            {
                'title': 'TechCorp Product Launch',
                'description': 'Complete 3D product visualization and marketing campaign for a revolutionary tech product.',
                'media_url': 'https://via.placeholder.com/600x400/6366f1/ffffff?text=TechCorp+Project',
                'media_type': 'image',
                'tags': ['3D Animation', 'Product Visualization', 'Marketing'],
                'client': 'TechCorp Solutions',
                'project_url': 'https://example.com/techcorp-project',
                'order': 1,
                'is_featured': True
            },
            {
                'title': 'Brand Identity Redesign',
                'description': 'Complete brand overhaul including logo design, brand guidelines, and visual identity system.',
                'media_url': 'https://via.placeholder.com/600x400/10b981/ffffff?text=Brand+Identity',
                'media_type': 'image',
                'tags': ['Brand Design', 'Logo Design', 'Visual Identity'],
                'client': 'InnovateLab',
                'project_url': 'https://example.com/brand-identity',
                'order': 2,
                'is_featured': True
            }
        ]

        for project_data in portfolio_data:
            project, created = PortfolioProject.objects.get_or_create(
                title=project_data['title'],
                defaults=project_data
            )
            if created:
                self.stdout.write(f'✓ Created Portfolio Project: {project.title}')

        # Create About Content
        about, created = AboutContent.objects.get_or_create(
            defaults={
                'title': 'About Pixel Box Studio',
                'description': 'We are a creative studio specializing in animation and digital marketing, dedicated to bringing your vision to life.',
                'story': 'Founded in 2016, Pixel Box Studio began as a small team of passionate animators and designers. Over the years, we\'ve grown into a full-service creative agency, helping brands tell their stories through compelling visuals and strategic marketing.',
                'vision': 'To be the leading creative partner for brands seeking innovative animation and marketing solutions that drive real results.',
                'mission': 'We combine artistic excellence with strategic thinking to create memorable experiences that connect brands with their audiences.',
                'values': ['Creativity', 'Quality', 'Innovation', 'Collaboration', 'Results']
            }
        )
        if created:
            self.stdout.write('✓ Created About Content')

        # Create Contact Info
        contact_info, created = ContactInfo.objects.get_or_create(
            defaults={
                'phone': '+1 (555) 123-4567',
                'email': 'hello@pixelboxstudio.com',
                'address': '123 Creative Street, Design District, New York, NY 10001',
                'social_links': {
                    'facebook': 'https://facebook.com/pixelboxstudio',
                    'instagram': 'https://instagram.com/pixelboxstudio',
                    'linkedin': 'https://linkedin.com/company/pixelboxstudio',
                    'twitter': 'https://twitter.com/pixelboxstudio'
                },
                'business_hours': {
                    'monday': '9:00 AM - 6:00 PM',
                    'tuesday': '9:00 AM - 6:00 PM',
                    'wednesday': '9:00 AM - 6:00 PM',
                    'thursday': '9:00 AM - 6:00 PM',
                    'friday': '9:00 AM - 6:00 PM',
                    'saturday': '10:00 AM - 4:00 PM',
                    'sunday': 'Closed'
                }
            }
        )
        if created:
            self.stdout.write('✓ Created Contact Info')

        self.stdout.write(
            self.style.SUCCESS('Successfully populated database with sample data!')
        )
        self.stdout.write('You can now access the admin panel at http://localhost:8000/admin/')
        self.stdout.write('Username: admin, Password: admin123')






