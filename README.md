# A simple Python implementation of a file store

This service allows you to store, retrieve and delete files by a unique key.

## Configuration

The file `config.py` contains the following configuration settings:

`data_folder`: The folder to which files should be written or retrieved from
`access_key` : A simple access key that needs to be passed when accessing the file store
`access_secret`: The secret that needs to be passed when accessing the file store

The default configuration reads those configuration settings from the following environment variables:

* `FS_DATA_FOLDER`
* `FS_ACCESS_KEY`
* `FS_ACCESS_SECRET`

## How to use

The file store provides the following API:

* HTTP POST to `/store/<key>`
* HTTP GET from `/retrieve/<key>`
* HTTP DELETE to `/delete/<key>`

The HTTP `Content-Type` header must be set to `application/octet-stream`. The authentication parameters must be passed as URL parameters.

Here are some examples:


* Upload a file: 

```
curl --header 'Content-Type:application/octet-stream' --request POST --data-binary "@./logo.png" "http://localhost:5000/store/test-1.png?access_key=<access_key>&access_secret=<access_secret>"
```

* Get a file:

```
curl --output "../data/output.png" "http://localhost:5000/retrieve/test-1.png?access_key=<access_key>&access_secret=<access_secret>"
```

* Delete a file:

```
curl --request DELETE "http://localhost:5000/delete/test-1.png?access_key=<access_key>&access_secret=<access_secret>"
```

> Note: This example uses the command line tool `curl`, but any HTTP client can be used. Python comes with the [`requests`](https://www.w3schools.com/python/module_requests.asp) module.
