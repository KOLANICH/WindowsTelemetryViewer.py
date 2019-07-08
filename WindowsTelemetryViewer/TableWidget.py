import sys
from threading import Thread
from pathlib import Path

from functools import partial

from PyQt5.QtCore import Qt, QVariant, QSize, QEvent
from PyQt5.QtWidgets import QWidget, QTableWidget, QCheckBox, QFileDialog, QMessageBox, QBoxLayout, QSizePolicy, QLabel, QProgressBar
from PyQt5.QtGui import QWindow, QIcon


class TableWidget(QWidget):
	@property
	def columns(self):
		return self._columns

	@columns.setter
	def columns(self, columns):
		self._columns = columns
		self.table.setHorizontalHeaderLabels(columns)
		self.table.resizeColumnsToContents()

	def __init__(self, columns, parent=None, callback=None):
		super().__init__(parent)
		self.callback = callback
		self.table = QTableWidget(0, len(columns), self)
		self.columns = columns
		self.table.setMinimumSize(400, 300)
		self.table.setShowGrid(True)

		self.hh = self.table.horizontalHeader()
		self.hh.setStretchLastSection(False)

		self.vh = self.table.verticalHeader()

		layout = QBoxLayout(QBoxLayout.LeftToRight | QBoxLayout.TopToBottom)
		layout.addWidget(self.table)
		self.setLayout(layout)
		# self.setSizePolicy(QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum, QSizePolicy.DefaultType))

		self.callback = callback
		if self.callback:
			# self.table.cellEntered.connect(self.enterProcessor)
			# self.vh.activated.connect(self.enterProcessor)
			# self.vh.selected.connect(self.enterProcessor)
			#self.table.clicked.connect(self.enterProcessor)
			self.table.itemSelectionChanged.connect(self.enterProcessor)

	def removeRow(self, rowNo):
		for i in range(len(self.systemColumnsDefs)):
			try:
				self.table.cellWidget(rowNo, i).disconnect()
			except Exception as ex:
				print("DAMN!", ex)
			self.table.removeCellWidget(rowNo, i)
		self.table.removeRow(rowNo)

	def appendRow(self, i, row, isN=False):
		newRowNo = i + 1
		self.table.insertRow(newRowNo)

		for j, cell in enumerate(row):
			w = QLabel()
			w.setText(str(cell))
			self.table.setCellWidget(newRowNo, j, w)

	def clear(self):
		self.table.clearSelection()
		# self.table.disconnect()
		self.table.clearContents()
		self.table.setRowCount(0)

	def enterProcessor(self):
		#rowNo = idx.row()
		rowNo = self.table.currentIndex().row()
		self.callback(self, rowNo)