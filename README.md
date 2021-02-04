<h1 align="center">Website RESTful API :cloud:</h1>

<p align="center">
  <img src="https://circleci.com/gh/chapmankyle/website-api/tree/master.svg?style=svg" alt="Build Status"></img>
  <img src="https://img.shields.io/github/license/chapmankyle/website-api.svg?" alt="license: GPL-3.0"></img>
  <img src="https://img.shields.io/github/v/release/chapmankyle/website-api.svg?" alt="Release"></img>
</p>

Official API endpoint is available at https://kylechapman-api.netlify.app/ :zap:

Official portfolio website is available at https://kylechapman.netlify.app/ :tada:

This repository serves as the source code for the RESTful API that serves content to my website :cloud:

# Setup :rocket:

Clone the repository and navigate to the `website-api` directory.
```bash
# clone the repo
git clone git@github.com:chapmankyle/website-api.git

# navigate to the `website-api` directory
cd website-api
```

You need to have [Python3](https://www.python.org/downloads/) installed in order to compile
from the source code.

# Building :hammer:

You need to install all the requirements first, so type the following into the
terminal of your choice:
```bash
# install requirements
pip install -r requirements.txt
```

You can now run the RESTful API server by typing the following:
```bash
python main.py
```

The RESTful API is now accessible at http://localhost:5000 :tada:
