from abc import ABC, abstractmethod

class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int
    ):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self) -> str:
        """Возвращает строковое представление продукта."""
        pass

class PrintMixin:
    """Миксин для вывода информации о созданном объекте."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(repr(self))

    def __repr__(self) -> str:
        parameters = ", ".join(
            f"{name}={value!r}"
            for name, value in self.__dict__.items()
        )
        return f"{self.__class__.__name__}({parameters})"

class Product(PrintMixin, BaseProduct):
    """Класс для представления товара."""

    def __str__(self) -> str:
        return (
            f"{self.name}, {self.price} руб. "
            f"Остаток: {self.quantity} шт."
        )

    def __add__(self, other: object) -> float:
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только товары.")

        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных классов.")

        return (
            self.price * self.quantity
            + other.price * other.quantity
        )

class Smartphone(Product):
    """Класс для представления смартфонов."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str
    ):
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

        super().__init__(name, description, price, quantity)

class LawnGrass(Product):
    """Класс для представления газонной травы."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: int,
        color: str
    ):
        self.country = country
        self.germination_period = germination_period
        self.color = color

        super().__init__(name, description, price, quantity)

class Category:
    """Класс для представления категории товаров."""

    category_count = 0
    product_count = 0

    def __init__(
        self,
        name: str,
        description: str,
        products: list[Product]
    ):
        self.name = name
        self.description = description
        self.__products: list[Product] = []

        Category.category_count += 1

        for product in products:
            self.add_product(product)

    @property
    def products(self) -> list[Product]:
        return self.__products

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError(
                "В категорию можно добавлять только товары."
            )

        self.__products.append(product)
        Category.product_count += 1

    def __str__(self) -> str:
        total_quantity = sum(
            product.quantity for product in self.__products
        )
        return (
            f"{self.name}, количество продуктов: "
            f"{total_quantity} шт."
        )