def get_status(is_busy):
    return {"status": ("available", "busy")[is_busy]}
    # return {"status": "busy" if is_busy else "available"}
