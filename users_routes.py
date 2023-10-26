import contextlib
import sqlite3
import base64
import hashlib
import secrets

from fastapi import Depends, HTTPException, APIRouter, status
from schemas import Class

import json
from pydantic import BaseModel

users_router = APIRouter()

database = "users.db"
enrollmentdb = "database.db"

ALGORITHM = "pbkdf2_sha256"

class Login(BaseModel):
    username: str
    password: str


# Connect to the database
def get_users_db():
    with contextlib.closing(sqlite3.connect(database, check_same_thread=False)) as db:
        db.row_factory = sqlite3.Row
        yield db

# Connect to the database
def get_enrollment_db():
    with contextlib.closing(sqlite3.connect(enrollmentdb, check_same_thread=False)) as edb:
        edb.row_factory = sqlite3.Row
        yield edb

def hash_password(password, salt=None, iterations=260000):
    if salt is None:
        salt = secrets.token_hex(16)
    assert salt and isinstance(salt, str) and "$" not in salt
    assert isinstance(password, str)
    pw_hash = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt.encode("utf-8"), iterations
    )
    b64_hash = base64.b64encode(pw_hash).decode("ascii").strip()
    return "{}${}${}${}".format(ALGORITHM, iterations, salt, b64_hash)

# Verify if the password inputted matches the stored hash password when hashed.
def verify_password(password, password_hash):
    if (password_hash or "").count("$") != 3:
        return False
    algorithm, iterations, salt, b64_hash = password_hash.split("$", 3)
    iterations = int(iterations)
    assert algorithm == ALGORITHM
    compare_hash = hash_password(password, salt, iterations)

    # This returns a boolean
    return secrets.compare_digest(password_hash, compare_hash)

@users_router.post("/login")
def login(login: Login, db: sqlite3.Connection = Depends(get_users_db)):

    cur = db.execute("SELECT * FROM USERS WHERE username = ?", [login.username])
    user = cur.fetchone()

        # json response when login is successful
    json_response = {
    "access_token": {
        "jti": "mnb23vcsrt756yuiomnbvcx98ertyuiop",
        "roles": ["admin"],
        "exp": 1735689600
        },
    "refresh_token": {
        "sub": "1234567890qwertyuio",
        "jti": "mnb23vcsrt756yuiomn12876bvcx98ertyuiop",
        "exp": 1735689600
        },
    "exp": 1735689600
    }

    if user:
        stored_password = user["password"]
        password_match = verify_password(login.password, stored_password)

        if not password_match:
            raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password.")
        
        return json_response
    
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User account not found."
        )


@users_router.get("/protected")
def protected():
    return {"message": "JWT Verified, access granted"}




