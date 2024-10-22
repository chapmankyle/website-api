<h1 align="center">Website RESTful API :cloud:</h1>

<p align="center">
  <img src="https://img.shields.io/github/license/chapmankyle/website-api.svg?" alt="license: GPL-3.0"></img>
  <img src="https://img.shields.io/github/v/release/chapmankyle/website-api.svg?" alt="Release"></img>
</p>

Official API endpoint is available at https://kylechapman-api.netlify.app/ :zap:

Official portfolio website is available at https://kylechapman.netlify.app/ :tada:

This repository serves as the source code for the RESTful API that serves content to my website :cloud:

# Routes :surfer:

| Endpoint      | Methods       | Description |
| :------------ | :-----------: | :---------- |
| `/`           | `GET`         | Returns a welcome message. |
| `/banner`     | `GET`         | Returns the banner information displayed on the Home page. |
| `/about`      | `GET`         | Returns the 'About Me' information displayed on the Home page. |
| `/story`      | `GET`         | Returns the 'Personal Story' information displayed on the Home page. |
| `/projects`   | `GET`, `POST` | Returns the current projects (`GET`) or adds a project (`POST`) |
| `/experience` | `GET`, `POST` | Returns the current experience (`GET`) or adds to the experiences (`POST`) |
| `/education`  | `GET`, `POST` | Returns the current education (`GET`) or adds an education (`POST`) |

# Setup :rocket:

Clone the repository and navigate to the `website-api` directory.
```bash
# clone the repo
git clone git@github.com:chapmankyle/website-api.git

# navigate to the `website-api` directory
cd website-api
```

You need to have <a href="https://bun.sh/"><img src="images/bun.svg" width="16" height="16" style="position: relative; top: 3px;" /> Bun</a> installed in order to compile from the source code.

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
