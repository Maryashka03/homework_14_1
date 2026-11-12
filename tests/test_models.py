import pytest

from src.models import Category, Product


@pytest.fixture(autouse=True)
def reset_counters():
    Category.category_count = 0
    Category.product_count = 0


def test_product_initialization():
    product = Product(
        "Телефон",
        "Смартфон",
        50000.0,
        10
    )

    assert product.name == "Телефон"
    assert product.description == "Смартфон"
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
    assert category.products == (
        "Телефон, 50000.0 руб. Остаток: 10 шт.\n"
    )


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


def test_add_product():
    category = Category("Электроника", "Техника", [])
    product = Product("Телефон", "Смартфон", 50000.0, 10)

    result = category.add_product(product)

    assert result is None
    assert category.products == (
        "Телефон, 50000.0 руб. Остаток: 10 шт.\n"
    )
    assert Category.product_count == 1


def test_new_product():
    product_data = {
        "name": "Телефон",
        "description": "Смартфон",
        "price": 50000.0,
        "quantity": 10
    }

    product = Product.new_product(product_data)

    assert isinstance(product, Product)
    assert product.name == "Телефон"
    assert product.price == 50000.0


def test_price_setter():
    product = Product("Телефон", "Смартфон", 50000.0, 10)

    product.price = 60000.0

    assert product.price == 60000.0


def test_invalid_price():
    product = Product("Телефон", "Смартфон", 50000.0, 10)

    product.price = 0

    assert product.price == 50000.0
