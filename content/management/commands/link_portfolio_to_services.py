from django.core.management.base import BaseCommand
from content.models import PortfolioProject, ServiceItem


class Command(BaseCommand):
    help = 'Link existing portfolio projects to appropriate services'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting to link portfolio projects to services...')
        
        # Get services
        animation_service = ServiceItem.objects.filter(title__icontains='Animation').first()
        brand_identity_service = ServiceItem.objects.filter(title__icontains='Brand Identity').first()
        web_design_service = ServiceItem.objects.filter(title__icontains='Web Design').first()
        digital_marketing_service = ServiceItem.objects.filter(title__icontains='Digital Marketing').first()
        
        # Link portfolio projects based on their titles/tags
        portfolio_mappings = {
            'Animated Character Mascot': animation_service,
            '3D Product Animation': animation_service,
            'Motion Graphics Explainer': animation_service,
            'Brand Identity Design': brand_identity_service,
            'Corporate Branding Package': brand_identity_service,
            'Logo Design & Guidelines': brand_identity_service,
            'Interactive Web Experience': web_design_service,
            'E-commerce Website': web_design_service,
            'Responsive Web Design': web_design_service,
            'Digital Marketing Campaign': digital_marketing_service,
            'Social Media Strategy': digital_marketing_service,
            'Content Marketing Campaign': digital_marketing_service,
        }
        
        linked_count = 0
        
        for project_title_part, service in portfolio_mappings.items():
            if service:
                projects = PortfolioProject.objects.filter(title__icontains=project_title_part)
                for project in projects:
                    if not project.service:  # Only update if not already linked
                        project.service = service
                        project.save()
                        linked_count += 1
                        self.stdout.write(
                            self.style.SUCCESS(f'Linked "{project.title}" to "{service.title}"')
                        )
        
        # Also link remaining projects by checking tags manually
        remaining_projects = PortfolioProject.objects.filter(service__isnull=True)
        
        for project in remaining_projects:
            tags_str = str(project.tags).lower() if project.tags else ''
            
            if animation_service and ('animation' in tags_str or '3d' in tags_str or 'motion' in tags_str):
                project.service = animation_service
                project.save()
                linked_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Linked "{project.title}" to "{animation_service.title}" (by tag)')
                )
            elif brand_identity_service and ('brand' in tags_str or 'logo' in tags_str or 'identity' in tags_str):
                project.service = brand_identity_service
                project.save()
                linked_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Linked "{project.title}" to "{brand_identity_service.title}" (by tag)')
                )
            elif web_design_service and ('web' in tags_str or 'website' in tags_str or 'ui' in tags_str or 'ux' in tags_str):
                project.service = web_design_service
                project.save()
                linked_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Linked "{project.title}" to "{web_design_service.title}" (by tag)')
                )
            elif digital_marketing_service and ('marketing' in tags_str or 'social' in tags_str or 'campaign' in tags_str):
                project.service = digital_marketing_service
                project.save()
                linked_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Linked "{project.title}" to "{digital_marketing_service.title}" (by tag)')
                )
        
        self.stdout.write(
            self.style.SUCCESS(f'\nSuccessfully linked {linked_count} portfolio projects to services!')
        )

