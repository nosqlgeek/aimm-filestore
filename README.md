# A simple file store service that allows storing artifact images and more


This service allows you to store, retrieve and delete files with a unique key.

## Configuration

The file `config.py` contains the following configuration settings:

* `data_folder`: The folder to which files should be written or retrieved from
* `access_key`: A simple access key that needs to be passed when accessing the file store
* `access_secret`: The secret that needs to be passed when accessing the file store

The default configuration reads those configuration settings from the following environment variables:

* `FS_DATA_FOLDER`
* `FS_ACCESS_KEY`
* `FS_ACCESS_SECRET`

## API

The file store provides the following API:

* HTTP POST to `/store/<key>`
* HTTP GET from `/retrieve/<key>`
* HTTP GET from `/list`
* HTTP DELETE to `/delete/<key>`

The HTTP `Content-Type` header must be set to `application/octet-stream`. The authentication parameters must be passed within the header via the following custom fields:

* `X-Access-Key`
* `X-Access-Secret`

Here are some examples:


* Upload a file: 

```
curl -H 'Content-Type:application/octet-stream' -H 'X-Access-Key:<access_key>' -H 'X-Access-Secret:<access_secret>' --request POST --data-binary '@./logo.png' 'http://localhost:5000/store/test-1.png'
```

* Get a file:

```
curl  -H 'X-Access-Key:<access_key>' -H 'X-Access-Secret:<access_secret>' --output '../data/output.png' 'http://localhost:5000/retrieve/test-1.png'
```

* List all files:

```
curl  -H 'X-Access-Key:<access_key>' -H 'X-Access-Secret:<access_secret>' 'http://localhost:5000/list'
```

* Delete a file:

```
curl  -H 'X-Access-Key:<access_key>' -H 'X-Access-Secret:<access_secret>' --request DELETE 'http://localhost:5000/delete/test-1.png'
```

> Note: This example uses the command line tool `curl`, but any HTTP client can be used. Python comes with the [`requests`](https://www.w3schools.com/python/module_requests.asp) module.
