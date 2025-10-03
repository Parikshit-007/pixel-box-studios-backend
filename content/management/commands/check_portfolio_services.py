from django.core.management.base import BaseCommand
from content.models import PortfolioProject, ServiceItem


class Command(BaseCommand):
    help = 'Check portfolio-service mappings'

    def handle(self, *args, **kwargs):
        self.stdout.write('=== Portfolio-Service Mapping ===')
        
        portfolios = PortfolioProject.objects.all()
        
        for p in portfolios:
            service_name = p.service.title if p.service else "No service"
            service_id = p.service.id if p.service else "N/A"
            self.stdout.write(f'{p.title} -> Service ID: {service_id}, Name: {service_name}')
        
        self.stdout.write('\n=== Services with Portfolios ===')
        services = ServiceItem.objects.all()
        for s in services:
            count = PortfolioProject.objects.filter(service=s).count()
            self.stdout.write(f'Service ID {s.id}: {s.title} - {count} portfolios')



