## Dependencies:

- [Python3](https://www.python.org/downloads/)

### Pip:

- SQLAlchemy `pip install flask-sqlalchemy`
- Flask `pip install flask`
- SQLite3 `pip install db-sqlite3` (Just in case)

## To run the server

You must have the above dependencies installed. Once this is done, simply run
`python3 server.py <PORT>`, where `<PORT>` is your desired port number (default 8000)

Alternatively, you can run the startup script firstly with `chmod +x run` and then `./run`.
The first command only needs to be run once for installation.
This was made with Python 3.9 and should work with older versions of Python 3, however if you have any issues, please try installing Python 3.9.


## How this server works

This server uses Flask as a backend, which handles requests, routing, and serving inside `server.py`.

The SQLite3
