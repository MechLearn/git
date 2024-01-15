from matriz import Matrix


class Vector(Matrix):
    def __init__(self, elements):
        super().__init__(1, len(elements), elements)