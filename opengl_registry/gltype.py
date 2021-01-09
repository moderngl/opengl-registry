from typing import Optional


class GlType:
    """GL type definition"""

    def __init__(
        self, *, name: str, text: str = None, comment: str = None, requires: str = None
    ):
        """Initialize a GL type.

        Keyword Args:
            name (str): Name of the type
            text (str): text data
            comment (str): Type comment
            requires (str): References a type name
        """
        self._name = name
        self._text = text
        self._comment = comment
        self._requires = requires

    @property
    def name(self) -> str:
        """str: Name of the type"""
        return self._name

    @property
    def text(self) -> Optional[str]:
        """str: text data"""
        return self._text

    @property
    def comment(self) -> Optional[str]:
        """str: Type comment"""
        return self._comment

    @property
    def requires(self) -> Optional[str]:
        """str: References a type name"""
        return self._requires

    def __str__(self):
        return "<Type: {}>".format(self._name)

    def __repr__(self):
        return str(self)
