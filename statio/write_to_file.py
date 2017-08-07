import json

class WriteToFile():

    def __init__(self, resource_name, attributes, output_dir, tags):

        self.output_file = open(output_dir + resource_name + '.tf', 'w')
        self.resource_name = resource_name
        self.attributes = attributes
        self.tags = tags

    def run_write(self):
        attributes = self.attributes

        self.output_file.write('resource "datadog_monitor" "{res_name}" {{'
                               .format(res_name=self.resource_name))

        self.output_file.write("""\n\n  name = "{:>2}"
  metric_type = "{m_type}"\n 
  message = <<EOF\n{message}\nEOF\n
  query = "{query}"
\n  thresholds {{   
""".format(attributes["name"],
           message=attributes["message"],                            
           query=attributes["query"],                            
           m_type = attributes["type"]))                            

        for key in ("ok", "warning", "critical"):
            if 'thresholds.' + key in attributes:
                self.output_file.write('    {}  = "{}"\n'.format(
                                                                 key, 
                                                                 attributes \
                                                                 ['thresholds.' + key]))

        self.output_file.write("""\n  }}
\n  notify_no_data = "{not_no_d}"
  notify_audit = "{not_audit}"
\n  new_host_delay = "{delay}"
  no_data_timeframe = "{ndt}"
\n  require_new_window = "{req_nw}"
\n""".format(not_no_d=attributes["notify_no_data"],
               not_audit=attributes["notify_audit"],
               delay=attributes["new_host_delay"],
               ndt=attributes["no_data_timeframe"],
               req_nw=attributes["require_full_window"]))

        if len(self.tags) > 0:
           self.output_file.write('\n  tags = {}'.format(json.dumps(self.tags)))
        self.output_file.write('\n}')


        self.output_file.close()



