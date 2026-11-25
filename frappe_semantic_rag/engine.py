"""Frappe v16 Semantic Vector Search & RAG Copilot Engine."""
import math
from typing import List, Dict, Any

class VectorEmbeddingMath:
    @staticmethod
    def cosine_similarity(v1: List[float], v2: List[float]) -> float:
        if len(v1) != len(v2) or not v1:
            return 0.0
        dot_prod = sum(a * b for a, b in zip(v1, v2))
        norm1 = math.sqrt(sum(a * a for a in v1))
        norm2 = math.sqrt(sum(b * b for b in v2))
        if norm1 == 0 or norm2 == 0:
            return 0.0
        return round(dot_prod / (norm1 * norm2), 4)

class SemanticDocTypeIndex:
    def __init__(self):
        self.indexed_docs: List[Dict[str, Any]] = []

    def index_document(self, doctype: str, doc_name: str, content: str, vector: List[float]):
        self.indexed_docs.append({
            "doctype": doctype,
            "doc_name": doc_name,
            "content": content,
            "vector": vector
        })

    def search_semantic(self, query_vector: List[float], top_k: int = 3, threshold: float = 0.5) -> List[Dict[str, Any]]:
        scored = []
        for item in self.indexed_docs:
            sim = VectorEmbeddingMath.cosine_similarity(query_vector, item["vector"])
            if sim >= threshold:
                scored.append({
                    "doctype": item["doctype"],
                    "doc_name": item["doc_name"],
                    "content": item["content"],
                    "similarity": sim
                })
        scored.sort(key=lambda x: x["similarity"], reverse=True)
        return scored[:top_k]

    def build_rag_prompt_context(self, search_results: List[Dict[str, Any]], user_query: str) -> Dict[str, Any]:
        context_str = "\n---\n".join([f"[{r['doctype']} {r['doc_name']} (Relevance: {r['similarity']})]: {r['content']}" for r in search_results])
        return {
            "augmented_prompt": f"System Context from Frappe v16:\n{context_str}\n\nUser Query: {user_query}",
            "retrieved_context_sources": len(search_results),
            "engine": "FRAPPE_V16_VECTOR_COPILOT"
        }
