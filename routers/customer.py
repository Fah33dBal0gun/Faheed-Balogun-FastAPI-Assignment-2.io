from fastapi import APIRouter

from schema.customer import Customer, CustomerCreate, customers

customer_router = APIRouter()

#create a customer
#list customers
#Edit a customer

#creating a customer
@customer_router.post('/', status_code=201)
def create_customer(payload: CustomerCreate):
        customer_id = len(customers) + 1
        new_customer = customer(
                id=customer_id,
                username=payload.username,
                address=payload.address
        )
        customers.append(new_customer)
        return {'message': 'customer created successfully', 'data': new_customer}

@customer_router.get('/', status_code=201)
def list_customers():
        return {'message': 'successfully listed all customers', 'data': customers}

@customer_router.put('/', status_code=200)
def edit_customer(customer_id: int, payload: CustomerCreate):
        current_customer = None
        #get the customer
        for customer in customers:
                if customer.id == customer_id:
                        current_customer = customer
                        break
        if not current_customer:
                raise HTTPException(status_code=404, details="customer not found")
        current_customer.username = payload.username
        current_customer.address = payload.address
        return {'message': 'customer edited successfully', 'data': current_customer}
