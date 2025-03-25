document.addEventListener("DOMContentLoaded", () => {
    const catalogo = document.getElementById("catalogo")
    const pedidoModal = document.getElementById("pedidoModal")
    const closePedidoModal = document.getElementById("closePedidoModal")
    const pedidoForm = document.getElementById("pedidoForm")
    const productoIdInput = document.getElementById("productoId")
    const productoNombre = document.getElementById("productoNombre")
  
    const productos = [
      { id: 1, nombre: "Helado de Vainilla-Oreo", imagen: "/static/images/Vainilla.jpg" },
      { id: 2, nombre: "Helado de Pistacho", imagen: "/static/images/Pistacho.jpg" },
      { id: 3, nombre: "Helado de Mora", imagen: "/static/images/Mora.jpg" },
      { id: 4, nombre: "Helado de Arequipe", imagen: "/static/images/Arequipe.jpg" }
    ];
  
    function cargarProductos() {
      catalogo.innerHTML = ""
      productos.forEach((producto) => {
        const productoElement = document.createElement("div")
        productoElement.className = "bg-white p-4 rounded-lg shadow-md"
        productoElement.innerHTML = `
                  <img src="${producto.imagen}" alt="${producto.nombre}" class="w-full h-40 object-cover mb-4 rounded">
                  <h3 class="text-lg font-semibold mb-2">${producto.nombre}</h3>
                  <p class="text-gray-600 mb-4">$2,500 COP</p>
                  <button class="bg-purple-500 text-white px-4 py-2 rounded hover:bg-purple-600" data-id="${producto.id}">Solicitar</button>
              `
        catalogo.appendChild(productoElement)
      })
    }
  
    cargarProductos()
  
    catalogo.addEventListener("click", (e) => {
      if (e.target.tagName === "BUTTON") {
        const productoId = e.target.getAttribute("data-id")
        const producto = productos.find((p) => p.id == productoId)
        productoIdInput.value = productoId
        productoNombre.textContent = producto.nombre
        pedidoModal.classList.remove("hidden")
        pedidoModal.classList.add("flex")
      }
    })
  
    closePedidoModal.addEventListener("click", () => {
      pedidoModal.classList.add("hidden")
      pedidoModal.classList.remove("flex")
    })
  
    pedidoForm.addEventListener("submit", (e) => {
      e.preventDefault()
      const productoId = productoIdInput.value
      const cantidad = document.getElementById("cantidad").value
      // Aquí iría la lógica para procesar el pedido
      console.log("Pedido realizado:", productoId, cantidad)
      alert("Pedido realizado con éxito")
      pedidoModal.classList.add("hidden")
      pedidoModal.classList.remove("flex")
    })
  })
  
  