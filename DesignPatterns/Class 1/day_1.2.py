# singleton

# decorator realizing singleton pattern
def singleton(instance):
    created_instances = {}

    def get_instance(*args, **kwargs):
        if instance not in created_instances:
            created_instances[instance] = instance(*args, **kwargs)
        return created_instances[instance]
    return get_instance


@singleton
class Myself:
    def __init__(self):
        print("I am unique <3")

# if we are decorating the class (singleton) myself_1 object is created
# and myself_2 is NOT NEW object, it points to the myself_1 (myself_1 and myself_2 are the same object)


myself_1 = Myself()
myself_2 = Myself()

print(myself_1, myself_2)
