import dataclasses


def _identity_decorator(*args, **kwargs):
    def decorator(func):
        return func

    return decorator


def __getattr__(name):
    return _DummyObject()


class _DummyObject:
    def __call__(self, *args, **kwargs):
        return self

    def __getattr__(self, name):
        return self


@dataclasses.dataclass
class Record:
    pass


node = _identity_decorator
data = dataclasses.dataclass
