from xml.etree import ElementTree
import requests

from opengl_api_registry_reader.types import (
    Enum,
    Enums,
    Group,
    Registry,
    Type,
)

DEFAULT_URL = 'https://raw.githubusercontent.com/KhronosGroup/OpenGL-Registry/master/xml/gl.xml'


class RegistryReader:
    """Reads ``gl.xml`` file into a ``Registry`` structure
    that can easily be inspected.
    """
    #: The registry class. Can be replaced with a custom class
    registry_cls = Registry
    group_cls = Group
    type_cls = Type
    enums_cls = Enums
    enum_cls = Enum

    def __init__(self, tree: ElementTree):
        self._tree = tree
        self._registry = self.registry_cls()
        # Parser data
        self._groups = []
        self._types = []
        self._enums = []
        self._command = []
        self._features = []
        self._extensions = []

    @classmethod
    def from_local_file(cls, path: str) -> 'RegistryReader':
        """Create a RegistryReader with a local gl.xml file"""
        tree = ElementTree.parse(path)
        return RegistryReader(tree)

    @classmethod
    def from_url(cls, url: str = None) -> 'RegistryReader':
        """Create a RegistryReader with a url to the gl.xml file"""
        response = requests.get(url or DEFAULT_URL)
        if response.status_code != requests.codes.ok:
            response.raise_for_error()

        tree = ElementTree.fromstring(response.text)
        return RegistryReader(tree)

    def read(self):
        """Reads the registry structure.

        Returns:
            Registry: The ``Registry`` instance
        """
        self.read_types()
        self.read_groups()
        self.read_enums()
        self.read_commands()
        self.read_features()
        self.read_extensions()
        return self.registry_cls(
            types=self._types,
            groups=self._groups,
        )

    def read_types(self):
        """Read all GL type definitions"""
        for type_elem in self._tree.getroot().iter('type'):
            name = None
            try:
                name = next(type_elem.iter('name')).text
            except StopIteration:
                name = type_elem.get('name')

            self._types.append(
                self.type_cls(
                    name=name,
                    text="".join(type_elem.itertext()),
                    comment=type_elem.get('comment'),
                    requires=type_elem.get('requires'),
                )
            )

    def read_groups(self):
        """Reads all group nodes"""
        for groups_elem in self._tree.getroot().iter('group'):
            self._groups.append(
                self.group_cls(
                    groups_elem.attrib['name'],
                    entries={e.attrib['name'] for e in groups_elem.iter('enum')},
                )
            )

    def read_enums(self):
        """Reads all enums"""
        for enums_elem in self._tree.getroot().iter('enums'):
            print(enums_elem)

    def read_commands(self):
        pass

    def read_features(self):
        pass

    def read_extensions(self):
        pass


if __name__ == '__main__':
    reader = RegistryReader.from_local_file('gl.xml')
    # reader = RegistryReader.from_url()
    registry = reader.read()

    # # Types
    # for tp in registry.types:
    #     print(tp)

    # # Groups
    # for _, grp in registry.groups.items():
    #     print(type(grp), grp)
