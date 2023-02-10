import sys
import shlex

def  main():
    cmdline = " ".join(map(shlex.quote, sys.argv[1:]))
    for thing in sys.argv:
        args = str(sys.argv[1:])
        args = args.replace("[","")
        args = args.replace("]","")
        args = args.replace(",","")
        args = args.replace("'","")
        args = args.swapcase()
    print(args[::-1])
main()