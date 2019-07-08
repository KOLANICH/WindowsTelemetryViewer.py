import sys
from . import *
from plumbum import cli


class App(cli.Application):
	def main(self, f=None):
		app = QApplication(sys.argv)
		w = TelemetryViewerGUI()
		w.show()
		if f is not None:
			w.loadTelemetry(f)
		else:
			w.openTelemetry()
		sys.exit(app.exec_())


if __name__ == "__main__":
	App.run()