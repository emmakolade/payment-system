# payment-system

TThis is a payment system API that enables users to register and login, automate payments, fund their wallets, and view their wallet balances and payment histories.

### Installation

To use the API locally, follow these steps:

- Clone the repository to your local machine.
- Create a virtual environment in the cloned directory.
- Activate the virtual environment.
- Install the requirements by running **pip install -r requirements.txt**
- Start the server. **python manage.py runserver**
- Start the Celery Task: **celery -A payment.celery worker --pool=solo -l info**
- Start the Celery Work: **celery -A payment beat -l info**

## Endpoints

### Register

- **URL**: authentication/register/
- **Method**: POST

- **Data parameters**:
  - full_name (required)
  - email (required)
  - password (required)
  - sex
  - country
  - phone_number
- **Success response**
  - Code: 201 CREATED
  - Content: The created user object

### Login

- **URL**: authentication/login/
- **Method**: POST
- **Data parameters**:
  - email (required)
  - password (required)
- **Success response**
  - Code: 200 OK
  - Content: The user object and JWT token
- **Error response**
  - Code: 401 UNAUTHORIZED

### Automate Payment

- **URL**: testpay/payment-automation/{product_id}/
- **Method**: POST
- **Success response**
  - Code: 202 ACCEPTED
  - Content: A message indicating the payment was made successfully.
- **Error response**
  - Code: 400 BAD REQUEST
  - Content: A message indicating there is insufficient balance in the user's wallet.

### Stop Recurring Payment

- **URL**: testpay/payment/{product_id}/stop/
- **Method**: POST
- **Success response**
  - Code: 204 NO CONTENT
  - Content: A message indicating the recurring payment was stopped.
- **Error response**
  - Code: 404 NOT FOUND
  - Content: A message indicating no recurring payment was found for the given product..

### Fund Wallet

- **URL**: testpay/wallet/fund
- **Method**: POST
  - Data parameters:
  - amount (required)
- **Success response**
  - Code: 200 OK
  - Content: A message indicating the wallet has been successfully funded.

### Wallet Balance

- **URL**: testpay/wallet/balance/
- **Method**: GET
- Data parameters:
    None
- **Success response**
    Code: 200 OK
    Content: The user's wallet object containing their current balance.

### Create Product

    - **URL**: testpay/products/create
    - **Method**: POST
    - **Data parameters:
        product_name (required)
        price (required)
    - **Success response**
        Code: 200 OK
        Content: The created product object.

### List Products

    - **URL**: testpay/products/list
    - **Method**: GET
    Data parameters:
        None
    - **Success response**
        Code: 200 OK
        Content: A list of all product objects.

### List Payments

  **URL**: testpay/payment/list
  **Method**: GET
    Data parameters:
        None
  **Success response**
        Code: 200 OK
        Content: A list of all payment objects made
