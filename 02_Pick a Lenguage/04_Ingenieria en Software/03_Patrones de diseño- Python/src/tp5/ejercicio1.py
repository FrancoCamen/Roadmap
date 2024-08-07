from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass

class AbstractHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class NumerosPrimosHandler(AbstractHandler):
    def handle(self, request: Any):
        if request > 1:
            for i in range(2, int(request ** 0.5) + 1):
                if request % i == 0:
                    return super().handle(request)
            return f"NumerosPrimosHandler consumio {request} porque es primo"
        else:
            return super().handle(request)
    
class NumerosParHandler(AbstractHandler):
    def handle(self, request: Any):
        if request % 2 == 0:
            return f"NumerosParHandler consumio {request} porque es par"
        else:
            return super().handle(request)
    

def client_code(handler: Handler) -> None:

    for num in range(1, 100):
        print(f"\nNumero : {num}?")
        result = handler.handle(num)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"{num} no fue consumido por ningun Handler")
        

if __name__ == "__main__":
    primos = NumerosPrimosHandler()
    par = NumerosParHandler()

    primos.set_next(par)

    print("Chain: Primos > Par\n")
    client_code(primos)
    print("\n")
