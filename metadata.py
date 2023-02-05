import json
import requests

def vm_metadata(metadata_key):
    metadata_url = "http://metadata.google.internal/computeMetadata/v1/instance/" + metadata_key
    headers = {'Metadata-Flavor': 'Google'}
    response = requests.get(metadata_url, headers=headers)
    return response.text

def retrieve_metadata(metadata_keys):
    instance_metadata = {}
    for key in metadata_keys:
        instance_metadata[key] = vm_metadata(key)
    return instance_metadata

def execute(keys=None):

    default_metadata_keys = [
        "id",
        "project/project-id",
        "zone",
        "hostname"
    ]

    if keys:
        metadata = retrieve_metadata(keys)
    else:
        metadata = retrieve_metadata(default_metadata_keys)

    print(f"metadata_info: {json.dumps(metadata)}")

#custom metadata info. to retrieve
execute(["id", "project/project-id"])