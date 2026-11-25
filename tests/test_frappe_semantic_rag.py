import unittest
from frappe_semantic_rag.engine import SemanticDocTypeIndex, VectorEmbeddingMath

class TestSemanticRAGCopilot(unittest.TestCase):
    def setUp(self):
        self.index = SemanticDocTypeIndex()
        self.index.index_document("Customer", "CUST-001", "Acme Corporation - High value retail client in Mumbai", [0.8, 0.6, 0.0, 0.0])
        self.index.index_document("Item", "ITEM-LAPTOP", "Dell Precision 5570 Mobile Workstation 32GB RAM", [0.0, 0.0, 0.9, 0.4])
        self.index.index_document("Sales Order", "SO-2026-10", "Order for Acme Corp 5x Laptops", [0.7, 0.5, 0.4, 0.2])

    def test_semantic_retrieval(self):
        query_vec = [0.85, 0.52, 0.0, 0.0]
        results = self.index.search_semantic(query_vec, top_k=2)
        self.assertTrue(len(results) >= 1)
        self.assertEqual(results[0]["doctype"], "Customer")
        self.assertTrue(results[0]["similarity"] > 0.9)

        rag = self.index.build_rag_prompt_context(results, "Who is Acme Corp?")
        self.assertEqual(rag["retrieved_context_sources"], len(results))
        self.assertEqual(rag["engine"], "FRAPPE_V16_VECTOR_COPILOT")

if __name__ == "__main__":
    unittest.main()
