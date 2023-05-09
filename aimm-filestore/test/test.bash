#!/bin/bash

echo '## Should work:'
curl -H 'Content-Type:application/octet-stream' -H 'X-Access-Key:student' -H 'X-Access-Secret:5ccdc06e9dfece4b67a531e2dc83e4b9' --request POST --data-binary '@./logo.png' 'http://localhost:5000/store/test-1.png'
curl -H 'X-Access-Key:student' -H 'X-Access-Secret:5ccdc06e9dfece4b67a531e2dc83e4b9' --output '../data/output.png' 'http://localhost:5000/retrieve/test-1.png'
curl -H 'X-Access-Key:student' -H 'X-Access-Secret:5ccdc06e9dfece4b67a531e2dc83e4b9' --request DELETE 'http://localhost:5000/delete/test-1.png'
curl -H 'X-Access-Key:student' -H 'X-Access-Secret:5ccdc06e9dfece4b67a531e2dc83e4b9' --request DELETE 'http://localhost:5000/delete/output.png'

echo '## Should fail because the wrong credentials were passed:'
curl -H 'Content-Type:application/octet-stream' -H 'X-Access-Key:student' -H 'X-Access-Secret:5ccdc06e9dfece4b67a531e2dc8' --request POST --data-binary '@./logo.png' 'http://localhost:5000/store/test-1.png'

echo "## Should fail because the key is not correctly formatted:"
curl -H 'Content-Type:application/octet-stream' -H 'X-Access-Key:student' -H 'X-Access-Secret:5ccdc06e9dfece4b67a531e2dc83e4b9' --request POST --data-binary '@./logo.png' 'http://localhost:5000/store/test*2.png'
