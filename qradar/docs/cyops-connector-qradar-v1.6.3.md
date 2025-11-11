## About the connector
IBM QRadar is an enterprise security information and event management (SIEM) product. Fortinet FortiSOAR connector for IBM QRadar allows users to invoke QRadar API, perform Ariel Queries and operations like Get Offense,related events,update and close offenses.
<p>This document provides information about the IBM QRadar Connector, which facilitates automated interactions, with a IBM QRadar server using FortiSOAR&trade; playbooks. Add the IBM QRadar Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with IBM QRadar.</p>

### Version information

Connector Version: 1.6.3

FortiSOAR&trade; Version Tested on: 6.4.4-3164 and later

IBM QRadar Version Tested on: 

Authored By: Fortinet

Certified: Yes
## Release Notes for version 1.6.3
Following enhancements have been made to the IBM QRadar Connector in version 1.6.3:
<ul>
<li>Added a new action <code>Fetch Offenses from QRadar</code>.</li>
</ul>
## Installing the connector
<p>From FortiSOAR&trade; 5.0.0 onwards, use the <strong>Connector Store</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.<br>You can also use the following <code>yum</code> command as a root user to install connectors from an SSH session:</p>
`yum install cyops-connector-qradar`

## Prerequisites to configuring the connector
- You must have the URL of IBM QRadar server to which you will connect and perform automated operations and credentials to access that server.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the IBM QRadar server.

## Minimum Permissions Required
- N/A

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>IBM QRadar</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations&nbsp;</strong> tab enter the required configuration details:&nbsp;</p>
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Address<br></td><td>Specify the IP address of the QRadar server from where the connector gets offenses information and to which you connect and perform automated operations.<br>
<tr><td>API Token<br></td><td>Specify the API token to access the QRadar server to which you connect and perform automated operations.<br>
<tr><td>API Version<br></td><td>Specify the version of the QRadar API to be used for performing automated operations. By default, this is set to 14.0.<br>
<tr><td>Verify SSL<br></td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set as True.<br></td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function<br></th><th>Description<br></th><th>Annotation and Category<br></th></tr></thead><tbody><tr><td>Get Offenses from QRadar<br></td><td>Retrieves a list of offenses from the QRadar server based on the filter string that you have specified.<br></td><td>get_offenses <br/>Investigation<br></td></tr>
<tr><td>Make an Ariel Query to QRadar<br></td><td>Executes an Ariel query on the QRadar server. QRadar uses the Ariel Query Language (AQL) to search for offenses or events based on query parameters.<br></td><td>run_query <br/>Investigation<br></td></tr>
<tr><td>Get Offense Closing Reasons<br></td><td>Retrieves a list of closing reasons associated with all offenses from the QRadar server.<br></td><td>get_offense_closing_reasons <br/>Remediation<br></td></tr>
<tr><td>Get Offense Types<br></td><td>Retrieves a list containing IDs of all the offense types from the QRadar server.<br></td><td>get_offense_type <br/>Investigation<br></td></tr>
<tr><td>Get Offense Notes<br></td><td>Retrieves a list of notes associated with a specified offense in QRadar based on the offense ID you have specified.<br></td><td>get_notes <br/>Remediation<br></td></tr>
<tr><td>Close Offense<br></td><td>Closes an offense on the QRadar server based on the offense ID that you have specified.<br></td><td>close_offense <br/>Remediation<br></td></tr>
<tr><td>Create Note<br></td><td>Creates a note for a specified offense in QRadar based on the offense ID you have specified.<br></td><td>add_notes <br/>Remediation<br></td></tr>
<tr><td>Get Events Related to an Offense<br></td><td>Retrieves details of events associated with a QRadar offense, from the QRadar server, based on the QRadar offense ID that you have specified.<br></td><td>get_events <br/>Investigation<br></td></tr>
<tr><td>Get Source IP Addresses<br></td><td>Retrieves IP address details associated with source address IDs from the QRadar server, based on the source address IDs that you have specified<br></td><td>ip_details <br/>Investigation<br></td></tr>
<tr><td>Get Destination IP Addresses<br></td><td>Retrieves IP address details associated with the destination address IDs from the QRadar server, based on the destination address IDs that you have specified<br></td><td>ip_details <br/>Investigation<br></td></tr>
<tr><td>Invoke QRadar REST API<br></td><td>Invokes a function to Get or Post an API endpoint on the QRadar server.<br></td><td>api_call <br/>Investigation<br></td></tr>
<tr><td>Manipulate Reference Set Content<br></td><td>Adds or deletes the content that you have specified from a reference set on QRadar.<br></td><td>handle_reference_set_value <br/>Investigation<br></td></tr>
<tr><td>Get Assets Properties<br></td><td>Retrieves a detailed list of available asset properties or specific available asset properties from QRadar based on input parameters specified.<br></td><td>get_assets_properties <br/>Investigation<br></td></tr>
<tr><td>Get Assets<br></td><td>Retrieves a detailed list of all available assets or specific available assets from QRadar based on input parameters specified.<br></td><td>get_assets <br/>Investigation<br></td></tr>
<tr><td>Update Asset<br></td><td>Updates the attributes of a specific asset on the QRadar server based on the asset ID and asset properties you have specified. Note: You can retrieve the list of asset properties using the 'Get Assets Properties' operation.<br></td><td>update_asset <br/>Investigation<br></td></tr>
<tr><td>Get Cases<br></td><td>Retrieves a detailed list of all cases or specific cases from QRadar based on input parameters specified. Note: This action is supported on QRadar API version 7.0 and later.<br></td><td>get_cases <br/>Investigation<br></td></tr>
<tr><td>Create Case<br></td><td>Creates a new case on QRadar based on the case properties you have specified. Note: This action is supported on QRadar API version 7.0 and later.<br></td><td>create_case <br/>Investigation<br></td></tr>
<tr><td>Get Reference Tables<br></td><td>Retrieves a detailed list of all reference tables or specific reference tables from QRadar based on input parameters specified.<br></td><td>get_reference_tables <br/>Investigation<br></td></tr>
<tr><td>Delete or Purge Reference Table<br></td><td>Deletes a specific reference table and optionally purges its content from QRadar based on the reference table name you have specified. Note: You can retrieve names and details of reference tables using the 'Get Reference Tables' operation.<br></td><td>delete_reference_table <br/>Investigation<br></td></tr>
<tr><td>Get Table Elements<br></td><td>Retrieves the record details (elements) of a specific reference table based on the reference table name you have specified. Note: You can retrieve names and details of reference tables using the 'Get Reference Tables' operation.<br></td><td>get_table_elements <br/>Investigation<br></td></tr>
<tr><td>Add or Update Table Element<br></td><td>Adds or updates an element in the specified reference table based on the reference table name, outer key, inner key, and other input parameters you have specified.<br></td><td>add_table_element <br/>Investigation<br></td></tr>
<tr><td>Delete Table Element<br></td><td>Specify the element to be deleted from a reference table on Qradar based on the input parameters specified.<br></td><td>delete_table_element <br/>Investigation<br></td></tr>
<tr><td>Fetch Offenses from QRadar<br></td><td>Retrieves a list of offenses from the QRadar server based on the filter string and start datetime that you have specified.<br></td><td>fetch_offenses <br/>Investigation<br></td></tr>
<tr><td>Get Mitre Mapping Related To Offense<br></td><td>Retrieves the MITRE mapping details associated with a QRadar offense from the QRadar server, based on the specified Offense ID.<br></td><td>get_mitre_mapping_related_to_an_offense <br/>Investigation<br></td></tr>
</tbody></table>

### operation: Get Offenses from QRadar
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Filter String<br></td><td>Specify the filter string based on which you want to retrieve the list of offenses from QRadar. For example, assigned_to="admin".<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "credibility": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "source_address_ids": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "remote_destination_count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "local_destination_address_ids": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "assigned_to": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "local_destination_count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "source_count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "start_time": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "destination_networks": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "inactive": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "protected": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "policy_category_count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "description": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "category_count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "domain_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "relevance": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "device_count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "security_category_count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "flow_count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "event_count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "offense_source": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "magnitude": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "severity": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "username_count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "closing_user": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "follow_up": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "closing_reason_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "close_time": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "source_network": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "last_updated_time": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "categories": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "offense_type": ""
</code><code><br>}</code>

### operation: Make an Ariel Query to QRadar
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Ariel Search String<br></td><td>Specify the Ariel query that you want to run on the QRadar server.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.

### operation: Get Offense Closing Reasons
#### Input parameters
None.

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "is_deleted": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "is_reserved": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "text": ""
</code><code><br>}</code>

### operation: Get Offense Types
#### Input parameters
None.

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "property_name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "database_type": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "custom": ""
</code><code><br>}</code>

### operation: Get Offense Notes
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Offense ID<br></td><td>Specify the ID of the offense whose associated notes you want to retrieve from the QRadar server.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "note_text": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "create_time": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "username": ""
</code><code><br>}</code>

### operation: Close Offense
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Offense ID<br></td><td>Specify the ID of the offense that you want to close on the QRadar server.<br>
</td></tr><tr><td>Offense Closing Reason - ID<br></td><td>Specify the ID of the offense closing reason using which you want to close the offense on the QRadar server.<br>
</td></tr><tr><td>Closure Note<br></td><td>(Optional) Note that you want to associate with the offense that you want to close on the QRadar server.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "credibility": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "source_address_ids": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "remote_destination_count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "local_destination_address_ids": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "assigned_to": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "local_destination_count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "source_count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "start_time": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "destination_networks": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "inactive": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "protected": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "policy_category_count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "description": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "category_count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "domain_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "relevance": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "device_count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "security_category_count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "flow_count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "event_count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "offense_source": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "magnitude": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "severity": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "username_count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "closing_user": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "follow_up": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "closing_reason_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "close_time": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "source_network": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "last_updated_time": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "categories": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "offense_type": ""
</code><code><br>}</code>

### operation: Create Note
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Offense ID<br></td><td>Specify the ID of the offense for which you want to create a note on the QRadar server.<br>
</td></tr><tr><td>Closure Note<br></td><td>Specify the text of the closure note that you want to create for the specified offense on the QRadar server.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "note_text": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "create_time": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "username": ""
</code><code><br>}</code>

### operation: Get Events Related to an Offense
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>QRadar Offense ID<br></td><td>Specify the Offense ID based on which you want to retrieve events from QRadar.<br>
</td></tr><tr><td>Offense Start Time<br></td><td>Specify the number of milliseconds since the epoch from the offense was started.<br>
</td></tr><tr><td>Offense Last Update Time<br></td><td>Specify the number of milliseconds since the epoch from the offense was last modified.<br>
</td></tr><tr><td>Max Events to return<br></td><td>(Optional) Specify the maximum number of events that this operation should return.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "events": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "qid": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "category": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "sourceip": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "username": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "magnitude": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "starttime": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "eventcount": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "identityip": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "protocolid": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "sourceport": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "logsourceid": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "destinationip": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "destinationport": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ]
</code><code><br>}</code>

### operation: Get Source IP Addresses
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Source Address Ids<br></td><td>Specify the IDs of source addresses based on which you want to retrieve IP address details from the QRadar server. For example, [3,4,5].<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "source_ip": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "network": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "magnitude": ""
</code><code><br>}</code>

### operation: Get Destination IP Addresses
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Destination Address Ids<br></td><td>IDs of destination addresses based on which you want to retrieve IP address details from the QRadar server. For example, [3,4,5].<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "local_destination_ip": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "network": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "magnitude": ""
</code><code><br>}</code>

### operation: Invoke QRadar REST API
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Endpoint<br></td><td>Specifies the REST endpoint. For example, /siem/offenses.<br>
</td></tr><tr><td>Request Method<br></td><td>Select the request method. You can choose between GET, POST, or PATCH. If you select GET, then you should specify the Request Parameters parameter. In the Request parameters parameter, specify the request parameters for the specified endpoint. If you select POST, then you can specify either the Request Parameters in JSON Format or the Request Payload in JSON Format parameter. In these parameters, specify either the request parameters or the request JSON payload for the specified endpoint. If you select PATCH, then you can specify either the Request Parameters in JSON Format or the Request Payload in JSON Format parameter. In these parameters, specify either the request parameters or the request JSON payload for the specified endpoint.<br>
<strong>If you choose 'GET'</strong><ul><li>Request Parameters: Provide the request parameters for the above endpoint that you have specified</li></ul><strong>If you choose 'POST'</strong><ul><li>Provide Parameters: </li><strong>If you choose 'Request Parameters'</strong><ul><li>Request Parameters in JSON Format: Provide the request parameters for the above endpoint that you have specified</li></ul><strong>If you choose 'Request Payload'</strong><ul><li>Request Payload in JSON Format: Provide the request json payload for the above endpoint that you have specified</li></ul></ul><strong>If you choose 'PATCH'</strong><ul><li>Provide Parameters: </li><strong>If you choose 'Request Parameters'</strong><ul><li>Request Parameters in JSON Format: Provide the request parameters for the above endpoint that you have specified</li></ul><strong>If you choose 'Request Payload'</strong><ul><li>Request Payload in JSON Format: Provide the request json payload for the above endpoint that you have specified</li></ul></ul></td></tr><tr><td>Headers in json format<br></td><td>(Optional) Additional JSON formatted headers. The following headers are already added by the connector: 'Accept': 'application/JSON', 'Content-Type': 'application/JSON', 'SEC': <token>, 'Version': <api_version>,<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.

### operation: Manipulate Reference Set Content
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Request Method<br></td><td>Select the request method option of the operation that you want to perform on the specified reference set in QRadar. You can choose from following options: Retrieves Value: Specify values in the following field: Reference Set Name: Specify the name of the reference set from which to retrieve the content in QRadar. Add Value: Specify values in the following field: Reference Set Name: Specify the name of the reference set in which to add the content in QRadar. Value: Specify the value to add to the specified reference set. Delete Value: Specify values in the following field: Reference Set Name: Specify the name of the reference set from which to delete the content in QRadar. Value: Specify the value to delete from the specified reference set.<br>
<strong>If you choose 'Retrieves Value'</strong><ul><li>Reference Set Name: Specify the name of the reference set to be used for this operation based on the option you have specified in the Request Method. If you choose Add Value as the Request Method, then this operation will add the specified value to the reference set you have specified in this field. If you choose Delete Value as the Request Method, then this operation will delete the specified value from the reference set you have specified in this field. If you choose Retrieves Value as the Request Method, then this operation will retrieve the values of the reference set you have specified in this field.</li></ul><strong>If you choose 'Add Value'</strong><ul><li>Reference Set Name: Specify the name of the reference set to be used for this operation based on the option you have specified in the Request Method. If you choose Add Value as the Request Method, then this operation will add the specified value to the reference set you have specified in this field. If you choose Delete Value as the Request Method, then this operation will delete the specified value from the reference set you have specified in this field. If you choose Retrieves Value as the Request Method, then this operation will retrieve the values of the reference set you have specified in this field.</li><li>Value: Specify the value that you want to add or remove from the specified reference set. You must specify the value in this field if you have chosen Add Value or Delete Value as the Request Method.</li></ul><strong>If you choose 'Delete Value'</strong><ul><li>Reference Set Name: Specify the name of the reference set to be used for this operation based on the option you have specified in the Request Method. If you choose Add Value as the Request Method, then this operation will add the specified value to the reference set you have specified in this field. If you choose Delete Value as the Request Method, then this operation will delete the specified value from the reference set you have specified in this field. If you choose Retrieves Value as the Request Method, then this operation will retrieve the values of the reference set you have specified in this field.</li><li>Value: Specify the value that you want to add or remove from the specified reference set. You must specify the value in this field if you have chosen Add Value or Delete Value as the Request Method.</li></ul></td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

Output schema when you choose "Request Method" as "Retrieves Value":
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "data": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "first_seen": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "last_seen": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "source": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "value": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "message": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "element_type": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "timeout_type": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "number_of_elements": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "creation_time": ""
</code><code><br>}</code>

If you choose "Add Value" or "Delete Value" as the "Request Method", then the output contains the following populated JSON schema:
 <code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "message": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "element_type": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "timeout_type": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "number_of_elements": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "creation_time": ""
</code><code><br>}</code>

### operation: Get Assets Properties
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Limit<br></td><td>Specify the maximum count of asset properties to be returned by this operation in the response. Use this parameter to restrict the number of elements that are returned in the list to a specified range. The list is indexed starting at zero.<br>
</td></tr><tr><td>Filter<br></td><td>Specify the parameters to be used to filter (restrict) the list of asset properties to be returned by this operation in the response.<br>
</td></tr><tr><td>Fields<br></td><td>Specify the fields to be returned in the response. Fields that are not named are excluded. Specify subfields in brackets, and multiple fields in the same object are separated by commas.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "data_type": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "display": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "custom": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "state": ""
</code><code><br>}</code>

### operation: Get Assets
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Filter<br></td><td>Specify the parameters to be used to filter (restrict) the list of assets to be returned by this operation in the response.<br>
</td></tr><tr><td>Limit<br></td><td>Specify the maximum count of assets to be returned by this operation in the response. Use this parameter to restrict the number of elements that are returned in the list to a specified range. The list is indexed starting at zero.<br>
</td></tr><tr><td>Fields<br></td><td>Specify the fields to be returned in the response. Fields that are not named are excluded. Specify subfields in brackets, and multiple fields in the same object are separated by commas.<br>
</td></tr><tr><td>Sort<br></td><td>Specify the fields using which you want to sort the response. Specify the negative (-) sign to sort the results in descending order and the positive sign (+) to sort in ascending order.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "vulnerability_count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "interfaces": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "mac_address": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "last_seen_profiler": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "created": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "last_seen_scanner": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "first_seen_scanner": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "ip_addresses": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "last_seen_profiler": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "created": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "last_seen_scanner": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "first_seen_scanner": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "network_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "type": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "first_seen_profiler": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "value": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            ],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "first_seen_profiler": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "risk_score_sum": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "hostnames": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "users": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "domain_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "properties": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "last_reported": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "type_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "last_reported_by": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "value": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "products": ""
</code><code><br>}</code>

### operation: Update Asset
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Asset ID<br></td><td>Specify the ID of the asset whose properties you want to update on QRadar.<br>
</td></tr><tr><td>Asset Properties<br></td><td>Specify a JSON dictionary with the asset properties that you want to update in the specified asset you want to update on QRadar<br>
</td></tr><tr><td>Content Type<br></td><td>This is a system field that cannot be edited.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

The output contains a non-dictionary value.

### operation: Get Cases
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Fields<br></td><td>Specify the fields to be returned in the response. Fields that are not named are excluded. Specify subfields in brackets, and multiple fields in the same object are separated by commas.<br>
</td></tr><tr><td>Filter<br></td><td>Specify the parameters to be used to filter (restrict) the list of cases to be returned by this operation in the response.<br>
</td></tr><tr><td>Limit<br></td><td>Specify the maximum count of cases to be returned by this operation in the response. Use this parameter to restrict the number of elements that are returned in the list to a specified range. The list is indexed starting at zero.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "assigned_to": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "name": ""
</code><code><br>}</code>

### operation: Create Case
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Case Properties<br></td><td>Specify a JSON dictionary with the case properties using which you want to create the case on QRadar.<br>
</td></tr><tr><td>Content Type<br></td><td>This is a system field that cannot be edited.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "case_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "state": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "assigned_to": []
</code><code><br>}</code>

### operation: Get Reference Tables
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Filter<br></td><td>Specify the parameters to be used to filter (restrict) the list of reference tables to be returned by this operation in the response.<br>
</td></tr><tr><td>Limit<br></td><td>Specify the maximum count of reference tables to be returned by this operation in the response. Use this parameter to restrict the number of elements that are returned in the list to a specified range. The list is indexed starting at zero.<br>
</td></tr><tr><td>Fields<br></td><td>Specify the fields to be returned in the response. Fields that are not named are excluded. Specify subfields in brackets, and multiple fields in the same object are separated by commas.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "timeout_type": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "number_of_elements": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "creation_time": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "key_name_types": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "port": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "source_ip": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "timestamp": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "element_type": ""
</code><code><br>}</code>

### operation: Delete or Purge Reference Table
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Reference Table Name<br></td><td>Specify the name of the reference table that you want to delete from QRadar.<br>
</td></tr><tr><td>Purge Table<br></td><td>Select the 'true' option from the Purge Table drop-down list if you want to have the contents of the specified reference table to be purged from QRadar, i.e., in this case, the structure of the specified reference table is retained. Select the 'false' (default) option from the Purge Table drop-down list to purge the contents of the specified reference table, i.e., in this case, the specified reference table is completely removed.<br>
</td></tr><tr><td>Fields<br></td><td>(Optional) Specify the fields to be returned in the response. Fields that are not named are excluded. Specify subfields in brackets, and multiple fields in the same object are separated by commas.<br>
</td></tr><tr><td>Namespace<br></td><td>(Optional) Specify the namespace of the reference table that you want to delete from QRadar. By default, it is 'SHARED' for 'admin' users and 'TENANT' for 'tenant' users. Note: If you select true from the Purge Table drop-down list, i.e., purge_only is set to true, then the default is 'SHARED' for all users.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "created_by": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "created": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "modified": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "started": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "completed": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "message": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "status": ""
</code><code><br>}</code>

### operation: Get Table Elements
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Reference Table Name<br></td><td>Specify the name of the reference table whose record details (elements) you want to retrieve from QRadar.<br>
</td></tr><tr><td>Limit<br></td><td>(Optional) Specify the maximum count of table elements to be returned by this operation in the response. Use this parameter to restrict the number of elements that are returned in the list to a specified range. The list is indexed starting at zero.<br>
</td></tr><tr><td>Fields<br></td><td>(Optional) Specify the fields to be returned in the response. Fields that are not named are excluded. Specify subfields in brackets, and multiple fields in the same object are separated by commas.<br>
</td></tr><tr><td>Namespace<br></td><td>(Optional) Specify the namespace of the reference table whose record details (elements) you want to retrieve from QRadar. By default, it is 'SHARED' for 'admin' users and 'TENANT' for 'tenant' users. Note: If you select true from the Purge Table drop-down list, i.e., purge_only is set to true, then the default is 'SHARED' for all users.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "timeout_type": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "number_of_elements": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "data": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "outer_key": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "inner_key": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "last_seen": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "first_seen": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "source": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "value": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "creation_time": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "key_name_types": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "element_type": ""
</code><code><br>}</code>

### operation: Add or Update Table Element
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Reference Table Name<br></td><td>Specify the name of the reference table in which you want to add or update the specified element.<br>
</td></tr><tr><td>Outer Key<br></td><td>Specify the outer key in which you want to add or update the specified element.<br>
</td></tr><tr><td>Inner Key<br></td><td>Specify the inner key in which you want to add or update the specified element.<br>
</td></tr><tr><td>Value<br></td><td>Specify the value of the element that you want to add or update in the specified reference table. Note: Date values must be represented in Unix Epoch milliseconds.<br>
</td></tr><tr><td>Domain ID<br></td><td>(Optional) In the case of MSSP setups, you can specify the domain ID to be set for the 'value' you have specified in the 'Value' field. If the 'Domain ID' field is null, then the shared domain is used.<br>
</td></tr><tr><td>Element Source<br></td><td>(Optional) Specify the source of the specified element that you want to add or update in the specified table. By default, this is set to 'FortiSOAR'.<br>
</td></tr><tr><td>Fields<br></td><td>(Optional) Specify the fields to be returned in the response. Fields that are not named are excluded. Specify subfields in brackets, and multiple fields in the same object are separated by commas.<br>
</td></tr><tr><td>Namespace<br></td><td>(Optional) Specify the namespace of the reference table in which you want to add or update the specified element. By default, it is 'SHARED' for 'admin' users and 'TENANT' for 'tenant' users. Note: If you select true from the Purge Table drop-down list, i.e., purge_only is set to true, then the default is 'SHARED' for all users<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "timeout_type": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "number_of_elements": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "creation_time": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "key_name_types": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "element_type": ""
</code><code><br>}</code>

### operation: Delete Table Element
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Reference Table Name<br></td><td>Specify the name of the reference table from which you want to delete the specified element.<br>
</td></tr><tr><td>Outer Key<br></td><td>Specify the outer key from which you want to delete the specified element.<br>
</td></tr><tr><td>Inner Key<br></td><td>Specify the inner key from which you want to delete the specified element.<br>
</td></tr><tr><td>value<br></td><td>Specify the value of the element that you want to delete from the specified reference table. Note: Date values must be represented in Epoch milliseconds.<br>
</td></tr><tr><td>Domain ID<br></td><td>(Optional) In the case of MSSP setups, you can specify the domain ID to be set for the 'value' you have specified in the 'Value' field. If the 'Domain ID' field is null, then the shared domain is used.<br>
</td></tr><tr><td>Fields<br></td><td>(Optional) Specify the fields to be returned in the response. Fields that are not named are excluded. Specify subfields in brackets, and multiple fields in the same object are separated by commas.<br>
</td></tr><tr><td>Namespace<br></td><td>(Optional) Specify the namespace of the reference table from which you want to delete the specified element. By default, it is 'SHARED' for 'admin' users and 'TENANT' for 'tenant' users. Note: If you select true from the Purge Table drop-down list, i.e., purge_only is set to true, then the default is 'SHARED' for all users<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "timeout_type": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "number_of_elements": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "creation_time": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "key_name_types": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "element_type": ""
</code><code><br>}</code>

### operation: Fetch Offenses from QRadar
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Filter String<br></td><td>Specify the filter string based on which to retrieve the list of offenses from QRadar. For example, assigned_to="admin".<br>
</td></tr><tr><td>Created After<br></td><td>Select the date and time using which to filter the result set to only include items that have been created after the specified timestamp.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "rules": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "type": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "inactive": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "severity": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "domain_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "follow_up": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "magnitude": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "protected": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "relevance": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "categories": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "close_time": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "flow_count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "start_time": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "assigned_to": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "credibility": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "description": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "event_count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "log_sources": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "type_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "type_name": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "closing_user": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "device_count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "offense_type": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "source_count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "category_count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "offense_source": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "source_network": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "username_count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "closing_reason_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "last_updated_time": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "source_address_ids": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "last_persisted_time": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "destination_networks": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "first_persisted_time": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "policy_category_count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "source_address_details": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "network": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "magnitude": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "source_ip": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "local_destination_count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "security_category_count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "remote_destination_count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "destination_address_details": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "network": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "magnitude": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "local_destination_ip": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "local_destination_address_ids": []
</code><code><br>}</code>

### operation: Get Mitre Mapping Related To Offense
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>QRadar Offense ID<br></td><td>Specify the Offense ID based on which you want to retrieve mitre mapping from QRadar.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "rule_name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "override_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "has_ibm_default": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "last_updated": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "min_mitre_version": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "mapping": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "tactic_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "tactic_name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "confidence": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "user_override": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "enabled": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "ibm_default": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "techniques": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "technique_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "technique_name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "confidence": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "enabled": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            ]
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ]
</code><code><br>}</code>

## Included playbooks
The `Sample - qradar - 1.6.3` playbook collection comes bundled with the IBM QRadar connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR<sup>TM</sup> after importing the IBM QRadar connector.

- Add or Update Table Element
- Close Offense
- Create Case
- Create Note
- Delete Table Element
- Delete or Purge Reference Table
- Fetch Offenses from QRadar
- Get Assets
- Get Assets Properties
- Get Cases
- Get Destination IP Addresses
- Get Events Related to an Offense
- Get Mitre Mapping Related To Offense
- Get Offense Closing Reasons
- Get Offense Notes
- Get Offense Types
- Get Offenses from QRadar
- Get Reference Tables
- Get Source IP Addresses
- Get Table Elements
- Invoke QRadar REST API
- Make an Ariel Query to QRadar
- Manipulate Reference Set Content
- Update Asset

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection, since the sample playbook collection gets deleted during connector upgrade and delete.
## Data Ingestion Support
Use the Data Ingestion Wizard to easily ingest data into FortiSOAR&trade; by pulling events/alerts/incidents, based on the requirement.

**TODO:** provide the list of steps to configure the ingestion with the screen shots and limitations if any in this section.