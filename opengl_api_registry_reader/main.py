from xml.etree import ElementTree
import requests

from opengl_api_registry_reader.types import (
    Group,
    Registry,
)

DEFAULT_URL = 'https://raw.githubusercontent.com/KhronosGroup/OpenGL-Registry/master/xml/gl.xml'


class RegistryReader:
    """Reads ``gl.xml`` file into a ``Registry`` structure
    that can easily be inspected.
    """
    registry_cls = Registry

    def __init__(self, tree: ElementTree):
        self._tree = tree
        self._registry = self.registry_cls()
        # Parser data
        self._groups = []

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
        self.read_groups()
        self.read_enums()
        self.read_commands()
        self.read_features()
        self.read_extensions()
        return self.registry_cls(
            groups=self._groups,
        )

    def read_groups(self):
        """Reads all enum group info"""
        for groups_elem in self._tree.getroot().iter('group'):
            self._groups.append(
                Group(
                    groups_elem.attrib['name'],
                    entries={e.attrib['name'] for e in groups_elem.iter('enum')},
                )
            )

    def read_enums(self):
        pass

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
    for _, grp in registry.groups.items():
        print(type(grp), grp)
