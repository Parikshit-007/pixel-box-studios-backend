from django.core.management.base import BaseCommand
from content.models import TeamMember


class Command(BaseCommand):
    help = 'Populate team members with static data'

    def handle(self, *args, **options):
        self.stdout.write('Adding team members...')

        team_data = [
            {
                'name': 'Alex Rivera',
                'role': 'Creative Director',
                'bio': '10+ years in animation and visual storytelling. Passionate about bringing ideas to life through motion.',
                'image': '/creative-director-professional-headshot.jpg',
                'social_links': {
                    'linkedin': '#',
                    'twitter': '#',
                    'instagram': '#'
                },
                'order': 1,
                'is_featured': True
            },
            {
                'name': 'Maya Patel',
                'role': 'Lead Animator',
                'bio': 'Specialist in 2D/3D animation with expertise in character design and motion graphics.',
                'image': '/female-animator-professional-headshot.jpg',
                'social_links': {
                    'linkedin': '#',
                    'twitter': '#',
                    'instagram': '#'
                },
                'order': 2,
                'is_featured': True
            },
            {
                'name': 'David Kim',
                'role': 'Digital Marketing Strategist',
                'bio': 'Data-driven marketer who creates campaigns that convert and build lasting brand connections.',
                'image': '/marketing-strategist-professional-headshot-asian.jpg',
                'social_links': {
                    'linkedin': '#',
                    'twitter': '#',
                    'instagram': '#'
                },
                'order': 3,
                'is_featured': True
            },
            {
                'name': 'Sophie Chen',
                'role': 'Brand Designer',
                'bio': 'Visual identity expert who crafts memorable brands that stand out in crowded markets.',
                'image': '/brand-designer-professional-headshot.jpg',
                'social_links': {
                    'linkedin': '#',
                    'twitter': '#',
                    'instagram': '#'
                },
                'order': 4,
                'is_featured': True
            }
        ]

        for member_data in team_data:
            member, created = TeamMember.objects.get_or_create(
                name=member_data['name'],
                defaults=member_data
            )
            if created:
                self.stdout.write(f'Created team member: {member.name}')
            else:
                self.stdout.write(f'Team member already exists: {member.name}')

        self.stdout.write(self.style.SUCCESS('Team members populated successfully!'))


