from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
import sys, os

###############################################################################
# Setup client
apiEndpoint = 'https://' + os.getenv('twingate_domain', None) + ''.twingate.com/api/graphql/'
headers = {'X-API-KEY': os.getenv('twingate_BT', None)}

_transport = RequestsHTTPTransport(
    url=apiEndpoint,
    headers=headers,
    use_json=True,
)

client = Client(
    transport=_transport,
    fetch_schema_from_transport=True,
)

###############################################################################
# Get value from ARGV
trustStatus = sys.argv[1]
if trustStatus.lower() == "trust":
    trustStatus = 'true'
elif trustStatus.lower() == "untrust":
    trustStatus = 'false'
else:
    print("\n\n\nSomeone isn't tall enough for this ride, eh???")
    print("Security will help you exit the amusement park via the nearest gate. Bye.")
    exit()
print("\n\n\nChanging the Trust status of all devices to: {}\n\n".format(trustStatus))

###############################################################################
# Get client ids
getDeviceIDs_query = gql("""{devices(after: null) {
	edges {node {id, isTrusted}}
	pageInfo {startCursor, hasNextPage}}}
""")

###############################################################################
# Script body
getDeviceIDs = client.execute(getDeviceIDs_query)
print("Before: ", getDeviceIDs)
devicesList = getDeviceIDs['devices']['edges']
for i in devicesList:
    itemsList = [item for sublist in list(i.items()) for item in sublist]
    string = r'''mutation {
    deviceUpdate(id: "DEVICE_ID", isTrusted: TRUSTED_STATUS) {
      ok, error}
}'''
    string = string.replace('DEVICE_ID', itemsList[1]['id'])
    string = string.replace('TRUSTED_STATUS', trustStatus)
    updateTrustStatus_query = gql(string)
    client.execute(updateTrustStatus_query)
print("After:  ", client.execute(getDeviceIDs_query))
