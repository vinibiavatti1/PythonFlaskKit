"""
Services are used to process business rules
"""
from project.repositories import example_repository


def some_business_rule(p1, p2, p3):
    """
    Process data before insert (example)
    """
    # Process business rules before insert...
    example_repository.insert(p1, p2, p3)
