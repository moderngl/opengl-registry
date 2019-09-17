from typing import List
import logging

from opengl_registry.gltype import GlType
from opengl_registry.group import Group
from opengl_registry.enums import Enums
from opengl_registry.commands import Command
from opengl_registry.features import Feature
from opengl_registry.extensions import Extension

logger = logging.getLogger(__name__)


class Registry:
    """A collection of all registry information"""

    def __init__(self,
                 *,
                 types: List[GlType],
                 groups: List[Group],
                 enums: List[Enums],
                 commands: List[Command],
                 features: List[Feature],
                 extensions:  List[Extension]):
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
    def types(self) -> List[GlType]:
        """List[Type]: List of all types"""
        return self._types

    # TODO: Finalize this method
    def get_features(api: str = 'gl', profile: str = 'core', version: str = '3.3', extensions=None):
        """Generate a subset of the registry"""
        raise NotImplementedError()
