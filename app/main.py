import math


class Vector:
    def __init__(self, x_cord: float, y_cord: float) -> None:
        self.x_cord = round(x_cord, 2)
        self.y_cord = round(y_cord, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x_cord + other.x_cord, self.y_cord + other.y_cord)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x_cord - other.x_cord, self.y_cord - other.y_cord)

    def __mul__(self, other: "Vector") -> any:
        if isinstance(other, (int, float)):
            return Vector(self.x_cord * other, self.y_cord * other)
        elif isinstance(other, Vector):
            return self.x_cord * other.x_cord + self.y_cord * other.y_cord
        else:
            raise TypeError(
                "Unsupported operand type(s)"
                " for *: 'Vector' and '{}'".format(type(other).__name__)
            )

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[float, float],
            end_point: tuple[float, float]
    ) -> "Vector":
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x_cord ** 2 + self.y_cord ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot normalize a zero-length vector.")
        return Vector(self.x_cord / length, self.y_cord / length)

    def angle_between(self, other: "Vector") -> int:
        dot_product = self * other
        length_product = self.get_length() * other.get_length()
        if length_product == 0:
            raise ValueError("Cannot calculate angle with zero-length vector.")

        cos_angle = max(-1, min(1, dot_product / length_product))
        angle = math.degrees(math.acos(cos_angle))
        return round(angle)

    def get_angle(self) -> int:
        positive_y_vector = Vector(0, 1)
        return self.angle_between(positive_y_vector)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        new_x = (self.x_cord * math.cos(radians)
                 - self.y_cord * math.sin(radians))
        new_y = (self.x_cord * math.sin(radians)
                 + self.y_cord * math.cos(radians))
        return Vector(new_x, new_y)
