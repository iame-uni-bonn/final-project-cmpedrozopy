"""All the general configuration of the project."""

from pathlib import Path

PROJECT = Path(__file__).parent.resolve()
SRC = Path(__file__).parent.parent.resolve()
ROOT = PROJECT.joinpath("..", "..").resolve()

BLD = ROOT.joinpath("bld").resolve()


DOCUMENTS = ROOT.joinpath("documents").resolve()
