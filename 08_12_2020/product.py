class Product:
    _id: int
    _name: str
    _description: str
    _category: str
    _price: float
    _weight: float
    _width: float
    _height: float
    _depth: float
    _idCategory: int

    def get_id(self) -> int:
        return self._id

    def set_id(self, id: int) -> None:
        self._id = id

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        self._name = name

    def get_description(self) -> str:
        return self._description

    def set_description(self, description: str) -> None:
        self._description = description

    def get_category(self) -> str:
        return self._category

    def set_category(self, category: str) -> None:
        self._category = category

    def get_price(self) -> float:
        return self._price

    def set_price(self, price: float) -> None:
        self._price = price

    def get_idCategory(self) -> int:
        return self._idCategory

    def set_idCategory(self, idCategory: int) -> None:
        self._idCategory = idCategory

    def get_weight(self) -> float:
        return self._weight

    def set_weight(self, weight: float) -> None:
        self._weight = weight

    def get_width(self) -> float:
        return self._width

    def set_width(self, width: float) -> None:
        self._width = width

    def get_height(self) -> float:
        return self._height

    def set_height(self, height: float) -> None:
        self._height = height

    def get_depth(self) -> float:
        return self._depth

    def set_depth(self, depth: float) -> None:
        self._depth = depth
