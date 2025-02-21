import streamlit as st
from PIL import Image
import pandas as pd
import os

# Configuración de la página
st.set_page_config(
    page_title="GameStore - Tu tienda de videojuegos",
    page_icon="🎮",
    layout="wide"
)

# Aplicar algunos estilos CSS personalizados
st.markdown("""
<style>
    .header {
        padding: 1.5rem 0;
        background-color: #1E1E2E;
        color: white;
        text-align: center;
        border-radius: 5px;
        margin-bottom: 2rem;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #1E1E2E;
        color: white;
        text-align: center;
        padding: 1rem 0;
        margin-top: 2rem;
    }
    .game-card {
        background-color: #2E2E42;
        border-radius: 10px;
        padding: 1rem;
        margin-bottom: 1rem;
        transition: transform 0.3s;
    }
    .game-card:hover {
        transform: translateY(-5px);
    }
    .game-title {
        color: #FFD700;
        font-size: 1.2rem;
        margin-bottom: 0.5rem;
    }
    .game-price {
        color: #00FF7F;
        font-weight: bold;
        font-size: 1.1rem;
    }
    .section-title {
        color: #FFD700;
        border-bottom: 2px solid #FFD700;
        padding-bottom: 0.5rem;
        margin-bottom: 1.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="header">
    <h1>🎮 GameStore</h1>
    <p>Tu destino para los mejores videojuegos al mejor precio</p>
</div>
""", unsafe_allow_html=True)

# Barra de navegación
menu = st.selectbox("Menú", ["Inicio", "Catálogo", "Ofertas", "Contacto"])

# Cargar datos de juegos (simulados)
@st.cache_data
def load_game_data():
    return pd.DataFrame({
        'id': range(1, 11),
        'titulo': [
            'The Legend of Zelda: Breath of the Wild',
            'God of War Ragnarök',
            'Elden Ring',
            'Cyberpunk 2077',
            'FIFA 23',
            'Call of Duty: Modern Warfare II',
            'Horizon Forbidden West',
            'Red Dead Redemption 2',
            'Minecraft',
            'Grand Theft Auto V'
        ],
        'plataforma': ['Nintendo Switch', 'PS5', 'Multi', 'Multi', 'Multi', 'Multi', 'PS5', 'Multi', 'Multi', 'Multi'],
        'precio': [59.99, 69.99, 59.99, 29.99, 39.99, 69.99, 49.99, 39.99, 19.99, 29.99],
        'descuento': [0, 10, 0, 50, 0, 0, 20, 0, 0, 0],
        'imagen': [f"game_{i}.jpg" for i in range(1, 11)],
        'categoria': ['Aventura', 'Acción', 'RPG', 'RPG', 'Deportes', 'FPS', 'Aventura', 'Acción', 'Sandbox', 'Acción']
    })

games_df = load_game_data()

# Función para mostrar un juego
def show_game_card(game):
    col1, col2 = st.columns([1, 3])
    
    with col1:
        # Aquí es donde normalmente cargaríamos una imagen real
        # Como no tenemos imágenes reales, usamos un placeholder
        st.image("https://via.placeholder.com/150x200", caption="")
        
    with col2:
        st.markdown(f"<div class='game-title'>{game['titulo']}</div>", unsafe_allow_html=True)
        st.write(f"Plataforma: {game['plataforma']}")
        st.write(f"Categoría: {game['categoria']}")
        
        if game['descuento'] > 0:
            precio_original = game['precio']
            precio_final = precio_original * (1 - game['descuento']/100)
            st.markdown(f"""
                <span style='text-decoration: line-through;'>${precio_original:.2f}</span> 
                <span class='game-price'>${precio_final:.2f}</span> 
                <span style='color: red;'>(-{game['descuento']}%)</span>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"<span class='game-price'>${game['precio']:.2f}</span>", unsafe_allow_html=True)
        
        st.button("Añadir al Carrito", key=f"btn_{game['id']}")

# Contenido principal según la navegación
if menu == "Inicio":
    # Banner principal
    st.image("https://via.placeholder.com/1200x300", caption="")
    
    # Juegos destacados
    st.markdown("<h2 class='section-title'>Juegos Destacados</h2>", unsafe_allow_html=True)
    
    # Mostrar juegos en filas de 3
    featured_games = games_df.head(6)
    rows = [featured_games.iloc[i:i+3] for i in range(0, len(featured_games), 3)]
    
    for row in rows:
        cols = st.columns(3)
        for i, (_, game) in enumerate(row.iterrows()):
            with cols[i]:
                st.markdown("<div class='game-card'>", unsafe_allow_html=True)
                show_game_card(game)
                st.markdown("</div>", unsafe_allow_html=True)
    
    # Categorías populares
    st.markdown("<h2 class='section-title'>Categorías Populares</h2>", unsafe_allow_html=True)
    categories = ["Acción", "Aventura", "RPG", "Deportes", "FPS", "Estrategia"]
    cat_cols = st.columns(len(categories))
    
    for i, category in enumerate(categories):
        with cat_cols[i]:
            st.button(category, key=f"cat_{category}")

elif menu == "Catálogo":
    # Filtros laterales
    st.sidebar.markdown("## Filtros")
    selected_platforms = st.sidebar.multiselect(
        "Plataforma", 
        options=["Nintendo Switch", "PS5", "Xbox Series X", "PC", "Multi"]
    )
    
    price_range = st.sidebar.slider("Rango de Precio", 0, 100, (0, 100))
    selected_categories = st.sidebar.multiselect(
        "Categoría", 
        options=["Acción", "Aventura", "RPG", "Deportes", "FPS", "Estrategia", "Sandbox"]
    )
    
    # Mostrar todos los juegos
    st.markdown("<h2 class='section-title'>Catálogo Completo</h2>", unsafe_allow_html=True)
    
    # Aplicar filtros si existen
    filtered_games = games_df
    if selected_platforms:
        filtered_games = filtered_games[filtered_games['plataforma'].isin(selected_platforms)]
    filtered_games = filtered_games[(filtered_games['precio'] >= price_range[0]) & 
                                   (filtered_games['precio'] <= price_range[1])]
    if selected_categories:
        filtered_games = filtered_games[filtered_games['categoria'].isin(selected_categories)]
    
    # Mostrar juegos en filas de 3
    rows = [filtered_games.iloc[i:i+3] for i in range(0, len(filtered_games), 3)]
    
    for row in rows:
        cols = st.columns(3)
        for i, (_, game) in enumerate(row.iterrows()):
            with cols[i]:
                st.markdown("<div class='game-card'>", unsafe_allow_html=True)
                show_game_card(game)
                st.markdown("</div>", unsafe_allow_html=True)

elif menu == "Ofertas":
    st.markdown("<h2 class='section-title'>Juegos en Oferta</h2>", unsafe_allow_html=True)
    
    # Filtrar juegos con descuento
    discounted_games = games_df[games_df['descuento'] > 0]
    
    # Mostrar juegos en filas de 3
    rows = [discounted_games.iloc[i:i+3] for i in range(0, len(discounted_games), 3)]
    
    for row in rows:
        cols = st.columns(3)
        for i, (_, game) in enumerate(row.iterrows()):
            with cols[i]:
                st.markdown("<div class='game-card'>", unsafe_allow_html=True)
                show_game_card(game)
                st.markdown("</div>", unsafe_allow_html=True)

elif menu == "Contacto":
    st.markdown("<h2 class='section-title'>Contáctanos</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("### Información de Contacto")
        st.write("📞 Teléfono: +34 123 456 789")
        st.write("✉️ Email: info@gamestore.com")
        st.write("🏢 Dirección: Calle de los Videojuegos, 123, 28001 Madrid")
        
        st.write("### Horario de Atención")
        st.write("Lunes a Viernes: 10:00 - 20:00")
        st.write("Sábados: 10:00 - 14:00")
        st.write("Domingos: Cerrado")
    
    with col2:
        st.write("### Envíanos un mensaje")
        nombre = st.text_input("Nombre")
        email = st.text_input("Email")
        asunto = st.text_input("Asunto")
        mensaje = st.text_area("Mensaje")
        
        st.button("Enviar Mensaje")

# Footer
st.markdown("""
<div class="footer">
    <div style="display: flex; justify-content: space-around; max-width: 800px; margin: 0 auto;">
        <div>
            <h4>GameStore</h4>
            <p>Tu tienda de videojuegos de confianza desde 2010</p>
        </div>
        <div>
            <h4>Enlaces rápidos</h4>
            <p>Inicio | Catálogo | Ofertas | Contacto</p>
        </div>
        <div>
            <h4>Síguenos</h4>
            <p>Facebook | Twitter | Instagram</p>
        </div>
    </div>
    <p>© 2025 GameStore. Todos los derechos reservados.</p>
</div>
""", unsafe_allow_html=True)
