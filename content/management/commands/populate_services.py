from django.core.management.base import BaseCommand
from content.models import ServiceCategory, ServiceItem


class Command(BaseCommand):
  help = 'Populate service categories and items based on original static data'

  def handle(self, *args, **options):
    self.stdout.write('Populating services...')

    categories = {
      'Animation & Motion Graphics': {
        'description': 'Stunning 2D/3D animations, motion graphics, and visual storytelling that captivate audiences.',
        'icon': 'Video',
        'order': 1,
      },
      'Digital Marketing': {
        'description': 'Data-driven digital marketing campaigns, social media strategies, and content creation.',
        'icon': 'Megaphone',
        'order': 2,
      },
      'Brand Identity': {
        'description': 'Complete brand identity packages, logo design, and visual systems.',
        'icon': 'Zap',
        'order': 3,
      },
      'Interactive Experiences': {
        'description': 'Immersive web experiences that engage users through innovative design and seamless functionality.',
        'icon': 'Code',
        'order': 4,
      },
      'Campaign Strategy': {
        'description': 'Strategic campaign development that aligns creative vision with business objectives.',
        'icon': 'Target',
        'order': 5,
      },
    }

    created_categories = {}
    for name, data in categories.items():
      cat, _ = ServiceCategory.objects.get_or_create(name=name, defaults=data)
      created_categories[name] = cat

    items = [
      {
        'category': 'Animation & Motion Graphics',
        'title': '3D Animation',
        'description': 'Cutting-edge 3D animations that bring your vision to life with photorealistic detail and fluid motion.',
        'features': ['Character Animation', 'Product Visualization', 'Architectural Renders'],
        'icon': 'Video',
        'order': 1,
        'is_featured': True,
      },
      {
        'category': 'Animation & Motion Graphics',
        'title': 'Motion Graphics',
        'description': 'Dynamic motion graphics that captivate audiences and communicate complex ideas with visual clarity.',
        'features': ['Logo Animation', 'Explainer Videos', 'UI/UX Animation'],
        'icon': 'Palette',
        'order': 2,
        'is_featured': True,
      },
      {
        'category': 'Digital Marketing',
        'title': 'Digital Marketing',
        'description': 'Data-driven marketing strategies that amplify your brand\'s reach and drive measurable results.',
        'features': ['Social Media Campaigns', 'Content Strategy', 'Performance Analytics'],
        'icon': 'Megaphone',
        'order': 1,
        'is_featured': True,
      },
      {
        'category': 'Interactive Experiences',
        'title': 'Interactive Experiences',
        'description': 'Immersive web experiences that engage users through innovative design and seamless functionality.',
        'features': ['WebGL Development', 'AR/VR Experiences', 'Interactive Installations'],
        'icon': 'Code',
        'order': 1,
        'is_featured': False,
      },
      {
        'category': 'Brand Identity',
        'title': 'Brand Identity',
        'description': 'Comprehensive brand identity solutions that establish your unique presence in the market.',
        'features': ['Logo Design', 'Brand Guidelines', 'Visual Systems'],
        'icon': 'Zap',
        'order': 1,
        'is_featured': True,
      },
      {
        'category': 'Campaign Strategy',
        'title': 'Campaign Strategy',
        'description': 'Strategic campaign development that aligns creative vision with business objectives.',
        'features': ['Market Research', 'Creative Direction', 'ROI Optimization'],
        'icon': 'Target',
        'order': 1,
        'is_featured': False,
      },
    ]

    for data in items:
      category = created_categories[data['category']]
      defaults = data.copy()
      defaults.pop('category', None)
      obj, created = ServiceItem.objects.get_or_create(
        category=category,
        title=data['title'],
        defaults=defaults,
      )
      self.stdout.write(f"{'Created' if created else 'Exists'}: {obj.title}")

    self.stdout.write(self.style.SUCCESS('Services populated.'))




