from typing import Set


class Group:
    """Grouped enums"""

    def __init__(self, name: str, entries: Set[str]):
        """Initialize a group.

        Args:
            name (str): Group name
            entries (Set[str]): A set of enums beloging to this group
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
