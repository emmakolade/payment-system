# payment-system


### Installation
To use the API locally, follow these steps:

* Clone the repository to your local machine.
* Create a virtual environment in the cloned directory.
* Activate the virtual environment.
* Install the requirements by running **pip install -r requirements.txt**
* Start the server. **python manage.py runserver**
* Start the Celery Task: **celery -A payment.celery worker  --pool=solo -l info**
* Start the Celery Work: **celery -A payment beat -l INFO**
 
 ### Register
* **URL**: authentication/register/
* **Method**: POST

* **Data parameters**:
   * full_name (required)
   * email (required)
   * password (required)
   * sex
   * country
   * phone_number
* **Success response**
  * Code: 201 CREATED
  * Content: The created user object
  
### Login
* **URL**: authentication/login/
* **Method**: POST
* **Data parameters**:
  * email (required)
  * password (required)
* **Success response**
  * Code: 200 OK
  * Content: The user object and JWT token
* **Error response**
  * Code: 401 UNAUTHORIZED

### Login
* **URL**: testpay/payment-automate/
* **Method**: POST
* run this endpoint to automate the payment process