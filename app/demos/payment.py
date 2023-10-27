import logging

from app.backend.session import create_session
from app.services.payment import PaymentService


def run():
    """Demonstrates how to use the PaymentService to retrieve all payments from the database."""

    with create_session() as session:
        payment_service = PaymentService(session)
        all_payments = payment_service.get_all_payments()
        for payment in all_payments:
            logging.info(f"Payment ID: {payment.payment_id} - Method: {payment.payment_method} - Amount: {payment.amount}")
