from datetime import datetime, timezone


def date_string_to_epoch(date_str) -> int:
    # parse the date string into a datetime object, assuming it's in utc
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")

    # set the datetime object to utc
    date_obj = date_obj.replace(tzinfo=timezone.utc)

    # convert the datetime object to a unix epoch timestamp
    epoch = int(date_obj.timestamp())
    return epoch
