from typing import List, Set


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

    def __init__(self, groups: List[Group] = None):
        self._groups = dict()

        if groups:
            self._groups = {grp.name: grp for grp in groups}

    @property
    def groups(self) -> dict:
        return self._groups


