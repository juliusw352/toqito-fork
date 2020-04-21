"""Tests for dephasing function."""
import unittest
import numpy as np

from toqito.channels.operations.apply_map import apply_map
from toqito.channels.channels.dephasing import dephasing


class TestDephasingChannel(unittest.TestCase):
    """Unit test for dephasing."""

    def test_standard_dephasing(self):
        """The dephasing channel kills everything off the diagonals."""
        test_input_mat = np.array(
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        )

        expected_res = np.array(
            [[1, 0, 0, 0], [0, 6, 0, 0], [0, 0, 11, 0], [0, 0, 0, 16]]
        )

        res = apply_map(test_input_mat, dephasing(4))

        bool_mat = np.isclose(expected_res, res)
        self.assertEqual(np.all(bool_mat), True)


if __name__ == "__main__":
    unittest.main()
