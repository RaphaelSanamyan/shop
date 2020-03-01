from typing import List

from app.models import Category, Good


def mark_categories(good: Good, categories: List[str]) -> Good:
    good_categories = Category.query.filter(Category.name.in_(categories)).all()
    for category in good_categories:
        good.category.append(category)
    return good
