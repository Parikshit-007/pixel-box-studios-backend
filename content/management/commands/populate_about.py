from django.core.management.base import BaseCommand
from content.models import AboutContent, Stat


class Command(BaseCommand):
    help = 'Populate about content and stats with sample data'

    def handle(self, *args, **options):
        self.stdout.write('Adding about content...')

        # Create About Content
        about_content, created = AboutContent.objects.get_or_create(
            defaults={
                'title': 'About Pixel Box Studio',
                'description': 'We are a creative powerhouse that bridges the gap between imagination and reality. Our team of passionate artists, strategists, and technologists work together to create immersive experiences that captivate audiences and drive business growth.',
                'story': 'From stunning 3D animations to data-driven marketing campaigns, we combine artistic vision with strategic thinking to deliver solutions that not only look amazing but also achieve measurable results.',
                'vision': 'To be the leading creative studio that transforms ideas into extraordinary digital experiences.',
                'mission': 'Empowering businesses through innovative animation and digital marketing solutions.',
                'values': ['Creativity', 'Excellence', 'Innovation', 'Collaboration', 'Quality', 'Trust']
            }
        )
        
        if created:
            self.stdout.write(f'Created about content: {about_content.title}')
        else:
            self.stdout.write(f'About content already exists: {about_content.title}')

        # Create Stats
        self.stdout.write('Adding stats...')
        
        stats_data = [
            {
                'title': 'Creative Professionals',
                'number': 50,
                'suffix': '+',
                'order': 1
            },
            {
                'title': 'Projects Completed',
                'number': 200,
                'suffix': '+',
                'order': 2
            },
            {
                'title': 'Years of Excellence',
                'number': 5,
                'suffix': '+',
                'order': 3
            },
            {
                'title': 'Countries Served',
                'number': 25,
                'suffix': '+',
                'order': 4
            }
        ]

        for stat_data in stats_data:
            stat, created = Stat.objects.get_or_create(
                title=stat_data['title'],
                defaults=stat_data
            )
            if created:
                self.stdout.write(f'Created stat: {stat.title}')
            else:
                self.stdout.write(f'Stat already exists: {stat.title}')

        self.stdout.write(self.style.SUCCESS('About content and stats populated successfully!'))


