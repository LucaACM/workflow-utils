import sys
from services.get_service import get_service

def main():
    args = []
    flags = []

    for arg in sys.argv[2:]:
        if arg.startswith("-"):
            flags.append(arg.replace('-',''))
        else:
            args.append(arg)

    serviceArg = sys.argv[1]

    service = get_service(serviceArg)
    service.execute(args, flags)

if __name__ == "__main__":
    main()
