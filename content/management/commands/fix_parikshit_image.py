from django.core.management.base import BaseCommand
from content.models import TeamMember


class Command(BaseCommand):
    help = 'Add placeholder image for Parikshit Pandey'

    def handle(self, *args, **options):
        try:
            parikshit = TeamMember.objects.get(name="Parikshit Pandey")
            parikshit.image = "/professional-man-headshot.png"
            parikshit.save()
            self.stdout.write(self.style.SUCCESS(f'Updated image for {parikshit.name}'))
        except TeamMember.DoesNotExist:
            self.stdout.write(self.style.ERROR('Parikshit Pandey not found'))


