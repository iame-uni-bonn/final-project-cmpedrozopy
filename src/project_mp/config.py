"""All the general configuration of the project."""

import sys
from pathlib import Path

SRC = Path(__file__).parent.parent / "project_mp"  # src directory
ROOT = SRC.parent.parent.resolve()

BLD = ROOT.joinpath("bld").resolve()
DOCUMENTS = ROOT.joinpath("documents").resolve()

# Add src to the system path
sys.path.append(str(SRC))
