
# Data Analysis Jupyter Notebook Templates - ODOT Crash Data
* [Locally Running Postgres Server](#local-postgres-sever)
* [Locally Running API](#local-api)

## Local Postgres Server

To access the ODOT crash data through a local copy of the Postgres database.
* Make sure you have the Docker container set up and running (instructions [here](https://github.com/hackoregon/transportation-system-backend)).

* Import the `psycopg2` Postgres adaptor for python (can be installed with `pip` or `conda`).

```python
import psycopg2
```

* Use the Pandas data analysis library to handle the database data.

```python
import pandas as pd
```


* Create a connection object `conn` to the database using the listed arguments. Of important note is matching `dbname` to the one you're looking for, and that the `port` # is correct (I believe it is defined by the Docker container. Make sure to use the `password` you set in the .env file when setting up the database).

```python
conn = psycopg2.connect(host='localhost',
                        dbname='odot_crash_data',
                        user='postgres',
                        port='5439',
                        password='<sUpEr.SeCrEt.PaSsWoRD>')
```

* For a little information about the database, we can get a list of the table names from the schema using a `curs` object.

```python
curs.execute("""SELECT table_name FROM information_schema.tables WHERE table_schema='public'""")
tables = [x[0] for x in curs.fetchall()]
print(tables)
```

* Currently, we've identified the "crash", "vhcl" and "partic" tables as the ones to begin with. However, there are additional tables available that are NOT yet enabled in the API. To make a DataFrame out of one of them, in this case the "crash" database, use the `pd.read_sql()` method. This usage pulls the full table into a pandas DataFrame.

```python
dataframe = pd.read_sql("SELECT * FROM crash", conn)
```

* After just a second, the DataFrame should be populated. To view the first couple of rows, use the `.head()` method.

```python
dataframe.head()
```

Now you have a pandas DataFrame full with your odot crash data using a locally run copy of the Postgres database!


```python
import psycopg2
import pandas as pd
conn = psycopg2.connect(host='localhost', dbname='odot_crash_data', user='postgres', port='5439', password='')
curs = conn.cursor()
curs.execute("""SELECT table_name FROM information_schema.tables WHERE table_schema='public'""")
tables = [_[0] for _ in curs.fetchall()]
print(tables)
dataframe = pd.read_sql("SELECT * FROM crash", conn)
dataframe.head()
```

## Local API

To access the ODOT crash data through a local copy of the API.

* Make sure you have the Docker container set up and running (instructions [here](https://github.com/hackoregon/transportation-system-backend)).

* Import the `requests` library to make the API calls.

```python
import requests
```

* Use the Pandas data analysis library to handle the database data.

```python
import pandas as pd
```


* First make a call to the base api. That will give schema information.

```python
response = requests.get('http://localhost:8000/api/')
for key in response.json().keys()
    print(key)
```

* To access a specific table from that list, enter it into the next field in the URL. In this call, we'll see how many records are in the "crashes" table. This can be found in the 'count' field of the json response object. If you were curious, the other fields available in addition to 'count' are 'next', 'previous', and 'results'. The 'next' and 'previous' fields are used to access the pagination.

```python
response = requests.get('http://localhost:8000/api/crashes/')
num_records = response.json()['count']
```

* Anyway, now that we have the record count, we can pull the full database at once (rather than paginate) by passing `num_records` as the 'limit' parameter in our query. If no 'limit' parameter is passed, the default pagination returns 10 records. Note: This makes use of Python f-strings, which came about in Python 3.6.

```python
response = requests.get(f"http://localhost:8000/api/crashes/?limit={num_records}")
```

* This call may take some time (for all the records), but after it returns you can create a DataFrame directly from the 'results' field of the json response object. 

```python
df_crash = pd.DataFrame(response.json()['results'])
```

* To view the first couple of rows of the data, use the `.head()` method.

```python
dataframe.head()
```

* Finally, you may was to set the `crash_id` field as the index of the DataFrame. To do so:

```python
df_crash.set_index('crash_id', drop=True, inplace=True)
```

Now you have a pandas DataFrame full with your odot crash data using a locally run copy of the API!


```python
import requests
import pandas as pd
# Get API schema.
response = requests.get('http://localhost:8000/api/')
for key in response.json().keys():
    print(key)
# Get the 'crashes' table record count.
response = requests.get('http://localhost:8000/api/crashes/')
num_records = response.json()['count']
# Pull all the records from the 'crashes' table.
response = requests.get(f"http://localhost:8000/api/crashes/?limit={num_records}")
dataframe = pd.DataFrame(response.json()['results'])
dataframe.set_index('crash_id', drop=True, inplace=True)
dataframe.head()
```
