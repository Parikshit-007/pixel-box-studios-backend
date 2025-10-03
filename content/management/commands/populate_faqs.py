from django.core.management.base import BaseCommand
from content.models import FAQ


class Command(BaseCommand):
    help = 'Populate FAQs with static data'

    def handle(self, *args, **options):
        self.stdout.write('Adding FAQs...')

        faqs_data = [
            {
                'question': 'What types of animation services do you offer?',
                'answer': 'We offer a comprehensive range of animation services including 2D/3D character animation, motion graphics, explainer videos, logo animations, product visualizations, and interactive animations for web and mobile applications.',
                'order': 1,
                'is_featured': True
            },
            {
                'question': 'How long does a typical project take?',
                'answer': 'Project timelines vary depending on complexity and scope. Simple logo animations may take 1-2 weeks, while complex 3D animations or comprehensive marketing campaigns can take 4-8 weeks. We provide detailed timelines during our initial consultation.',
                'order': 2,
                'is_featured': True
            },
            {
                'question': 'Do you work with businesses of all sizes?',
                'answer': 'We work with startups, small businesses, and large enterprises. Our flexible approach allows us to scale our services to meet your specific needs and budget requirements.',
                'order': 3,
                'is_featured': True
            },
            {
                'question': 'What\'s included in your digital marketing services?',
                'answer': 'Our digital marketing services include social media strategy and management, content creation, influencer partnerships, paid advertising campaigns, SEO optimization, email marketing, and comprehensive analytics and reporting.',
                'order': 4,
                'is_featured': True
            },
            {
                'question': 'Can you help with rebranding existing businesses?',
                'answer': 'Yes, we specialize in both new brand creation and rebranding projects. We\'ll work with you to understand your current brand challenges and develop a fresh identity that better represents your evolved business goals.',
                'order': 5,
                'is_featured': True
            },
            {
                'question': 'What file formats do you deliver?',
                'answer': 'We deliver projects in all standard formats including MP4, MOV, GIF for animations; PNG, SVG, PDF for graphics; and provide source files in Adobe Creative Suite formats. We ensure compatibility across all platforms and use cases.',
                'order': 6,
                'is_featured': True
            },
            {
                'question': 'Do you offer revisions?',
                'answer': 'Yes, we include multiple revision rounds in all our packages. Typically, we offer 2-3 rounds of revisions to ensure the final product meets your expectations. Additional revisions can be accommodated if needed.',
                'order': 7,
                'is_featured': True
            },
            {
                'question': 'How do you handle project communication?',
                'answer': 'We maintain clear communication throughout the project via email, video calls, and project management tools. You\'ll receive regular updates, preview links, and have direct access to your project manager for any questions or feedback.',
                'order': 8,
                'is_featured': True
            }
        ]

        for faq_data in faqs_data:
            faq, created = FAQ.objects.get_or_create(
                question=faq_data['question'],
                defaults=faq_data
            )
            if created:
                self.stdout.write(f'Created FAQ: {faq.question[:50]}...')
            else:
                self.stdout.write(f'FAQ already exists: {faq.question[:50]}...')

        self.stdout.write(self.style.SUCCESS('FAQs populated successfully!'))


