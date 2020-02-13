# Cloud Foundry + Python + MSSQL Example

## References

https://stackoverflow.com/questions/58087045/pivotal-django-settings-for-user-provided-mssql-database

## Setup

### Create User Provided Service

First edit `mssql-service.json` with the appropriate information for your environment.

Then create the necessary User Provided Service:
```sh
cf cups mssql-service -p mssql-service.json
```

### Push the Demo App

```sh
cf push
```

## Verify Setup

Navigate to the URL of your newly pushed sample app and verify the output. You will see something similar to the following if everything is working correctly:

```
/home/vcap/deps/1/bin:/home/vcap/deps/0/bin:/usr/local/bin:/usr/bin:/bin:/home/vcap/deps/0/apt/opt/mssql-tools/bin/
/home/vcap/app/
/home/vcap/deps/1/lib:/home/vcap/deps/0/lib
/home/vcap/deps/1/lib:/home/vcap/deps/0/lib
Microsoft SQL Server 2017 (RTM-CU18) (KB4527377) - 14.0.3257.3 (X64) Nov 16 2019 01:14:50 Copyright (C) 2017 Microsoft Corporation Standard Edition (64-bit) on Linux (Ubuntu 16.04.6 LTS)
```
