from fastapi import FastAPI
import uvicorn

from app.api.credit import router as credit_router
from app.api.debit import router as debit_router
from app.api.balance import router as balance_router
from app.api.audit import router as audit_router
from app.api.withdraw import router as withdraw_router
from app.database import db


def start_application():
    app = FastAPI()
    db.create_tables()
    return app


app = start_application()


# Endpoints
app.include_router(credit_router)
app.include_router(debit_router)
app.include_router(balance_router)
app.include_router(audit_router)
app.include_router(withdraw_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
