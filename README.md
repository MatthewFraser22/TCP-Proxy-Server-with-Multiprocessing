# TCP-Proxy-Server-with-Multiprocessing
Uses socket programming in python, and uses HTTP protocol. The objective of this assignment was to develop a network application using stream socket API. This application understands simple HTTP GET-requests. The program implements Multiprocessing where the server can handle multiple clients at the same time. Error Handling cases are implemented. The proxy caches the web pages. 


***NOTE*****************************************
Make sure to run the proxy only in google crome
************************************************

Step 1: get the directory of where the proxy is located
For example: C:\Users\'username'\Documents\CP363\networksServer\src\proxy.py

Step 2: paste the directory into your cmd prompt and make sure to specify a port to run on and click enter
For example: C:\Users\'username'\Documents\CP363\networksServer\src\proxy.py 80

Step 3: open your browser and type 'localhost: port#/site to reach'
******Note link cannot contain http******
For example: http://localhost:8888/apache.org

Step 4: Click enter

Step 4: you should see the responses in the console


Since in our proxy design you have to enter a link in the format "http://localhost:8888/(website link goes here)", HTTP will be used always.
We have error handling throughout our program to catch any errors that may come about such as bad request, internal server error, ect.
We error handling for the cache, if the cache folder is not present we will make one on your disk as it is required to have to write to. 
Theres multiple trys, except, and if/else statements to catch any possible server errors that may occure . 

************************************************************************
The first 20 lines of http messages that are sent from browser to proxy:
************************************************************************
www.example.com:
HTTP/1.1 200 OK\r\nAge: 65582\r\nCache-Control: max-age=604800\r\nContent-Type: text/html; charset=UTF-8\r\nDate: Thu, 11 Feb 2021 03:29:40 GMT\r\nEtag: "3147526947+ident"\r\nExpires: Thu, 18 Feb 2021 03:29:40 GMT\r\nLast-Modified: Thu, 17 Oct 2019 07:18:26 GMT\r\nServer: ECS (ord/573B)\r\nVary: Accept-Encoding\r\nX-Cache: HIT\r\nContent-Length: 1256\r\n\r\n<!doctype html>\n<html>\n<head>\n    <title>Example Domain</title>\n\n    <meta charset="utf-8" />\n    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />\n    <meta name="viewport" content="width=device-width, initial-scale=1" />\n    <style type="text/css">\n    body {\n        background-color: #f0f0f2;\n        margin: 0;\n        padding: 0;\n        font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;\n    
    \n    }\n    div {\n        width: 600px;\n        margin: 5em auto;\n        padding: 2em;\n        background-color: #fdfdff;\n        border-radius: 0.5em;\n        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);\n    }\n    a:link, a:visited {\n        color: #38488f;\n        text-decoration: none;\n    }\n    @media (max-width: 700px) {\n        div {\n            margin: 0 auto;\n            width: auto;\n        }\n    }\n  
  </style>    \n</head>\n\n<body>\n<div>\n    <h1>Example Domain</h1>\n    <p>This domain is for use in illustrative examples in documents. You may use this\n    domain in literature without prior coordination or asking for permission.</p>\n    <p><a href="https://www.iana.org/domains/example">More information...</a></p>\n</div>\n</body>\n</html>\n


