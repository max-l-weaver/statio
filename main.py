#!/usr/local/bin/python3
import argparse
import json
from statio import SingleResource, WriteToFile

parser = argparse.ArgumentParser(description='TODO')
parser.add_argument(
        '--tfstate', help='TODO')
parser.add_argument(
        '--output', help='TODO')

args = parser.parse_args()

if args.tfstate is not None:
    statio_input = SingleResource(args.tfstate, args.output)
else:
    raise EnvironmentError("TODo")

statio_input.run()


