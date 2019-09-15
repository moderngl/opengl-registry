import os
from unittest import TestCase
from opengl_api_registry_reader import RegistryReader


class ParserTestCase(TestCase):
    registry_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'gl.xml')

    def test_create_from_file(self):
        reader = RegistryReader.from_local_file(self.registry_path)
        reader.read()
