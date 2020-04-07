# fastapi-example

A very basic fastAPI application that serves data from a sqlite database. Run using

```
uvicorn sql_app.main:app --reload
```

### Dependencies

```
pip install fastapi uvicorn sqlalchemy
```

If you want to regenerate the database you'll also need to install pandas

```
pip install pandas
```