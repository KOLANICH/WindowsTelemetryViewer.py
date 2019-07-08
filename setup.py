#!/usr/bin/env python3
from setuptools import setup

formatsPath = thisDir / "kaitai_struct_formats"
kaitaiSetuptoolsCfg = {
	"formats": {
		"windows_diagnostics_framework_rbs.py": {
			"path": "windows/windows_diagnostics_framework_rbs.ksy",
		}
	},
	"formatsRepo": {
		"git": "https://github.com/KOLANICH/kaitai_struct_formats.git",
		"refspec": "windows_diagnostics_framework_rbs",
		"localPath" : formatsPath,
		"update": True
	},
	"outputDir": thisDir / "WindowsTelemetryViewer" / "kaitai",
	"inputDir": formatsPath
}


setup(use_scm_version = True)
