WindowsTelemetryViewer.py
=========================
[wheel](https://gitlab.com/KOLANICH/WindowsTelemetryViewer.py/-/jobs/artifacts/master/raw/wheels/WindowsTelemetryViewer.py-0.CI-py3-none-any.whl?job=build)
[![PyPi Status](https://img.shields.io/pypi/v/WindowsTelemetryViewer.py.svg)](https://pypi.python.org/pypi/WindowsTelemetryViewer.py)
![GitLab Build Status](https://gitlab.com/KOLANICH/WindowsTelemetryViewer.py/badges/master/pipeline.svg)
[![TravisCI Build Status](https://travis-ci.org/KOLANICH/WindowsTelemetryViewer.py.svg?branch=master)](https://travis-ci.org/KOLANICH/WindowsTelemetryViewer.py)
[![Coveralls Coverage](https://img.shields.io/coveralls/KOLANICH/WindowsTelemetryViewer.py.svg)](https://coveralls.io/r/KOLANICH/WindowsTelemetryViewer.py)
![GitLab Coverage](https://gitlab.com/KOLANICH/WindowsTelemetryViewer.py/badges/master/coverage.svg)
[![Libraries.io Status](https://img.shields.io/librariesio/github/KOLANICH/WindowsTelemetryViewer.py.svg)](https://libraries.io/github/KOLANICH/WindowsTelemetryViewer.py)


This is a Free Open-Source Qt 5 app allowing you to view contents of Windows Diagnostics Framework files (`.rbs`) used to store the data collected by Telemetry (see the files in `%ProgramData%\Microsoft\Diagnosis`).

Uses inlined modified version of https://github.com/GrxE/PyQJsonModel , which is licensed under MIT license (see the license of that file in the file itself).


Requirements
------------
* [`Python >=3.4`](https://www.python.org/downloads/). [```Python 2``` is dead, stop raping its corpse.](https://python3statement.org/) Use `2to3` with manual postprocessing to migrate incompatible code to `3`. It shouldn't take so much time. For unit-testing you need Python 3.6+ or PyPy3 because their `dict` is ordered and deterministic.

* [```kaitaistruct```](https://github.com/kaitai-io/kaitai_struct_python_runtime)
  [![PyPi Status](https://img.shields.io/pypi/v/kaitaistruct.svg)](https://pypi.python.org/pypi/kaitaistruct)
  ![License](https://img.shields.io/github/license/kaitai-io/kaitai_struct_python_runtime.svg) as a runtime for Kaitai Struct-generated code

* [```kaitai.compress```](https://github.com/KOLANICH/kaitai_compress/tree/python_fixes/python/kaitai/compress)
  [![PyPi Status](https://img.shields.io/pypi/v/kaitai.compress.svg)](https://pypi.python.org/pypi/kaitai_compress)
  ![License](https://img.shields.io/github/license/kaitai-io/kaitai_compress.svg) contains decompressors

* `PyQt5` [![PyPi Status](https://img.shields.io/pypi/v/PyQt5.svg)](https://pypi.python.org/pypi/PyQt5)