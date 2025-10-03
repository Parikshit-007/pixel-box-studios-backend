from django.core.management.base import BaseCommand
from content.models import PortfolioProject


class Command(BaseCommand):
    help = 'Populate portfolio with the original static data'

    def handle(self, *args, **options):
        self.stdout.write('Adding portfolio projects...')

        # Original static portfolio data
        portfolio_data = [
            {
                'title': 'Immersive Brand Experience',
                'description': 'A captivating 3D brand experience that showcases product innovation through stunning visual storytelling.',
                'media_url': '/3d-product-animation-showcase.jpg',
                'media_type': 'image',
                'tags': ['3D Animation', 'Product Viz', 'WebGL'],
                'client': 'TechCorp Solutions',
                'project_url': 'https://example.com/immersive-brand',
                'order': 1,
                'is_featured': True
            },
            {
                'title': 'Digital Campaign Success',
                'description': 'Multi-platform digital campaign that increased brand awareness by 300% and drove record engagement.',
                'media_url': '/digital-marketing-campaign-analytics.jpg',
                'media_type': 'image',
                'tags': ['Social Media', 'Analytics', 'Strategy'],
                'client': 'MarketingPro Inc',
                'project_url': 'https://example.com/digital-campaign',
                'order': 2,
                'is_featured': True
            },
            {
                'title': 'Interactive Web Experience',
                'description': 'Award-winning interactive website that combines stunning visuals with seamless user experience.',
                'media_url': '/interactive-web-design-interface.jpg',
                'media_type': 'image',
                'tags': ['Web Design', 'UX/UI', 'Animation'],
                'client': 'DesignStudio Co',
                'project_url': 'https://example.com/interactive-web',
                'order': 3,
                'is_featured': True
            },
            {
                'title': 'Motion Graphics Series',
                'description': 'Dynamic motion graphics series that explains complex concepts through engaging visual narratives.',
                'media_url': '/motion-graphics-explainer-video.jpg',
                'media_type': 'image',
                'tags': ['Motion Graphics', 'Storytelling', 'Education'],
                'client': 'EduTech Solutions',
                'project_url': 'https://example.com/motion-graphics',
                'order': 4,
                'is_featured': True
            }
        ]

        for project_data in portfolio_data:
            project, created = PortfolioProject.objects.get_or_create(
                title=project_data['title'],
                defaults=project_data
            )
            if created:
                self.stdout.write(f'Created Portfolio Project: {project.title}')
            else:
                self.stdout.write(f'Portfolio Project already exists: {project.title}')

        self.stdout.write(
            self.style.SUCCESS('Successfully populated portfolio with static data!')
        )
        self.stdout.write('You can now view the portfolio at http://localhost:3000/portfolio')
