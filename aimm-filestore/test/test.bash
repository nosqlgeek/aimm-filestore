#!/bin/bash

echo "## Should work:"
curl --header 'Content-Type:application/octet-stream' --request POST --data-binary "@./logo.png" "http://localhost:5000/store/test-1.png?access_key=student&access_secret=5ccdc06e9dfece4b67a531e2dc83e4b9"
curl --output "../data/output.png" "http://localhost:5000/retrieve/test-1.png?access_key=student&access_secret=5ccdc06e9dfece4b67a531e2dc83e4b9"
curl --request DELETE "http://localhost:5000/delete/test-1.png?access_key=student&access_secret=5ccdc06e9dfece4b67a531e2dc83e4b9"
curl --request DELETE "http://localhost:5000/delete/output.png?access_key=student&access_secret=5ccdc06e9dfece4b67a531e2dc83e4b9"

echo "## Should fail because the wrong credentials were passed:"
curl --header 'Content-Type:application/octet-stream' --request POST --data-binary "@./logo.png" "http://localhost:5000/store/test-1.png?access_key=student&access_secret=password"

echo "## Should fail because the key is not correctly formatted:"
curl --header 'Content-Type:application/octet-stream' --request POST --data-binary "@./logo.png" "http://localhost:5000/store/test*2.png?access_key=student&access_secret=5ccdc06e9dfece4b67a531e2dc83e4b9"
