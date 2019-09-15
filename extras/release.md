
# Making a release

- Change version number
  - `docs/conf.py`
  - `setup.py`
  - `opengl_registry.__init__.py`
- Run `tox` ensuring tests pass for all enviroments
- Build the wheel : `python setup.py bdist_wheel`
- Upload the wheel to PyPI : `twine upload dist/opengl_registry-<version>-py3-none-any.whl`
- Draft a new release on github : https://github.com/moderngl/opengl-registry/releases/new
- Ensure docs are built on readthedocs
- Ensure things look correct on PyPI
