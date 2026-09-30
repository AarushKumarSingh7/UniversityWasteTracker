# Basic data structures used by the project.

CATEGORIES = ["Plastic", "Paper", "Food", "Metal", "Glass", "Other"]

LOCATIONS = [
    "Academic Block",
    "Hostel",
    "Canteen",
    "Library",
    "Admin Block",
    "Sports Area"
]


def create_sample_data():
    
    records = [
        {
            "date": "30-09-2026",
            "location": "Canteen",
            "category": "Food",
            "quantity": 12.5
        },
        {
            "date": "30-09-2026",
            "location": "Academic Block",
            "category": "Paper",
            "quantity": 6.0
        },
        {
            "date": "29-09-2026",
            "location": "Hostel",
            "category": "Plastic",
            "quantity": 8.5
        }
    ]
    return records
