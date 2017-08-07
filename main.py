#!/usr/local/bin/python3
import argparse
import os
from statio import SingleResource

TERRAFORM_ROLES_FOLDER = os.environ.get('TERRAFORM_ROLES_FOLDER')
MODULE_FILE_LOCATION = os.environ.get('MODULE_FILE_LOCATION')

parser = argparse.ArgumentParser(description='Converts tfstate files into HCL')
parser.add_argument(
    '--tfstate', help='location of your tfstate file')
parser.add_argument(
    '--output-dir', '-o', help='output directory')

args = parser.parse_args()

if args.tfstate is not None:

    tf_input_file = TERRAFORM_ROLES_FOLDER + args.tfstate
    tf_output_file = TERRAFORM_ROLES_FOLDER + args.output_dir

    statio_input = SingleResource(tf_input_file,
                                  tf_output_file,
                                  MODULE_FILE_LOCATION)
else:
    raise EnvironmentError("Issues with input file and/or output dir")


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
