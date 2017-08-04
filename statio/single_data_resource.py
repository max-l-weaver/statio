import json
import re
from statio.write_to_file import WriteToFile

class SingleResource():

    def __init__(self,
                input_data, output_data):

        self.input_data = input_data
        self.module_name = ''
        self.attributes_dict = {}
        self.resource_name = ''
        self.output = output_data
        self.data_resources = {}

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
        resource_name_strip = re.sub('[:\{\}.*]',
                                     '',
                                     unstripped_resource_name)
        rem_spaces = resource_name_strip.replace(" ", "_")
        self.resource_name = rem_spaces.lower()

    def run(self):
        
        self.load_input_data()
        self.set_resource_name()
        self.form_main_data_dict()
        
        write_to_file = WriteToFile(self.resource_name, 
                                    self.attributes_dict,
                                    self.output)
        write_to_file.run_write()

# class WriteToFile():
# 
#     def __init__(self, resource_name, attributes, output_file):
# 
#         self.output_file = open(output_file, 'w')
#         self.resource_name = resource_name
#         self.attributes = attributes
# 
#     def run_write(self):
#         attributes = self.attributes
# 
#         self.output_file.write('resource "datadog_monitor" "{res_name}" {{'
#                                .format(res_name=self.resource_name))
# 
#         self.output_file.write("""\n\n  name = "{name}"
#   metric_type = "{m_type}"\n 
#   message = <<EOF\n{message}\nEOF\n
#   query = "{query}"
# \n  thresholds {{   
# """.format(name=attributes["name"],
#                                         message=attributes["message"],
#                                         query=attributes["query"],
#                                         m_type = attributes["type"]))
# 
#         for key in ("ok", "warning", "critical"):
#             if 'thresholds.' + key in attributes:
#                 self.output_file.write('   {}  = "{}"'.format(
#                                                               key, 
#                                                               attributes \
#                                                               ['thresholds.' + key]))
# 
#         self.output_file.write("""\n  }}
# \n  notify_no_data = "{not_no_d}"
#   notify_audit = "{not_audit}"
# \n  new_host_delay = "{delay}"
#   no_data_timeframe = "{ndt}"
# \n  require_new_window = "{req_nw}"
# \n}}""".format(not_no_d=attributes["notify_no_data"],
#                not_audit=attributes["notify_audit"],
#                delay=attributes["new_host_delay"],
#                ndt=attributes["no_data_timeframe"],
#                req_nw=attributes["require_full_window"]))
# 
#         self.output_file.close()
# 
# 
