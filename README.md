<h1 align="center">Website RESTful API :cloud:</h1>

<p align="center">
  <img src="https://github.com/chapmankyle/website-api/actions/workflows/deploy.yml/badge.svg" alt="Deploy status"></img>
  <img src="https://img.shields.io/github/license/chapmankyle/website-api.svg?" alt="license: GPL-3.0"></img>
  <img src="https://img.shields.io/github/v/release/chapmankyle/website-api.svg?" alt="Release"></img>
</p>

Official API endpoint is available at https://api.kylechapman.dev/ :zap:

Official portfolio website is available at https://kylechapman.dev/ :tada:

This repository serves as the source code for the RESTful API that serves content to my website :cloud:

# Routes :surfer:

All routes other than `/` are protected by Bearer authorization, just to make sure nobody other than myself can touch that data.
However, if you really want the data, then it is in the `src/data.json` file of this repo.

| Endpoint      | Methods       | Description |
| :------------ | :-----------: | :---------- |
| `/`           | `GET` | Returns a welcome message. |
| `/all`        | `GET` | Returns all of the information from the API. |
| `/metadata`   | `GET` | Returns the metadata used for SEO in my website. |
| `/experience` | `GET` | Returns my software development experience. |
| `/education`  | `GET` | Returns my education. |
| `/projects`   | `GET` | Returns my personal projects |
| `/contact`    | `GET` | Returns my contact informaton |

# Setup :rocket:

Clone the repository and navigate to the `website-api` directory.
```bash
# clone the repo
git clone git@github.com:chapmankyle/website-api.git

# navigate to the `website-api` directory
cd website-api
```

You need to have <a href="https://bun.sh/"><img src="public/static/bun.svg" width="16" height="16" style="position: relative; top: 3px;" /> Bun</a> installed in order to compile from the source code.

# Building :hammer:

You need to install all the requirements first, so type the following into the
terminal of your choice:
```bash
# install requirements
bun install
```

You can now run the RESTful API server by typing the following:
```bash
# run locally
bun run dev
```

The RESTful API is now accessible at http://localhost:8787 :tada:
