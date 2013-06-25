trac-ticket-chained-fields-plugin
=================================

This is a fork of the Trac TicketChainedFields plugin. The original plugin can be seen here: http://trac-hacks.org/wiki/TracTicketChainedFieldsPlugin

I have added the ability to load the json data that the plugin is powered by via the trac-admin command line tool.

Ex: trac-admin /path/to/my-trac-env load_tcf_json_file /path/to/my_data_file.json

This comes in useful when configuring a Trac instance using a configuration management system like Salt or Puppet.
