# Entry point for the application.
# Initializes logging and starts the [entity]-demo, e.g. product, users, etc.

import logging
from app.demos import product, users, payment

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting application")

    print("-"*50) # Just to make the output easier to read
    logging.info("Starting product demo") 
    product.run()

    print("-"*50)
    logging.info("Starting payment demo")
    payment.run()
    
    print("-"*50)
    logging.info("Starting users demo")
    users.run() 
    
    # the second time it runs, it will fail because the user already exists. 
    # work around this by either modifying:
    # 1. the database
    # 2. the code to create a new user