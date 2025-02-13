import sys
import pytest
from tam_sorter.networking import start_client, start_server

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python main.py [client|server]")
        sys.exit(1)
    if sys.argv[1] == 'client':
        start_client()
    elif sys.argv[1] == 'server':
        start_server()
    elif sys.argv[1] == 'tests':
        sys.exit(pytest.main(["tests.py", "-v"]))
    else:
        print("Usage: python main.py [client|server|tests]")
        sys.exit(1)

