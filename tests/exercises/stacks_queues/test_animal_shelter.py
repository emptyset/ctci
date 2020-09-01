from exercises.stacks_queues.animal_shelter import Animal
from exercises.stacks_queues.animal_shelter import AnimalShelter


def test_AnimalShelter__operations():
    shelter = AnimalShelter([
        Animal('dog', 'Dusty'),
        Animal('dog', 'Sydney'),
        Animal('cat', 'Mr. Whiskers'),
        Animal('dog', 'Adolphus'),
        Animal('cat', 'Skeletor'),
        Animal('dog', 'Zero')
    ])

    shelter.enqueue(Animal('cat', 'Magdalena'))

    animal = shelter.dequeue_any()
    assert animal.kind == 'dog'
    assert animal.name == 'Dusty'

    animal = shelter.dequeue_cat()
    assert animal.kind == 'cat'
    assert animal.name == 'Mr. Whiskers'

    _ = shelter.dequeue_any()   # Sydney

    animal = shelter.dequeue_cat()
    assert animal.kind == 'cat'
    assert animal.name == 'Skeletor'

    _ = shelter.dequeue_dog()   # Adolphus

    animal = shelter.dequeue_dog()
    assert animal.kind == 'dog'
    assert animal.name == 'Zero'

    animal = shelter.dequeue_any()
    assert animal.kind == 'cat'
    assert animal.name == 'Magdalena'

    animal = shelter.dequeue_any()
    assert animal is None
