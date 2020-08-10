# filesystem-rest-api
Simple rest api in Flask for interacting with the filesystem

How does it work:
1) Change constant BASE_DIR in the script to the required directory
2) `py rest_api.py` will run app on http://localhost:5000/ and point to the defined directory with BASE_DIR.
3) Append any path to the url for browsing the directory 
4) With request methods it is allowed to:
    * GET info about files and directory contents
    * DELETE a file or an empty folder
    * PUT (create) a new file
