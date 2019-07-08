# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO
import kaitai.compress


if parse_version(ks_version) < parse_version("0.7"):
	raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % ks_version)


class WindowsDiagnosticsFrameworkRbs(KaitaiStruct):
	"""The file format used by Windows Diagnostics Framework (including so called telemetery).
	If you have Windows with "telemetry" (Windows 10 and Windows 7,8,8.1 with the updates containing telemetry), you can find these files in %ProgramData%\Microsoft\Diagnosis directory.
	
	.. seealso::
	   Source - https://github.com/bluec0re/windows-rbs-parser
	"""

	def __init__(self, _io, _parent=None, _root=None):
		self._io = _io
		self._parent = _parent
		self._root = _root if _root else self
		self._read()

	def _read(self):
		self.header = self._root.Header(self._io, self, self._root)
		self._raw_reserved_size = self._io.read_bytes(self.header.reserved_space_size)
		_io__raw_reserved_size = KaitaiStream(BytesIO(self._raw_reserved_size))
		self.reserved_size = self._root.ReservedSpace(_io__raw_reserved_size, self, self._root)

	class ReservedSpace(KaitaiStruct):
		def __init__(self, _io, _parent=None, _root=None):
			self._io = _io
			self._parent = _parent
			self._root = _root if _root else self
			self._read()

		def _read(self):
			self._raw_items = self._io.read_bytes(self._root.header.items_collection_size)
			_io__raw_items = KaitaiStream(BytesIO(self._raw_items))
			self.items = self._root.ReservedSpace.ItemsCollection(_io__raw_items, self, self._root)

		class ItemsCollection(KaitaiStruct):
			def __init__(self, _io, _parent=None, _root=None):
				self._io = _io
				self._parent = _parent
				self._root = _root if _root else self
				self._read()

			def _read(self):
				self.items = [None] * (self._root.header.elements_count)
				for i in range(self._root.header.elements_count):
					self.items[i] = self._root.Item(self._io, self, self._root)

	class Header(KaitaiStruct):
		def __init__(self, _io, _parent=None, _root=None):
			self._io = _io
			self._parent = _parent
			self._root = _root if _root else self
			self._read()

		def _read(self):
			self.signature = self._io.ensure_fixed_contents(b"\x55\x54\x43\x52\x42\x45\x53")
			self.version_str = (self._io.read_bytes(1)).decode(u"utf-8")
			self.unkn0 = self._io.read_bytes(8)
			self.items_collection_size = self._io.read_u4le()
			self.items_collection_size_again = self._io.read_u4le()
			self.unkn1 = self._io.read_u4le()
			self.reserved_space_size = self._io.read_u4le()
			if self.version >= 5:
				self.unkn2 = self._io.read_bytes(4)

			self.elements_count = self._io.read_u4le()
			if self.version < 5:
				self.elements_count_again = self._io.read_u4le()

			self.unkn3 = self._io.read_u2le()
			if self.version >= 5:
				self.unkn4 = self._io.read_bytes(5)

		@property
		def version(self):
			if hasattr(self, "_m_version"):
				return self._m_version if hasattr(self, "_m_version") else None

			self._m_version = int(self.version_str)
			return self._m_version if hasattr(self, "_m_version") else None

	class Item(KaitaiStruct):
		def __init__(self, _io, _parent=None, _root=None):
			self._io = _io
			self._parent = _parent
			self._root = _root if _root else self
			self._read()

		def _read(self):
			self.header = self._root.Item.Header(self._io, self, self._root)
			self._raw__raw_data = self._io.read_bytes(self.header.size)
			_process = kaitai.compress.Zlib(-1, 15)
			self._raw_data = _process.decode(self._raw__raw_data)
			_io__raw_data = KaitaiStream(BytesIO(self._raw_data))
			self.data = self._root.Item.WrappedString(_io__raw_data, self, self._root)

		class WrappedString(KaitaiStruct):
			def __init__(self, _io, _parent=None, _root=None):
				self._io = _io
				self._parent = _parent
				self._root = _root if _root else self
				self._read()

			def _read(self):
				self.value = (self._io.read_bytes_full()).decode(u"utf-8")

		class Header(KaitaiStruct):
			def __init__(self, _io, _parent=None, _root=None):
				self._io = _io
				self._parent = _parent
				self._root = _root if _root else self
				self._read()

			def _read(self):
				self.unkn0 = self._io.read_bytes(4)
				self.index = self._io.read_u4le()
				self.unkn1 = self._io.read_bytes(4)
				if self._root.header.version >= 5:
					self.unkn2 = self._io.read_bytes(8)

				self.size = self._io.read_u4le()
				self.unkn3 = self._io.read_u4le()
				_on = self._root.header.version >= 5
				if _on == False:
					self.unkn4 = self._io.read_u2le()
				elif _on == True:
					self.unkn4 = self._io.read_u1()