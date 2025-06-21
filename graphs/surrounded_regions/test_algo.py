import pytest
from .algo import solve

@pytest.mark.parametrize("board, expected", [
    # (
    #     [
    #         ["X","X","X"],
    #         ["X","O","X"],
    #         ["X","X","X"]
    #     ],
    #     [
    #         ["X","X","X"],
    #         ["X","X","X"],
    #         ["X","X","X"]
    #     ]
    # ),
    # (
    #     [
    #         ["X","X","X"],
    #         ["X","O","X"],
    #         ["X","O","X"]
    #     ],
    #     [
    #         ["X","X","X"],
    #         ["X","O","X"],
    #         ["X","O","X"]
    #     ]
    # ),
    (
        [
            ["O","X","X"],
            ["X","O","X"],
            ["X","X","X"]
        ],
        [
            ["O","X","X"],
            ["X","X","X"],
            ["X","X","X"]
        ]
    ),
    # (
    #     [
    #         ["X","X","X","X"],
    #         ["X","O","O","X"],
    #         ["X","X","O","X"],
    #         ["X","O","X","X"]
    #     ],
    #     [
    #         ["X","X","X","X"],
    #         ["X","X","X","X"],
    #         ["X","X","X","X"],
    #         ["X","O","X","X"]
    #     ]
    # ),
    # (
    #     [
    #         ["X","X","X","X"],
    #         ["X","O","O","O"],
    #         ["X","O","X","O"],
    #         ["X","O","O","O"]
    #     ],
    #     [
    #         ["X","X","X","X"],
    #         ["X","O","O","O"],
    #         ["X","O","X","O"],
    #         ["X","O","O","O"]
    #     ],
    # ),
])
def test_surrounded_regions(board, expected):
    solve(board)
    assert board == expected

if __name__ == "__main__":
    pytest.main([__file__, "-vv"])
