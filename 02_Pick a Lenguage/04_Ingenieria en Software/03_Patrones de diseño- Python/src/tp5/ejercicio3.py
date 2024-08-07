from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass

class ConcreteSubject(Subject):
    _state: int = None
    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)
    
    def notify(self) -> None:
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self, num: int) -> None:
        self._state = num

        print(f"Subject: Se establecio la ID: {self._state}")
        self.notify()

class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass

class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 1234:
            print("ConcreteObserverA: Coinsidencia de ID")

class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 1111:
            print("ConcreteObserverB: Coinsidencia de ID")

class ConcreteObserverC(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 2222:
            print("ConcreteObserverC: Coinsidencia de ID")

class ConcreteObserverD(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 3333:
            print("ConcreteObserverD: Coinsidencia de ID")

if __name__ == "__main__":
    # The client code.
    subject = ConcreteSubject()

    print("Cargando observador A con ID: 1234")
    observer_a = ConcreteObserverA()
    subject.attach(observer_a)
    print("\n")

    print("Cargando observador B con ID: 1111")
    observer_b = ConcreteObserverB()
    subject.attach(observer_b)
    print("\n")

    print("Cargando observador C con ID: 2222")
    observer_c = ConcreteObserverC()
    subject.attach(observer_c)
    print("\n")

    print("Cargando observador D con ID: 3333")
    observer_d = ConcreteObserverD()
    subject.attach(observer_d)
    print("\n")

    subject.some_business_logic(1234)
    subject.some_business_logic(2222)
    subject.some_business_logic(4444)
    subject.some_business_logic(1212)
    subject.some_business_logic(3333)
    subject.some_business_logic(2323)
    subject.some_business_logic(1111)
    subject.some_business_logic(4343)




