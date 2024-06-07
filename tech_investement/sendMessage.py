from quickstart import *
from generate_password import *

def reset_password(reciever, subject, message):
    data = {
        "reciever": reciever,
        "subject": subject,
        "message": message,
    }

    main(**data)


