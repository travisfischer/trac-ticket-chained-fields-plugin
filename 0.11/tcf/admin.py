from trac.core import Component
from trac.core import implements
from trac.core import TracError

from trac.admin import IAdminCommandProvider

from trac.util.text import printout

import simplejson

from model import TracTicketChainedFields_List

__all__ = ['ImportTicketChainedFieldsJSONFile']

class ImportTicketChainedFieldsJSONFile(Component):
    implements(IAdminCommandProvider)

    def get_admin_commands(self):
        yield ('import_tcf_json_file', 'File containing TCF json',
               'Import a json file to use for Ticket Chained Fields',
               None, self.import_tcf_json_file)

    def import_tcf_json_file(self, filename):

        json_file = open(filename)
        json_string = json_file.read()

        try:
            json_data = simplejson.loads(json_string)
        except:
            raise TracError(u"Format error, which should be JSON. Please back to last page and check the configuration.")

        printout("Added JSON Data for TCF plugin:\n%s" % json_data)


        TracTicketChainedFields_List.insert(self.env, json_string)
