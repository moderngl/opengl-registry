import logging
from io import StringIO
from typing import List
from xml.etree import ElementTree
import requests

# NOTE: Consider moving this to __init__ when finalized
from opengl_registry.registry import Registry
from opengl_registry.gltype import GlType
from opengl_registry.enums import Enums, Enum
from opengl_registry.group import Group
from opengl_registry.commands import Command
from opengl_registry.features import Feature
from opengl_registry.extensions import Extension

logger = logging.getLogger(__name__)

DEFAULT_URL = 'https://raw.githubusercontent.com/KhronosGroup/OpenGL-Registry/master/xml/gl.xml'


class RegistryReader:
    """Reads ``gl.xml`` file into a ``Registry`` structure
    that can easily be inspected.

    The reader instantiates data objects for every tag in the xml
    file. The created ``Registry`` is then responsible for making
    sense of the information.

    Example::

        # From a local file
        reader = RegistryReader.from_file('gl.xml')
        registry = reader.read()

        # From url. If no url paramter is passed in the last known url for this file is used.
        # Currently it resides on github in the KhronosGroup organization
        reader = RegistryReader.from_url()
        registry = reader.read()
    """
    #: The registry class. Can be replaced with a custom class
    registry_cls = Registry
    #: The Group class. Can be replaced with a custom class
    group_cls = Group
    #: The GlType class. Can be replaced with a custom class
    type_cls = GlType
    #: The Enums class. Can be replaced with a custom class
    enums_cls = Enums
    #: The Enum class. Can be replaced with a custom class
    enum_cls = Enum

    def __init__(self, tree: ElementTree):
        """Initialize the reader.

        Currently we use `xml.etree.ElementTree` for parsing the
        registry information.

        Args:
            tree (ElementTree): The `ElementTree` instance
        """
        self._tree = tree

    @classmethod
    def from_file(cls, path: str) -> 'RegistryReader':
        """Create a RegistryReader with a local gl.xml file"""
        logger.info("Reading registry file: '%s'", path)
        tree = ElementTree.parse(path)
        return cls(tree)

    @classmethod
    def from_url(cls, url: str = None) -> 'RegistryReader':
        """Create a RegistryReader with a url to the gl.xml file"""
        url = url or DEFAULT_URL
        logger.info("Reading registry file from url: '%s'", url)

        response = requests.get(url)
        if response.status_code != requests.codes.ok:
            response.raise_for_error()

        tree = ElementTree.parse(StringIO(response.text))
        return cls(tree)

    def read(self) -> Registry:
        """Reads the registry structure.

        Returns:
            Registry: The ``Registry`` instance
        """
        return self.registry_cls(
            types=self.read_types(),
            groups=self.read_groups(),
            enums=self.read_enums(),
            commands=self.read_commands(),
            features=self.read_features(),
            extensions=self.read_extensions(),
        )

    def read_types(self) -> List[GlType]:
        """Read all GL type definitions

        Returns:
            List[GlType]: list of types
        """
        types = []

        for type_elem in self._tree.getroot().iter('type'):
            name = None
            try:
                name = next(type_elem.iter('name')).text
            except StopIteration:
                name = type_elem.get('name')

            types.append(
                self.type_cls(
                    name=name,
                    text="".join(type_elem.itertext()),
                    comment=type_elem.get('comment'),
                    requires=type_elem.get('requires'),
                )
            )

        return types

    def read_groups(self) -> List[Group]:
        """Reads all group nodes.

        Returns:
            List[Group]: list of groups
        """
        groups = []

        for groups_elem in self._tree.getroot().iter('group'):
            groups.append(
                self.group_cls(
                    groups_elem.attrib['name'],
                    entries={e.attrib['name'] for e in groups_elem.iter('enum')},
                )
            )

        return groups

    def read_enums(self) -> List[Enums]:
        """Reads all enums groups.

        Returns:
            List[Enums]: list of enums groups
        """
        enums = []
        for enums_elem in self._tree.getroot().iter('enums'):
            enums_instance = self.enums_cls(
                namespace=enums_elem.get('namespace'),
                group_name=enums_elem.get('group'),
                type=enums_elem.get('type'),
                comment=enums_elem.get('comment'),
                vendor=enums_elem.get('vendor'),
                start=enums_elem.get('start'),
                end=enums_elem.get('end'),
                entries=[
                    Enum(
                        name=el.get('name'),
                        value=el.get('value'),
                        comment=el.get('comment'),
                        alias=el.get('alias'),
                    )
                    for el in enums_elem.iter('enum')
                ]
            )
            enums.append(enums_instance)

        return enums

    def read_commands(self) -> List[Command]:
        """Reads all commands.

        Returns:
            List[Command]: list of commands
        """
        commands = []
        return commands

    def read_features(self) -> List[Feature]:
        """Reads all features.

        Returns:
            List[Feature]: list of features
        """
        features = []
        return features

    def read_extensions(self) -> List[Extension]:
        """Reads all extensions.

        Returns:
            List[Extension]: list of extensions
        """
        extensions = []
        return extensions
