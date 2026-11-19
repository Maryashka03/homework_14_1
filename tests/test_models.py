import pytest

from src.models import Category, Product


@pytest.fixture(autouse=True)
def reset_counters():
    Category.category_count = 0
    Category.product_count = 0


def test_product_initialization():
    product = Product(
        "Телефон",
        "Современный смартфон",
        50000.0,
        10
    )

    assert product.name == "Телефон"
    assert product.description == "Современный смартфон"
    assert product.price == 50000.0
    assert product.quantity == 10


def test_category_initialization():
    product = Product("Телефон", "Смартфон", 50000.0, 10)

    category = Category(
        "Электроника",
        "Электронные устройства",
        [product]
    )

    assert category.name == "Электроника"
    assert category.description == "Электронные устройства"
    assert category.products == [product]


def test_category_count():
    product = Product("Телефон", "Смартфон", 50000.0, 10)

    Category("Электроника", "Устройства", [product])
    Category("Одежда", "Одежда и обувь", [])

    assert Category.category_count == 2


def test_product_count():
    product1 = Product("Телефон", "Смартфон", 50000.0, 10)
    product2 = Product("Ноутбук", "Компьютер", 80000.0, 5)
    product3 = Product("Куртка", "Зимняя куртка", 7000.0, 3)

    Category("Электроника", "Техника", [product1, product2])
    Category("Одежда", "Вещи", [product3])

    assert Category.product_count == 3


def test_product_str():
    product = Product("Телефон", "Смартфон", 100.0, 10)

    assert str(product) == "Телефон, 100.0 руб. Остаток: 10 шт."


def test_category_str():
    product1 = Product("Телефон", "Смартфон", 100.0, 10)
    product2 = Product("Ноутбук", "Компьютер", 200.0, 5)

    category = Category("Электроника", "Техника", [product1, product2])

    assert str(category) == "Электроника, количество продуктов: 15 шт."


def test_product_add():
    product1 = Product("Телефон", "Смартфон", 100.0, 10)
    product2 = Product("Ноутбук", "Компьютер", 200.0, 2)

    assert product1 + product2 == 1400.0


def test_product_add_invalid_type():
    product = Product("Телефон", "Смартфон", 100.0, 10)

    with pytest.raises(TypeError):
        product + 100
