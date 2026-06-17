import sys
from src.server import run_server

def main():
    try:
        run_server()
    except KeyboardInterrupt:
        print("\n[+] LocalAI Data Gateway shut down successfully.")
        sys.exit(0)

if __name__ == "__main__":
    main()
