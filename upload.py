from azure.storage.file import ContentSettings
from azure.storage.file import FileService

file_service = FileService(account_name='storagenavarro', account_key='sz7ewSbmF7+K8KkQZdYNsiiGeG9b8s1EDc+QFLyItJXjJmx0rxho0yb6wBK/jyXI7SgczB/5rTxRX1us6Os7mw==')

#fileservernavarro	ya existe se creo otro repo
#file_service.create_share('repositorio')

#https://github.com/MicrosoftDocs/azure-docs.es-es/blob/master/articles/storage/files/storage-python-how-to-use-file-storage.md
#file_service.create_directory('fileservernavarro', 'repository')

#repository directorio o None  para crear en la raiz
"""
file_service.create_file_from_path(
    'fileservernavarro',
    'repository',  
    'foto.jpg',
    'dog.jpg',
    content_settings=ContentSettings(content_type='image/jpg'))
	
"""


print ("Verify")

