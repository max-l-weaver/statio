#!venv/bin/python3
import argparse
import os
import re
from statio import SingleResource
from subprocess import call

TERRAFORM_ROLES_FOLDER = os.environ.get('TERRAFORM_ROLES_FOLDER')
MODULE_FILE_LOCATION = os.environ.get('MODULE_FILE_LOCATION')

parser = argparse.ArgumentParser(description='Converts tfstate files into HCL')
parser.add_argument(
    '--dir', '-d', help='output directory')

args = parser.parse_args()

if args.dir is not None:

    tf_input_file = TERRAFORM_ROLES_FOLDER + args.dir + 'terraform.tfstate'
    tf_output_file = TERRAFORM_ROLES_FOLDER + args.dir
    
    statio_input = SingleResource(tf_input_file,
                                  tf_output_file,
                                  MODULE_FILE_LOCATION)
else:
    raise EnvironmentError("Issues with input file and/or output dir")

def clean_up():
    os.unlink(tf_input_file)

statio_input.run()
clean_up()
