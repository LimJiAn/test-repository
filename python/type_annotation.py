from typing import NewType, List


def greet(greeting: str, name: str) -> str:
    return greeting + name


print(greet("hello", "jian"))


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        TEST annotation
        """
        return List[0]


UserId = NewType('UserId', int)
some_id = UserId(524313)
print('some_id', type(some_id))


def get_user_name(user_id: UserId) -> str:

    return "TEST annotation"


# typechecks
user_a = get_user_name(UserId(42351))
# does not typecheck; an int is not a UserId
user_b = get_user_name(-1)


Vector = list[float]


def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]


# typechecks; a list of floats qualifies as a Vector.
new_vector = scale(2.0, [1.0, -4.2, 5.4])
