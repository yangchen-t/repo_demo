#!/bin/bash



supervisorctl restart flask_update 

supervisorctl tail -f flask_update
