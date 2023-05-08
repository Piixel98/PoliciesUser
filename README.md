# PoliciesUser

Project implemented using the microservices design pattern (layered architecture).\
The CQRS pattern has been applied for command and query segregation, maximizing application performance and scalability.\
The Repository pattern has also been applied to the project's repositories to provide data abstraction,
allowing the business logic to communicate with the repository instead of interacting directly with the data source.

The project has been implemented in Python using the [FastAPI Framework](https://fastapi.tiangolo.com/) to demonstrate
its excellent performance results, competing directly with Django or Flask, allowing easy management of asynchronous requests.

The application has been modeled using [Starlette](https://www.starlette.io/) models.
The data models have not been added because in this project database models are not used. 
However, it's recommended to use an Object-Relational Mapping (ORM) to abstract the database from the application logic.

Regarding the use of a database in this kind of projects, I have omitted the use because we just have a mock and no data persistence is required.
A database could be implemented for token or access management, as well as for data persistence when developing an ORM. 
Additionally, combining it with an event manager like Kafka could lead to a more interesting project.

For dependency management, I used pipenv providing greater agility in the development.

For authentication and authorization management, I used HTTP authentication using API Key with Json Web Tokens (JWT). 
The user_id content is sent in the Authorization header, which is later used to obtain the role from the mock. 
The user's role is checked to authenticate them in the designated endpoints.

It's important to note that HTTP authentication has been implemented simplified because we only have a mock with limited information. 
If we had a user database with credentials, we could implement OAuth2 for increased security.

Below are the JWT data generated for testing purposes in the project:

JWT Payload: {"user_id": "a0ece5db-cd14-4f21-812f-966633e7be86"} <-- User role: admin
ADMIN_JWT = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYTBlY2U1ZGItY2QxNC00ZjIxLTgxMmYtOTY2NjMzZTdiZTg2In0.LP3WPtY01QsZxAdCXQGHS4JsNTJ0fQsxDpHtMGr9s00"

JWT Payload: {"user_id": "a3b8d425-2b60-4ad7-becc-bedf2ef860bd"} <-- User role: user
USER_JWT = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYTNiOGQ0MjUtMmI2MC00YWQ3LWJlY2MtYmVkZjJlZjg2MGJkIn0.EbNRbDaaVhzJ9dXsyknWpqOiBgSsgJ1sIdrih6yvBZU"

Example Usage:
`curl -X "GET" "http://127.0.0.1:8000/api/v1/users/policy/64cceef9-3a01-49ae-a23b-3761b604800b" -H "accept: application/json" -H "Authorization: bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYTBlY2U1ZGItY2QxNC00ZjIxLTgxMmYtOTY2NjMzZTdiZTg2In0.LP3WPtY01QsZxAdCXQGHS4JsNTJ0fQsxDpHtMGr9s00"`

All the libraries used in this project are licensed under the MIT License.

A brief docker-compose file has been provided at the root of the project, exposing the API on port 8000.

Run docker-compose: 

`docker-compose up -d`

Run project manually:

`pipenv run && pipenv install`

`python main.py`


Due to lack of time, I was unable to generate the corresponding tests for the project. However, I created a "tests" 
folder for their future implementation.

Personal note: \
I assumed that the goal of this test was to apply MVC in Node.js with role-based authentication.
Due to the lack of data persistence, I have chosen not implement a relational database because data persistence is not needed.
Additionally, I implemented this project in python to demonstrate his power on backend.


Jordi Sánchez Mora \
Software Engineer \
[GitHub](https://github.com/Piixel98) \
[LinkedIn](https://www.linkedin.com/in/jsanchezm98/)
