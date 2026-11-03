"""Unit tests for ReciprocalRankFusion."""
import unittest
from rag_reciprocal_rank.fusion import ReciprocalRankFusion

class TestReciprocalRankFusion(unittest.TestCase):
    def test_shared_document_boost(self):
        l1 = ["docA", "docB"]
        l2 = ["docB", "docC"]
        fused = ReciprocalRankFusion.fuse([l1, l2], k=10)
        # docB appears in both lists, should have high fused score
        self.assertEqual(fused[0]["doc_id"], "docB")

if __name__ == "__main__":
    unittest.main()
