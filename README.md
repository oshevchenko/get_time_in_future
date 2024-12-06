# get_time_in_future
Check if the **Year** and **Month** is incremented correctly for the case when one second is added to the date: **dd.mm.YYYY 23:59:59**

```
(MainThread) current_datetime:2024-12-06 15:03:04.925752 type:<class 'datetime.datetime'>
(MainThread) current_datetime:2024-12-06 15:03:05.925752 type:<class 'datetime.datetime'>
(MainThread) current_datetime:1900-01-01 14:55:49 type:<class 'datetime.datetime'>
(MainThread) current_datetime:1900-01-01 14:55:50 type:<class 'datetime.datetime'>
(MainThread) current_datetime:2024-12-31 23:59:59 type:<class 'datetime.datetime'>
(MainThread) current_datetime:2025-01-01 00:00:00 type:<class 'datetime.datetime'>
(MainThread) current_datetime:2024-02-28 23:59:59 type:<class 'datetime.datetime'>
(MainThread) current_datetime:2024-02-29 00:00:00 type:<class 'datetime.datetime'>
(MainThread) current_datetime:2023-02-28 23:59:59 type:<class 'datetime.datetime'>
(MainThread) current_datetime:2023-03-01 00:00:00 type:<class 'datetime.datetime'>
```

