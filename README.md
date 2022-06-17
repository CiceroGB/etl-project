<h1 align="center">
  ETL Project
</h1>

<div align="center">
   
 <img src="https://user-images.githubusercontent.com/63745509/168498554-84807e4d-0260-4266-9a4b-ba8efe8cef81.svg" width="80"/>
 <img src="https://user-images.githubusercontent.com/63745509/168498573-6dab86d5-203f-44cb-bb01-9a08a847d1fe.svg" width="80"/>
 <img src="https://user-images.githubusercontent.com/63745509/168498176-ab845ae5-4bf4-45d1-afbe-73ecb6493db0.svg" width="80"/>
 
</div>


## About project
<strong>Extract:</strong> Extract data from https://web.archive.org/<br>
<strong>Transform:</strong> Transformation of html data.<br>
<strong>Load:</strong> Relational database MySQL has been used to load the data.
<div align="center">
 <img src="https://user-images.githubusercontent.com/63745509/168498262-cb123e60-95bc-42cf-a4ba-e1bd0f7f79d6.png" width="600"/>
</div>

## Tecnologies
Python<br>
MySQL<br>
Docker<br>

## How to build and run

1. Up docker image:

    ```docker-compose up --build -d      ```
  
2. Run script:

    ```docker exec etl_run python run.py        ```
