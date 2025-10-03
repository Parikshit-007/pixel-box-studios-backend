from django.core.management.base import BaseCommand
from django.utils.text import slugify
from content.models import PortfolioProject


class Command(BaseCommand):
    help = 'Generate slugs for existing portfolio projects'

    def handle(self, *args, **kwargs):
        self.stdout.write('Generating slugs for existing portfolio projects...')
        
        projects = PortfolioProject.objects.all()
        updated_count = 0
        
        for project in projects:
            if not project.slug:
                base_slug = slugify(project.title)
                slug = base_slug
                counter = 1
                
                # Ensure unique slug
                while PortfolioProject.objects.filter(slug=slug).exclude(pk=project.pk).exists():
                    slug = f"{base_slug}-{counter}"
                    counter += 1
                
                # Update without triggering save method to avoid recursion
                PortfolioProject.objects.filter(pk=project.pk).update(slug=slug)
                updated_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Generated slug "{slug}" for "{project.title}"')
                )
        
        self.stdout.write(
            self.style.SUCCESS(f'\nSuccessfully generated {updated_count} slugs!')
        )



