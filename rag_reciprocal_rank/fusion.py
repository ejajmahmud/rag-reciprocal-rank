"""Reciprocal Rank Fusion (RRF) for combining multiple retrieval rankings."""
from typing import List, Dict, Any


class ReciprocalRankFusion:
    @staticmethod
    def fuse(rankings: List[List[str]], k: int = 60, top_n: int = 10) -> List[Dict[str, Any]]:
        """
        Calculates RRF score: score(d) = sum(1 / (k + rank(d)))
        rankings is a list of lists of doc_ids ordered from best (rank 1) to worst.
        """
        scores: Dict[str, float] = {}

        for rank_list in rankings:
            for rank_idx, doc_id in enumerate(rank_list, start=1):
                rrf_score = 1.0 / (k + rank_idx)
                scores[doc_id] = scores.get(doc_id, 0.0) + rrf_score

        sorted_docs = sorted(scores.items(), key=lambda item: item[1], reverse=True)
        return [{"doc_id": doc_id, "score": round(score, 6), "rank": i + 1}
                for i, (doc_id, score) in enumerate(sorted_docs[:top_n])]
