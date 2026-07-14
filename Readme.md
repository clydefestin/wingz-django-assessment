# Wingz Django REST API Assessment

# Technologies Used

- Python 3.12
- Django
- Django REST Framework
- SQLite (Development)
- PostgreSQL-compatible SQL (Bonus)
- Simple JWT Authentication
- django-filter
- Git & GitHub


# Features

### Authentication

- JWT Authentication
- Token Generation
- Token Refresh

### User Management

- Custom User Model
- Rider and Driver Roles

### Ride Management

- Create Ride
- Retrieve Ride
- Update Ride
- Delete Ride

### Ride Events

- Create Ride Events
- Retrieve Ride Events
- Update Ride Events
- Delete Ride Events

### Filtering

Filter rides by:

- Ride Status
- Rider Email

Example:

```
GET /api/rides/?status=pickup
```

```
GET /api/rides/?rider_email=admin@test.com
```

### Search

Search rides by rider or driver information.

Example:

```
GET /api/rides/?search=clyde
```


### Ordering

Sort rides by pickup time.

Ascending


GET /api/rides/?ordering=pickup_time
```

Descending

```
GET /api/rides/?ordering=-pickup_time
```


### Database-Level Distance Sorting

Sort rides by the nearest pickup location using latitude and longitude parameters.

Example


GET /api/rides/?latitude=14.5995&longitude=120.9842
```

Distance calculations are performed at the database query level using Django ORM annotations to avoid loading all records into application memory.


### Pagination

Ride results are paginated using Django REST Framework pagination.

Default page size:

```
10 records
```


### Database Optimization

The Ride API is optimized using:

- select_related()
- prefetch_related()
- Query annotations

These optimizations reduce unnecessary SQL queries while retrieving rider, driver, and ride event information.

## Testing

The project includes basic API tests using Django REST Framework's `APITestCase`.

### Run the tests

```bash
python manage.py test


# Project Structure

wingz-django-assessment/
│
├── config/
│
├── rides/
│   ├── migrations/
│   ├── admin.py
│   ├── filters.py
│   ├── models.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── test.py
│   ├── urls.py
│   └── views.py
│
├── bonus_sql.sql
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```


# Installation

Clone the repository

```
git clone https://github.com/clydefestin/wingz-django-assessment.git


Navigate into the project

```bash
cd wingz-django-assessment
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

macOS / Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run database migrations

```bash
python manage.py migrate
```

Create an administrator account

```bash
python manage.py createsuperuser
```

Run the development server

```bash
python manage.py runserver
```

---

# Authentication

Generate JWT Token

```
POST /api/token/
```

Refresh JWT Token

```
POST /api/token/refresh/
```

Include the access token in the request header.

```
Authorization: Bearer <access_token>
```

---

# API Endpoints

## Users

| Method | Endpoint |
|---------|----------|
| GET | /api/users/ |
| POST | /api/users/ |
| GET | /api/users/{id}/ |
| PATCH | /api/users/{id}/ |
| DELETE | /api/users/{id}/ |

---

## Rides

| Method | Endpoint |
|---------|----------|
| GET | /api/rides/ |
| POST | /api/rides/ |
| GET | /api/rides/{id}/ |
| PATCH | /api/rides/{id}/ |
| DELETE | /api/rides/{id}/ |

---

## Ride Events

| Method | Endpoint |
|---------|----------|
| GET | /api/ride-events/ |
| POST | /api/ride-events/ |
| GET | /api/ride-events/{id}/ |
| PATCH | /api/ride-events/{id}/ |
| DELETE | /api/ride-events/{id}/ |

---

# Sample Requests

Filter by Status

```
GET /api/rides/?status=pickup
```

Filter by Rider Email

```
GET /api/rides/?rider_email=admin@test.com
```

Search

```
GET /api/rides/?search=clyde
```

Order by Pickup Time

```
GET /api/rides/?ordering=-pickup_time
```

Distance Sorting

```
GET /api/rides/?latitude=14.5995&longitude=120.9842
```

---



# Bonus SQL

The repository includes a PostgreSQL-compatible SQL query(`bonus_sql.sql`) that generates a monthly report of drivers whose trips exceeded one hour.

The query:

- Uses the `RideEvent` table to locate the pickup and dropoff events.
- Calculates trip duration from the difference between the pickup and dropoff timestamps.
- Filters trips with a duration greater than one hour.
- Groups the results by **month** and **driver**.
- Returns the total number of qualifying trips for each driver per month.

Example output:

| Month | Driver | Trips Over 1 Hour |
|--------|--------|-------------------|
| 2024-01 | Chris H | 4 |
| 2024-01 | Howard Y | 5 |
| 2024-02 | Chris H | 7 |

# Notes

- SQLite was used for local development.
- The bonus SQL query is written for PostgreSQL.
- JWT authentication is implemented using Django REST Framework Simple JWT.
- Database-level query optimization is implemented using Django ORM features such as `select_related()`, `prefetch_related()`, and query annotations.


# Future Improvements

Potential enhancements include:

- React Native mobile integration
- API documentation with Swagger/OpenAPI
- Docker containerization
- PostgreSQL database deployment
- CI/CD pipeline
- Automated unit and integration testing



# Author

**Clyde Cyril Festin**
