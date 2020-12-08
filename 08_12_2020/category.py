class Category:
    _id: int
    _name: str
    _sub_name: str

    def get_id(self) -> int:
        return self._id

    def set_id(self, id: int) -> None:
        self._id = id

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        self._name = name

    def get_subname(self) -> str:
        return self._sub_name

    def set_subname(self, subname: str) -> None:
        self._sub_name = subname
