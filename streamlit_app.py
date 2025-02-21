import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(
    page_title="GameShop",
    page_icon="🎮",
    layout="wide"
)

# Estilos minimalistas
st.markdown("""
<style>
    body {
        font-family: 'Inter', sans-serif;
        background-color: #f5f5f7;
    }
    .header {
        padding: 1rem 0;
        margin-bottom: 2rem;
        border-bottom: 1px solid #e0e0e0;
    }
    .game-card {
        background-color: white;
        border-radius: 5px;
        padding: 1rem;
        margin-bottom: 1rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    .game-title {
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    .game-price {
        font-weight: bold;
        color: #007bff;
    }
    .footer {
        margin-top: 3rem;
        padding-top: 1rem;
        border-top: 1px solid #e0e0e0;
        text-align: center;
        color: #6c757d;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# Header minimalista
st.markdown("""
<div class="header">
    <h1>GameShop</h1>
</div>
""", unsafe_allow_html=True)

# Menú horizontal con tabs en lugar de selectbox
tabs = st.tabs(["Recientes", "Tendencias", "Colección", "Soporte"])

# Datos de juegos (simplificado)
games_df = pd.DataFrame({
    'id': range(1, 7),
    'titulo': [
        'Hollow Knight',
        'Hades',
        'Stardew Valley',
        'Celeste',
        'Outer Wilds',
        'Undertale'
    ],
    'plataforma': ['Multi', 'Multi', 'Multi', 'Multi', 'Multi', 'Multi'],
    'precio': [14.99, 24.99, 14.99, 19.99, 24.99, 9.99],
    'categoria': ['Metroidvania', 'Roguelike', 'Simulación', 'Plataformas', 'Aventura', 'RPG']
})

# Función para mostrar un juego (simplificada)
def show_game_card(game):
    st.markdown(f"<div class='game-title'>{game['titulo']}</div>", unsafe_allow_html=True)
    st.write(f"{game['categoria']} · {game['plataforma']}")
    st.markdown(f"<span class='game-price'>${game['precio']:.2f}</span>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    with col2:
        st.button("Comprar", key=f"btn_{game['id']}")

# Contenido según la pestaña seleccionada
with tabs[0]:  # Recientes
    st.subheader("Juegos Recientes")
    
    # Mostrar juegos en grid de 3
    for i in range(0, len(games_df), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(games_df):
                with cols[j]:
                    st.markdown("<div class='game-card'>", unsafe_allow_html=True)
                    # Mostrar imagen placeholder
                    st.image("https://via.placeholder.com/300x150", use_column_width=True)
                    show_game_card(games_df.iloc[i + j])
                    st.markdown("</div>", unsafe_allow_html=True)

with tabs[1]:  # Tendencias
    st.subheader("Tendencias")
    
    # Mostrar estadísticas simples
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Más vendidos esta semana")
        st.markdown("1. **Hades**")
        st.markdown("2. **Hollow Knight**")
        st.markdown("3. **Stardew Valley**")
    
    with col2:
        st.markdown("#### Mejor valorados")
        st.markdown("1. **Outer Wilds** - 9.7/10")
        st.markdown("2. **Celeste** - 9.5/10")
        st.markdown("3. **Undertale** - 9.3/10")

with tabs[2]:  # Colección
    st.subheader("Tu Colección")
    
    if not st.session_state.get("logged_in", False):
        st.info("Inicia sesión para ver tu colección")
        
        col1, col2 = st.columns(2)
        with col1:
            st.text_input("Usuario", placeholder="Nombre de usuario")
        with col2:
            st.text_input("Contraseña", type="password", placeholder="Contraseña")
        
        st.button("Iniciar Sesión")
    else:
        st.write("No tienes juegos en tu colección todavía.")

with tabs[3]:  # Soporte
    st.subheader("Soporte")
    
    st.write("### Preguntas Frecuentes")
    
    with st.expander("¿Cómo descargo mis juegos?"):
        st.write("Una vez completada la compra, los juegos aparecerán en tu biblioteca. Haz clic en 'Descargar' para iniciar el proceso.")
    
    with st.expander("¿Cuáles son los métodos de pago aceptados?"):
        st.write("Aceptamos tarjetas de crédito/débito, PayPal y transferencia bancaria.")
    
    with st.expander("¿Puedo solicitar un reembolso?"):
        st.write("Sí, ofrecemos reembolsos completos dentro de los primeros 14 días después de la compra si el juego tiene menos de 2 horas de juego.")
    
    st.write("### Contacto")
    st.write("Para más ayuda, escríbenos a support@gameshop.com")

# Footer minimalista
st.markdown("""
<div class="footer">
    <p>© 2025 GameShop. Todos los derechos reservados.</p>
</div>
""", unsafe_allow_html=True)
