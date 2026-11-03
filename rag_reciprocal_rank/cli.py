"""Command-line interface for RAG Reciprocal Rank."""
import argparse
from .fusion import ReciprocalRankFusion

def main():
    parser = argparse.ArgumentParser(description="RAG Reciprocal Rank CLI")
    parser.add_argument("--demo", action="store_true", help="Demonstrate hybrid reciprocal rank fusion")
    args = parser.parse_args()

    dense_results = ["doc_sem_1", "doc_shared", "doc_sem_2"]
    sparse_results = ["doc_shared", "doc_bm25_1", "doc_sem_1"]

    fused = ReciprocalRankFusion.fuse([dense_results, sparse_results], k=60, top_n=3)
    print("Fused Hybrid Results:")
    for res in fused:
        print(f"  Rank #{res['rank']}: {res['doc_id']} (Score: {res['score']})")

if __name__ == "__main__":
    main()
