_DB: list[dict] = []


def log_upload(record: dict) -> None:
    """Store an upload record in the in-memory 'database'."""
    _DB.append(record)


def get_all_uploads() -> list[dict]:
    """Return all stored upload records."""
    return list(_DB)