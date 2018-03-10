
# Data Analysis Jupyter Notebook Templates - ODOT Crash Data
* [Locally Running Postgres Server](Accessing_API_and_Postgres_in_Python.md#local-postgres-server)
* [Locally Running API](Accessing_API_and_Postgres_in_Python.md#local-api)

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

    ['mvmnt', 'geography_columns', 'geometry_columns', 'spatial_ref_sys', 'raster_columns', 'raster_overviews', 'lgt_cond', 'medn_typ', 'mlge_typ', 'non_motrst_loc', 'partic', 'partic_typ', 'pop_rng', 'actn', 'cause', 'city_fips_hist', 'city_sect', 'cmpss_drct', 'cnty', 'collis_typ', 'crash', 'crash_hr', 'crash_key_xref', 'crash_svrty', 'crash_typ', 'drvr_lic_stat', 'drvr_res_stat', 'err', 'evnt', 'func_class', 'hwy_compnt', 'hwy_hist', 'impct_loc', 'inj_svrty', 'invstg_agy', 'isect_typ', 'jrsdct_grp', 'rd_char', 'rd_cntl', 'rd_surf_cond', 'rdwy', 'rte', 'sex', 'sfty_equip_use', 'specl_jrsdct', 'traf_cntl_device', 'urb_area', 'urb_area_fips_hist', 'vhcl', 'vhcl_ownshp', 'vhcl_typ', 'vhcl_use', 'wkday', 'wthr_cond', 'django_migrations', 'django_content_type', 'auth_group_permissions', 'auth_group', 'auth_user_groups', 'django_session', 'auth_permission', 'auth_user_user_permissions', 'auth_user', 'django_admin_log']





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>row.names</th>
      <th>crash_id</th>
      <th>ser_no</th>
      <th>crash_dt</th>
      <th>crash_mo_no</th>
      <th>crash_day_no</th>
      <th>crash_yr_no</th>
      <th>crash_wk_day_cd</th>
      <th>crash_hr_no</th>
      <th>crash_hr_short_desc</th>
      <th>...</th>
      <th>tot_sfty_equip_use_unknown_qty</th>
      <th>tot_psngr_vhcl_occ_unrestrnd_fatal_cnt</th>
      <th>tot_mcyclst_fatal_cnt</th>
      <th>tot_mcyclst_inj_lvl_a_cnt</th>
      <th>tot_mcyclst_inj_cnt</th>
      <th>tot_mcyclst_unhelmtd_fatal_cnt</th>
      <th>tot_alchl_impaired_drvr_inv_fatal_cnt</th>
      <th>tot_drvr_age_01_20_cnt</th>
      <th>lane_rdwy_dprt_crash_flg</th>
      <th>geom_4269</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1096439</td>
      <td>00058</td>
      <td>01/05/04 00:00:00</td>
      <td>1</td>
      <td>5</td>
      <td>2004</td>
      <td>2</td>
      <td>20</td>
      <td>8P</td>
      <td>...</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>N</td>
      <td>None</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1096444</td>
      <td>00056</td>
      <td>01/05/04 00:00:00</td>
      <td>1</td>
      <td>5</td>
      <td>2004</td>
      <td>2</td>
      <td>17</td>
      <td>5P</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>N</td>
      <td>None</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1096447</td>
      <td>00031</td>
      <td>01/03/04 00:00:00</td>
      <td>1</td>
      <td>3</td>
      <td>2004</td>
      <td>7</td>
      <td>4</td>
      <td>4A</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>Y</td>
      <td>None</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1096449</td>
      <td>00005</td>
      <td>01/02/04 00:00:00</td>
      <td>1</td>
      <td>2</td>
      <td>2004</td>
      <td>6</td>
      <td>18</td>
      <td>6P</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>N</td>
      <td>None</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>1096452</td>
      <td>00018</td>
      <td>01/02/04 00:00:00</td>
      <td>1</td>
      <td>2</td>
      <td>2004</td>
      <td>6</td>
      <td>12</td>
      <td>12P</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>N</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 146 columns</p>
</div>



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

    crashes
    participants
    vehicles





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>agy_st_no</th>
      <th>alchl_invlv_flg</th>
      <th>city_sect_id</th>
      <th>city_sect_nm</th>
      <th>cmpss_dir_cd</th>
      <th>cnty_id</th>
      <th>cnty_nm</th>
      <th>collis_typ_cd</th>
      <th>collis_typ_short_desc</th>
      <th>crash_cause_1_cd</th>
      <th>...</th>
      <th>traf_cntl_device_cd</th>
      <th>traf_cntl_device_short_desc</th>
      <th>traf_cntl_func_flg</th>
      <th>turng_leg_qty</th>
      <th>unloct_flg</th>
      <th>urb_area_cd</th>
      <th>urb_area_short_nm</th>
      <th>wrk_zone_ind</th>
      <th>wthr_cond_cd</th>
      <th>wthr_cond_short_desc</th>
    </tr>
    <tr>
      <th>crash_id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1593309</th>
      <td>00457</td>
      <td>1</td>
      <td>245</td>
      <td>Portland SE</td>
      <td>1</td>
      <td>26</td>
      <td>Multnomah</td>
      <td>0</td>
      <td>PED</td>
      <td>18.0</td>
      <td>...</td>
      <td>4</td>
      <td>STOP SIGN</td>
      <td>1</td>
      <td>0.0</td>
      <td>0</td>
      <td>57</td>
      <td>PORTLAND UA</td>
      <td>0.0</td>
      <td>2</td>
      <td>CLD</td>
    </tr>
    <tr>
      <th>1593337</th>
      <td>01028</td>
      <td>0</td>
      <td>245</td>
      <td>Portland SE</td>
      <td>3</td>
      <td>26</td>
      <td>Multnomah</td>
      <td>0</td>
      <td>PED</td>
      <td>2.0</td>
      <td>...</td>
      <td>99</td>
      <td>UNKNOWN</td>
      <td>1</td>
      <td>NaN</td>
      <td>0</td>
      <td>57</td>
      <td>PORTLAND UA</td>
      <td>0.0</td>
      <td>2</td>
      <td>CLD</td>
    </tr>
    <tr>
      <th>1593356</th>
      <td>00305</td>
      <td>0</td>
      <td>243</td>
      <td>Portland NE</td>
      <td>3</td>
      <td>26</td>
      <td>Multnomah</td>
      <td>5</td>
      <td>SS-O</td>
      <td>13.0</td>
      <td>...</td>
      <td>15</td>
      <td>ONE-WAY</td>
      <td>1</td>
      <td>NaN</td>
      <td>0</td>
      <td>57</td>
      <td>PORTLAND UA</td>
      <td>NaN</td>
      <td>3</td>
      <td>RAIN</td>
    </tr>
    <tr>
      <th>1593367</th>
      <td>00745</td>
      <td>0</td>
      <td>245</td>
      <td>Portland SE</td>
      <td>1</td>
      <td>26</td>
      <td>Multnomah</td>
      <td>3</td>
      <td>REAR</td>
      <td>7.0</td>
      <td>...</td>
      <td>15</td>
      <td>ONE-WAY</td>
      <td>1</td>
      <td>NaN</td>
      <td>0</td>
      <td>57</td>
      <td>PORTLAND UA</td>
      <td>NaN</td>
      <td>1</td>
      <td>CLR</td>
    </tr>
    <tr>
      <th>1593384</th>
      <td>00322</td>
      <td>0</td>
      <td>242</td>
      <td>Portland N</td>
      <td>8</td>
      <td>26</td>
      <td>Multnomah</td>
      <td>3</td>
      <td>REAR</td>
      <td>7.0</td>
      <td>...</td>
      <td>15</td>
      <td>ONE-WAY</td>
      <td>1</td>
      <td>NaN</td>
      <td>0</td>
      <td>57</td>
      <td>PORTLAND UA</td>
      <td>NaN</td>
      <td>1</td>
      <td>CLR</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 143 columns</p>
</div>


