# Pixel Box Studio - Django Backend

A comprehensive Django REST API backend for the Pixel Box Studio Animation & Digital Marketing Agency website.

## Features

- **Complete Content Management**: All website content is dynamic and manageable through Django Admin
- **RESTful APIs**: Full CRUD operations for all content types
- **Nested Relationships**: Services organized by categories with nested serialization
- **Custom Endpoints**: Specialized endpoints for featured content and current configurations
- **Contact Form Handling**: Automated contact form submission processing
- **Media Support**: URL-based media handling for images and videos
- **Admin Interface**: User-friendly Django Admin with organized fieldsets

## Models

### Core Content Models
- **Navigation**: Logo and menu configuration
- **Hero**: Main hero section content
- **ServiceCategory**: Service categories (Animation, Marketing, etc.)
- **ServiceItem**: Individual services with features
- **Feature**: Features section items
- **Stat**: Statistics/numbers display
- **Testimonial**: Customer testimonials
- **TeamMember**: Team member profiles
- **PortfolioProject**: Portfolio projects with media
- **AboutContent**: About section content
- **ContactInfo**: Contact information
- **ContactFormSubmission**: Contact form submissions

## API Endpoints

### Base URL: `/api/`

#### Navigation
- `GET /api/navigation/` - List all navigation configs
- `GET /api/navigation/current/` - Get current navigation

#### Hero
- `GET /api/hero/` - List all hero content
- `GET /api/hero/current/` - Get current hero content

#### Services
- `GET /api/service-categories/` - List service categories
- `GET /api/service-categories/{id}/services/` - Get services for a category
- `GET /api/services/` - List all services
- `GET /api/services/featured/` - Get featured services only

#### Features
- `GET /api/features/` - List all features

#### Statistics
- `GET /api/stats/` - List all statistics

#### Testimonials
- `GET /api/testimonials/` - List all testimonials
- `GET /api/testimonials/featured/` - Get featured testimonials only

#### Team
- `GET /api/team/` - List all team members
- `GET /api/team/featured/` - Get featured team members only

#### Portfolio
- `GET /api/portfolio/` - List all portfolio projects
- `GET /api/portfolio/featured/` - Get featured projects only

#### About
- `GET /api/about/` - List all about content
- `GET /api/about/current/` - Get current about content

#### Contact
- `GET /api/contact-info/` - List contact information
- `GET /api/contact-info/current/` - Get current contact info
- `POST /api/contact-form/` - Submit contact form
- `GET /api/contact-form/unread/` - Get unread submissions
- `PATCH /api/contact-form/{id}/mark_read/` - Mark submission as read

## Installation

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

3. **Create Superuser**
   ```bash
   python manage.py createsuperuser
   ```

4. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

## Admin Access

- **URL**: `http://localhost:8000/admin/`
- **Username**: `admin`
- **Password**: `admin123`

## Frontend Integration

The Next.js frontend can fetch all content dynamically using these APIs:

```javascript
// Example: Fetch hero content
const heroResponse = await fetch('http://localhost:8000/api/hero/current/');
const heroData = await heroResponse.json();

// Example: Fetch featured services
const servicesResponse = await fetch('http://localhost:8000/api/services/featured/');
const servicesData = await servicesResponse.json();

// Example: Submit contact form
const contactResponse = await fetch('http://localhost:8000/api/contact-form/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    name: 'John Doe',
    email: 'john@example.com',
    message: 'Hello, I would like to discuss a project.'
  })
});
```

## Content Management

All website content can be managed through the Django Admin interface:

1. **Navigation**: Configure logo and menu links
2. **Hero Section**: Set main title, subtitle, and call-to-action
3. **Services**: Organize services by categories with features
4. **Features**: Manage feature highlights
5. **Statistics**: Set company statistics/numbers
6. **Testimonials**: Add customer reviews with ratings
7. **Team**: Manage team member profiles
8. **Portfolio**: Showcase projects with media
9. **About**: Company story, vision, and mission
10. **Contact**: Contact information and business hours

## Development Notes

- **Media Handling**: Uses URL fields for images/videos (can be extended to use FileField for local storage)
- **JSON Fields**: Used for flexible data like menu links, features, tags, and social links
- **Ordering**: Most models include order fields for custom display ordering
- **Featured Content**: Boolean fields to highlight important content
- **CORS**: Configured for frontend integration
- **Pagination**: Default pagination of 20 items per page

## Production Considerations

- Update `SECRET_KEY` in production
- Set `DEBUG = False`
- Configure proper database (PostgreSQL recommended)
- Set up media file serving
- Configure CORS for production domains
- Add authentication/permissions as needed
- Set up email backend for contact form notifications






