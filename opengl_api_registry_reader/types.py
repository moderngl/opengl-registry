from typing import List, Set


class Type:
    """GL type definition"""

    def __init__(self, name: str = None, text: str = None,
                 comment: str = None, requires: str = None):
        """Initialize a GL type.

        Args:
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
    def text(self) -> str:
        """str: text data"""
        return self._text

    @property
    def comment(self) -> str:
        """str: Type comment"""
        return self._comment

    @property
    def requires(self) -> str:
        """str: References a type name"""
        return self._requires

    def __str__(self):
        return "<Type: {}>".format(self._name)

    def __repr__(self):
        return str(self)


class Group:
    """Grouped enums"""

    def __init__(self, name: str, entries: Set[str] = None):
        """Initialize a group.

        Args:
            name (str): Group name
            entries (Set[str]): 
        """
        self._name = name
        self._entries = entries

    @property
    def name(self) -> str:
        """str: group name"""
        return self._name
    
    @property
    def entires(self) -> Set[str]:
        """Set[str]: All enum entires in the group"""
        return self._entires

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return "<Group name={} entires={}>".format(self._name, self._entries)


class Registry:
    """A collection of all registry information"""

    def __init__(self, types: List[Type] = None, groups: List[Group] = None):
        """Initialize the registry.

        Args:
            types: 
            groups: 
        """
        self._groups = {grp.name: grp for grp in groups} if groups else dict()
        self._types = types

    @property
    def groups(self) -> dict:
        return self._groups

    @property
    def types(self) -> List[Type]:
        return self._types

    # TODO: Finalize this method
    def get_features(api='gl', profile='core', version='3.3', extensions=None):
        """Generate a subset of the registry"""
        raise NotImplementedError()
