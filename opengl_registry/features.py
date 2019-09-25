from typing import List


class FeatureDetails:
    """May represent addition or removal"""
    REQUIRE = 0
    REMOVE = 1

    def __init__(self, mode: int, profile: str = None, comment: str = None,
                 enums: List[str] = None, commands: List[str] = None):
        """Intialize feature details.
        This is simply a group of enum and command names
        a feature wants to add or remove from this the
        specific version.

        Args:
            mode (int): FeatureDetails.REQUIRE or REMOVE
        Keyword Args:
            profile (str): core, compatibility or None
            comment (str): Comment about this addition/removal
            enums: (List[str]) of enums names
            commands (List[str]): List of commands names
        """

        self._profile = profile
        self._comment = comment
        self._enums = []
        self._commands = []

    @property
    def profile(self) -> str:
        """str: the profile needed. Usually core or compatibility"""
        return self._profile

    @property
    def comment(self) -> str:
        """str: a comment"""
        return self._comment

    @property
    def enums(self) -> List[str]:
        """List[str]: list of enum names"""
        return self._enums

    @property
    def commands(self) -> List[str]:
        """List[str]: list of command names"""
        return self._commands


class Feature:

    def __init__(self, api: str = None, name: str = None, number: str = None):
        self._api = api
        self._name = name
        self._number = number
        self.require = []
        self.remove = []

    @property
    def api(self) -> str:
        """str: The api. For example: gl, gles1, gles2)"""
        return self._api

    @property
    def name(self) -> str:
        """str: version name. For example: GL_VERSION_4_1, GL_ES_VERSION_2_0"""
        return self._name

    @property
    def number(self) -> str:
        """str: version number. For example: 4.1, 2.0"""
        return self._number

    @property
    def require(self) -> List[FeatureDetails]:
        """List[FeatureDetails]: list of commands and enums required"""
        return self._require

    @property
    def remove(self) -> List[FeatureDetails]:
        """List[FeatureDetails]: list of commands and enums for removal"""
        return self._remove
