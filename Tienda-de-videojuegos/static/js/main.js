document.addEventListener('DOMContentLoaded', function() {
    const fkRol = 1; // Supongamos que este es el valor de fk_rol del usuario

    const modal = document.getElementById('modal');
    const openModalBtn = document.querySelector('.crear-juego');
    const closeModalBtn = document.querySelector('.close');

    if (fkRol === 1 && modal && openModalBtn && closeModalBtn) {
        openModalBtn.addEventListener('click', function() {
            modal.classList.add('show');
        });

        closeModalBtn.addEventListener('click', function() {
            modal.classList.remove('show');
        });

        window.addEventListener('click', function(event) {
            if (event.target == modal) {
                modal.classList.remove('show');
            }
        });

        document.getElementById('modal-form').addEventListener('submit', function(event) {
            event.preventDefault();
            const formData = new FormData(this);
            fetch('/guardarJuego', {
                method: 'POST',
                body: formData
            })
            .then(response => {
                if (response.ok) {
                    alert('¡Formulario enviado con éxito!');
                    modal.classList.remove('show');
                } else {
                    throw new Error('Error al enviar el formulario');
                }
            })
            .catch(error => alert('Error al enviar el formulario:', error));
        });

        const botonesEditar = document.querySelectorAll('.boton-editar');
        const modalEditar = document.getElementById('modal-editar');
        const spanCerrar = document.querySelector('.close');
        const formEditar = document.getElementById('form-editar');
        const idInput = document.getElementById('id_juego');
        const nombreInput = document.getElementById('nombre_juego');
        const precioInput = document.getElementById('precio_unitario');
        const cantidadInput = document.querySelector('#form-editar .editar');

        if (modalEditar && spanCerrar && formEditar && idInput && nombreInput && precioInput && cantidadInput) {
            botonesEditar.forEach(boton => {
                boton.addEventListener('click', function() {
                    idInput.value = this.getAttribute('data-id');
                    nombreInput.value = this.getAttribute('data-nombre');
                    precioInput.value = this.getAttribute('data-precio');
                    cantidadInput.value = this.getAttribute('data-cantidad');
                    modalEditar.style.display = 'block';

                    console.log('ID:', idInput.value);
                    console.log('Nombre:', nombreInput.value);
                    console.log('Precio:', precioInput.value);
                    console.log('Cantidad:', cantidadInput.value);
                });
            });

            spanCerrar.addEventListener('click', function() {
                modalEditar.style.display = 'none';
            });

            window.addEventListener('click', function(event) {
                if (event.target == modalEditar) {
                    modalEditar.style.display = 'none';
                }
            });

            formEditar.addEventListener('submit', function(event) {
                event.preventDefault();
                const formData = new FormData(formEditar);
                fetch('/editar_juego', {
                    method: 'POST',
                    body: formData
                })
                .then(response => {
                    if (response.ok) {
                        modalEditar.style.display = 'none';
                        location.reload();
                    } else {
                        throw new Error('Error en la respuesta del servidor');
                    }
                })
                .catch(error => {
                    console.error('Error al enviar la solicitud:', error);
                    alert('Error al enviar la solicitud. Por favor, intenta de nuevo más tarde.');
                });
            });
        }

        const modalCategoria = document.getElementById('modal-categoria');
        const openModalCategoriaBtn = document.querySelector('.crear-categoria');
        const closeModalCategoriaBtn = modalCategoria.querySelector('.close');

        openModalCategoriaBtn.addEventListener('click', function() {
            modalCategoria.classList.add('show');
        });

        closeModalCategoriaBtn.addEventListener('click', function() {
            modalCategoria.classList.remove('show');
        });

        window.addEventListener('click', function(event) {
            if (event.target == modalCategoria) {
                modalCategoria.classList.remove('show');
            }
        });

        document.getElementById('modal-form-categoria').addEventListener('submit', function(event) {
            event.preventDefault();
            const formData = new FormData(this);
            fetch('/guardarCategoria', {
                method: 'POST',
                body: formData
            })
            .then(response => {
                if (response.ok) {
                    alert('¡Categoría creada con éxito!');
                    modalCategoria.classList.remove('show');
                } else {
                    throw new Error('Error al crear la categoría');
                }
            })
            .catch(error => alert('Error al crear la categoría: ' + error));
        });

    } else {
        console.log('El usuario no es administrador o algún elemento no se encontró.');
    }
});

document.addEventListener('DOMContentLoaded', function() {
    const inputBuscar = document.getElementById('input-buscar');
    const contenedorJuegos = document.getElementById('contenedor-juegos');
    const juegos = Array.from(contenedorJuegos.children);

    if (inputBuscar) {
        inputBuscar.addEventListener('input', function () {
            const valorBusqueda = inputBuscar.value.trim().toLowerCase();

            juegos.forEach(function (elemento) {
                const nombreJuego = elemento.querySelector('.nombre').textContent.trim().toLowerCase();
                if (nombreJuego.includes(valorBusqueda) || valorBusqueda === '') {
                    elemento.style.display = 'block';
                } else {
                    elemento.style.display = 'none';
                }
            });
        });
    }
});


document.addEventListener('DOMContentLoaded', function() {
    const inputBuscar = document.getElementById('input-buscar');
    const contenedorJuegos = document.getElementById('contenedor-juegos');
    const juegos = Array.from(contenedorJuegos.children);

    if (inputBuscar) {
        inputBuscar.addEventListener('input', function () {
            const valorBusqueda = inputBuscar.value.trim().toLowerCase();

            juegos.forEach(function (elemento) {
                const nombreJuego = elemento.querySelector('.nombre').textContent.trim().toLowerCase();
                if (nombreJuego.includes(valorBusqueda) || valorBusqueda === '') {
                    elemento.style.display = 'block';
                } else {
                    elemento.style.display = 'none';
                }
            });
        });
    }
});


document.addEventListener('DOMContentLoaded', function() {
    const inputBuscar = document.getElementById('input-buscar');
    const contenedorJuegos = document.getElementById('contenedor-juegos');
    const juegos = Array.from(contenedorJuegos.children);

    if (inputBuscar) {
        inputBuscar.addEventListener('input', function () {
            const valorBusqueda = inputBuscar.value.trim().toLowerCase();

            juegos.forEach(function (elemento) {
                const nombreJuego = elemento.querySelector('.nombre').textContent.trim().toLowerCase();
                if (nombreJuego.includes(valorBusqueda) || valorBusqueda === '') {
                    elemento.style.display = 'block';
                } else {
                    elemento.style.display = 'none';
                }
            });
        });
    }
});

document.addEventListener('DOMContentLoaded', function() {
    const botonesEliminar = document.querySelectorAll('.boton-eliminar');

    botonesEliminar.forEach(boton => {
        boton.addEventListener('click', function() {
            const idJuego = this.getAttribute('data-id');
            eliminarJuego(idJuego);
        });
    });

    function eliminarJuego(idJuego) {
        fetch('/eliminar_juego', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ id: idJuego })
        })
        .then(response => {
            if (response.ok) {
                alert('Juego eliminado correctamente');
                window.location.reload(); 
            } else {
                throw new Error('Error al eliminar juego');
            }
        })
        .catch(error => alert('Error al eliminar juego: ' + error));
    }
});


document.addEventListener('DOMContentLoaded', function() {
    const fkRol = 1; 

    const modal = document.getElementById('modal');
    const openModalBtn = document.querySelector('.crear-juego');
    const closeModalBtn = document.querySelector('.close');

    if (fkRol === 1 && modal && openModalBtn && closeModalBtn) {

        const modalEditarCategoria = document.getElementById('modal-editar-categoria');
        const openModalEditarCategoriaBtn = document.querySelectorAll('.boton-editar-categoria');
        const closeModalEditarCategoriaBtn = modalEditarCategoria.querySelector('.close');
        const formEditarCategoria = document.getElementById('form-editar');
        const idCategoriaInput = document.getElementById('id_cate');
        const categoriaInput = document.getElementById('categoria');

        if (modalEditarCategoria && openModalEditarCategoriaBtn && closeModalEditarCategoriaBtn && formEditarCategoria && idCategoriaInput && categoriaInput) {
            openModalEditarCategoriaBtn.forEach(boton => {
                boton.addEventListener('click', function() {

                    const categoriaId = this.parentNode.querySelector('.boton-eliminar').getAttribute('data-id');
                    const nombreCategoria = this.parentNode.querySelector('.nombre').textContent;

                    idCategoriaInput.value = categoriaId;
                    categoriaInput.value = nombreCategoria;

                    modalEditarCategoria.style.display = 'block';
                });
            });

            closeModalEditarCategoriaBtn.addEventListener('click', function() {
                modalEditarCategoria.style.display = 'none';
            });

            window.addEventListener('click', function(event) {
                if (event.target == modalEditarCategoria) {
                    modalEditarCategoria.style.display = 'none';
                }
            });

            formEditarCategoria.addEventListener('submit', function(event) {
                event.preventDefault();
                const formData = new FormData(formEditarCategoria);

                fetch('/editar_categoria', {
                    method: 'POST',
                    body: formData
                })
                .then(response => {
                    if (response.ok) {
                        alert('¡Categoría editada con éxito!');
                        modalEditarCategoria.style.display = 'none';
                        // Aquí puedes añadir lógica adicional si necesitas actualizar la página u otra acción después de editar la categoría
                    } else {
                        throw new Error('Error al enviar el formulario');
                    }
                })
                .catch(error => {
                    console.error('Error al enviar el formulario:', error);
                    alert('Error al enviar el formulario. Por favor, intenta de nuevo más tarde.');
                });
            });
        }
    } else {
        console.log('El usuario no es administrador o algún elemento no se encontró.');
    }
});


document.addEventListener('DOMContentLoaded', function() {
    const botonesEliminar = document.querySelectorAll('.boton-eliminar');

    botonesEliminar.forEach(boton => {
        boton.addEventListener('click', function() {
            const idCategoria = this.getAttribute('data-id');
            eliminarCategoria(idCategoria);
        });
    });

    function eliminarCategoria(idCategoria) {
        fetch('/eliminar_categoria', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ id: idCategoria })
        })
        .then(response => {
            if (response.ok) {
                alert('Categoría eliminada correctamente');
                document.getElementById('categoria-' + idCategoria).remove(); // Eliminar el elemento del DOM
            } else {
                throw new Error('Error al eliminar categoría');
            }
        })
        .catch(error => alert('Error al eliminar categoría: ' + error));
    }
});


document.addEventListener('DOMContentLoaded', function() {
    const body = document.querySelector('body');
    const autenticado = body.getAttribute('data-authenticated') === 'true';

    const botonesComprar = document.querySelectorAll('.boton-comprar');

    botonesComprar.forEach(boton => {
        boton.addEventListener('click', function() {
            const fkRol = parseInt(this.getAttribute('data-fk-rol'));
            console.log('Valor de data-fk-rol:', this.getAttribute('data-fk-rol'));


            console.log('Autenticado:', autenticado);
            console.log('Rol del juego:', fkRol);

            if (fkRol === 2 && autenticado) {
                alert('Modal de compra abierto');
            } else if (fkRol === 2 && !autenticado) {
                alert('Debes iniciar sesión para comprar este juego.');
            } else {
                alert('No tienes permisos para comprar este juego.');
            }
        });
    });

    console.log('Botones de compra:', botonesComprar);
});


document.addEventListener('DOMContentLoaded', function() {
    const botonesComprar = document.querySelectorAll('.boton-comprar');
    const modal = document.querySelector('.modal');
    const modalNombre = document.getElementById('modal-nombre');
    const modalPrecio = document.getElementById('modal-precio');
    const modalComprar = document.getElementById('modal-comprar');

    botonesComprar.forEach(boton => {
        boton.addEventListener('click', function() {
            const nombreJuego = this.parentElement.querySelector('.nombre_juego').innerText;
            const precioJuego = this.parentElement.querySelector('.precio_unitario').innerText;

            modalNombre.innerText = nombreJuego;
            modalPrecio.innerText = precioJuego;

            modal.style.display = 'block';
        });
    });

    document.querySelector('.close').addEventListener('click', function() {
        modal.style.display = 'none';
    });

    modalComprar.addEventListener('click', function() {
        modal.style.display = 'none';
    });

    window.addEventListener('click', function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    });
});

