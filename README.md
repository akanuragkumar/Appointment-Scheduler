# Appointment-Scheduler
Schedule your appointments with ease through Appointment-scheduler
## Quickstart

To work in a sandboxed Python environment it is recommended to install the app in a Python [virtualenv](https://pypi.python.org/pypi/virtualenv).

1. Install dependencies

    ```bash
    $ cd Appointment-Scheduler
    $ pip install -r requirements.txt
    ```
2. Install Mongo

   If MongoDB is not installed then follow these steps to install [MongoDB](https://docs.mongodb.com/manual/tutorial/).   

3. Running app

   ```bash
   $ python manage.py makemigrations appointment
   $ python manage.py migrate
   $ python manage.py runserver
   ```   
   
### [Link for questionnaire](https://github.com/akanuragkumar/Appointment-Scheduler/blob/master/Questionnaire.pdf)  
### [Link for screenshots of API response](https://github.com/akanuragkumar/Appointment-Scheduler/tree/master/screenshots)
   
## Project Structure

### Backend 
```shell
Appointment-Scheduler/                         # All application code in this directory.
│
├─ Scheduler/ ─────┐-- __init__.py             # initializing file for Django module.
│                  ├── asgi.py                 # standard interface between web servers, frameworks, and applications.    
│                  ├── settings.py             # all settings for Django applications stored here.
│                  ├── urls.py                 # all API end-points to be blended with views.
│                  └─  wsgi.py                 # wsgi file for Django app        
├─- appointment/ ─────┐-- __init__.py          # initializing file for appointment app.
│                     ├── apps.py              # All apps created are to be added here.
│                     ├── models.py.           # Databases models are created here.
│                     ├── serializer.py.       # Converts querrysets and models to datatype.
│                     ├── urls.py.             # Contains all the end-points for API.
│                     └─  views.py             # All views for the app is added here.
├─ requirements.txt                            # requirements file.
└─ manage.py                                   # Main entry-point into the Django application.
```
## API Documentation 

### `This Endpoint takes the candidate/interview details and their available time-slot` 

1. `POST /api/schedule` 

```json
 application/json - {"role":"Candidate","name":"Anurag Kumar","email":"akanuragkumar712@gmail.com","phone":"2147483641","date":"23/08/2020","start_time":"10","end_time":"14"}
```
##### `response`

```json
Status- 201 Created    
```
2. `PUT /api/schedule` 

```json
 application/json - {"id":"1","role":"Candidate","name":"Anurag Kumar","email":"akanuragkumar711@gmail.com","phone":"2147483641","date":"23/08/2020","start_time":"10","end_time":"14"}
```
##### `response`

```json
Status- 200 OK  
    
```
3. `DELETE /api/schedule` 

```json
{"id":1}
```

##### `response`

```json
{"message": "appointment was deleted successfully!"}
    
```
### `This Endpoint takes candidate_id, interviewer_id, date and returns their matching time-slots for that date` 

1. `GET /api/appointment?candidate_id=1&interviewer_id=2&date=22/08/2020` 

##### `response`

```json
 application/json - {"Matching Slots":[[11,1],[12,13],[13,14]]}
```

### `This Endpoint takes candidate_id, interviewer_id and their preferred matching time-slots and creates an entry in DB` 

1. `POST /api/scheduled` 

```json
 application/json - {"interviewer_id":"7","candidate_id":"8","start_time":"12","end_time":"13"}
```
##### `response`

```json
Status- 201 Created    
```
2. `PUT /api/scheduled` 

```json
 application/json - {"id":"1","role":"Candidate","name":"Anurag Kumar","email":"akanuragkumar711@gmail.com","phone":"2147483641","date":"23/08/2020","start_time":"10","end_time":"14"}
```
##### `response`

```json
Status- 200 OK  
    
```
3. `DELETE /api/scheduled` 

```json
{"id":1}
```

##### `response`

```json
{"message": "appointment was deleted successfully!"}
    
```
4. `GET /api/scheduled` 

##### `response`

```json
 application/json - [{"interviewer_id":7,"candidate_id":8,"start_time":11,"end_time":12}]
```
