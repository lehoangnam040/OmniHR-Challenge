
class RateLimiter:

    def __init__(self) -> None:
        self.max_concurrent_request = 2
        self._limit_bucket: dict[str, list] = dict()

    def is_this_request_valid(self, request_identifier: str) -> bool:
        if request_identifier not in self._limit_bucket:
            return True
        if len(self._limit_bucket[request_identifier]) >= self.max_concurrent_request:
            return False
        return True

    def inc(self, request_identifier: str, unix_ts: float) -> None:
        if request_identifier not in self._limit_bucket:
            self._limit_bucket[request_identifier] = []
        self._limit_bucket[request_identifier].append(unix_ts)

    def dec(self, request_identifier: str, unix_ts) -> None:
        if request_identifier not in self._limit_bucket:
            return
        try:
            self._limit_bucket[request_identifier].remove(unix_ts)
        except:
            return
