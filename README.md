## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Components](#components)

## Overview

Project structure is as follows:

- root
    - app
        - api
        - ui
            - public
            - src
    - data


`data` contains a Dockerfile and init script for the Postgres database.

`app` contains the API and UI used by the app. The Dockerfile at this location creates the Python/Nodejs server used for the application. The UI is a consumer of the API, and the API is a consumer of the Postgres database. All Python and Node code has been linted with `pylint` and `eslint`

## Installation

### Pre-requisites
- Docker engine
- Docker compose plugin

### Build Project
After cloning repo, navigate to the project root and execute:

```bash
docker compose up
```
## Usage

After Docker compose has created all the components, navigate a browser to `http://127.0.0.1:5001`

This simple app is a list of automobiles by make and model. A list of automobiles is pre-loaded. New makes and models can be added with the form.

## Components
To build the code components separately, you'll need:
- Python3
- pip3
- Nodejs
- npm

#### UI
Navigate to `ui` and execute:
```bash
npm install
npm run build
```

#### API
Navigate to `api` and execute:
```bash
pip install -r requirements.txt
python3 -m flask run
```
