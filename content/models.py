from django.db import models
from django.core.validators import URLValidator


class Navigation(models.Model):
    """Navigation configuration for the website"""
    logo_image = models.ImageField(
        upload_to='navigation/',
        blank=True,
        null=True,
        help_text="Upload logo image"
    )
    logo_url = models.URLField(
        max_length=500,
        blank=True,
        help_text="OR URL for the logo image"
    )
    menu_links = models.JSONField(
        default=list,
        help_text="JSON array of menu links with name and href"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Navigation"
        verbose_name_plural = "Navigation"

    def __str__(self):
        return "Navigation Configuration"


class Hero(models.Model):
    """Hero section content"""
    # Video fields
    hero_video = models.FileField(
        upload_to='hero/videos/',
        blank=True,
        null=True,
        help_text="Upload hero video file (Landscape/Desktop - 16:9)"
    )
    hero_video_portrait = models.FileField(
        upload_to='hero/videos/',
        blank=True,
        null=True,
        help_text="Upload portrait hero video file (Mobile Portrait - 9:16)"
    )
    video_url = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        help_text="OR URL for the landscape hero video"
    )
    video_url_portrait = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        help_text="OR URL for the portrait hero video"
    )
    
    # Image fields (alternative to video)
    hero_image = models.ImageField(
        upload_to='hero/images/',
        blank=True,
        null=True,
        help_text="Upload hero image (Landscape/Desktop - 16:9)"
    )
    hero_image_portrait = models.ImageField(
        upload_to='hero/images/',
        blank=True,
        null=True,
        help_text="Upload portrait hero image (Mobile Portrait - 9:16)"
    )
    image_url = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        help_text="OR URL for the landscape hero image"
    )
    image_url_portrait = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        help_text="OR URL for the portrait hero image"
    )
    
    # Logo fields
    logo_upload = models.ImageField(
        upload_to='hero/logos/',
        blank=True,
        null=True,
        help_text="Upload company logo"
    )
    logo_url = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        help_text="OR URL for the company logo"
    )
    
    title = models.CharField(
        max_length=200,
        help_text="Main hero title"
    )
    subtitle = models.TextField(
        help_text="Hero subtitle/description"
    )
    cta_text = models.CharField(
        max_length=100,
        help_text="Call-to-action button text"
    )
    cta_link = models.URLField(
        max_length=500,
        help_text="Call-to-action button link"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Hero Section"
        verbose_name_plural = "Hero Section"

    def __str__(self):
        return self.title


class ServiceCategory(models.Model):
    """Service categories for organizing services"""
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="Category name (e.g., Animation, Marketing)"
    )
    description = models.TextField(
        help_text="Category description"
    )
    icon = models.CharField(
        max_length=50,
        blank=True,
        help_text="Icon name or URL for the category"
    )
    order = models.PositiveIntegerField(
        default=0,
        help_text="Display order"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Service Category"
        verbose_name_plural = "Service Categories"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class ServiceItem(models.Model):
    """Individual service items"""
    category = models.ForeignKey(
        ServiceCategory,
        on_delete=models.CASCADE,
        related_name='services'
    )
    title = models.CharField(
        max_length=200,
        help_text="Service title"
    )
    description = models.TextField(
        help_text="Service description"
    )
    features = models.JSONField(
        default=list,
        help_text="JSON array of service features"
    )
    icon = models.CharField(
        max_length=50,
        blank=True,
        help_text="Icon name or URL for the service"
    )
    order = models.PositiveIntegerField(
        default=0,
        help_text="Display order within category"
    )
    is_featured = models.BooleanField(
        default=False,
        help_text="Whether this service should be featured"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Service Item"
        verbose_name_plural = "Service Items"
        ordering = ['category', 'order', 'title']

    def __str__(self):
        return f"{self.category.name} - {self.title}"


class Feature(models.Model):
    """Features section items"""
    title = models.CharField(
        max_length=200,
        help_text="Feature title"
    )
    description = models.TextField(
        help_text="Feature description"
    )
    icon = models.CharField(
        max_length=50,
        help_text="Icon name or URL"
    )
    order = models.PositiveIntegerField(
        default=0,
        help_text="Display order"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Feature"
        verbose_name_plural = "Features"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title


class Stat(models.Model):
    """Statistics/numbers section"""
    title = models.CharField(
        max_length=200,
        help_text="Stat title (e.g., 'Projects Completed')"
    )
    number = models.PositiveIntegerField(
        help_text="The statistic number"
    )
    suffix = models.CharField(
        max_length=10,
        blank=True,
        help_text="Suffix for the number (e.g., '+', '%', 'K')"
    )
    order = models.PositiveIntegerField(
        default=0,
        help_text="Display order"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Statistic"
        verbose_name_plural = "Statistics"
        ordering = ['order', 'title']

    def __str__(self):
        return f"{self.title}: {self.number}{self.suffix}"


class Testimonial(models.Model):
    """Customer testimonials"""
    name = models.CharField(
        max_length=100,
        help_text="Customer name"
    )
    role = models.CharField(
        max_length=100,
        help_text="Customer role/position"
    )
    company = models.CharField(
        max_length=100,
        blank=True,
        help_text="Customer company"
    )
    review = models.TextField(
        help_text="Testimonial text"
    )
    photo_image = models.ImageField(
        upload_to='testimonials/photos/',
        blank=True,
        null=True,
        help_text="Upload customer photo"
    )
    photo = models.URLField(
        max_length=500,
        blank=True,
        help_text="OR Customer photo URL"
    )
    rating = models.PositiveIntegerField(
        default=5,
        choices=[(i, i) for i in range(1, 6)],
        help_text="Rating out of 5"
    )
    order = models.PositiveIntegerField(
        default=0,
        help_text="Display order"
    )
    is_featured = models.BooleanField(
        default=False,
        help_text="Whether this testimonial should be featured"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} - {self.company or self.role}"


class TeamMember(models.Model):
    """Team members"""
    name = models.CharField(
        max_length=100,
        help_text="Team member name"
    )
    role = models.CharField(
        max_length=100,
        help_text="Team member role/position"
    )
    bio = models.TextField(
        help_text="Team member bio"
    )
    image_upload = models.ImageField(
        upload_to='team/photos/',
        blank=True,
        null=True,
        help_text="Upload team member photo"
    )
    image = models.URLField(
        max_length=500,
        blank=True,
        help_text="OR Team member photo URL"
    )
    social_links = models.JSONField(
        default=dict,
        help_text="JSON object with social media links"
    )
    order = models.PositiveIntegerField(
        default=0,
        help_text="Display order"
    )
    is_featured = models.BooleanField(
        default=False,
        help_text="Whether this team member should be featured"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} - {self.role}"


class PortfolioProject(models.Model):
    """Portfolio projects"""
    title = models.CharField(
        max_length=200,
        help_text="Project title"
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        blank=True,
        null=True,
        help_text="URL-friendly version of title (auto-generated)"
    )
    description = models.TextField(
        help_text="Project description"
    )
    detailed_description = models.TextField(
        blank=True,
        help_text="Detailed project description for detail page"
    )
    challenge = models.TextField(
        blank=True,
        help_text="The challenge or problem this project solved"
    )
    solution = models.TextField(
        blank=True,
        help_text="How you solved the challenge"
    )
    results = models.TextField(
        blank=True,
        help_text="Project results and outcomes"
    )
    media_upload = models.FileField(
        upload_to='portfolio/media/',
        blank=True,
        null=True,
        help_text="Upload project media (image/video)"
    )
    media_url = models.URLField(
        max_length=500,
        blank=True,
        help_text="OR Project media URL (image or video)"
    )
    media_type = models.CharField(
        max_length=20,
        choices=[
            ('image', 'Image'),
            ('video', 'Video'),
            ('gif', 'GIF'),
        ],
        default='image',
        help_text="Type of media"
    )
    tags = models.JSONField(
        default=list,
        help_text="JSON array of project tags"
    )
    service = models.ForeignKey(
        ServiceItem,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='portfolio_projects',
        help_text="Related service for this portfolio project"
    )
    client = models.CharField(
        max_length=100,
        blank=True,
        help_text="Client name"
    )
    project_url = models.URLField(
        max_length=500,
        blank=True,
        help_text="Project URL or demo link"
    )
    order = models.PositiveIntegerField(
        default=0,
        help_text="Display order"
    )
    is_featured = models.BooleanField(
        default=False,
        help_text="Whether this project should be featured"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Portfolio Project"
        verbose_name_plural = "Portfolio Projects"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while PortfolioProject.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


class PortfolioGalleryImage(models.Model):
    """Gallery images for portfolio projects"""
    portfolio_project = models.ForeignKey(
        PortfolioProject,
        on_delete=models.CASCADE,
        related_name='gallery_images',
        help_text="Related portfolio project"
    )
    image_upload = models.ImageField(
        upload_to='portfolio/gallery/',
        blank=True,
        null=True,
        help_text="Upload gallery image"
    )
    image_url = models.URLField(
        max_length=500,
        blank=True,
        help_text="OR Gallery image URL"
    )
    caption = models.CharField(
        max_length=200,
        blank=True,
        help_text="Image caption (optional)"
    )
    order = models.PositiveIntegerField(
        default=0,
        help_text="Display order"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Portfolio Gallery Image"
        verbose_name_plural = "Portfolio Gallery Images"
        ordering = ['order', 'created_at']

    def __str__(self):
        return f"{self.portfolio_project.title} - Image {self.order}"


class AboutContent(models.Model):
    """About section content"""
    title = models.CharField(
        max_length=200,
        help_text="About section title"
    )
    description = models.TextField(
        help_text="About description"
    )
    story = models.TextField(
        help_text="Company story"
    )
    vision = models.TextField(
        help_text="Company vision"
    )
    mission = models.TextField(
        blank=True,
        help_text="Company mission"
    )
    values = models.JSONField(
        default=list,
        help_text="JSON array of company values"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "About Content"
        verbose_name_plural = "About Content"

    def __str__(self):
        return self.title


class ContactInfo(models.Model):
    """Contact information"""
    phone = models.CharField(
        max_length=20,
        help_text="Phone number"
    )
    email = models.EmailField(
        help_text="Email address"
    )
    address = models.TextField(
        help_text="Physical address"
    )
    social_links = models.JSONField(
        default=dict,
        help_text="JSON object with social media links"
    )
    business_hours = models.JSONField(
        default=dict,
        help_text="JSON object with business hours"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Contact Information"
        verbose_name_plural = "Contact Information"

    def __str__(self):
        return f"Contact Info - {self.email}"


class ContactFormSubmission(models.Model):
    """Contact form submissions"""
    name = models.CharField(
        max_length=100,
        help_text="Contact person name"
    )
    email = models.EmailField(
        help_text="Contact email"
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        help_text="Contact phone number"
    )
    company = models.CharField(
        max_length=100,
        blank=True,
        help_text="Company name"
    )
    subject = models.CharField(
        max_length=200,
        blank=True,
        help_text="Message subject"
    )
    message = models.TextField(
        help_text="Message content"
    )
    timestamp = models.DateTimeField(
        auto_now_add=True,
        help_text="Submission timestamp"
    )
    is_read = models.BooleanField(
        default=False,
        help_text="Whether the message has been read"
    )

    class Meta:
        verbose_name = "Contact Form Submission"
        verbose_name_plural = "Contact Form Submissions"
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.name} - {self.email} ({self.timestamp.strftime('%Y-%m-%d')})"


class FAQ(models.Model):
    """Frequently Asked Questions"""
    question = models.CharField(
        max_length=500,
        help_text="FAQ question"
    )
    answer = models.TextField(
        help_text="FAQ answer"
    )
    order = models.PositiveIntegerField(
        default=0,
        help_text="Display order"
    )
    is_featured = models.BooleanField(
        default=False,
        help_text="Whether this FAQ should be featured"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"
        ordering = ['order', 'question']

    def __str__(self):
        return self.question
