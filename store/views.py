from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    """Homepage view with modern design"""
    context = {
        'title': 'Welcome to Our Modern Website',
        'subtitle': 'Discover amazing products and services',
        'features': [
            {
                'title': 'Modern Design',
                'description': 'Beautiful, responsive design that works on all devices',
                'icon': '🎨'
            },
            {
                'title': 'Fast Performance',
                'description': 'Optimized for speed and great user experience',
                'icon': '⚡'
            },
            {
                'title': 'Secure & Reliable',
                'description': 'Built with security and reliability in mind',
                'icon': '🔒'
            }
        ]
    }
    return render(request, 'store/home.html', context)

def about(request):
    """About page view"""
    context = {
        'title': 'About Us',
        'subtitle': 'Learn more about our company and mission'
    }
    return render(request, 'store/about.html', context)

def contact(request):
    """Contact page view"""
    context = {
        'title': 'Contact Us',
        'subtitle': 'Get in touch with our team'
    }
    return render(request, 'store/contact.html', context)
