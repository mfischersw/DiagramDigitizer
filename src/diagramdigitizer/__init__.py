from . import ui

from . import diagramdigitizer
from . import graphscene
from . import export
from . import utils


def main():
    """Entry point for the application script"""
    print("Starting DiagramDigitizer from command line")
    diagramdigitizer.run()
