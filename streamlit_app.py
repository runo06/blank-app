import streamlit as st

# Datos simulados de videojuegos
juegos = [
    {"id": 1, "nombre": "CyberQuest", "precio": 39.99},
    {"id": 2, "nombre": "Pixel Wars", "precio": 29.99},
    {"id": 3, "nombre": "Dungeon Master", "precio": 24.99},
    {"id": 4, "nombre": "Racing Pro", "precio": 19.99}
]

# Inicializar carrito en la sesión si no existe
if "carrito" not in st.session_state:
    st.session_state.carrito = []

st.title("Runplay Store")
st.subheader("Compra los mejores videojuegos al mejor precio")

# Mostrar lista de videojuegos
tab1, tab2 = st.tabs(["Tienda", "Carrito"])

with tab1:
    st.write("### Juegos disponibles")
    for juego in juegos:
        col1, col2, col3 = st.columns([3, 1, 1])
        col1.write(f"**{juego['nombre']}**")
        col2.write(f"${juego['precio']:.2f}")
        if col3.button("Agregar", key=juego["id"]):
            st.session_state.carrito.append(juego)
            st.success(f"{juego['nombre']} agregado al carrito")

with tab2:
    st.write("### Carrito de compras")
    if not st.session_state.carrito:
        st.write("Tu carrito está vacío.")
    else:
        total = 0
        for juego in st.session_state.carrito:
            st.write(f"{juego['nombre']} - ${juego['precio']:.2f}")
            total += juego['precio']
        st.write(f"**Total: ${total:.2f}**")
        if st.button("Finalizar compra"):
            st.session_state.carrito = []
            st.success("¡Compra realizada con éxito!")
