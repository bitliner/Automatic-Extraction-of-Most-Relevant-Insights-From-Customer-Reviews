import argparse

parser = argparse.ArgumentParser(description='Automatic extractor of overall insights from customer reviews')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                   help='an integer for the accumulator')
parser.add_argument('--sum', dest='sum', action='store_const',
                   const=3, default=max,
                   help='sum the integers (default: find the max)')

args = parser.parse_args()
print args.sum
#print args
#print(args.accumulate(args.integers))
