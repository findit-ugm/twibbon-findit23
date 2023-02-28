# Twibbon Find IT! 2023

Ini merupakan repo ML API untuk pengecekan twibbon peserta Find IT!.

<br>

## Prerequisite

- python3.10
- python3.10-venv

Create python virtual environment ex; python-venv, python-virtualenv etc.
Type script on active directories

```sh
$ virtualenv -m venv
```

Activate your python environment
```sh
$ source bin/activate
(venv)$ 
```

Install dependencies.
```sh
(venv)$ pip install -r requirements.txt
```

## Activate FastApi

```sh
(venv)$ python src/main.py
```

Access at `http://0.0.0.0:8000/docs/`

**Input instagram format** 

`https://www.instagram.com/p/Co3XdlDBqQx/`
`https://www.instagram.com/p/Co3XdlDBqQx`