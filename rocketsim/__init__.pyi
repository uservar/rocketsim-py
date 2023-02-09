class Vec3:
    x: float
    y: float
    z: float

    def __init__(x: float, y: float, z: float) -> Vec3: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...

    def with_x(self, x: float) -> Vec3: ...
    def with_y(self, y: float) -> Vec3: ...
    def with_z(self, z: float) -> Vec3: ...

class Angle:
    pitch: float
    yaw: float
    roll: float
