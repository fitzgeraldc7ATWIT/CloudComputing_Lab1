import unittest
from queries import run_query

class TestQueries(unittest.TestCase):

    def test_q1_returns_rows(self):
        rows = run_query("q1")
        self.assertTrue(len(rows) > 0)

    def test_invalid_query_key(self):
        with self.assertRaises(KeyError):
            run_query("badkey")

    def test_q2_has_brand_counts(self):
        rows = run_query("q2")
        self.assertTrue(all(len(row) == 2 for row in rows))

if __name__ == "__main__":
    unittest.main()