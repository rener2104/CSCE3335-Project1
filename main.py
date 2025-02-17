import sys
import pytest
from tam_sorter.networking import start_client, start_server
from gui import gui_main

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("Usage: python main.py [start|client|server|tests]")
        sys.exit(1)
    if sys.argv[1] == 'client':
        start_client()
    elif sys.argv[1] == 'server':
        start_server()
    elif sys.argv[1] == 'tests':
        sys.exit(pytest.main(["tests.py", "-v"]))
    elif sys.argv[1] == 'start':
        gui_main.show_overview()
    else:
        print("Usage: python main.py [start|client|server|tests]")
        sys.exit(1)
