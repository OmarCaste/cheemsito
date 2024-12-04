function registrar(id) {
  var url = "/ciudad-registro";
  $.get(url, function (data) {
    $("#modal_info").html(data);
    $("#modal_info").modal({ backdrop: "static", keyboard: false });
    $("#modal_info").modal("show");
  });
}

function save() {
  const nombre = document.getElementById("form-nombre").value;
  const codigo = document.getElementById("form-codigo").value;

  const data = { nombre, codigo };
  fetch("/ciudad", {
    method: "POST",
    headers: { "Content-type": "application/json" },
    body: JSON.stringify(data),
  })
    .then((response) => {
      if (response.status === 201) {
        alert("El registro se guardo correctamente");
        location.reload();
      } else {
        alert(`Ocurrió un error al guardar: ${response.status}`);
      }
    })
    .catch((error) => console.error("Error:", error));
}

function eliminar(id) {
  if (confirm("¿Estás seguro de que deseas eliminar esta ciudad?")) {
    fetch(`/ciudad/eliminar/${id}`, {
      method: "DELETE",
    })
      .then((response) => {
        if (response.ok) {
          alert("Ciudad eliminada exitosamente.");
          location.reload(); // Recarga la página para reflejar los cambios
        } else {
          response.text().then((text) => {
            alert("Error al eliminar: " + text);
          });
        }
      })
      .catch((error) => {
        alert("Error al eliminar: " + error.message);
      });
  }
}
