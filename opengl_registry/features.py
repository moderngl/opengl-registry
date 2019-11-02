from typing import List


class FeatureDetails:
    """May represent addition or removal"""
    REQUIRE = 'require'
    REMOVE = 'remove'

    def __init__(self, mode: int, profile: str = None, comment: str = None,
                 enums: List[str] = None, commands: List[str] = None, types: List[str] = None):
        """Initialize feature details.
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
            types (List[str]): List of type names
        """
        self._mode = mode
        self._profile = profile
        self._comment = comment
        self._enums = enums or []
        self._commands = commands or []
        self._types = types or []

    @property
    def mode(self):
        """FeatureDetails.REQUIRE or REMOVE"""
        return self._mode

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

    @property
    def types(self):
        """List[str]: list of types"""
        return self._types

    def __str__(self):
        return "<FeatureDetails {} profile={} enums={} commands={} types={}>".format(
            self._mode, self._profile, self._enums, self._commands, self._types,
        )

    def __repr__(self):
        return str(self)


class Feature:

    def __init__(self, api: str = None, name: str = None, number: str = None):
        self._api = api
        self._name = name
        self._number = number
        self._require = []
        self._remove = []

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

    def __str__(self):
        return "<Feature {} {} {}>".format(self._api, self._number, self._name)

    def __repr__(self):
        return str(self)
