from typing import List, Set


class Type:
    """GL type definition"""

    def __init__(self, name: str = None, text: str = None,
                 comment: str = None, requires: str = None):
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

    def __init__(self, name: str, entries: Set[str]):
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


class Enums:
    """Group of enums in a range reserved for a vendor"""

    def __init__(self, namespace: str = None, start: str = None, end: str = None,
                 vendor: str = None, comment: str = None):
        """Initialize an enum group.
        
        This represents a reserved enum range normally reserved for a specific vendor.

        Keyword Args:
            namespace (str): Namespace for the range (Usually always ``GL``)
            start (str): Range start as a hex string
            end (str): Range end as a hex string
            vendor (str): The vendor this enum block as assigned to (ARB, MESA, NV, AMD, QCOM etc.)
            comment (str): Enum range comment from the spec
        """
        self._namespace = namespace
        self._start = start
        self._end = end
        self._vendor = vendor
        self._comment = comment
        self._group

    @property
    def namespace(self):
        """str: Namespace for the range (Usually always ``GL``)"""
        return self._namespace

    @property
    def start(self) -> str:
        """str: Range start as a hex string"""
        return self._start

    @property
    def start_int(self) -> int:
        """str: Range start as an int"""
        return int(self._start, base=16)

    @property
    def end(self) -> str:
        """str: Range end as a hex string"""
        return self._end

    @property
    def end_int(self) -> int:
        """str: Range end as an int"""
        return int(self._end, base=16)

    @property
    def vendor(self) -> str:
        """str: The vendor this enum block as assigned to (ARB, MESA, NV, AMD, QCOM etc.)"""
        return self._vendor


    @property
    def group(self) -> Group:
        """Group: The group this enum range belongs to"""
        return self._group

    @group.setter
    def group(self, value: Group):
        self._group = value

    @property
    def comment(self) -> str:
        """str: Enum range comment from the spec"""
        return self._comment

    def __str__(self) -> str:
        return "<Enums {} - {}>".format(self._start, self._end)

    def __repr__(self) -> str:
        return str(self)


class Enum:
    """Container for GL enum info"""

    def __init__(self, name: str, value: str, comment=None):
        """Initialize an enum instance.

        Args:
            name (str): Name of the enum
            value (str): Enum value (hex number as string)
        Keyword Args:
            comment (str): Enum comment
        """
        self._name = name
        self._value = value
        self._comment = comment
        self._range = None
    
    @property
    def name(self) -> str:
        """str: Name of the enum"""
        return self._name

    @property
    def comment(self)-> str:
        """str: Enum comment"""
        return self._comment

    @property
    def value(self) -> str:
        """str: Enum value (hex number as string)"""
        return self._value

    @property
    def value_int(self) -> int:
        """int: Enum value as as int"""
        return int(self._value, base=16)

    @property
    def range(self) -> Enums:
        """Enums: The enum range this enum belongs to"""
        return self._range

    @range.setter
    def range(self, value: Enums):
        self._range = value

    def __str__(self) -> str:
        return "<Enum {} [{}]>".format(self._name, self._value)

    def __repr__(self) -> str:
        return str(self)


class Registry:
    """A collection of all registry information"""

    def __init__(self, types: List[Type] = None, groups: List[Group] = None):
        """Initialize the registry.

        Keyword Args:
            types (List[Type]): List of types
            groups (List[Group]): List of groups
        """
        self._groups = {grp.name: grp for grp in groups} if groups else dict()
        self._types = types

    @property
    def groups(self) -> dict:
        """dict: Dictionary for all groups with group name as key"""
        return self._groups

    @property
    def types(self) -> List[Type]:
        """List[Type]: List of all types"""
        return self._types

    # TODO: Finalize this method
    def get_features(api: str = 'gl', profile: str = 'core', version: str = '3.3', extensions=None):
        """Generate a subset of the registry"""
        raise NotImplementedError()
