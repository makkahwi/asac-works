import pytest
from stack_and_queue_animal_shelter.stack_and_queue_animal_shelter import (
    Cat,
    Dog,
    Hamster,
    AnimalShelter,
)


def test_enqueue(shelter):
    actual = shelter.enqueue(Cat())
    expected = "{ cat } -> { dog } -> { cat } -> { dog } -> { cat } -> None"
    assert actual == expected


def test_dequeue(shelter):
    actual = shelter.dequeue("cat")
    expected = "{ dog } -> { cat } -> { dog } -> None"
    assert actual == expected


def test_hamster(shelter):
    with pytest.raises(Exception):
        shelter.enqueue(Hamster())


def test_dequeue_non_existing(shelter):
    with pytest.raises(Exception):
        actual = shelter.dequeue("cat")
        actual = shelter.dequeue("cat")
        actual = shelter.dequeue("cat")


@pytest.fixture
def shelter():
    shelter = AnimalShelter()
    shelter.enqueue(Cat())
    shelter.enqueue(Dog())
    shelter.enqueue(Cat())
    shelter.enqueue(Dog())
    return shelter
