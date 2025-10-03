from django.core.management.base import BaseCommand
from content.models import Stat


class Command(BaseCommand):
    help = 'Update stats with new numbers'

    def handle(self, *args, **options):
        self.stdout.write('Updating stats with new numbers...')

        # Update existing stats with new numbers
        stats_data = [
            {
                'title': 'Projects Completed',
                'number': 150,
                'suffix': '+',
                'order': 1
            },
            {
                'title': 'Creative Professionals',
                'number': 50,
                'suffix': '+',
                'order': 2
            },
            {
                'title': 'Happy Clients',
                'number': 74,
                'suffix': '+',
                'order': 3
            },
            {
                'title': 'Years Experience',
                'number': 8,
                'suffix': '+',
                'order': 4
            },
            {
                'title': 'Years of Excellence',
                'number': 5,
                'suffix': '+',
                'order': 5
            },
            {
                'title': 'Team Members',
                'number': 12,
                'suffix': '+',
                'order': 6
            },
            {
                'title': 'Countries Served',
                'number': 25,
                'suffix': '+',
                'order': 7
            }
        ]

        for stat_data in stats_data:
            stat, created = Stat.objects.update_or_create(
                title=stat_data['title'],
                defaults={
                    'number': stat_data['number'],
                    'suffix': stat_data['suffix'],
                    'order': stat_data['order']
                }
            )
            if created:
                self.stdout.write(f'Created stat: {stat.title} - {stat.number}{stat.suffix}')
            else:
                self.stdout.write(f'Updated stat: {stat.title} - {stat.number}{stat.suffix}')

        self.stdout.write(self.style.SUCCESS('Stats updated successfully!'))


