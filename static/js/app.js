document.addEventListener("DOMContentLoaded", () => {
    const loginBtn = document.getElementById("loginBtn")
    const registerBtn = document.getElementById("registerBtn")
    const loginModal = document.getElementById("loginModal")
    const registerModal = document.getElementById("registerModal")
    const closeLoginModal = document.getElementById("closeLoginModal")
    const closeRegisterModal = document.getElementById("closeRegisterModal")
    const loginForm = document.getElementById("loginForm")
    const registerForm = document.getElementById("registerForm")
  
    loginBtn.addEventListener("click", () => {
      loginModal.classList.remove("hidden")
      loginModal.classList.add("flex")
    })
  
    registerBtn.addEventListener("click", () => {
      registerModal.classList.remove("hidden")
      registerModal.classList.add("flex")
    })
  
    closeLoginModal.addEventListener("click", () => {
      loginModal.classList.add("hidden")
      loginModal.classList.remove("flex")
    })
  
    closeRegisterModal.addEventListener("click", () => {
      registerModal.classList.add("hidden")
      registerModal.classList.remove("flex")
    })
  
    loginForm.addEventListener("submit", (e) => {
      e.preventDefault()
      const username = document.getElementById("loginUsername").value
      const password = document.getElementById("loginPassword").value
      // Aquí iría la lógica para verificar las credenciales
      console.log("Intento de inicio de sesión:", username, password)
      // Simulamos una redirección basada en el rol (esto se haría del lado del servidor en una aplicación real)
      if (username === "admin") {
        window.location.href = "admin.html"
      } else {
        window.location.href = "catalogo.html"
      }
    })
  
    registerForm.addEventListener("submit", (e) => {
      e.preventDefault()
      const username = document.getElementById("registerUsername").value
      const email = document.getElementById("registerEmail").value
      const password = document.getElementById("registerPassword").value
      // Aquí iría la lógica para registrar al usuario
      console.log("Intento de registro:", username, email, password)
      alert("Registro exitoso. Por favor, inicia sesión.")
      registerModal.classList.add("hidden")
      registerModal.classList.remove("flex")
    })
  })
  
  