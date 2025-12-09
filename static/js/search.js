document.addEventListener("DOMContentLoaded", function () {
  const searchInput = document.getElementById("searchInput");
  const tableRows = document.querySelectorAll("#inventoryTable tbody tr");

  searchInput.addEventListener("keyup", function (event) {
    const query = event.target.value.toLowerCase();

    tableRows.forEach((row) => {
      // Get all text in the row (Name + Location + etc)
      const rowText = row.textContent.toLowerCase();

      if (rowText.includes(query)) {
        row.style.display = ""; // Show row
      } else {
        row.style.display = "none"; // Hide row
      }
    });
  });
});
