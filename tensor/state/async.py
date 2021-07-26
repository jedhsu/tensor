from typing import Protocol

from .stateful import Stateful


class UpdateEffect(Protocol):
    ...



class AsyncUpdate:
    @staticmethod
    async def async_update(state: Stateful) -> Stateful:
        await 
