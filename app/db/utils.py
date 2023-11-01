from app.core.utils import hash_string
from app.db.session import session
from app.db.models import Logs
from datetime import datetime

def add_log(command_name: str, log_message: str, hash: str):
    log = Logs(command_name=command_name, message=log_message, created_at=datetime.now(), hashed_url=hash_string(hash))
    session.add(log)
    session.commit()
    session.flush()
    session.close()
