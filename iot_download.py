import os, uuid, sys, time
from azure.storage.blob import BlockBlobService, PublicAccess

def run_sample():
    try:
        # Create the BlockBlockService that is used to call the Blob service for the storage account
        block_blob_service = BlockBlobService(account_name='no662', account_key='k8xm7XDmHTpkc9VLa9ZISxHoWpDfLgTspAHdwpjSckOI546AoopE17lKUDlVeaqD+GAz7FN+uh1M9/B7eEDgzg==')

        # Create a container called 'quickstartblobs'.
        container_name ='data2'
        block_blob_service.create_container(container_name)

        # Set the permission so the blobs are public.
        block_blob_service.set_container_acl(container_name, public_access=PublicAccess.Container)

        # List the blobs in the container
        print("\nList blobs in the container")
        generator = block_blob_service.list_blobs(container_name)
        length=0
        for blob in generator:
            length+=1
            print("\t Blob name: " + blob.name)

        # Download the blob(s).
        # Add '_DOWNLOADED' as prefix to '.txt' so you can see both files in Documents.
        local_path=os.path.expanduser("~/Desktop/MakeNTU/make_ntu_no_66-master/download")
        blob_counter=0
        for blob in generator:
            blob_counter+=1
            if blob_counter==length:
                local_file_name= blob.name
        full_path_to_file2 = os.path.join(local_path, time.strftime("%m-%d-%H-%M-%S", time.localtime()) + '.txt')
        print("\nDownloading blob to " + full_path_to_file2)
        block_blob_service.get_blob_to_path(container_name,local_file_name, full_path_to_file2)

    except Exception as e:
        print(e)


# Main method.
if __name__ == '__main__':
    run_sample()