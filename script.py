#!/usr/local/bin/python3

import json
from statio import SingleResource 

file_path = '/Users/maxweaver/infectious/terraform-datadog/roles/consul/terraform.tfstate'
output_file = 'test_1.tf'

with open(file_path, 'r') as f:
    data = json.load(f)

foo = SingleResource(data, output_file)

foo.run()

