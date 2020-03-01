from typing import List

from app.models import Category, Good


def mark_categories(good: Good, categories: List[str]) -> Good:
    good.category.extend(Category.query.filter(
        Category.name.in_(categories)).all())
    return good
