import uuid

def generate_uuid():
    # Generate a UUID4
    full_uuid = uuid.uuid4()

    # Convert the UUID to a string without hyphens
    # short_uuid = str(full_uuid).replace("-", "")
    short_uuid = (full_uuid)

    # Use only the first 12 characters
    code = short_uuid

    return code

