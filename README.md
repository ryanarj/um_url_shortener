#   URL Shortener Backend Project
    
A simple django restful backend to support a URL shortener feature.


## Design

Database: I went with a django backend for this exercise because I am familar with django, but would have not used a 
relational database in postgres, but a NoSQL one as that is a faster lookup for key-value pairs and would be perfect for this product.

Pregenerate URL: After researching about urls shorteners one issue that can arise is latency of creating a new shortener
so I prebaked a few hundreds. This should run on a cron-job nightly or hourly depending on traffic.

UI: I did not complete a django forms or any interface, instead decided to use POSTMAN to test the API.

##  Time it took to complete

I believe north of 3 hours. I was able to complete most of the backend in 2 hours but wanted a finished product 
where the API wasn't running on POSTMAN, also the unit testing took some more time.

##  Installing
    
1.  Clone repo
2.  Run the following
        
        pip install virtualenv
        source ./venv/bin/active
        python -m pip install -r requirements.txt
        python manage.py runserver

##  Testing API on Postman

Creating a new shorten URL

    POST http://127.0.0.1:8000/short_urls/
    {
        "original_url": "https://test.com/"
    }

Response from the post request
    
    {
        "shorten_url": "http://127.0.0.1:8000/um/b9b85d1"
    }

Getting the original url

    GET http://127.0.0.1:8000/short_urls?shorten_url=http://127.0.0.1:8000/um/b9b85d1
    
Response from the get request
    
    {
        "original_url": "https://test.com/"
    }

##  Authors
  
@ryanarj
    
