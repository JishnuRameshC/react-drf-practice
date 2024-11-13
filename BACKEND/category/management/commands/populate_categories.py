from django.core.management.base import BaseCommand
from category.models import Category, Subcategory

categories_data = [
    {"name": "Electronics", "slug": "electronics", "is_active": True, "description": "All things electronic.", "image": None, "banner_image": None, "meta_title": "Electronics", "meta_description": "Best Electronics Store.", "subcategories": [
        {"name": "Mobile Phones", "slug": "mobile-phones", "description": "Smartphones for every need."},
        {"name": "Laptops", "slug": "laptops", "description": "Laptops for work and play."},
        {"name": "Headphones", "slug": "headphones", "description": "Quality sound at your fingertips."},
    ]},
    {"name": "Fashion", "slug": "fashion", "is_active": True, "description": "Latest fashion trends.", "image": None, "banner_image": None, "meta_title": "Fashion", "meta_description": "Stylish clothes for all.", "subcategories": [
        {"name": "Men's Clothing", "slug": "mens-clothing", "description": "Latest trends in men's clothing."},
        {"name": "Women's Clothing", "slug": "womens-clothing", "description": "Trendy clothing for women."},
        {"name": "Footwear", "slug": "footwear", "description": "Footwear for all seasons."},
    ]},
    {"name": "Home Appliances", "slug": "home-appliances", "is_active": True, "description": "Essential appliances for your home.", "image": None, "banner_image": None, "meta_title": "Home Appliances", "meta_description": "Home appliances to make life easier.", "subcategories": [
        {"name": "Refrigerators", "slug": "refrigerators", "description": "Keep your food fresh with our refrigerators."},
        {"name": "Washing Machines", "slug": "washing-machines", "description": "Convenient washing machines for your laundry."},
        {"name": "Microwaves", "slug": "microwaves", "description": "Cook and heat food with our microwave ovens."},
    ]},
    {"name": "Sports & Outdoors", "slug": "sports-outdoors", "is_active": True, "description": "Equipment and clothing for sports and outdoor activities.", "image": None, "banner_image": None, "meta_title": "Sports & Outdoors", "meta_description": "Get fit and outdoors.", "subcategories": [
        {"name": "Fitness Equipment", "slug": "fitness-equipment", "description": "Equipment for your home gym."},
        {"name": "Camping", "slug": "camping", "description": "Everything for your camping trips."},
        {"name": "Cycling", "slug": "cycling", "description": "Bikes and cycling accessories."},
    ]},
    {"name": "Beauty & Health", "slug": "beauty-health", "is_active": True, "description": "Beauty products and health essentials.", "image": None, "banner_image": None, "meta_title": "Beauty & Health", "meta_description": "Your health and beauty needs.", "subcategories": [
        {"name": "Skincare", "slug": "skincare", "description": "Moisturizers, serums, and treatments."},
        {"name": "Makeup", "slug": "makeup", "description": "Cosmetics for all beauty types."},
        {"name": "Health Supplements", "slug": "health-supplements", "description": "Vitamins and supplements to improve your health."},
    ]},
    {"name": "Toys & Games", "slug": "toys-games", "is_active": True, "description": "Fun and educational toys for kids.", "image": None, "banner_image": None, "meta_title": "Toys & Games", "meta_description": "Toys to spark imagination.", "subcategories": [
        {"name": "Action Figures", "slug": "action-figures", "description": "Collectible action figures from popular brands."},
        {"name": "Board Games", "slug": "board-games", "description": "Fun for the whole family."},
        {"name": "Building Blocks", "slug": "building-blocks", "description": "Toys to help your kids build and create."},
    ]},
    {"name": "Automotive", "slug": "automotive", "is_active": True, "description": "Car accessories, tools, and parts.", "image": None, "banner_image": None, "meta_title": "Automotive", "meta_description": "Everything for your car.", "subcategories": [
        {"name": "Car Parts", "slug": "car-parts", "description": "Parts for your car's performance and repair."},
        {"name": "Car Accessories", "slug": "car-accessories", "description": "Upgrade your car with these accessories."},
        {"name": "Motorcycle Accessories", "slug": "motorcycle-accessories", "description": "Motorcycle parts and accessories."},
    ]},
    {"name": "Books", "slug": "books", "is_active": True, "description": "A wide range of books for all ages.", "image": None, "banner_image": None, "meta_title": "Books", "meta_description": "Books to expand your knowledge.", "subcategories": [
        {"name": "Fiction", "slug": "fiction", "description": "Novels and stories from a variety of genres."},
        {"name": "Non-Fiction", "slug": "non-fiction", "description": "True stories and educational books."},
        {"name": "Children's Books", "slug": "childrens-books", "description": "Books for kids of all ages."},
    ]},
    {"name": "Food & Beverages", "slug": "food-beverages", "is_active": True, "description": "Delicious and healthy food options.", "image": None, "banner_image": None, "meta_title": "Food & Beverages", "meta_description": "Tasty food and drinks.", "subcategories": [
        {"name": "Snacks", "slug": "snacks", "description": "Chips, cookies, and other snacks."},
        {"name": "Beverages", "slug": "beverages", "description": "Drinks to refresh and hydrate."},
        {"name": "Organic", "slug": "organic", "description": "Healthy organic food and beverages."},
    ]},
    {"name": "Furniture", "slug": "furniture", "is_active": True, "description": "Furniture for every room in your home.", "image": None, "banner_image": None, "meta_title": "Furniture", "meta_description": "Furniture to fit your style.", "subcategories": [
        {"name": "Living Room Furniture", "slug": "living-room-furniture", "description": "Sofas, tables, and more."},
        {"name": "Bedroom Furniture", "slug": "bedroom-furniture", "description": "Beds, wardrobes, and nightstands."},
        {"name": "Office Furniture", "slug": "office-furniture", "description": "Desks, chairs, and filing cabinets."},
    ]},
    {"name": "Pets", "slug": "pets", "is_active": True, "description": "Everything for your pets.", "image": None, "banner_image": None, "meta_title": "Pets", "meta_description": "Food, toys, and accessories for pets.", "subcategories": [
        {"name": "Pet Food", "slug": "pet-food", "description": "Healthy food for your pets."},
        {"name": "Pet Toys", "slug": "pet-toys", "description": "Toys for dogs, cats, and other pets."},
        {"name": "Pet Accessories", "slug": "pet-accessories", "description": "Collars, leashes, and more."},
    ]},
    {"name": "Jewelry & Watches", "slug": "jewelry-watches", "is_active": True, "description": "Jewelry and watches for all occasions.", "image": None, "banner_image": None, "meta_title": "Jewelry & Watches", "meta_description": "Elegant pieces to complement your style.", "subcategories": [
        {"name": "Rings", "slug": "rings", "description": "A wide selection of rings."},
        {"name": "Necklaces", "slug": "necklaces", "description": "Beautiful necklaces for all tastes."},
        {"name": "Watches", "slug": "watches", "description": "Timepieces for every occasion."},
    ]},
    {"name": "Computers", "slug": "computers", "is_active": True, "description": "Desktop computers, components, and accessories.", "image": None, "banner_image": None, "meta_title": "Computers", "meta_description": "For work and play, the best computers.", "subcategories": [
        {"name": "Desktops", "slug": "desktops", "description": "High-performance desktop computers."},
        {"name": "Components", "slug": "components", "description": "PC parts for building or upgrading."},
        {"name": "Monitors", "slug": "monitors", "description": "Display screens for your setup."},
    ]},
    {"name": "Music", "slug": "music", "is_active": True, "description": "Instruments, equipment, and accessories.", "image": None, "banner_image": None, "meta_title": "Music", "meta_description": "For music lovers and musicians.", "subcategories": [
        {"name": "Guitars", "slug": "guitars", "description": "Electric and acoustic guitars."},
        {"name": "Pianos", "slug": "pianos", "description": "Keyboards and pianos for all levels."},
        {"name": "Sound Equipment", "slug": "sound-equipment", "description": "Speakers, mixers, and audio gear."},
    ]},
    {"name": "Garden", "slug": "garden", "is_active": True, "description": "Tools, plants, and accessories for your garden.", "image": None, "banner_image": None, "meta_title": "Garden", "meta_description": "Everything you need for a beautiful garden.", "subcategories": [
        {"name": "Gardening Tools", "slug": "gardening-tools", "description": "Tools for planting, pruning, and maintaining."},
        {"name": "Plants", "slug": "plants", "description": "Indoor and outdoor plants."},
        {"name": "Outdoor Furniture", "slug": "outdoor-furniture", "description": "Furniture for your garden or patio."},
    ]},
    {"name": "Art & Craft", "slug": "art-craft", "is_active": True, "description": "Materials for artists and crafters.", "image": None, "banner_image": None, "meta_title": "Art & Craft", "meta_description": "Supplies for creative people.", "subcategories": [
        {"name": "Painting", "slug": "painting", "description": "Brushes, paints, and canvases."},
        {"name": "Sewing", "slug": "sewing", "description": "Sewing machines and accessories."},
        {"name": "Craft Supplies", "slug": "craft-supplies", "description": "Materials for various craft projects."},
    ]}
]


class Command(BaseCommand):
    help = 'Populate categories and subcategories'

    def handle(self, *args, **kwargs):
        for category_data in categories_data:
            # Check if category already exists
            category, created = Category.objects.get_or_create(
                name=category_data['name'],
                defaults={
                    'slug': category_data['slug'],
                    'is_active': category_data['is_active'],
                    'description': category_data['description'],
                    'image': category_data['image'],
                    'banner_image': category_data['banner_image'],
                    'meta_title': category_data['meta_title'],
                    'meta_description': category_data['meta_description'],
                }
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Category "{category.name}" created successfully'))
            else:
                self.stdout.write(self.style.WARNING(f'Category "{category.name}" already exists'))

            # Create the subcategories for each category
            for subcategory_data in category_data['subcategories']:
                Subcategory.objects.create(
                    category=category,
                    name=subcategory_data['name'],
                    slug=subcategory_data['slug'],
                    description=subcategory_data['description'],
                    is_active=True,  # assuming all subcategories are active
                )

        self.stdout.write(self.style.SUCCESS('Successfully populated categories and subcategories'))
