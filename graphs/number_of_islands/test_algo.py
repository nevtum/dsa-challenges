import pytest
from .algo import number_of_islands

@pytest.mark.parametrize("grid, expected", [
  (
    [
      [1,1,0,0,1],
      [0,1,0,0,1],
      [0,0,1,0,0],
      [1,1,1,0,1],
    ],
    4
  )
])
def test_number_of_islands(grid, expected):
  assert number_of_islands(grid) == expected

if __name__ == "__main__":
  pytest.main([__file__, "-sv"])
