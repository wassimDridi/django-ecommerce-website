// pdf.js

// Function to generate PDF
function generatePDF() {
    const doc = new jsPDF();
    // Add title
    doc.text("Shopping Cart", 10, 10);
    // Add table headers
    doc.setFontSize(12);
    doc.text("Product", 10, 20);
    doc.text("Quantity", 70, 20);
    doc.text("Price", 120, 20);
    // Add table content
    let startY = 30;
    let productName = "{{ produit.produit.libelle }}";
    let quantity = "{{ produit.qnt }}";
    let price = "{{ produit.produit.prix }} DT";
    doc.text(productName, 10, startY);
    doc.text(quantity, 70, startY);
    doc.text(price, 120, startY);
    startY += 10; // Increase Y position for next row
    // Add total price
    let totalPrice = "{{ total_price }} DT";
    doc.text("Total:", 10, startY + 10);
    doc.text(totalPrice, 120, startY + 10);
    // Save PDF
    doc.save("order.pdf");
}

// Event listener for print button
document.getElementById("print-btn").addEventListener("click", function() {
    generatePDF();
});
