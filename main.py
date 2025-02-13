import sys
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
        #TODO: Run tests
        pass
    else:
        print("Usage: python main.py [client|server]")
        sys.exit(1)

