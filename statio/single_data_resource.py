import re
import json
from statio.write_to_file import WriteToFile


class SingleResource():

    def __init__(self,
                 input_data,
                 output_dir,
                 module_file):

        self.input_data = input_data
        self.module_name = ''
        self.attributes_dict = {}
        self.resource_name = ''
        self.output = output_dir
        self.data_resources = {}
        self.tags = []
        self.module_file = module_file

    def load_input_data(self):
        with open(self.input_data) as f:
            data = json.load(f)

        self.data_resources = data['modules'][0]['resources']

    def set_resource_name(self):

        resources = self.data_resources

        for i in resources.keys():
            self.module_name = i

    def form_main_data_dict(self):

        resources = self.data_resources

        self.attributes_dict = resources[self.module_name] \
                                        ['primary'] \
                                        ['attributes']
        unstripped_resource_name = self.attributes_dict["name"]                                       
        resource_name_comparison = unstripped_resource_name \
                                   .replace(">", "gt") \
                                   .replace("<", "lt")

        resource_name_strip = re.sub('[,:%\{\}.*()\-!\'#]',
                                     '',
                                     resource_name_comparison)

        rem_spaces = resource_name_strip.replace(" ", "_").replace("__", "_")

        self.resource_name = rem_spaces.lower()

        self.check_for_tags()

    def check_for_tags(self):

        if int(self.attributes_dict['tags.#']) > 1:
            self.get_tags()

    def get_tags(self):
        tag_quantity = int(self.attributes_dict['tags.#'])
        if tag_quantity > 2:
            for i in range(1, tag_quantity):
                self.tags.append(self.attributes_dict['tags.' + str(i)]) 
        else:
            self.tags = [self.attributes_dict['tags.1']]

    def run(self):
        
        self.load_input_data()
        self.set_resource_name()
        self.form_main_data_dict()
        
        write_to_file = WriteToFile(self.resource_name, 
                                    self.attributes_dict,
                                    self.output, 
                                    self.module_file,
                                    self.tags
                                    )
        write_to_file.run_write()
