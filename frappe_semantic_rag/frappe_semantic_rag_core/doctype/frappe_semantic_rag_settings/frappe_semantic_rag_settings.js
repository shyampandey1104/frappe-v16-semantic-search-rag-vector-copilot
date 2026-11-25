frappe.ui.form.on("Frappe v16 Vector Search & Semantic RAG Copilot Settings", {
    refresh: function(frm) {
        frm.add_custom_button(__("Test v16 Connection"), function() {
            frm.call({ doc: frm.doc, method: "test_connection" });
        });
    }
});
