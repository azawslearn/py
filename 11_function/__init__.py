import logging
import azure.functions as func
from azure.identity import ClientSecretCredential
from azure.storage.blob import BlobServiceClient
import requests

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Enter your Azure AD app registration details
    client_id = ''
    client_secret = ''
    tenant_id = ''
    graph_scope = 'https://graph.microsoft.com/.default'

    # Enter your storage account connection string and container name
    connection_string = ""
    container_name = 'user-container'

    # Create a client secret credential
    credential = ClientSecretCredential(tenant_id, client_id, client_secret)

    # Get an access token for Microsoft Graph
    token = credential.get_token(graph_scope)

    # Query the Microsoft Graph for all users
    graph_endpoint = 'https://graph.microsoft.com/v1.0/users'
    headers = {
        'Authorization': 'Bearer ' + token.token,
        'Content-Type': 'application/json'
    }
    response = requests.get(graph_endpoint, headers=headers)
    response_data = response.json()

    # Store the query result in a file in Azure Blob Storage
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)
    blob_client = container_client.get_blob_client('result.txt')

    result = ""
    for user in response_data['value']:
        result += user['displayName'] + '\n'

    blob_client.upload_blob(result, overwrite=True)

    return func.HttpResponse(
        "Query result stored in Azure Blob Storage.",
        status_code=200
    )
