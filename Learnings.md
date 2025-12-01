# Things I've learned so far

## Generic

## RPGLE
- %Div to divide and get the integer portion
- Reading an IFS file line by line with SQL is way way easier than the read-open-close stuff
```rpgle
  exec sql
    DECLARE c1 CURSOR FOR
    SELECT line FROM table(qsys2.ifs_read_utf8(path_name => :filePath));
```



## Python