# MiniTwit

"Because writing todo lists is not fun"

# What is MiniTwit?

A simple twitter clone, written in Python, powered by SQLite and Flask.

## Design

* `PlantUML`: https://gist.github.com/marcellodesales/3eee0af42de6c08b9652470ad4230d1e

> **NOTE**: Needs some more work for the design

![Minitwit Diagram](http://www.plantuml.com/plantuml/proxy?src=https://gist.githubusercontent.com/marcellodesales/3eee0af42de6c08b9652470ad4230d1e/raw/6004b21021ecfee590bc3afd7d6835bde95a1a30/minitwit.puml)

# Runtime

> **Requirements**: Python 3, C++, MySQL Client to build clients

## :snake: How do I use it using Python?

1. install flask and flask-cli via pip
2. edit the configuration in the minitwit.py file 
  * export the environment variable `MINITWIT_SETTINGS` pointing to a configuration file.
3. Initialize the database by running:

```console
export FLASK_APP=minitwit.py; \
export LC_ALL=en_US.utf-8; \
export LANG=en_US.utf-8; \
flask initdb
```

4. Now you can run `minitwit`:

```console
flask run --host=0.0.0.0 --with-threads --no-debugger --no-reload
```

The application will greet you on:

```
[2023-03-07 19:54:16,940] INFO in minitwit: Using local db sqlite:////var/minitwit/minitwit.db
 * Serving Flask app 'minitwit.py'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://10.105.238.6:5000
Press CTRL+C to quit
```

5. Go to the browser at http://127.0.0.1:5000.

## :whale: How do I use it using Docker?

> **Requirement**: Make sure to have the docker engine or containerd installed.

1. Make sure to adjust the port number on `docker-compose.yaml`
2. Initialize a container with `docker compose up`

```console
$ docker compose up --build minitwit-runtime
minitwit-minitwit-runtime-1  | Initializing the app server...
minitwit-minitwit-runtime-1  | [2023-03-09 14:28:29,780] INFO in config_service: Current environment:
minitwit-minitwit-runtime-1  | _=/usr/local/bin/flask
minitwit-minitwit-runtime-1  | PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
minitwit-minitwit-runtime-1  | PYTHON_GET_PIP_URL=https://github.com/pypa/get-pip/raw/d5cb0afaf23b8520f1bbcfed521017b4a95f5c01/public/get-pip.py
minitwit-minitwit-runtime-1  | LC_ALL=en_US.utf-8
minitwit-minitwit-runtime-1  | PYTHON_GET_PIP_SHA256=394be00f13fa1b9aaa47e911bdb59a09c3b2986472130f30aa0bfaf7f3980637
minitwit-minitwit-runtime-1  | PYTHON_PIP_VERSION=22.0.4
minitwit-minitwit-runtime-1  | SHLVL=1
minitwit-minitwit-runtime-1  | FLASK_APP=minitwit.py
minitwit-minitwit-runtime-1  | GPG_KEY=E3FF2839C048B25C084DEBE9B26995E310250568
minitwit-minitwit-runtime-1  | LANG=en_US.utf-8
minitwit-minitwit-runtime-1  | HOME=/root
minitwit-minitwit-runtime-1  | PYTHON_SETUPTOOLS_VERSION=57.5.0
minitwit-minitwit-runtime-1  | PWD=/viasat/minitwit
minitwit-minitwit-runtime-1  | DB_DIR=/var/minitwit
minitwit-minitwit-runtime-1  | PYTHON_VERSION=3.8.16
minitwit-minitwit-runtime-1  | HOSTNAME=52900b592410
minitwit-minitwit-runtime-1  | FLASK_RUN_FROM_CLI=true
minitwit-minitwit-runtime-1  |
minitwit-minitwit-runtime-1  | [2023-03-09 14:28:29,785] INFO in config_service: Bootstrapping app server...
minitwit-minitwit-runtime-1  | [2023-03-09 14:28:31,830] INFO in host_service: Not running in the Cloud...
minitwit-minitwit-runtime-1  | [2023-03-09 14:28:31,831] WARNING in config_service: Can't fetch the cloud metadata because this instance is not in the cloud!
minitwit-minitwit-runtime-1  | [2023-03-09 14:28:31,834] INFO in config_service: Loaded with the following config: {
minitwit-minitwit-runtime-1  |     "APPLICATION_ROOT": "/",
minitwit-minitwit-runtime-1  |     "CONFIG_DB_ENDPOINT": "DB_ENDPOINT",
minitwit-minitwit-runtime-1  |     "CONFIG_DB_NAME": "DB_NAME",
minitwit-minitwit-runtime-1  |     "CONFIG_DB_PASSWORD": "DB_PASSWORD",
minitwit-minitwit-runtime-1  |     "CONFIG_DB_SECRET_ARN": "DB_SECRET_ARN",
minitwit-minitwit-runtime-1  |     "CONFIG_DB_SECRET_KEY_PASSWORD": "DB_SECRET_KEY_PASSWORD",
minitwit-minitwit-runtime-1  |     "CONFIG_DB_SECRET_KEY_USERNAME": "DB_SECRET_KEY_USERNAME",
minitwit-minitwit-runtime-1  |     "CONFIG_DB_TYPE": "DB_TYPE",
minitwit-minitwit-runtime-1  |     "CONFIG_DB_USER": "DB_USER",
minitwit-minitwit-runtime-1  |     "DB_STASH": "db",
minitwit-minitwit-runtime-1  |     "DB_TYPE_MYSQL": "mysql",
minitwit-minitwit-runtime-1  |     "DB_TYPE_SQLITE": "sqlite",
minitwit-minitwit-runtime-1  |     "DEBUG": true,
minitwit-minitwit-runtime-1  |     "ENV": "production",
minitwit-minitwit-runtime-1  |     "EXPLAIN_TEMPLATE_LOADING": false,
minitwit-minitwit-runtime-1  |     "HOSTNAME": "52900b592410",
minitwit-minitwit-runtime-1  |     "IN_CLOUD": {
minitwit-minitwit-runtime-1  |         "metadata": {},
minitwit-minitwit-runtime-1  |         "status": false,
minitwit-minitwit-runtime-1  |         "type": "local"
minitwit-minitwit-runtime-1  |     },
minitwit-minitwit-runtime-1  |     "JSONIFY_MIMETYPE": null,
minitwit-minitwit-runtime-1  |     "JSONIFY_PRETTYPRINT_REGULAR": null,
minitwit-minitwit-runtime-1  |     "JSON_AS_ASCII": null,
minitwit-minitwit-runtime-1  |     "JSON_SORT_KEYS": null,
minitwit-minitwit-runtime-1  |     "LOCAL_DATABASE_URL": "sqlite:////var/minitwit/minitwit.db",
minitwit-minitwit-runtime-1  |     "LOCAL_DB_TYPE": "sqlite",
minitwit-minitwit-runtime-1  |     "MAX_CONTENT_LENGTH": null,
minitwit-minitwit-runtime-1  |     "MAX_COOKIE_SIZE": 4093,
minitwit-minitwit-runtime-1  |     "PERMANENT_SESSION_LIFETIME": "31 days, 0:00:00",
minitwit-minitwit-runtime-1  |     "PER_PAGE": 30,
minitwit-minitwit-runtime-1  |     "PREFERRED_URL_SCHEME": "http",
minitwit-minitwit-runtime-1  |     "PROPAGATE_EXCEPTIONS": null,
minitwit-minitwit-runtime-1  |     "SCHEMAS": {
minitwit-minitwit-runtime-1  |         "mysql": "db_mysql.sql",
minitwit-minitwit-runtime-1  |         "sqlite": "db_sqlite.sql"
minitwit-minitwit-runtime-1  |     },
minitwit-minitwit-runtime-1  |     "SECRET_FRIENDLY_NAME": "mtdb-credentials",
minitwit-minitwit-runtime-1  |     "SECRET_KEY": "development key",
minitwit-minitwit-runtime-1  |     "SECRET_PASSWORD": "password",
minitwit-minitwit-runtime-1  |     "SECRET_USERNAME": "username",
minitwit-minitwit-runtime-1  |     "SEND_FILE_MAX_AGE_DEFAULT": null,
minitwit-minitwit-runtime-1  |     "SERVER_NAME": null,
minitwit-minitwit-runtime-1  |     "SESSION_COOKIE_DOMAIN": null,
minitwit-minitwit-runtime-1  |     "SESSION_COOKIE_HTTPONLY": true,
minitwit-minitwit-runtime-1  |     "SESSION_COOKIE_NAME": "session",
minitwit-minitwit-runtime-1  |     "SESSION_COOKIE_PATH": null,
minitwit-minitwit-runtime-1  |     "SESSION_COOKIE_SAMESITE": null,
minitwit-minitwit-runtime-1  |     "SESSION_COOKIE_SECURE": false,
minitwit-minitwit-runtime-1  |     "SESSION_REFRESH_EACH_REQUEST": true,
minitwit-minitwit-runtime-1  |     "TEMPLATES_AUTO_RELOAD": null,
minitwit-minitwit-runtime-1  |     "TESTING": false,
minitwit-minitwit-runtime-1  |     "TRAP_BAD_REQUEST_ERRORS": null,
minitwit-minitwit-runtime-1  |     "TRAP_HTTP_EXCEPTIONS": false,
minitwit-minitwit-runtime-1  |     "USE_X_SENDFILE": false
minitwit-minitwit-runtime-1  | }
minitwit-minitwit-runtime-1  | [2023-03-09 14:28:31,835] INFO in minitwit: Using local db sqlite:////var/minitwit/minitwit.db
minitwit-minitwit-runtime-1  | [2023-03-09 14:28:31,969] INFO in config_service: Endpoints: ['/static/<path:filename>', '/', '/public', '/<username>', '/<username>/follow', '/<username>/unfollow', '/add_message', '/login', '/register', '/logout', '/healthcheck/liveness', '/healthcheck/readiness', '/admin/env', '/admin/config', '/admin/endpoints']
minitwit-minitwit-runtime-1  |  * Serving Flask app 'minitwit.py'
minitwit-minitwit-runtime-1  |  * Debug mode: off
minitwit-minitwit-runtime-1  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
minitwit-minitwit-runtime-1  |  * Running on all addresses (0.0.0.0)
minitwit-minitwit-runtime-1  |  * Running on http://127.0.0.1:5000
minitwit-minitwit-runtime-1  |  * Running on http://192.168.208.2:5000
```

3. Go to the browser at http://127.0.0.1:5000.

> **NOTE**: When operating this server, the database file is created under the local dir `db/minitwit.db` as mapped in
> docker-compose.yaml. Make sure to change the path to anything else desired.

```console
☁️  aws-cli@2.9.15
☸️  kubectl@1.24.3 📛 kustomize@1.24.3 🎡 helm@3.10.2    🐳 docker@20.10.21-rd 🐙 docker-compose@v2.14.0
👮 marcellodesales
🏗  1.24.3+k3s1 🔐 rancher-desktop 🍱 default
~/dev/github.com/marcellodesales/minitwit on  feature/improve-experience-with-docker! 📅 03-07-2023 ⌚18:07:30
$ tree db
db
└── minitwit.db

0 directories, 1 file

$ file db/minitwit.db
db/minitwit.db: SQLite 3.x database, last written using SQLite version 3040001, file counter 5, database pages 5, cookie 0x3, schema 4, UTF-8, version-valid-for 5
```

# Development

> **Requirements**: Install `requirements-dev.txt` for build and testing tools.

## Is it tested?

You betcha.  Run the `test_minitwit.py` file to see the tests pass.

1. Install the dev dependencies

> **NOTE**: the runtime dependencies must have been installed as well.

```
$ pip install -r requirements-dev.txt
Collecting pytest==5.3.2
  Downloading pytest-5.3.2-py3-none-any.whl (234 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 234.5/234.5 KB 1.5 MB/s eta 0:00:00
Collecting attrs>=17.4.0
  Downloading attrs-22.2.0-py3-none-any.whl (60 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 60.0/60.0 KB 5.5 MB/s eta 0:00:00
Collecting more-itertools>=4.0.0
  Downloading more_itertools-9.1.0-py3-none-any.whl (54 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 54.2/54.2 KB 4.3 MB/s eta 0:00:00
Collecting py>=1.5.0
  Downloading py-1.11.0-py2.py3-none-any.whl (98 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 98.7/98.7 KB 7.1 MB/s eta 0:00:00
Collecting packaging
  Downloading packaging-23.0-py3-none-any.whl (42 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 42.7/42.7 KB 3.3 MB/s eta 0:00:00
Collecting pluggy<1.0,>=0.12
  Downloading pluggy-0.13.1-py2.py3-none-any.whl (18 kB)
Collecting wcwidth
  Downloading wcwidth-0.2.6-py2.py3-none-any.whl (29 kB)
Installing collected packages: wcwidth, py, pluggy, packaging, more-itertools, attrs, pytest
Successfully installed attrs-22.2.0 more-itertools-9.1.0 packaging-23.0 pluggy-0.13.1 py-1.11.0 pytest-5.3.2 wcwidth-0.2.6
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
WARNING: You are using pip version 22.0.4; however, version 23.0.1 is available.
You should consider upgrading via the '/usr/local/bin/python -m pip install --upgrade pip' command.
```

2. Execute the test cases

```console
pytest test_minitwit.py
==================================================================== test session starts =====================================================================
platform linux -- Python 3.8.16, pytest-5.3.2, py-1.11.0, pluggy-0.13.1
rootdir: /Users/mdesales/dev/github.com/marcellodesales/minitwit
collected 4 items

test_minitwit.py ....                                                                                                                                  [100%]

=============================================================== 4 passed, 1 warning in 29.14s ================================================================
```

## Test using Docker Container

1. Build a docker image with the runtime needed

> **NOTE**: The docker image `viasat/minitwit-test` is created locally.

The tests are executed within the docker build process and are set as CMD to execute as containers.

```console
$ docker compose build minitwit-test
[+] Building 63.0s (18/18) FINISHED
 => [internal] load build definition from Dockerfile                                                                                                     0.0s
 => => transferring dockerfile: 1.08kB                                                                                                                   0.0s
 => [internal] load .dockerignore                                                                                                                        0.0s
 => => transferring context: 2B                                                                                                                          0.0s
 => [internal] load metadata for docker.io/library/python:3.8.16-alpine3.17                                                                              0.4s
 => [builder 1/9] FROM docker.io/library/python:3.8.16-alpine3.17@sha256:8518dd6657131d938f283ea97385b1db6724e35d45ddab6cd1c583796e35566a                0.0s
 => => resolve docker.io/library/python:3.8.16-alpine3.17@sha256:8518dd6657131d938f283ea97385b1db6724e35d45ddab6cd1c583796e35566a                        0.0s
 => [internal] load build context                                                                                                                        0.0s
 => => transferring context: 490B                                                                                                                        0.0s
 => CACHED [builder 2/9] RUN apk add musl-dev python3-dev mariadb-dev gcc build-base bash                                                                0.0s
 => CACHED [builder 3/9] WORKDIR /viasat/minitwit                                                                                                        0.0s
 => CACHED [builder 4/9] COPY requirements.txt .                                                                                                         0.0s
 => CACHED [builder 5/9] RUN pip install -r requirements.txt                                                                                             0.0s
 => CACHED [builder 6/9] COPY ./static /viasat/minitwit/static                                                                                           0.0s
 => CACHED [builder 7/9] COPY ./templates /viasat/minitwit/templates                                                                                     0.0s
 => CACHED [builder 8/9] COPY *.py /viasat/minitwit                                                                                                      0.0s
 => CACHED [builder 9/9] COPY *.sql /viasat/minitwit                                                                                                     0.0s
 => [tester 1/3] COPY requirements-dev.txt .                                                                                                             0.0s
 => [tester 2/3] RUN pip install -r requirements-dev.txt                                                                                                12.2s
 => [tester 3/3] RUN pytest test_minitwit.py                                                                                                            30.5s
 => exporting to oci image format                                                                                                                       19.5s
 => => exporting layers                                                                                                                                  0.3s
 => => exporting manifest sha256:20a82b1dfbe5398ebb6e8f65917221f2a5bf2a932fb5f19d9e62e19b97ab4450                                                        0.0s
 => => exporting config sha256:64a9ebf40a546f12f97d3d74903846dc170bc776f110feb0cde2a508a51b300b                                                          0.0s
 => => sending tarball                                                                                                                                  19.0s
 => importing to docker
```

2. You can re-execute the test cases

```console
$ docker run -ti viasat/minitwit-test
WARNING: The requested image's platform (linux/amd64) does not match the detected host platform (linux/arm64/v8) and no specific platform was requested
==================================================================== test session starts =====================================================================
platform linux -- Python 3.8.16, pytest-5.3.2, py-1.11.0, pluggy-0.13.1
rootdir: /viasat/minitwit
collected 4 items

test_minitwit.py ....                                                                                                                                  [100%]

====================================================================== warnings summary ======================================================================
test_minitwit.py::test_register
  /viasat/minitwit/minitwit.py:200: RemovedIn20Warning: Deprecated API features detected! These feature(s) are not compatible with SQLAlchemy 2.0. To prevent incompatible upgrades prior to updating applications, ensure requirements files are pinned to "sqlalchemy<2.0". Set environment variable SQLALCHEMY_WARN_20=1 to show all deprecation warnings.  Set environment variable SQLALCHEMY_SILENCE_UBER_WARNING=1 to silence this message. (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    the_db.execute(query.strip() + ';')

-- Docs: https://docs.pytest.org/en/latest/warnings.html
=============================================================== 4 passed, 1 warning in 29.42s ================================================================
```

3. You can inspect the tests by initializing a docker container with the current sources mounted as a volume.

> **NOTE**: You need to override the entrypoint with bash.

```console
☁️  aws-cli@2.9.15
☸️  kubectl@1.24.3 📛 kustomize@1.24.3 🎡 helm@3.10.2    🐳 docker@20.10.21-rd 🐙 docker-compose@v2.14.0
👮 marcellodesales
🏗  1.24.3+k3s1 🔐 rancher-desktop 🍱 default
~/dev/github.com/marcellodesales/minitwit on  feature/improve-experience-with-docker! 📅 03-07-2023 ⌚16:41:53
$ docker run --platform linux/amd64 -ti -w $(pwd) -v $(pwd):$(pwd) --entrypoint bash viasat/minitwit
93078096ab1b:/Users/mdesales/dev/github.com/marcellodesales/minitwit#
```

4. Execute the test cases from within the container

```console
602f533b1fa6:/Users/mdesales/dev/github.com/marcellodesales/minitwit# pytest test_minitwit.py
==================================================================== test session starts =====================================================================
platform linux -- Python 3.8.16, pytest-5.3.2, py-1.11.0, pluggy-0.13.1
rootdir: /Users/mdesales/dev/github.com/marcellodesales/minitwit
collected 4 items

test_minitwit.py ... .                                                                                                                                  [100%]

====================================================================== warnings summary ======================================================================
test_minitwit.py::test_register
  /Users/mdesales/dev/github.com/marcellodesales/minitwit/minitwit.py:200: RemovedIn20Warning: Deprecated API features detected! These feature(s) are not compatible with SQLAlchemy 2.0. To prevent incompatible upgrades prior to updating applications, ensure requirements files are pinned to "sqlalchemy<2.0". Set environment variable SQLALCHEMY_WARN_20=1 to show all deprecation warnings.  Set environment variable SQLALCHEMY_SILENCE_UBER_WARNING=1 to silence this message. (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    the_db.execute(query.strip() + ';')

-- Docs: https://docs.pytest.org/en/latest/warnings.html
=============================================================== 4 passed, 1 warning in 29.50s ================================================================
602f533b1fa6:/Users/mdesales/dev/github.com/marcellodesales/minitwit# exit
exit
```

# Observability Capabilities

* Show bootstrap details for debugging
* Admin endpoints
* Healthcheck Endpoints

## Bootstrap config in Non-Cloud

* It does log `Not running in the Cloud...`
* Shows the current environment variables for debugging
* Shows the resolved configuration properties for the app
  * Some of them are resolved based on the environment variables
* Shows if the kind of database it is connected to.

```python
minitwit-minitwit-runtime-1  | Initializing the app server...
minitwit-minitwit-runtime-1  | [2023-03-09 04:54:34,273] INFO in minitwit: Current environment:
minitwit-minitwit-runtime-1  | _=/usr/local/bin/python
minitwit-minitwit-runtime-1  | PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
minitwit-minitwit-runtime-1  | PYTHON_GET_PIP_URL=https://github.com/pypa/get-pip/raw/d5cb0afaf23b8520f1bbcfed521017b4a95f5c01/public/get-pip.py
minitwit-minitwit-runtime-1  | LC_ALL=en_US.utf-8
minitwit-minitwit-runtime-1  | PYTHON_GET_PIP_SHA256=394be00f13fa1b9aaa47e911bdb59a09c3b2986472130f30aa0bfaf7f3980637
minitwit-minitwit-runtime-1  | PYTHON_PIP_VERSION=22.0.4
minitwit-minitwit-runtime-1  | SHLVL=1
minitwit-minitwit-runtime-1  | FLASK_APP=minitwit.py
minitwit-minitwit-runtime-1  | GPG_KEY=E3FF2839C048B25C084DEBE9B26995E310250568
minitwit-minitwit-runtime-1  | LANG=en_US.utf-8
minitwit-minitwit-runtime-1  | HOME=/root
minitwit-minitwit-runtime-1  | PYTHON_SETUPTOOLS_VERSION=57.5.0
minitwit-minitwit-runtime-1  | PWD=/viasat/minitwit
minitwit-minitwit-runtime-1  | DB_DIR=/var/minitwit
minitwit-minitwit-runtime-1  | PYTHON_VERSION=3.8.16
minitwit-minitwit-runtime-1  | HOSTNAME=6c57fa9fba26
minitwit-minitwit-runtime-1  |
minitwit-minitwit-runtime-1  | [2023-03-09 04:54:34,278] INFO in minitwit: Bootstrapping app server...
minitwit-minitwit-runtime-1  | [2023-03-09 04:54:36,316] INFO in minitwit: Not running in the Cloud...
minitwit-minitwit-runtime-1  | [2023-03-09 04:54:36,319] WARNING in minitwit: Can't fetch the cloud metadata because this instance is not in the cloud!
minitwit-minitwit-runtime-1  | [2023-03-09 04:54:36,323] INFO in minitwit: Loaded with the following config: {
minitwit-minitwit-runtime-1  |     "APPLICATION_ROOT": "/",
minitwit-minitwit-runtime-1  |     "CONFIG_DB_ENDPOINT": "DB_ENDPOINT",
minitwit-minitwit-runtime-1  |     "CONFIG_DB_NAME": "DB_NAME",
minitwit-minitwit-runtime-1  |     "CONFIG_DB_PASSWORD": "DB_PASSWORD",
minitwit-minitwit-runtime-1  |     "CONFIG_DB_SECRET_ARN": "DB_SECRET_ARN",
minitwit-minitwit-runtime-1  |     "CONFIG_DB_SECRET_KEY_PASSWORD": "DB_SECRET_KEY_PASSWORD",
minitwit-minitwit-runtime-1  |     "CONFIG_DB_SECRET_KEY_USERNAME": "DB_SECRET_KEY_USERNAME",
minitwit-minitwit-runtime-1  |     "CONFIG_DB_TYPE": "DB_TYPE",
minitwit-minitwit-runtime-1  |     "CONFIG_DB_USER": "DB_USER",
minitwit-minitwit-runtime-1  |     "DB_STASH": "db",
minitwit-minitwit-runtime-1  |     "DB_TYPE_MYSQL": "mysql",
minitwit-minitwit-runtime-1  |     "DB_TYPE_SQLITE": "sqlite",
minitwit-minitwit-runtime-1  |     "DEBUG": true,
minitwit-minitwit-runtime-1  |     "ENV": "production",
minitwit-minitwit-runtime-1  |     "EXPLAIN_TEMPLATE_LOADING": false,
minitwit-minitwit-runtime-1  |     "HOSTNAME": "6c57fa9fba26",
minitwit-minitwit-runtime-1  |     "IN_CLOUD": {
minitwit-minitwit-runtime-1  |         "metadata": {},
minitwit-minitwit-runtime-1  |         "status": false,
minitwit-minitwit-runtime-1  |         "type": "local"
minitwit-minitwit-runtime-1  |     },
minitwit-minitwit-runtime-1  |     "JSONIFY_MIMETYPE": null,
minitwit-minitwit-runtime-1  |     "JSONIFY_PRETTYPRINT_REGULAR": null,
minitwit-minitwit-runtime-1  |     "JSON_AS_ASCII": null,
minitwit-minitwit-runtime-1  |     "JSON_SORT_KEYS": null,
minitwit-minitwit-runtime-1  |     "LOCAL_DATABASE_URL": "sqlite:////var/minitwit/minitwit.db",
minitwit-minitwit-runtime-1  |     "LOCAL_DB_TYPE": "sqlite",
minitwit-minitwit-runtime-1  |     "MAX_CONTENT_LENGTH": null,
minitwit-minitwit-runtime-1  |     "MAX_COOKIE_SIZE": 4093,
minitwit-minitwit-runtime-1  |     "PERMANENT_SESSION_LIFETIME": "31 days, 0:00:00",
minitwit-minitwit-runtime-1  |     "PER_PAGE": 30,
minitwit-minitwit-runtime-1  |     "PREFERRED_URL_SCHEME": "http",
minitwit-minitwit-runtime-1  |     "PROPAGATE_EXCEPTIONS": null,
minitwit-minitwit-runtime-1  |     "SCHEMAS": {
minitwit-minitwit-runtime-1  |         "mysql": "db_mysql.sql",
minitwit-minitwit-runtime-1  |         "sqlite": "db_sqlite.sql"
minitwit-minitwit-runtime-1  |     },
minitwit-minitwit-runtime-1  |     "SECRET_FRIENDLY_NAME": "mtdb-credentials",
minitwit-minitwit-runtime-1  |     "SECRET_KEY": "development key",
minitwit-minitwit-runtime-1  |     "SECRET_PASSWORD": "password",
minitwit-minitwit-runtime-1  |     "SECRET_USERNAME": "username",
minitwit-minitwit-runtime-1  |     "SEND_FILE_MAX_AGE_DEFAULT": null,
minitwit-minitwit-runtime-1  |     "SERVER_NAME": null,
minitwit-minitwit-runtime-1  |     "SESSION_COOKIE_DOMAIN": null,
minitwit-minitwit-runtime-1  |     "SESSION_COOKIE_HTTPONLY": true,
minitwit-minitwit-runtime-1  |     "SESSION_COOKIE_NAME": "session",
minitwit-minitwit-runtime-1  |     "SESSION_COOKIE_PATH": null,
minitwit-minitwit-runtime-1  |     "SESSION_COOKIE_SAMESITE": null,
minitwit-minitwit-runtime-1  |     "SESSION_COOKIE_SECURE": false,
minitwit-minitwit-runtime-1  |     "SESSION_REFRESH_EACH_REQUEST": true,
minitwit-minitwit-runtime-1  |     "TEMPLATES_AUTO_RELOAD": null,
minitwit-minitwit-runtime-1  |     "TESTING": false,
minitwit-minitwit-runtime-1  |     "TRAP_BAD_REQUEST_ERRORS": null,
minitwit-minitwit-runtime-1  |     "TRAP_HTTP_EXCEPTIONS": false,
minitwit-minitwit-runtime-1  |     "USE_X_SENDFILE": false
minitwit-minitwit-runtime-1  | }
minitwit-minitwit-runtime-1  | [2023-03-09 04:54:36,324] INFO in minitwit: Using local db sqlite:////var/minitwit/minitwit.db
minitwit-minitwit-runtime-1  |  * Serving Flask app 'minitwit'
minitwit-minitwit-runtime-1  |  * Debug mode: off
minitwit-minitwit-runtime-1  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
minitwit-minitwit-runtime-1  |  * Running on all addresses (0.0.0.0)
minitwit-minitwit-runtime-1  |  * Running on http://127.0.0.1:5000
minitwit-minitwit-runtime-1  |  * Running on http://192.168.208.2:5000
minitwit-minitwit-runtime-1  | Press CTRL+C to quit
```

## Bootstrap config in Cloud

```python
Mar 09 01:16:25 ip-10-105-238-6 systemd[1]: Started Minitwit server II.
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]: [2023-03-09 01:16:26,164] INFO in minitwit: Bootstrapping app server...
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]: [2023-03-09 01:16:26,169] INFO in minitwit: Running in the Cloud...
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]: [2023-03-09 01:16:26,174] INFO in minitwit: Loaded with the following config: {
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "APPLICATION_ROOT": "/",
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "CONFIG_DB_ENDPOINT": "DB_ENDPOINT",
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "CONFIG_DB_NAME": "DB_NAME",
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "CONFIG_DB_PASSWORD": "DB_PASSWORD",
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "CONFIG_DB_SECRET_ARN": "DB_SECRET_ARN",
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "CONFIG_DB_SECRET_KEY_PASSWORD": "DB_SECRET_KEY_PASSWORD",
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "CONFIG_DB_SECRET_KEY_USERNAME": "DB_SECRET_KEY_USERNAME",
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "CONFIG_DB_TYPE": "DB_TYPE",
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "CONFIG_DB_USER": "DB_USER",
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "DB_ENDPOINT": "mtdb.cwxg4mojlhdg.us-east-1.rds.amazonaws.com",
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "DB_NAME": "mtdb",
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "DB_PASSWORD": "mt*****d",
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "DB_STASH": "db",
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "DB_TYPE": "mysql",
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "DB_TYPE_MYSQL": "mysql",
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "DB_TYPE_SQLITE": "sqlite",
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "DB_USER": "mtdbuser",
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "DEBUG": true,
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "ENV": "production",
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "EXPLAIN_TEMPLATE_LOADING": false,
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "HOSTNAME": "ec2-44-214-35-206.compute-1.amazonaws.com",
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "IN_CLOUD": {
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:         "metadata": {
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:             "accountId": "178468422646",
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:             "architecture": "x86_64",
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:             "availabilityZone": "us-east-1a",
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:             "billingProducts": null,
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:             "devpayProductCodes": null,
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:             "imageId": "ami-09cd747c78a9add63",
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:             "instanceId": "i-0412331f71f1cd3c8",
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:             "instanceType": "t3.medium",
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:             "kernelId": null,
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:             "marketplaceProductCodes": null,
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:             "pendingTime": "2023-03-06T18:09:23Z",
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:             "privateIp": "10.105.238.6",
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:             "ramdiskId": null,
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:             "region": "us-east-1",
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:             "version": "2017-09-30"
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:         },
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:         "status": true,
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:         "type": "ec2"
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     },
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "JSONIFY_MIMETYPE": null,
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "JSONIFY_PRETTYPRINT_REGULAR": null,
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "JSON_AS_ASCII": null,
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "JSON_SORT_KEYS": null,
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "LOCAL_DATABASE_URL": "sqlite:////var/minitwit/minitwit.db",
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "LOCAL_DB_TYPE": "sqlite",
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "MAX_CONTENT_LENGTH": null,
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "MAX_COOKIE_SIZE": 4093,
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "PERMANENT_SESSION_LIFETIME": "31 days, 0:00:00",
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "PER_PAGE": 30,
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "PREFERRED_URL_SCHEME": "http",
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "PROPAGATE_EXCEPTIONS": null,
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "SCHEMAS": {
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:         "mysql": "db_mysql.sql",
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:         "sqlite": "db_sqlite.sql"
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     },
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "SECRET_FRIENDLY_NAME": "mtdb-credentials",
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "SECRET_KEY": "development key",
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "SECRET_PASSWORD": "password",
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "SECRET_USERNAME": "username",
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "SEND_FILE_MAX_AGE_DEFAULT": null,
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "SERVER_NAME": null,
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "SESSION_COOKIE_DOMAIN": null,
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "SESSION_COOKIE_HTTPONLY": true,
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "SESSION_COOKIE_NAME": "session",
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "SESSION_COOKIE_PATH": null,
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "SESSION_COOKIE_SAMESITE": null,
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "SESSION_COOKIE_SECURE": false,
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "SESSION_REFRESH_EACH_REQUEST": true,
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "TEMPLATES_AUTO_RELOAD": null,
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "TESTING": false,
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "TRAP_BAD_REQUEST_ERRORS": null,
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "TRAP_HTTP_EXCEPTIONS": false,
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:     "USE_X_SENDFILE": false
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]: }
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]: [2023-03-09 01:16:26,174] INFO in minitwit: DB_SECRET_ARN=None
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]: [2023-03-09 01:16:26,224] INFO in minitwit: Unable to get credentials from secrets manager. Using stored credentials: Unable to locate credentials
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]: [2023-03-09 01:16:26,224] INFO in minitwit: db_type=mysql endpoint=mtdb.cwxg4mojlhdg.us-east-1.rds.amazonaws.com db=mtdb username=mtdbuser using_secret=False
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:  * Serving Flask app 'minitwit.py'
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:  * Debug mode: off
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]: WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:  * Running on all addresses (0.0.0.0)
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:  * Running on http://127.0.0.1:5000
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]:  * Running on http://10.105.238.6:5000
Mar 09 01:16:26 ip-10-105-238-6 flask[66728]: Press CTRL+C to quit
Mar 09 01:16:27 ip-10-105-238-6 flask[66728]: 10.105.238.68 - - [09/Mar/2023 01:16:27] "GET /public HTTP/1.1" 200 -
Mar 09 01:16:29 ip-10-105-238-6 flask[66728]: 10.105.238.5 - - [09/Mar/2023 01:16:29] "GET /public HTTP/1.1" 200 -
```

## Admin Env endpoint

* Just show the settings of the server
* It's important to show how the app is configured
* Protected with Basic auth

> **NOTE**: Credentials: `viasat:camper` 

```console
$ echo -n "viasat:camper" | base64 
dmlhc2F0OmNhbXBlcg==
```

```console
$ curl -i -H "Authorization: Basic dmlhc2F0OmNhbXBlcg==" http://localhost:4000/admin/env
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.8.16
Date: Thu, 09 Mar 2023 04:47:00 GMT
content-type: application/json
Content-Length: 700
Host: 5901c5e41daa
Connection: close

```
```json
{
  "_": "/usr/local/bin/python",
  "PATH": "/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
  "PYTHON_GET_PIP_URL": "https://github.com/pypa/get-pip/raw/d5cb0afaf23b8520f1bbcfed521017b4a95f5c01/public/get-pip.py",
  "LC_ALL": "en_US.utf-8",
  "PYTHON_GET_PIP_SHA256": "394be00f13fa1b9aaa47e911bdb59a09c3b2986472130f30aa0bfaf7f3980637",
  "PYTHON_PIP_VERSION": "22.0.4",
  "SHLVL": "1",
  "FLASK_APP": "minitwit.py",
  "LANG": "en_US.utf-8",
  "HOME": "/root",
  "PYTHON_SETUPTOOLS_VERSION": "57.5.0",
  "PWD": "/viasat/minitwit",
  "DB_DIR": "/var/minitwit",
  "PYTHON_VERSION": "3.8.16",
  "HOSTNAME": "879f79dddede",
  "WERKZEUG_SERVER_FD": "3"
}
```

## Admin Config Endpoint

* Used to help debug how the app is configured according to its internal settings

> **NOTE**: In production-grade services, this endpoint usually obfuscates secret values

```console
$ curl -i -H "Authorization: Basic dmlhc2F0OmNhbXBlcg==" http://localhost:4000/admin/config
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.8.16
Date: Thu, 09 Mar 2023 05:55:13 GMT
content-type: application/json
Content-Length: 1588
Host: 9dc7c92fe022
Connection: close

```
```json
{
  "ENV": "production",
  "DEBUG": false,
  "TESTING": false,
  "PROPAGATE_EXCEPTIONS": null,
  "SECRET_KEY": "development key",
  "PERMANENT_SESSION_LIFETIME": "31 days, 0:00:00",
  "USE_X_SENDFILE": false,
  "SERVER_NAME": null,
  "APPLICATION_ROOT": "/",
  "SESSION_COOKIE_NAME": "session",
  "SESSION_COOKIE_DOMAIN": null,
  "SESSION_COOKIE_PATH": null,
  "SESSION_COOKIE_HTTPONLY": true,
  "SESSION_COOKIE_SECURE": false,
  "SESSION_COOKIE_SAMESITE": null,
  "SESSION_REFRESH_EACH_REQUEST": true,
  "MAX_CONTENT_LENGTH": null,
  "SEND_FILE_MAX_AGE_DEFAULT": null,
  "TRAP_BAD_REQUEST_ERRORS": null,
  "TRAP_HTTP_EXCEPTIONS": false,
  "EXPLAIN_TEMPLATE_LOADING": false,
  "PREFERRED_URL_SCHEME": "http",
  "JSON_AS_ASCII": null,
  "JSON_SORT_KEYS": null,
  "JSONIFY_PRETTYPRINT_REGULAR": null,
  "JSONIFY_MIMETYPE": null,
  "TEMPLATES_AUTO_RELOAD": null,
  "MAX_COOKIE_SIZE": 4093,
  "CONFIG_DB_ENDPOINT": "DB_ENDPOINT",
  "CONFIG_DB_NAME": "DB_NAME",
  "CONFIG_DB_PASSWORD": "DB_PASSWORD",
  "CONFIG_DB_SECRET_ARN": "DB_SECRET_ARN",
  "CONFIG_DB_SECRET_KEY_PASSWORD": "DB_SECRET_KEY_PASSWORD",
  "CONFIG_DB_SECRET_KEY_USERNAME": "DB_SECRET_KEY_USERNAME",
  "CONFIG_DB_TYPE": "DB_TYPE",
  "CONFIG_DB_USER": "DB_USER",
  "DB_STASH": "db",
  "DB_TYPE_MYSQL": "mysql",
  "DB_TYPE_SQLITE": "sqlite",
  "LOCAL_DATABASE_URL": "sqlite:////var/minitwit/minitwit.db",
  "LOCAL_DB_TYPE": "sqlite",
  "PER_PAGE": 30,
  "SCHEMAS": {
    "sqlite": "db_sqlite.sql",
    "mysql": "db_mysql.sql"
  },
  "SECRET_FRIENDLY_NAME": "mtdb-credentials",
  "SECRET_PASSWORD": "password",
  "SECRET_USERNAME": "username",
  "IN_CLOUD": {
    "status": false,
    "metadata": {},
    "type": "local"
  },
  "HOSTNAME": "9dc7c92fe022"
}
```

* The server logs will show the current configs as well to record the request.

```console
minitwit-minitwit-runtime-1  | [2023-03-09 05:55:13,192] INFO in minitwit: Current config={"ENV": "production", "DEBUG": false, "TESTING": false, "PROPAGATE_EXCEPTIONS": null, "SECRET_KEY": "development key", "PERMANENT_SESSION_LIFETIME": "31 days, 0:00:00", "USE_X_SENDFILE": false, "SERVER_NAME": null, "APPLICATION_ROOT": "/", "SESSION_COOKIE_NAME": "session", "SESSION_COOKIE_DOMAIN": null, "SESSION_COOKIE_PATH": null, "SESSION_COOKIE_HTTPONLY": true, "SESSION_COOKIE_SECURE": false, "SESSION_COOKIE_SAMESITE": null, "SESSION_REFRESH_EACH_REQUEST": true, "MAX_CONTENT_LENGTH": null, "SEND_FILE_MAX_AGE_DEFAULT": null, "TRAP_BAD_REQUEST_ERRORS": null, "TRAP_HTTP_EXCEPTIONS": false, "EXPLAIN_TEMPLATE_LOADING": false, "PREFERRED_URL_SCHEME": "http", "JSON_AS_ASCII": null, "JSON_SORT_KEYS": null, "JSONIFY_PRETTYPRINT_REGULAR": null, "JSONIFY_MIMETYPE": null, "TEMPLATES_AUTO_RELOAD": null, "MAX_COOKIE_SIZE": 4093, "CONFIG_DB_ENDPOINT": "DB_ENDPOINT", "CONFIG_DB_NAME": "DB_NAME", "CONFIG_DB_PASSWORD": "DB_PASSWORD", "CONFIG_DB_SECRET_ARN": "DB_SECRET_ARN", "CONFIG_DB_SECRET_KEY_PASSWORD": "DB_SECRET_KEY_PASSWORD", "CONFIG_DB_SECRET_KEY_USERNAME": "DB_SECRET_KEY_USERNAME", "CONFIG_DB_TYPE": "DB_TYPE", "CONFIG_DB_USER": "DB_USER", "DB_STASH": "db", "DB_TYPE_MYSQL": "mysql", "DB_TYPE_SQLITE": "sqlite", "LOCAL_DATABASE_URL": "sqlite:////var/minitwit/minitwit.db", "LOCAL_DB_TYPE": "sqlite", "PER_PAGE": 30, "SCHEMAS": {"sqlite": "db_sqlite.sql", "mysql": "db_mysql.sql"}, "SECRET_FRIENDLY_NAME": "mtdb-credentials", "SECRET_PASSWORD": "password", "SECRET_USERNAME": "username", "IN_CLOUD": {"status": false, "metadata": {}, "type": "local"}, "HOSTNAME": "9dc7c92fe022"}
minitwit-minitwit-runtime-1  | 192.168.208.1 - - [09/Mar/2023 05:55:13] "GET /admin/config HTTP/1.1" 200 -
```

## Admin Endpoints Endpoint

* Used to help debug how the app is configured according to its internal settings

> **NOTE**: In production-grade services, this endpoint usually obfuscates secret values

```console
$ curl -i -H "Authorization: Basic dmlhc2F0OmNhbXBlcg==" http://localhost:4000/admin/endpoints
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.8.16
Date: Thu, 09 Mar 2023 14:29:06 GMT
content-type: application/json
Content-Length: 256
Host: 52900b592410
Connection: close

```
```json
[
  "/static/<path:filename>",
  "/",
  "/public",
  "/<username>",
  "/<username>/follow",
  "/<username>/unfollow",
  "/add_message",
  "/login",
  "/register",
  "/logout",
  "/healthcheck/liveness",
  "/healthcheck/readiness",
  "/admin/env",
  "/admin/config",
  "/admin/endpoints"
]
```

## Healthcheck Endpoints

* When architecting for cloud systems, make sure to have Healthcheck Probe services to make sure the service is working.

> **NOTE**: AWS documents this well at https://aws.amazon.com/builders-library/implementing-health-checks/

### `Liveness`

* Concept borrowed from Kubernetes, it defines if the app is running at the port that's been set.
* This can be used by the load balancer for less latency, better performance! Content-type of 2 bytes.

> **NOTE**: Flask apps sets default port number to 5000. If the app responds to the request, then it's 
> enough evidence that the service is alive.

```console
$ curl -i localhost:4000/admin/health/liveness 
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.8.16
Date: Thu, 09 Mar 2023 04:19:43 GMT
content-type: text/plain
Content-Length: 2
Host: 879f79dddede
Connection: close

Ok
```

### `Readiness`

* Implements a deep healthcheck in the sense that it will check if the dependent services are responding...

> **NOTE**: This is checking if RDS is available! Architectural decisions may be considered
> * This shouldn't be called by a load-balancer due to its frequency! Mostly by Fleet Admin Dashboards.

```console
$ curl -i localhost:4000/admin/health/readiness
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.8.16
Date: Thu, 09 Mar 2023 04:19:49 GMT
content-type: application/json
Content-Length: 129
Host: 879f79dddede
Connection: close

```
```json
{
  "overall": 200,
  "server": 200,
  "database": {
    "type": "sqlite",
    "resource": "sqlite:////var/minitwit/minitwit.db",
    "status": 200
  }
}
```

# Production Readiness

* Using Healthcheck endpoints for the load balancer
* Using HTTP Response headers for debugging the deployed app

## List of Endpoints

* When the app bootstraps, it will log its available endpoints
* It's helpful to verify if an existing or new endpoint is available

```console
minitwit-minitwit-runtime-1  | [2023-03-09 14:28:31,969] INFO in config_service: 
  Endpoints: ['/static/<path:filename>', '/', '/public', '/<username>', 
              '/<username>/follow', '/<username>/unfollow', '/add_message', 
              '/login', '/register', '/logout', '/healthcheck/liveness', 
              '/healthcheck/readiness', '/admin/env', '/admin/config', 
              '/admin/endpoints']
```

## HTTP Response Headers for Debugging

* That way you can make sure which server is responding

| HTTP Request  | Description                                                                    | Always returned | 
|---------------|--------------------------------------------------------------------------------|-----------------|
| Host          | Shows either the public hostname when in the cloud or the host's defined name  | Yes             |
| X-Host-AZ     | Which region served the request, only returned when the app is in the cloud    | No              |
| X-App-Version | The version of the server running based on git, only when the version is known | NO              | 

* Here's an example of the sequence of calls being load-balanced by the Load Balancer.

```console
☁️  aws-cli@2.9.15
☸️  kubectl@1.24.3 📛 kustomize@1.24.3 🎡 helm@3.10.2    🐳 docker@20.10.21-rd 🐙 docker-compose@v2.14.0
👮 marcellodesales
🏗  1.24.3+k3s1 🔐 rancher-desktop 🍱 default
~/dev/git.viasat.com/mdesales/minitwit on  feature/implement-admin-actuator-endpoints-better-logging! 📅 03-08-2023 ⌚22:22:16
$ curl -i http://web-server-alb-193477983.us-east-1.elb.amazonaws.com/admin/health/liveness
HTTP/1.1 200 OK
Date: Thu, 09 Mar 2023 06:22:22 GMT
Content-Type: text/plain
Content-Length: 2
Connection: keep-alive
Set-Cookie: AWSALB=9LauYKPy6bF6sQcIU6CTJ4UE6fLY8SWdHvPgVLdyXRiHjPMPNVckdKVfm5dq6Da5UFO/j617pAH2rDOB72eWh96dh2l+7hi9jHV5O8LrgcIK7wjiXOf0f0HECTV0; Expires=Thu, 16 Mar 2023 06:22:22 GMT; Path=/
Set-Cookie: AWSALBCORS=9LauYKPy6bF6sQcIU6CTJ4UE6fLY8SWdHvPgVLdyXRiHjPMPNVckdKVfm5dq6Da5UFO/j617pAH2rDOB72eWh96dh2l+7hi9jHV5O8LrgcIK7wjiXOf0f0HECTV0; Expires=Thu, 16 Mar 2023 06:22:22 GMT; Path=/; SameSite=None
Server: Werkzeug/2.2.3 Python/3.8.10
Host: ec2-52-21-148-181.compute-1.amazonaws.com
X-Host-AZ: us-east-1b
X-App-Version: 3a41fcd

Ok%

☁️  aws-cli@2.9.15
☸️  kubectl@1.24.3 📛 kustomize@1.24.3 🎡 helm@3.10.2    🐳 docker@20.10.21-rd 🐙 docker-compose@v2.14.0
👮 marcellodesales
🏗  1.24.3+k3s1 🔐 rancher-desktop 🍱 default
~/dev/git.viasat.com/mdesales/minitwit on  feature/implement-admin-actuator-endpoints-better-logging! 📅 03-08-2023 ⌚22:22:22
$ curl -i http://web-server-alb-193477983.us-east-1.elb.amazonaws.com/admin/health/liveness
HTTP/1.1 200 OK
Date: Thu, 09 Mar 2023 06:22:24 GMT
Content-Type: text/plain
Content-Length: 2
Connection: keep-alive
Set-Cookie: AWSALB=V+bO/NliUaRN/WNGcOsskLc6dyugcw1GtlHHejF1G3xu0pH0SYZ8tMChnJR/AT9oPt2CTYNV07CvOTfcDjmjPSsvj8BG1QnX/5Anc0R0WodpWO3+kAgaDXW+kJ4v; Expires=Thu, 16 Mar 2023 06:22:24 GMT; Path=/
Set-Cookie: AWSALBCORS=V+bO/NliUaRN/WNGcOsskLc6dyugcw1GtlHHejF1G3xu0pH0SYZ8tMChnJR/AT9oPt2CTYNV07CvOTfcDjmjPSsvj8BG1QnX/5Anc0R0WodpWO3+kAgaDXW+kJ4v; Expires=Thu, 16 Mar 2023 06:22:24 GMT; Path=/; SameSite=None
Server: Werkzeug/2.2.3 Python/3.8.10
Host: ec2-44-214-35-206.compute-1.amazonaws.com
X-Host-AZ: us-east-1a
X-App-Version: 3a41fcd

Ok%
```

### Verifying Config Version

* When running in the cloud, it will include information about the current version deployed as well.
  * See the value `X-App-Version: aa86e8b` in the HTTP Header (see section below)
* The verification can be done going to Github at https://github.com/marcellodesales/minitwit/commit/aa86e8b
  * The branch is returned by config property `BUILD_GIT_BRANCH`, verified at https://github.com/marcellodesales/minitwit/commits/feature/implement-admin-actuator-endpoints-better-logging

```console
$ curl -i http://web-server-alb-193477983.us-east-1.elb.amazonaws.com/admin/config
HTTP/1.1 200 OK
Date: Thu, 09 Mar 2023 06:25:15 GMT
Content-Type: application/json
Content-Length: 2415
Connection: keep-alive
Set-Cookie: AWSALB=iboZ/qrg3HbYcxZcXhEMtYfPBrY8kfkx3DIp63q6wICBi7byUlI7ZGFF5kVplV0ntoqHN/OKSGSLgKJzW7csQnUwZACYgvD69CZ2uOYm6n3eJULrHjmiGT5coOi8; Expires=Thu, 16 Mar 2023 06:25:15 GMT; Path=/
Set-Cookie: AWSALBCORS=iboZ/qrg3HbYcxZcXhEMtYfPBrY8kfkx3DIp63q6wICBi7byUlI7ZGFF5kVplV0ntoqHN/OKSGSLgKJzW7csQnUwZACYgvD69CZ2uOYm6n3eJULrHjmiGT5coOi8; Expires=Thu, 16 Mar 2023 06:25:15 GMT; Path=/; SameSite=None
Server: Werkzeug/2.2.3 Python/3.8.10
Host: ec2-44-214-35-206.compute-1.amazonaws.com
X-Host-AZ: us-east-1a
X-App-Version: aa86e8b

```
```json
{
  "ENV": "production",
  "DEBUG": false,
  "TESTING": false,
  "PROPAGATE_EXCEPTIONS": null,
  "SECRET_KEY": "development key",
  "PERMANENT_SESSION_LIFETIME": "31 days, 0:00:00",
  "USE_X_SENDFILE": false,
  "SERVER_NAME": null,
  "APPLICATION_ROOT": "/",
  "SESSION_COOKIE_NAME": "session",
  "SESSION_COOKIE_DOMAIN": false,
  "SESSION_COOKIE_PATH": null,
  "SESSION_COOKIE_HTTPONLY": true,
  "SESSION_COOKIE_SECURE": false,
  "SESSION_COOKIE_SAMESITE": null,
  "SESSION_REFRESH_EACH_REQUEST": true,
  "MAX_CONTENT_LENGTH": null,
  "SEND_FILE_MAX_AGE_DEFAULT": null,
  "TRAP_BAD_REQUEST_ERRORS": null,
  "TRAP_HTTP_EXCEPTIONS": false,
  "EXPLAIN_TEMPLATE_LOADING": false,
  "PREFERRED_URL_SCHEME": "http",
  "JSON_AS_ASCII": null,
  "JSON_SORT_KEYS": null,
  "JSONIFY_PRETTYPRINT_REGULAR": null,
  "JSONIFY_MIMETYPE": null,
  "TEMPLATES_AUTO_RELOAD": null,
  "MAX_COOKIE_SIZE": 4093,
  "CONFIG_DB_ENDPOINT": "DB_ENDPOINT",
  "CONFIG_DB_NAME": "DB_NAME",
  "CONFIG_DB_PASSWORD": "DB*****RD",
  "CONFIG_DB_SECRET_ARN": "DB_SECRET_ARN",
  "CONFIG_DB_SECRET_KEY_PASSWORD": "DB*****RD",
  "CONFIG_DB_SECRET_KEY_USERNAME": "DB_SECRET_KEY_USERNAME",
  "CONFIG_DB_TYPE": "DB_TYPE",
  "CONFIG_DB_USER": "DB_USER",
  "DB_STASH": "db",
  "DB_TYPE_MYSQL": "mysql",
  "DB_TYPE_SQLITE": "sqlite",
  "LOCAL_DB_TYPE": "sqlite",
  "PER_PAGE": 30,
  "SCHEMAS": {
    "sqlite": "db_sqlite.sql",
    "mysql": "db_mysql.sql"
  },
  "SECRET_FRIENDLY_NAME": "mtdb-credentials",
  "SECRET_PASSWORD": "pa*****rd",
  "SECRET_USERNAME": "username",
  "BUILD_GIT_BRANCH": "feature/implement-admin-actuator-endpoints-better-logging",
  "BUILD_GIT_REPO": "https://github.com/marcellodesales/minitwit.git",
  "BUILD_GIT_VERSION": "a3b58ebb788674640e08c39f515fad8869ececc4",
  "DB_ENDPOINT": "mtdb.cwxg4mojlhdg.us-east-1.rds.amazonaws.com",
  "DB_NAME": "mtdb",
  "DB_PASSWORD": "mt*****rd",
  "DB_TYPE": "mysql",
  "DB_USER": "mtdbuser",
  "IN_CLOUD": {
    "status": true,
    "metadata": {
      "accountId": "178468422646",
      "architecture": "x86_64",
      "availabilityZone": "us-east-1b",
      "billingProducts": null,
      "devpayProductCodes": null,
      "marketplaceProductCodes": null,
      "imageId": "ami-09cd747c78a9add63",
      "instanceId": "i-0bcc19c577d3a108d",
      "instanceType": "t3.medium",
      "kernelId": null,
      "pendingTime": "2023-03-08T19:54:48Z",
      "privateIp": "10.105.238.77",
      "ramdiskId": null,
      "region": "us-east-1",
      "version": "2017-09-30"
    },
    "type": "ec2"
  },
  "LOCAL_DATABASE_URL": "sqlite:////var/minitwit/minitwit.db",
  "HOSTNAME": "ec2-52-21-148-181.compute-1.amazonaws.com"
}
```

## Load Balancer Reaching app

* The healthcheck for liveness should be called by the Load Balancer
* You can use the endpoint `/healthcheck/liveness` as it is faster to server

```console
+ ssh -i key.pem ubuntu@52.21.148.181 sudo journalctl -u minitwit -n 100
-- Logs begin at Wed 2023-03-08 19:54:59 UTC, end at Thu 2023-03-09 10:58:07 UTC. --
Mar 09 10:55:38 ip-10-105-238-77 flask[45627]: [2023-03-09 10:55:38,526] INFO in healthcheck_routes: App successfully listening on port
Mar 09 10:55:38 ip-10-105-238-77 flask[45627]: 10.105.238.5 - - [09/Mar/2023 10:55:38] "GET /healthcheck/liveness HTTP/1.1" 200 -
Mar 09 10:55:42 ip-10-105-238-77 flask[45627]: [2023-03-09 10:55:42,431] INFO in healthcheck_routes: App successfully listening on port
Mar 09 10:55:42 ip-10-105-238-77 flask[45627]: 10.105.238.68 - - [09/Mar/2023 10:55:42] "GET /healthcheck/liveness HTTP/1.1" 200 -
Mar 09 10:56:02 ip-10-105-238-77 flask[45627]: [2023-03-09 10:56:02,549] INFO in healthcheck_routes: App successfully listening on port
Mar 09 10:56:02 ip-10-105-238-77 flask[45627]: 10.105.238.5 - - [09/Mar/2023 10:56:02] "GET /healthcheck/liveness HTTP/1.1" 200 -
Mar 09 10:56:06 ip-10-105-238-77 flask[45627]: [2023-03-09 10:56:06,452] INFO in healthcheck_routes: App successfully listening on port
Mar 09 10:56:06 ip-10-105-238-77 flask[45627]: 10.105.238.68 - - [09/Mar/2023 10:56:06] "GET /healthcheck/liveness HTTP/1.1" 200 -
Mar 09 10:56:08 ip-10-105-238-77 flask[45627]: [2023-03-09 10:56:08,555] INFO in healthcheck_routes: App successfully listening on port
Mar 09 10:56:08 ip-10-105-238-77 flask[45627]: 10.105.238.5 - - [09/Mar/2023 10:56:08] "GET /healthcheck/liveness HTTP/1.1" 200 -
Mar 09 10:56:12 ip-10-105-238-77 flask[45627]: [2023-03-09 10:56:12,459] INFO in healthcheck_routes: App successfully listening on port
Mar 09 10:56:12 ip-10-105-238-77 flask[45627]: 10.105.238.68 - - [09/Mar/2023 10:56:12] "GET /healthcheck/liveness HTTP/1.1" 200 -
Mar 09 10:56:14 ip-10-105-238-77 flask[45627]: [2023-03-09 10:56:14,562] INFO in healthcheck_routes: App successfully listening on port
Mar 09 10:56:14 ip-10-105-238-77 flask[45627]: 10.105.238.5 - - [09/Mar/2023 10:56:14] "GET /healthcheck/liveness HTTP/1.1" 200 
```

## Securing Admin APIs

* Since they are used by Dashboards, they need to have a separate authentication method
  * We are going to use basic auth

> **NOTE**: All Admin endpoints are now secured by basic auth for demo purposes

```console
$ curl -I http://web-server-alb-193477983.us-east-1.elb.amazonaws.com/admin/config
HTTP/1.1 401 UNAUTHORIZED
Date: Thu, 09 Mar 2023 12:25:17 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 19
Connection: keep-alive
Set-Cookie: AWSALB=ZUbJSWsUq4PnmlaGA0Z7G+SK/UobQMBY4GQz8Uwd6dDbvvr4BNBXSlIiGJZaXz5UzA5jN7SNrSstHH485ONsYNtXx1pXSmFbzOFp3G6os6FXTggBS/dzY79SPYHG; Expires=Thu, 16 Mar 2023 12:25:17 GMT; Path=/
Set-Cookie: AWSALBCORS=ZUbJSWsUq4PnmlaGA0Z7G+SK/UobQMBY4GQz8Uwd6dDbvvr4BNBXSlIiGJZaXz5UzA5jN7SNrSstHH485ONsYNtXx1pXSmFbzOFp3G6os6FXTggBS/dzY79SPYHG; Expires=Thu, 16 Mar 2023 12:25:17 GMT; Path=/; SameSite=None
Server: Werkzeug/2.2.3 Python/3.8.10
WWW-Authenticate: Basic realm="Authentication Required"
Host: ec2-52-21-148-181.compute-1.amazonaws.com
X-Host-AZ: us-east-1b
X-App-Version: 908b2ca

Unauthorized Access%
```

The server will report that

```console
Mar 09 12:27:24 ip-10-105-238-6 flask[98744]: 10.105.238.5 - - [09/Mar/2023 12:27:24] "GET /admin/config HTTP/1.1" 401 -
```

* The only way now is to provide the header `Authorization` using its basic form.
  * https://en.wikipedia.org/wiki/Basic_access_authentication

```console
$ echo -n "viasat:camper" | base64
dmlhc2F0OmNhbXBlcg==
```

* Now, prepare a new authentication...

```console
$ curl -I -H "Authorization: Basic dmlhc2F0OmNhbXBlcg==" http://web-server-alb-193477983.us-east-1.elb.amazonaws.com/admin/config
HTTP/1.1 200 OK
Date: Thu, 09 Mar 2023 12:26:25 GMT
Content-Type: application/json
Content-Length: 2399
Connection: keep-alive
Set-Cookie: AWSALB=FPv2Ml8aDpumOg+Pe3TlnXbS9DOt8REHiBDX5l0o3PdKCtZQ+51ypjRiT0d47bAzapgoLUCEHAxmWM3KG28d+s4cENONgrOILodZTSeFM5yzPUU0EPd8cjjkMoM5; Expires=Thu, 16 Mar 2023 12:26:25 GMT; Path=/
Set-Cookie: AWSALBCORS=FPv2Ml8aDpumOg+Pe3TlnXbS9DOt8REHiBDX5l0o3PdKCtZQ+51ypjRiT0d47bAzapgoLUCEHAxmWM3KG28d+s4cENONgrOILodZTSeFM5yzPUU0EPd8cjjkMoM5; Expires=Thu, 16 Mar 2023 12:26:25 GMT; Path=/; SameSite=None
Server: Werkzeug/2.2.3 Python/3.8.10
Host: ec2-52-21-148-181.compute-1.amazonaws.com
X-Host-AZ: us-east-1b
X-App-Version: 908b2ca
```

* Now the server shows ok!