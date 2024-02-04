## How to run

``` bash
docker build ./ --tag get_favicon
docker run --rm -v ./favicons:/opt/python/favicons get_favicon dzen.ru
```

Search result in *./favicons* directory