#### The following changes have been made to the IBM QRadar connector in version 1.7.0:

- Added the `Get MITRE Mapping Related to an Offense` action.
- Renamed the `Get Assets Properties` action to `Get Asset Properties`.
- Renamed the following parameters:
    - `Closure Note` to `Note Text` in the `Create Note` action.
    - `Offense Closing Reason - ID` to `Closing Reason ID` in the `Close Offense` action.
    - `Source Address Ids` to `Source Address IDs` in the `Get Source IP Addresses` action.
    - `Destination Address Ids` to `Destination Address IDs` in the `Get Destination IP Addresses` action.
    - `Max Events to return` to `Max Events to Return` in the `Get Events Related to an Offense` action.
    - `Headers in json format` to `Headers in JSON Format` in the `Invoke QRadar REST API` action.
    - `value` to `Value` in the `Delete Table Element` action.
- Changed the annotations of the `Get Source IP Addresses` and `Get Destination IP Addresses` actions from `ip_details`
  to `get_source_ip` and `get_destination_ip`.
- Updated the operation categories of nine actions to better reflect what each action does.
- Removed the `API - Push Offense From QRadar` playbook, which depended on the deprecated CyberSponse application. 