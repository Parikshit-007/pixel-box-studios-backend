from django.core.management.base import BaseCommand
from content.models import Testimonial


class Command(BaseCommand):
    help = 'Populate testimonials with static data'

    def handle(self, *args, **options):
        self.stdout.write('Adding testimonials...')

        testimonials_data = [
            {
                'name': 'Sarah Johnson',
                'company': 'TechStart Inc.',
                'role': 'Marketing Director',
                'review': 'Pixel Box Studio transformed our brand with stunning animations and a comprehensive digital strategy. Our engagement rates increased by 300%!',
                'photo': '/professional-woman-headshot.png',
                'rating': 5,
                'order': 1,
                'is_featured': True
            },
            {
                'name': 'Michael Chen',
                'company': 'Creative Labs',
                'role': 'CEO',
                'review': 'The team\'s creativity and attention to detail is unmatched. They brought our vision to life with beautiful animations that perfectly captured our brand essence.',
                'photo': '/professional-man-headshot.png',
                'rating': 5,
                'order': 2,
                'is_featured': True
            },
            {
                'name': 'Emily Rodriguez',
                'company': 'Fashion Forward',
                'role': 'Brand Manager',
                'review': 'Working with Pixel Box Studio was a game-changer. Their digital marketing campaigns helped us reach new audiences and grow our online presence significantly.',
                'photo': '/latina-professional-headshot.png',
                'rating': 5,
                'order': 3,
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
                self.stdout.write(f'Created testimonial: {testimonial.name}')
            else:
                self.stdout.write(f'Testimonial already exists: {testimonial.name}')

        self.stdout.write(self.style.SUCCESS('Testimonials populated successfully!'))


