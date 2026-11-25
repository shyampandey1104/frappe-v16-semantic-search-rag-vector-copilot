from setuptools import setup, find_packages

setup(
    name="frappe_semantic_rag",
    version="16.0.0",
    description="Frappe v16 Vector Search & Semantic RAG Copilot - Official Frappe & ERPNext v16 App",
    author="Shyamkumar Pandey",
    author_email="shyampandey1104@gmail.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=["frappe"]
)
