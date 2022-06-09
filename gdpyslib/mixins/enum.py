class StringCastMixin:
    """Mixin class implementing string casting into enums which support
    access to the value through the value attribute."""

    def __str__(self) -> str:
        return str(self.value)
