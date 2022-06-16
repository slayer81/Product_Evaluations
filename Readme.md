### Overview

Twingate provides an [Admin API](https://docs.twingate.com/docs/api-overview) that is GraphQL-based and currently provides the ability to:

    Create, read, update, and delete all Remote networks
    Create, read, update, delete, and generate tokens for all Connectors
    Create, read, update, and delete all Resources
    Create, read, update, and delete all Groups
    Create, read, update, and delete all Service Accounts and Service Keys
    Read and update the trust status of all Devices
    Read all Users

API schema documentation is part of the GraphQL API endpoint and is always up to date. 


### Value:
Large scale networks often require dynamic and automated changes to various configuration items in Twingate. The API allows customers to fit Twingate within their own environments, processes and constraints.

In the language of your choice (**python**, **javascript**, **bash**, **etc**.) write a small script to trust all devices.

#### Extra Mile:
Turn your script into a small utility that takes 1 input parameter (like `True` or `False`) and allows you to either trust all devices or untrust all devices, depending on the value of the input parameter.
 
