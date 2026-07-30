from pathlib import Path
import sys


CORE_PATH = Path(__file__).resolve().parent / "core"
if CORE_PATH.exists():
    sys.path.insert(0, str(CORE_PATH))

from avto_vinchick_tg.gui import main


if __name__ == "__main__":
    main()
