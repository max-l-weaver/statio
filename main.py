#!/usr/local/bin/python3
import argparse
import json
import os
from statio import SingleResource, WriteToFile

TERRAFORM_ROLES_FOLDER = os.environ.get('TERRAFORM_ROLES_FOLDER')

parser = argparse.ArgumentParser(description='TODO')
parser.add_argument(
        '--tfstate', help='TODO')
parser.add_argument(
        '--output-dir', '-o', help='TODO')

args = parser.parse_args()

tf_input_file = TERRAFORM_ROLES_FOLDER + args.tfstate
tf_output_file = TERRAFORM_ROLES_FOLDER + args.output_dir

if args.tfstate is not None:
    statio_input = SingleResource(tf_input_file, 
                                  tf_output_file)
else:
    raise EnvironmentError("TODo")

def clean_up():
    delete = input('Conversion complete! \
                   \nWould you like to delete the tfstate file? ')
    if delete.lower() == 'yes':
        os.unlink(tf_input_file)
        print('Deleted')
    else:
        print('Not Deleted')

statio_input.run()
clean_up()
