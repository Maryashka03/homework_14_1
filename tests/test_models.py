import pytest

from src.models import Category, Product, Smartphone, LawnGrass


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


def test_smartphone_initialization():
    phone = Smartphone(
        "iPhone",
        "Смартфон Apple",
        100000.0,
        5,
        2.5,
        "15 Pro",
        256,
        "Черный"
    )

    assert isinstance(phone, Product)
    assert phone.efficiency == 2.5
    assert phone.model == "15 Pro"
    assert phone.memory == 256
    assert phone.color == "Черный"


def test_lawn_grass_initialization():
    grass = LawnGrass(
        "Газон",
        "Газонная трава",
        1000.0,
        10,
        "Россия",
        14,
        "Зеленый"
    )

    assert isinstance(grass, Product)
    assert grass.country == "Россия"
    assert grass.germination_period == 14
    assert grass.color == "Зеленый"


def test_smartphone_add():
    phone1 = Smartphone(
        "iPhone", "Телефон", 100000.0, 2,
        2.5, "15 Pro", 256, "Черный"
    )
    phone2 = Smartphone(
        "Samsung", "Телефон", 80000.0, 3,
        3.0, "S24", 512, "Синий"
    )

    assert phone1 + phone2 == 440000.0


def test_lawn_grass_add():
    grass1 = LawnGrass(
        "Газон 1", "Трава", 100.0, 10,
        "Россия", 14, "Зеленый"
    )
    grass2 = LawnGrass(
        "Газон 2", "Трава", 200.0, 5,
        "Россия", 20, "Зеленый"
    )

    assert grass1 + grass2 == 2000.0


def test_different_products_add():
    phone = Smartphone(
        "iPhone", "Телефон", 100000.0, 2,
        2.5, "15 Pro", 256, "Черный"
    )
    grass = LawnGrass(
        "Газон", "Трава", 100.0, 10,
        "Россия", 14, "Зеленый"
    )

    with pytest.raises(TypeError):
        phone + grass


def test_category_add_product():
    category = Category("Техника", "Телефоны", [])

    phone = Smartphone(
        "iPhone", "Телефон", 100000.0, 2,
        2.5, "15 Pro", 256, "Черный"
    )

    category.add_product(phone)

    assert phone in category.products


def test_category_rejects_invalid_product():
    category = Category("Техника", "Телефоны", [])

    with pytest.raises(TypeError):
        category.add_product("Не товар")
