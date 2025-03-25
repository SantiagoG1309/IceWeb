document.addEventListener("DOMContentLoaded", () => {
    const inventarioForm = document.getElementById("inventarioForm")
    const pedidosPendientes = document.getElementById("pedidosPendientes")
  
    inventarioForm.addEventListener("submit", (e) => {
      e.preventDefault()
      const nombre = document.getElementById("nombreProducto").value
      const cantidad = document.getElementById("cantidadProducto").value
      const imagen = document.getElementById("imagenProducto").files[0]
      // Aquí iría la lógica para agregar el producto a la base de datos
      console.log("Producto agregado:", nombre, cantidad, imagen)
      alert("Producto agregado con éxito")
      inventarioForm.reset()
    })
  
    // Simulamos la carga de pedidos pendientes
    function cargarPedidosPendientes() {
      const pedidos = [
        { id: 1, cliente: "Juan Pérez", producto: "Helado de Vainilla", cantidad: 2 },
        { id: 2, cliente: "María García", producto: "Helado de Chocolate", cantidad: 1 },
        // Agrega más pedidos aquí
      ]
  
      pedidosPendientes.innerHTML = ""
      pedidos.forEach((pedido) => {
        const pedidoElement = document.createElement("div")
        pedidoElement.className = "mb-4 p-4 border rounded"
        pedidoElement.innerHTML = `
                  <p><strong>Cliente:</strong> ${pedido.cliente}</p>
                  <p><strong>Producto:</strong> ${pedido.producto}</p>
                  <p><strong>Cantidad:</strong> ${pedido.cantidad}</p>
                  <button class="bg-purple-500 text-white px-4 py-2 rounded hover:bg-purple-600 mt-2" data-id="${pedido.id}">Aceptar Pedido</button>
              `
        pedidosPendientes.appendChild(pedidoElement)
      })
    }
  
    cargarPedidosPendientes()
  
    pedidosPendientes.addEventListener("click", (e) => {
      if (e.target.tagName === "BUTTON") {
        const pedidoId = e.target.getAttribute("data-id")
        // Aquí iría la lógica para aceptar el pedido
        console.log("Pedido aceptado:", pedidoId)
        alert("Pedido aceptado con éxito")
        e.target.closest("div").remove()
      }
    })
  })
  
  