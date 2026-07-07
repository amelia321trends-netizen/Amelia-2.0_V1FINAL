# actualizador_rta.ps1
# Script de actualizacion de contingencia local para Windows (sin dependencias de Python)
# Nota: Este script esta escrito en ASCII puro y usa comillas simples para formateo de cadenas robusto.

Write-Host "Iniciando actualizacion de Inteligencia RTA desde PowerShell local..." -ForegroundColor Cyan

# # --- DATOS DE CLIENTES ---
$ClientsData = @{
    "SODIMAC COLOMBIA S.A" = @{
        short_name = "Sodimac"
        url_menu = "https://www.sodimac.com.co/sodimac-co/categoria/muebles"
        base_traffic = 92
        own_brand = 45.5
        country = "Colombia"
        cities = @("Bogota", "Medellin", "Cali", "Barranquilla")
        best_sellers = @("Modulo Fregadero MDP-RH 100cm", "Escritorio Home Office Smart 120cm", "Estanterias RTA Metalicas")
        future_sources = @("MercadoLibre Colombia (Tendencias de Busqueda)", "Homecenter Chile (Benchmark de Clones de Diseno)", "Google Analytics RTA (Tasa de rebote en categoria de cocinas modulares y descargas de instructivos de armado)")
        competitive_set = @("Cencosud", "Almacenes Exito", "Corona")
        jtbd = @{
            persona = "Remodelador Practico"
            job = "Optimizar el espacio de la cocina y zona de ropas de forma rapida y sin herramientas complejas."
            pain_points = "Aglomerados que se inflan con humedad, herrajes faltantes y manuales de ensamble confusos."
            triggers = "Renovacion de arriendo o mudanza a departamento nuevo de interes social (VIS)."
        }
        raw_menu_categories = @(
            "Muebles de Cocina - Modulares",
            "Ofertas Imperdibles de Cocinas",
            "Escritorios Home Office de Descuento",
            "Muebles de TV y Centros de Entretenimiento",
            "Estanterias y Closets RTA",
            "Descuentos de Cyber en Banos",
            "Muebles de Bano RH Resistentes a Humedad",
            "Combos Dormitorio con Ofertas Especiales"
        )
        products = @(
            @{ name = "Modulo Fregadero 100cm MDP Estandar"; rh = $false; assembly = "estandar"; desc = "Estructura aglomerada 15mm" },
            @{ name = "Escritorio Home Office Smart 120cm"; rh = $false; assembly = "minifix"; desc = "Ensamble rapido con tornillos minifix" },
            @{ name = "Modulo Alto de Cocina 60cm MDP-RH"; rh = $true; assembly = "estandar"; desc = "Madera resistente a humedad" },
            @{ name = "Centro de TV Prime Nogal 55 pulgadas"; rh = $false; assembly = "estandar"; desc = "Acabado estetico melaminico" }
        )
    }
    "INVERSIONES VIRTUAL MUEBLES S.A.S" = @{
        short_name = "Virtual Muebles"
        url_menu = "https://www.virtualmuebles.com/muebles-rta"
        base_traffic = 78
        own_brand = 90.0
        country = "Colombia"
        cities = @("Medellin", "Bogota", "Envigado")
        best_sellers = @("Centro de TV Nordico Blanco-Roble", "Escritorio Gamer Pro", "Escritorio Plegable Work-Space")
        future_sources = @("Amazon Global (Tendencias de Diseno Industrial)", "Instagram Shopping (Engagement de Muebles RTA)", "Google Analytics RTA (Embudo de conversion de la linea Gamer y rebote en landings de escritorio flexible)")
        competitive_set = @("TuHome", "Mobbly", "Novaventa")
        jtbd = @{
            persona = "Comprador Digital Joven"
            job = "Amoblar su primer apartamento con disenos atractivos que se puedan comprar 100% en linea y recibir rapido."
            pain_points = "Dificultad de envio, falta de soporte para piezas danadas en transporte, desconfianza en fotos web."
            triggers = "Primer empleo profesional, independencia de casa de los padres."
        }
        raw_menu_categories = @(
            "Novedades y Lanzamientos Esteticos",
            "Salas y Centros de TV Design",
            "Blackfriday Muebles de Dormitorio",
            "Escritorios Flexibles Modernos",
            "Cocinas Modulares Low Cost",
            "Ofertas de Lanzamiento Muebles Bano",
            "Zapateros y Armarios Multifuncion"
        )
        products = @(
            @{ name = "Centro de TV Nordico Blanco-Roble"; rh = $false; assembly = "minifix"; desc = "Diseno estetico escandinavo" },
            @{ name = "Escritorio Plegable Work-Space"; rh = $false; assembly = "click"; desc = "Sistema de ensamble rapido click" },
            @{ name = "Mesa de Noche Minimalista con Cajon"; rh = $false; assembly = "estandar"; desc = "MDP texturizado" },
            @{ name = "Mueble Auxiliar Microondas MDP"; rh = $false; assembly = "estandar"; desc = "Mueble modular para electrodomesticos" }
        )
    }
    "GRUPO CORONA Y ALIADOS" = @{
        short_name = "Corona"
        url_menu = "https://www.corona.co/muebles"
        base_traffic = 85
        own_brand = 35.0
        country = "Colombia"
        cities = @("Bogota", "Medellin", "Barranquilla", "Cartagena")
        best_sellers = @("Gabinete de Bano suspendido 60cm RH", "Alacena Organizadora Multiusos RH", "Modulo Cocina con Meson de Acero")
        future_sources = @("Sodimac Constructor Portal (Precios de Contratistas)", "Corona Retail Analytics (Ventas de Banos y Cocinas)", "Google Analytics RTA (Comportamiento de busquedas de lavamanos hidrofugos y descargas de fichas de garantia)")
        competitive_set = @("Sodimac", "Cencosud", "Ferreteria EPA")
        jtbd = @{
            persona = "Maestro Especialista / Instalador"
            job = "Instalar gabinetes de alta durabilidad en zonas expuestas a humedad, garantizando calidad al cliente final."
            pain_points = "Falsas promesas de resistencia al agua, herrajes que se oxidan en banos y cocinas costeras."
            triggers = "Contratos de remodelacion comercial o residencial en zonas humedas."
        }
        raw_menu_categories = @(
            "Muebles de Bano Certificados RH",
            "Cyber Muebles Sanitarios",
            "Cocinas Modulares con Meson",
            "Oferta Especial de Lavaplatos RTA",
            "Organizadores y Alacenas",
            "Garantia Corona en Muebles",
            "Muebles de Lavanderia Funcionales"
        )
        products = @(
            @{ name = "Gabinete de Bano suspendido 60cm RH"; rh = $true; assembly = "estandar"; desc = "Tablero RH resistente al agua" },
            @{ name = "Alacena Organizadora Multiusos RH"; rh = $true; assembly = "estandar"; desc = "Estructura hidrofuga" },
            @{ name = "Modulo Cocina con Meson de Acero"; rh = $false; assembly = "estandar"; desc = "Cocina basica MDP" },
            @{ name = "Mesa de Centro Estetica Corona"; rh = $false; assembly = "estandar"; desc = "Melamina texturizada" }
        )
    }
    "TUHOME SPA" = @{
        short_name = "TuHome"
        url_menu = "https://www.tuhome.cl/productos"
        base_traffic = 80
        own_brand = 95.0
        country = "Chile"
        cities = @("Santiago", "Concepcion", "Valparaiso", "Antofagasta")
        best_sellers = @("Escritorio Home Office Z-60 Nogal", "Mueble Lavamanos Split RH", "Closet RTA 4 Puertas Wengue")
        future_sources = @("Falabella.com Chile (Surtido y Quiebres de Stock)", "MercadoLibre Chile (Palabras clave de Muebles)", "Google Analytics RTA (Porcentaje de abandono del checkout B2B y telemetria de visualizacion de closets)")
        competitive_set = @("Virtual Muebles", "Mobbly", "Cencosud")
        jtbd = @{
            persona = "Hogares en Crecimiento"
            job = "Adaptar el mobiliario del hogar segun el crecimiento de los hijos con soluciones modulares y escalables."
            pain_points = "Muebles pesados dificiles de mover, poca variedad en tonos de madera real, ensamble que requiere 2 personas."
            triggers = "Llegada de un nuevo hijo o reorganizacion de dormitorios."
        }
        raw_menu_categories = @(
            "Coleccion Cocina y Despensa Modulares",
            "Descuentos Exclusivos Dormitorio",
            "Centros de Entretenimiento Modernos",
            "Linea Oficina y Escritorios RTA",
            "Muebles Auxiliares de Bano",
            "Cyber Ofertas Muebles de Jardin",
            "Novedades Diseno Industrial RTA"
        )
        products = @(
            @{ name = "Escritorio Home Office Z-60 Nogal"; rh = $false; assembly = "minifix"; desc = "Ensamble rapido con minifix" },
            @{ name = "Modulo de Cocina Auxiliar 2 Puertas"; rh = $false; assembly = "estandar"; desc = "Tablero estandar MDP" },
            @{ name = "Mueble Lavamanos Split RH"; rh = $true; assembly = "minifix"; desc = "Base hidrofuga con herrajes rapidos" },
            @{ name = "Closet RTA 4 Puertas Wengue"; rh = $false; assembly = "estandar"; desc = "Estructura aglomerada de gran capacidad" }
        )
    }
    "FERRETERIA EPA" = @{
        short_name = "EPA"
        url_menu = "https://www.epa.com.ve/muebles-rta"
        base_traffic = 70
        own_brand = 30.0
        country = "Venezuela"
        cities = @("Caracas", "Valencia", "Maracaibo", "Barquisimeto")
        best_sellers = @("Gabinete Auxiliar de Planchado MDP", "Escritorio Estudiante Basic Gris", "Modulo Cocina Fregadero 120cm")
        future_sources = @("MercadoLibre Venezuela (Demanda de Muebles RTA de Bajo Costo)", "EPA Costa Rica/El Salvador (Benchmarking de Precios RTA)", "Google Analytics RTA (Tasa de conversion en el configurador de muebles modulares de cocina)")
        competitive_set = @("Sodimac", "Novey", "Cencosud")
        jtbd = @{
            persona = "Auto-constructor RTA"
            job = "Hacer mejoras funcionales en el hogar los fines de semana de forma economica."
            pain_points = "Falta de herramientas de ensamble en casa, tornilleria incompleta en el empaque original."
            triggers = "Proyecto DIY (Hagalo usted mismo) de fin de semana."
        }
        raw_menu_categories = @(
            "Muebles Modulares para Cocina",
            "Armarios and Alacenas en Promocion",
            "Escritorios RTA Practicos",
            "Cyberlunes Muebles de Sala",
            "Linea de Organizadores Economicos",
            "Muebles de Bano Basicos"
        )
        products = @(
            @{ name = "Gabinete Auxiliar de Planchado MDP"; rh = $false; assembly = "estandar"; desc = "Tablero aglomerado estandar" },
            @{ name = "Escritorio Estudiante Basic Gris"; rh = $false; assembly = "estandar"; desc = "Estructura metalica y MDP" },
            @{ name = "Modulo Cocina Fregadero 120cm"; rh = $false; assembly = "estandar"; desc = "No resistente a humedad" },
            @{ name = "Gabinete Aereo Bano con Espejo"; rh = $false; assembly = "estandar"; desc = "MDP estandar" }
        )
    }
    "MOBBLY S.A.S" = @{
        short_name = "Mobbly"
        url_menu = "https://www.mobbly.com.co/rta-trends"
        base_traffic = 65
        own_brand = 80.0
        country = "Colombia"
        cities = @("Bogota", "Medellin", "Cali")
        best_sellers = @("Escritorio Gamer Pro con Luces LED", "Mesa de TV Flotante 140cm", "Biblioteca Modular 5 Niveles")
        future_sources = @("Pinterest Latam (Busquedas de Muebles Juveniles)", "TikTok Shopping (Conversion RTA en Audiencia Joven)", "Google Analytics RTA (Engagement en paginas de producto con visualizacion interactiva de centros de TV)")
        competitive_set = @("Virtual Muebles", "TuHome", "Novaventa")
        jtbd = @{
            persona = "Estudiante o Joven Profesional"
            job = "Montar un espacio de estudio o trabajo estetico y ergonomico con un presupuesto muy ajustado."
            pain_points = "Escritorios inestables, acabados que se rayan con facilidad, falta de espacio para cables."
            triggers = "Inicio de semestre universitario o transicion a trabajo remoto."
        }
        raw_menu_categories = @(
            "Escritorios Gamer y Home Office RTA",
            "Descuento en Linea Gamer Mobbly",
            "Estanterias Modulares Libres de Ruido",
            "Mesas de TV y Centros de Diseno",
            "Cyber Muebles Dormitorio Moderno"
        )
        products = @(
            @{ name = "Escritorio Gamer Pro con Luces LED"; rh = $false; assembly = "minifix"; desc = "Diseno ergonomico juvenil" },
            @{ name = "Mesa de TV Flotante 140cm"; rh = $false; assembly = "minifix"; desc = "Sistema de anclaje de pared" },
            @{ name = "Biblioteca Modular 5 Niveles"; rh = $false; assembly = "estandar"; desc = "Estructura MDP texturizado" },
            @{ name = "Comoda 4 Cajones Compacta"; rh = $false; assembly = "estandar"; desc = "Melamina color roble" }
        )
    }
    "ALMACENES EXITO S.A." = @{
        short_name = "Exito"
        url_menu = "https://www.exito.com/muebles"
        base_traffic = 94
        own_brand = 25.0
        country = "Colombia"
        cities = @("Medellin", "Bogota", "Cali", "Barranquilla")
        best_sellers = @("Closet RTA 3 Puertas Finlandek", "Escritorio Compacto Office Finlandek", "Gabinete Cocina Auxiliar con Ruedas")
        future_sources = @("Grupo Exito Marketplace (Conversion de Canje de Puntos)", "Carrefour Brasil (Modelos RTA de Alta Frecuencia)", "Google Analytics RTA (Trafico derivado a la categoria de dormitorio infantil y tasa de descarga de planos RTA)")
        competitive_set = @("Cencosud", "Sodimac", "Novaventa")
        jtbd = @{
            persona = "Madre de Familia / Administradora del Hogar"
            job = "Comprar muebles para organizar los cuartos de los ninos aprovechando puntos de lealtad y promociones de supermercado."
            pain_points = "Dificultad para coordinar la entrega con el mercado semanal, calidad inconsistente en productos importados."
            triggers = "Ofertas de fin de mes o acumulacion de puntos de fidelidad."
        }
        raw_menu_categories = @(
            "Muebles de Dormitorio y Closets RTA",
            "Descuentos Blackfriday Muebles",
            "Escritorios Finlandia Finlandek",
            "Cyber Ofertas Cocinas Listas",
            "Centros de Entretenimiento en Promocion",
            "Muebles Auxiliares de Cocina y Bano"
        )
        products = @(
            @{ name = "Closet RTA 3 Puertas Finlandek"; rh = $false; assembly = "estandar"; desc = "Madera aglomerada estandar" },
            @{ name = "Escritorio Compacto Office Finlandek"; rh = $false; assembly = "estandar"; desc = "Diseno simple estudiantil" },
            @{ name = "Gabinete Cocina Auxiliar con Ruedas"; rh = $false; assembly = "estandar"; desc = "MDP melaminico" },
            @{ name = "Mesa Auxiliar Multiusos 1 Cajon"; rh = $false; assembly = "estandar"; desc = "Finlandek RTA" }
        )
    }
    "NOVAVENTA S.A.S" = @{
        short_name = "Novaventa"
        url_menu = "https://www.novaventa.com.co/muebles-catalogo"
        base_traffic = 75
        own_brand = 15.0
        country = "Colombia"
        cities = @("Medellin", "Bogota", "Bucaramanga", "Cali")
        best_sellers = @("Mueble Zapatero RTA 12 Pares", "Escritorio Plegable Practico", "Organizador Microondas con Canastillas")
        future_sources = @("Novaventa App (Encuestas Directas a Mamas Empresarias)", "Leonisa/Catalogo Hogar (Analisis de Surtido Competidor)", "Google Analytics RTA (Interacciones en catalogo interactivo y clics de pedido rapido de zapateros)")
        competitive_set = @("Almacenes Exito", "Virtual Muebles", "Mobbly")
        jtbd = @{
            persona = "Mama Empresaria / Vendedora por Catalogo"
            job = "Ofrecer a sus vecinos de confianza muebles RTA practicos y de bajo costo que paguen a plazos comodos."
            pain_points = "Complicacion en el ensamble post-venta, cajas muy pesadas para transportar, cobros dificiles si el mueble falla."
            triggers = "Oportunidades de catalogo mensual para aumentar ingresos extras."
        }
        raw_menu_categories = @(
            "Muebles Practicos del Catálogo Novaventa",
            "Oferta Especial de Closets RTA",
            "Escritorios Juveniles en Descuento",
            "Organizadores de Cocina Practicos",
            "Cyber Muebles Auxiliares de Hogar"
        )
        products = @(
            @{ name = "Mueble Zapatero RTA 12 Pares"; rh = $false; assembly = "minifix"; desc = "Facil ensamble por catalogo" },
            @{ name = "Escritorio Plegable Practico"; rh = $false; assembly = "click"; desc = "Sistema autoensamble sin herramientas" },
            @{ name = "Organizador Microondas con Canastillas"; rh = $false; assembly = "estandar"; desc = "Estructura metalica y MDP" },
            @{ name = "Estanteria Multiusos 4 repisas"; rh = $false; assembly = "estandar"; desc = "Ligero y facil de ubicar" }
        )
    }
    "CENCOSUD COLOMBIA SA" = @{
        short_name = "Cencosud"
        url_menu = "https://www.jumbo.co/muebles-rta"
        base_traffic = 88
        own_brand = 30.0
        country = "Colombia"
        cities = @("Bogota", "Medellin", "Cali", "Barranquilla")
        best_sellers = @("Centro de TV Florencia Wengue", "Escritorio L-Shape Industrial Easy", "Modulo Cocina Aéreo Easy 100cm")
        future_sources = @("Easy Argentina/Chile (Surtido de Muebles RTA Krea)", "MercadoLibre Colombia (Precios de Centros de TV)", "Google Analytics RTA (Busqueda interna de centros de TV y tasa de abandono en carritos de muebles de sala)")
        competitive_set = @("Sodimac", "Almacenes Exito", "Corona")
        jtbd = @{
            persona = "Comprador de Hogar de Clase Media"
            job = "Encontrar un mueble de sala o estudio de buena apariencia que encaje exactamente en la sala de su apartamento sin gastar una fortuna."
            pain_points = "Falta de informacion clara sobre dimensiones en la web, retrasos en el despacho a domicilio."
            triggers = "Remodelacion de la sala para recibir visitas de fin de ano."
        }
        raw_menu_categories = @(
            "Centros de TV y Entretenimiento Easy",
            "Ofertas de Cyber en Muebles Easy",
            "Closets y Comodas RTA en Descuento",
            "Escritorios y Sillas de Oficina",
            "Muebles de Cocina y Comedor RTA",
            "Blackfriday Armarios Modulares"
        )
        products = @(
            @{ name = "Centro de TV Florencia Wengue"; rh = $false; assembly = "estandar"; desc = "Estilo moderno melaminico" },
            @{ name = "Escritorio L-Shape Industrial Easy"; rh = $false; assembly = "estandar"; desc = "Estructura metalica y MDP" },
            @{ name = "Modulo Cocina Aéreo Easy 100cm"; rh = $false; assembly = "estandar"; desc = "MDP estandar" },
            @{ name = "Mesa de Noche Krea 2 cajones"; rh = $false; assembly = "estandar"; desc = "Aglomerado basico" }
        )
    }
    "CORPORACION FAVORITA C.A." = @{
        short_name = "Favorita"
        url_menu = "https://www.sukasa.com/muebles-rta"
        base_traffic = 82
        own_brand = 20.0
        country = "Ecuador"
        cities = @("Quito", "Guayaquil", "Cuenca", "Manta")
        best_sellers = @("Aparador Buffet Nordico 150cm", "Centro de Entretenimiento Rovere", "Mueble de Bano Suspendido Zen RH")
        future_sources = @("Sukasa Online (Tendencias de Muebles de Alta Gama)", "MercadoLibre Ecuador (Precios de Muebles RTA de Comedor)", "Google Analytics RTA (Telemetria de la linea premium y clics en el boton de contacto para proyectos de sala)")
        competitive_set = @("Novey", "TuHome", "Sodimac")
        jtbd = @{
            persona = "Hogar Moderno Ecuatoriano"
            job = "Modernizar el comedor y la sala de estar con acabados elegantes y duraderos sin recurrir a carpinteros tradicionales."
            pain_points = "Poca oferta de disenos modernos en mercados locales, altos costos de importacion de muebles listos."
            triggers = "Fiestas locales o mudanza de fin de ano."
        }
        raw_menu_categories = @(
            "Muebles RTA de Diseno Exclusivo Sukasa",
            "Descuentos de Cyber en Comedores",
            "Aparadores y Centros de TV Modernos",
            "Escritorios Ejecutivos de Descuento",
            "Muebles Organizadores de Lujo"
        )
        products = @(
            @{ name = "Aparador Buffet Nordico 150cm"; rh = $false; assembly = "minifix"; desc = "Gran acabado estetico melaminico" },
            @{ name = "Centro de Entretenimiento Rovere"; rh = $false; assembly = "estandar"; desc = "Estructura robusta 18mm" },
            @{ name = "Mueble de Bano Suspendido Zen RH"; rh = $true; assembly = "minifix"; desc = "Modulo de bano en melamina RH" },
            @{ name = "Escritorio Executive Glass & Wood"; rh = $false; assembly = "estandar"; desc = "Combinacion vidrio y MDP" }
        )
    }
    "GEO F. NOVEY S.A." = @{
        short_name = "Novey"
        url_menu = "https://www.novey.com.pa/muebles"
        base_traffic = 74
        own_brand = 35.0
        country = "Panama"
        cities = @("Ciudad de Panama", "David", "Chitre", "Colon")
        best_sellers = @("Modulo Fregadero RH Novey 120cm", "Gabinete Espejo de Bano RH", "Escritorio Home Office Basic Rovere")
        future_sources = @("Novey.com.pa (Analytics de Busqueda de Productos Hidrofugos)", "Amazon EE.UU. (Importacion de Accesorios RTA a Panama)", "Google Analytics RTA (Trafico en fichas tecnicas de gabinetes de bano RH y descargas de guias de resistencia)")
        competitive_set = @("Favorita", "Sodimac", "Ferreteria EPA")
        jtbd = @{
            persona = "Propietario / Arrendador"
            job = "Amoblar de forma economica e higienica una propiedad en alquiler para proteger su valor a largo plazo."
            pain_points = "Danos por agua por descuido del inquilino, necesidad de reponer gabinetes deteriorados rapidamente."
            triggers = "Cambio de inquilino o adecuacion de departamento para Airbnb."
        }
        raw_menu_categories = @(
            "Muebles de Cocina Modular Novey",
            "Ofertas Cyber de Organizadores",
            "Muebles de Bano RH Hidrofugos",
            "Escritorios RTA de Alta Resistencia",
            "Descuentos Blackfriday Comodas"
        )
        products = @(
            @{ name = "Modulo Fregadero RH Novey 120cm"; rh = $true; assembly = "minifix"; desc = "Tablero RH resistente a humedad" },
            @{ name = "Escritorio Home Office Basic Rovere"; rh = $false; assembly = "estandar"; desc = "Tablero aglomerado estandar" },
            @{ name = "Organizador Lavanderia Multi-espacio"; rh = $false; assembly = "estandar"; desc = "MDP melaminico estandar" },
            @{ name = "Gabinete Espejo de Bano RH"; rh = $true; assembly = "minifix"; desc = "Gabinete hidrofugo de facil anclaje" }
        )
    }
}

# --- FILTROS Y LOGICA DE NEGOCIO ---

function Clean-AdvertisingNoise {
    param([string[]]$categories)
    $pattern = "(cyber|oferta|descuento|blackfriday|promocion|combo|barato|imperdible|descuentos|rebajas|lanzamiento|low cost)"
    $cleaned = @()
    foreach ($cat in $categories) {
        if ($cat -notmatch $pattern) {
            $cleaned += $cat.Trim()
        }
    }
    return $cleaned
}

function Analyze-CDTAndJTBD {
    param(
        [string[]]$cleanedCategories,
        [System.Collections.ArrayList]$products
    )
    
    $technicalWords = @('modular', 'rh', 'resistencia', 'medidas', 'alto', 'fregadero', 'suspender', 'plegable', 'auxiliar', 'lavanderia')
    $aestheticWords = @('nordico', 'diseno', 'design', 'moderno', 'exclusivo', 'nogal', 'wengue', 'blanco', 'sala', 'living', 'estetica', 'gamer')
    
    $techScore = 0
    $aesScore = 0
    
    $allText = ($cleanedCategories -join " ") + " " + (($products | ForEach-Object { $_.name }) -join " ")
    $allText = $allText.ToLower()
    
    foreach ($word in $technicalWords) {
        $techScore += ([regex]::Matches($allText, $word).Count)
    }
    foreach ($word in $aestheticWords) {
        $aesScore += ([regex]::Matches($allText, $word).Count)
    }
    
    if ($techScore -ge $aesScore) {
        $cdtFocus = "Benefit/Price-Driven (Atributos Tecnicos & Funcionalidad)"
    } else {
        $cdtFocus = "Design-Driven (Estetica, Acabados & Estilo de Vida)"
    }
    
    # Alertas de Espacios en Blanco
    $whiteSpaces = @()
    $totalProducts = $products.Count
    $rhProducts = ($products | Where-Object { $_.rh -eq $true }).Count
    $quickAssembly = ($products | Where-Object { $_.assembly -in 'minifix', 'click' }).Count
    
    $hasWetAreas = $false
    foreach ($cat in $cleanedCategories) {
        if ($cat.ToLower() -like "*cocina*" -or $cat.ToLower() -like "*bano*" -or $cat.ToLower() -like "*lavanderia*") {
            $hasWetAreas = $true
            break
        }
    }
    
    if ($hasWetAreas -and ($totalProducts -gt 0) -and (($rhProducts / $totalProducts) -lt 0.25)) {
        $pct = [int](($rhProducts / $totalProducts) * 100)
        $whiteSpaces += "Escasez de portafolio hidrofugo (RH) en zonas humedas. Solo el $pct% de los muebles de cocina/bano cuentan con propiedades hidrofugas."
    }
    
    if (($totalProducts -gt 0) -and (($quickAssembly / $totalProducts) -lt 0.30)) {
        $pctComplex = [int]((1 - ($quickAssembly / $totalProducts)) * 100)
        $whiteSpaces += "Deficit en sistemas de ensamble rapido (Minifix o Click). El catalogo aun depende en un $pctComplex% de tornilleria tradicional compleja."
    }
    
    return @{
        cdtFocus = $cdtFocus
        whiteSpaces = $whiteSpaces
    }
}

function New-WeekData {
    $processedClients = @()
    $totalWhitespaces = 0
    $rand = New-Object System.Random

    foreach ($entry in $ClientsData.GetEnumerator()) {
        $clientName = $entry.Key
        $info = $entry.Value
        
        $traffic = $info.base_traffic + $rand.Next(-3, 4)
        if ($traffic -lt 10) { $traffic = 10 }
        if ($traffic -gt 100) { $traffic = 100 }
        
        $brandWeight = [Math]::Round($info.own_brand + ($rand.NextDouble() * 3.0 - 1.5), 1)
        $cleanedCats = Clean-AdvertisingNoise $info.raw_menu_categories
        
        $analysisResult = Analyze-CDTAndJTBD -cleanedCategories $cleanedCats -products $info.products
        $cdtFocus = $analysisResult.cdtFocus
        
        # Asegurar que whiteSpaces siempre sea un ArrayList para evitar errores de tipo al agregar elementos mas tarde
        $whiteSpaces = [System.Collections.ArrayList]::new()
        if ($analysisResult.whiteSpaces -is [System.Collections.IList] -or $analysisResult.whiteSpaces -is [System.Array]) {
            foreach ($item in $analysisResult.whiteSpaces) { $whiteSpaces.Add($item) | Out-Null }
        } elseif ($analysisResult.whiteSpaces -ne $null -and $analysisResult.whiteSpaces -ne "") {
            $whiteSpaces.Add($analysisResult.whiteSpaces) | Out-Null
        }
        
        $totalWhitespaces += $whiteSpaces.Count
        
        if ($cdtFocus -like "*Benefit*") {
            $cdtTree = @(
                "1. Dimensiones y espacio disponible (Filtro numerico)",
                "2. Resistencia del material (Aglomerado estandar vs Tablero RH)",
                "3. Relacion precio-capacidad de almacenado"
            )
        } else {
            $cdtTree = @(
                "1. Combinacion de colores y estilo estetico (Nordico, Wengue, Industrial)",
                "2. Tipo de ensamble visual (Flotante, de patas de madera)",
                "3. Calificaciones de diseno y reviews en web"
            )
        }
        
        # CRM KPIs calculations
        $whitespacesCount = $whiteSpaces.Count
        $leadScore = [int]([Math]::Floor(($traffic * (100 - $brandWeight) * ($whitespacesCount + 1)) / 150))
        if ($leadScore -lt 0) { $leadScore = 0 }
        if ($leadScore -gt 100) { $leadScore = 100 }
        
        $suggestedPitch = "Ofrecer optimizacion de costos en tableros de MDP estandar de alto trafico"
        $hasRhGap = $false
        $hasAssemblyGap = $false
        foreach ($ws in $whiteSpaces) {
            if ($ws.ToLower() -like "*hidrofugo*" -or $ws.ToLower() -like "*rh*") { $hasRhGap = $true }
            if ($ws.ToLower() -like "*ensamble rapido*" -or $ws.ToLower() -like "*click*") { $hasAssemblyGap = $true }
        }
        
        $nextAction = "Coordinar sesion de co-creacion de diseno con su equipo de compras para presentar la nueva paleta de colores de tendencia (Rovere, Nordico, Wengue and Gamer) y planificar la renovacion del catalogo."
        if ($hasRhGap) {
            $suggestedPitch = "Ofrecer portafolio MDP-RH y Melamina Anti-humedad para Cocina/Bano"
            $nextAction = "Programar visita presencial con el equipo tecnico para certificar la resistencia a la humedad del portafolio MDP-RH y proponer el reemplazo de modulos de aglomerado estandar en zonas costeras."
        } elseif ($hasAssemblyGap) {
            $suggestedPitch = "Promocionar sistemas Click de Ensamble Rapido sin tornillos"
            $nextAction = "Enviar muestras fisicas de los tableros con herraje Click de ensamble rapido y agendar una demo virtual de 15 minutos para demostrar el ahorro de tiempo al comprador digital joven."
        } elseif ($cdtFocus -like "*Benefit*") {
            $suggestedPitch = "Presentar optimizacion de espesores MDP estandar para alto volumen"
            $nextAction = "Presentar propuesta de cotizacion preferencial en tableros de melamina estandar con espesores optimizados para grandes distribuidores que buscan liderar en precio."
        } else {
            $suggestedPitch = "Presentar nuevos acabados esteticos de tendencia (Nordico, Wengue y Gamer)"
        }
        
        $coastalCities = @("Barranquilla", "Cartagena", "Manta", "Guayaquil", "Colon", "David", "Valparaiso", "Antofagasta", "Ciudad de Panama")
        $isCoastal = $false
        foreach ($city in $info.cities) {
            foreach ($cc in $coastalCities) {
                if ($city.ToLower() -like "*$($cc.ToLower())*") {
                    $isCoastal = $true
                    break
                }
            }
            if ($isCoastal) { break }
        }
        
        $coastalChurnRisk = $false
        if ($isCoastal -and $hasRhGap) {
            $coastalChurnRisk = $true
        }

        $clientHash = @{
            name = $clientName
            country = $info.country
            cities = $info.cities
            best_sellers = $info.best_sellers
            future_sources = $info.future_sources
            menu_hierarchy = $cleanedCats
            cdt_focus = $cdtFocus
            cdt_tree = $cdtTree
            own_brand_weight = $brandWeight
            traffic_score = $traffic
            competitive_set = $info.competitive_set
            jtbd = $info.jtbd
            white_spaces = $whiteSpaces
            crm_lead_score = $leadScore
            crm_suggested_pitch = $suggestedPitch
            crm_next_action = $nextAction
            coastal_churn_risk = $coastalChurnRisk
        }
        
        $processedClients += $clientHash
    }
    
    $dominantTrend = "Benefit-Driven (RH & Ensamble)"
    if ($totalWhitespaces -le 6) {
        $dominantTrend = "Design-Driven (Estetica & Estilos)"
    }
    
    # Matriz de tendencias
    $trends = @(
        @{ name = "Cocinas Modulares"; x = (75 + $rand.Next(-2, 3)); y = (85 + $rand.Next(-1, 2)); phase = "Madurez" },
        @{ name = "Home Office"; x = (45 + $rand.Next(-3, 4)); y = (60 + $rand.Next(-2, 3)); phase = "Crecimiento" },
        @{ name = "Centros de TV"; x = (60 + $rand.Next(-1, 2)); y = (70 + $rand.Next(-2, 3)); phase = "Crecimiento" },
        @{ name = "Dormitorio RTA"; x = (80 + $rand.Next(-1, 3)); y = (50 + $rand.Next(-3, 2)); phase = "Madurez" },
        @{ name = "Banos RH"; x = (35 + $rand.Next(-4, 5)); y = (42 + $rand.Next(-2, 5)); phase = "Introduccion" }
    )

    return @{
        dominant_trend = $dominantTrend
        total_whitespaces = $totalWhitespaces
        trends = $trends
        clients = $processedClients
    }
}

# --- EJECUCION ---
$todayStr = (Get-Date).ToString("yyyy-MM-dd")

# --- RECOPILACION E HISTORICO ---

# Cargar historial existente si existe
$history = @{}
$dataPath = "data.json"

function Convert-PSCustomObjectToHashtable {
    param($InputObject)
    if ($InputObject -is [System.Management.Automation.PSCustomObject]) {
        $hash = @{}
        foreach ($property in $InputObject.PSObject.Properties) {
            $hash[$property.Name] = Convert-PSCustomObjectToHashtable -InputObject $property.Value
        }
        return $hash
    } elseif ($InputObject -is [System.Collections.IList] -or $InputObject -is [System.Array]) {
        $list = [System.Collections.ArrayList]::new()
        foreach ($item in $InputObject) {
            $list.Add((Convert-PSCustomObjectToHashtable -InputObject $item)) | Out-Null
        }
        return $list
    } else {
        return $InputObject
    }
}

if (Test-Path $dataPath) {
    try {
        $oldDataRaw = Get-Content -Path $dataPath -Raw -Encoding utf8
        if (![string]::IsNullOrEmpty($oldDataRaw)) {
            $oldData = ConvertFrom-Json $oldDataRaw
            if ($oldData -and $oldData.history) {
                $history = Convert-PSCustomObjectToHashtable -InputObject $oldData.history
                
                # Reparar crm_next_action en el historial cargado
                foreach ($weekKey in $history.Keys) {
                    $weekData = $history[$weekKey]
                    if ($weekData["clients"]) {
                        foreach ($c in $weekData["clients"]) {
                            if ([string]::IsNullOrEmpty($c["crm_next_action"])) {
                                $whiteSpaces = $c["white_spaces"]
                                $cdtFocus = $c["cdt_focus"]
                                $hasRhGap = $false
                                $hasAssemblyGap = $false
                                if ($whiteSpaces) {
                                    foreach ($ws in $whiteSpaces) {
                                        if ($ws.ToLower() -like "*hidrofugo*" -or $ws.ToLower() -like "*rh*") { $hasRhGap = $true }
                                        if ($ws.ToLower() -like "*ensamble rapido*" -or $ws.ToLower() -like "*click*") { $hasAssemblyGap = $true }
                                    }
                                }
                                $nextAction = "Coordinar sesion de co-creacion de diseno con su equipo de compras para presentar la nueva paleta de colores de tendencia (Rovere, Nordico, Wengue y Gamer) y planificar la renovacion del catalogo."
                                if ($hasRhGap) {
                                    $nextAction = "Programar visita presencial con el equipo tecnico para certificar la resistencia a la humedad del portafolio MDP-RH y proponer el reemplazo de modulos de aglomerado estandar en zonas costeras."
                                } elseif ($hasAssemblyGap) {
                                    $nextAction = "Enviar muestras fisicas de los tableros con herraje Click de ensamble rapido y agendar una demo virtual de 15 minutos para demostrar el ahorro de tiempo al comprador digital joven."
                                } elseif ($cdtFocus -like "*Benefit*") {
                                    $nextAction = "Presentar propuesta de cotizacion preferencial en tableros de melamina estandar con espesores optimizados para grandes distribuidores que buscan liderar en precio."
                                }
                                $c["crm_next_action"] = $nextAction
                            }
                        }
                    }
                }
            }
        }
    } catch {
        Write-Host "No se pudo cargar el historial anterior, se creara uno nuevo: $_" -ForegroundColor Yellow
    }
}

# Determinar si hay huecos semanales a rellenar
if ($history.Count -gt 0) {
    $sortedDates = $history.Keys | Sort-Object
    $lastDateStr = $sortedDates[-1]
    
    try {
        $lastDate = [datetime]::ParseExact($lastDateStr, "yyyy-MM-dd", $null)
        $today = [datetime]::ParseExact($todayStr, "yyyy-MM-dd", $null)
        
        $currentDate = $lastDate.AddDays(7)
        while ($currentDate -le $today) {
            $currentDateStr = $currentDate.ToString("yyyy-MM-dd")
            if (-not $history.ContainsKey($currentDateStr)) {
                Write-Host "Rellenando semana faltante en historial (PS): $currentDateStr" -ForegroundColor Yellow
                $history[$currentDateStr] = New-WeekData
            }
            $currentDate = $currentDate.AddDays(7)
        }
    } catch {
        Write-Host "Error al calcular fechas faltantes en PS: $_" -ForegroundColor Red
    }
}

if (-not $history.ContainsKey($todayStr)) {
    Write-Host "Generando datos para la semana actual (PS): $todayStr" -ForegroundColor Yellow
    $history[$todayStr] = New-WeekData
}

# Pre-cargar semanas históricas si es la primera ejecución (historial vacío o solo con hoy)
if ($history.Count -le 1) {
    $processedClients = $history[$todayStr].clients
    # Deep clone del cliente usando serialización a JSON temporal para evitar duplicar referencias
    $processedClientsJson = ConvertTo-Json $processedClients -Depth 10

    # --- 1. Post-Cyber & Coastal Rain Week (2026-06-04) ---
    $c_06_04 = Convert-PSCustomObjectToHashtable -InputObject (ConvertFrom-Json $processedClientsJson)
    $tot_ws_06_04 = 0
    foreach ($c in $c_06_04) {
        $newTraffic = $c.traffic_score - 3
        if ($newTraffic -lt 10) { $newTraffic = 10 }
        $c.traffic_score = $newTraffic
        
        if ($c.name -eq "GRUPO CORONA Y ALIADOS") {
            $c.white_spaces.Add("Deficit de portafolio hidrofugo (RH) en mueble de lavamanos suspendido (Zona Norte).") | Out-Null
        }
        $tot_ws_06_04 += $c.white_spaces.Count
        
        $leadScore = [int]([Math]::Floor(($c.traffic_score * (100 - $c.own_brand_weight) * ($c.white_spaces.Count + 1)) / 150))
        if ($leadScore -lt 0) { $leadScore = 0 }
        if ($leadScore -gt 100) { $leadScore = 100 }
        $c.crm_lead_score = $leadScore
    }
    $history["2026-06-04"] = @{
        dominant_trend = "Benefit-Driven (RH & Ensamble)"
        total_whitespaces = $tot_ws_06_04
        trends = @(
            @{ name = "Cocinas Modulares"; x = 74; y = 84; phase = "Madurez" },
            @{ name = "Home Office"; x = 46; y = 58; phase = "Crecimiento" },
            @{ name = "Centros de TV"; x = 60; y = 68; phase = "Crecimiento" },
            @{ name = "Dormitorio RTA"; x = 79; y = 50; phase = "Madurez" },
            @{ name = "Banos RH"; x = 36; y = 42; phase = "Introduccion" }
        )
        clients = $c_06_04
    }

    # --- 2. CyberDay Peak Week (2026-05-28) ---
    $c_05_28 = Convert-PSCustomObjectToHashtable -InputObject (ConvertFrom-Json $processedClientsJson)
    $tot_ws_05_28 = 0
    foreach ($c in $c_05_28) {
        $newTraffic = $c.traffic_score + 12
        if ($newTraffic -gt 100) { $newTraffic = 100 }
        $c.traffic_score = $newTraffic
        
        if ($c.name -eq "ALMACENES EXITO S.A." -or $c.name -eq "INVERSIONES VIRTUAL MUEBLES S.A.S") {
            $c.white_spaces.Add("Quiebre de stock critico en escritorios Home Office debido a alta demanda Cyber.") | Out-Null
        }
        $tot_ws_05_28 += $c.white_spaces.Count
        
        $leadScore = [int]([Math]::Floor(($c.traffic_score * (100 - $c.own_brand_weight) * ($c.white_spaces.Count + 1)) / 150))
        if ($leadScore -lt 0) { $leadScore = 0 }
        if ($leadScore -gt 100) { $leadScore = 100 }
        $c.crm_lead_score = $leadScore
    }
    $history["2026-05-28"] = @{
        dominant_trend = "Design-Driven (Estetica & Estilos)"
        total_whitespaces = $tot_ws_05_28
        trends = @(
            @{ name = "Cocinas Modulares"; x = 72; y = 80; phase = "Madurez" },
            @{ name = "Home Office"; x = 58; y = 75; phase = "Crecimiento" },
            @{ name = "Centros de TV"; x = 65; y = 74; phase = "Crecimiento" },
            @{ name = "Dormitorio RTA"; x = 78; y = 48; phase = "Madurez" },
            @{ name = "Banos RH"; x = 34; y = 38; phase = "Introduccion" }
        )
        clients = $c_05_28
    }

    # --- 3. Pre-Cyber Week (2026-05-21) ---
    $c_05_21 = Convert-PSCustomObjectToHashtable -InputObject (ConvertFrom-Json $processedClientsJson)
    $tot_ws_05_21 = 0
    foreach ($c in $c_05_21) {
        $newTraffic = $c.traffic_score - 5
        if ($newTraffic -lt 10) { $newTraffic = 10 }
        $c.traffic_score = $newTraffic
        
        if ($c.name -eq "GRUPO CORONA Y ALIADOS") {
            $c.white_spaces.Add("Deficit de portafolio hidrofugo (RH) en mueble de lavamanos suspendido (Zona Norte).") | Out-Null
        }
        $tot_ws_05_21 += $c.white_spaces.Count
        
        $leadScore = [int]([Math]::Floor(($c.traffic_score * (100 - $c.own_brand_weight) * ($c.white_spaces.Count + 1)) / 150))
        if ($leadScore -lt 0) { $leadScore = 0 }
        if ($leadScore -gt 100) { $leadScore = 100 }
        $c.crm_lead_score = $leadScore
    }
    $history["2026-05-21"] = @{
        dominant_trend = "Benefit-Driven (RH & Ensamble)"
        total_whitespaces = $tot_ws_05_21
        trends = @(
            @{ name = "Cocinas Modulares"; x = 73; y = 82; phase = "Madurez" },
            @{ name = "Home Office"; x = 44; y = 56; phase = "Crecimiento" },
            @{ name = "Centros de TV"; x = 59; y = 66; phase = "Crecimiento" },
            @{ name = "Dormitorio RTA"; x = 79; y = 49; phase = "Madurez" },
            @{ name = "Banos RH"; x = 35; y = 40; phase = "Introduccion" }
        )
        clients = $c_05_21
    }
}

# --- FUNCIONES DE SERIALIZACION JSON MANUAL ---

function Convert-WeekToJSON {
    param($weekData)
    
    $clientJSONList = @()
    foreach ($c in $weekData.clients) {
        $menuList = @()
        foreach ($item in $c.menu_hierarchy) { $menuList += ('"{0}"' -f $item) }
        $menuListStr = $menuList -join ", "
        
        $cdtList = @()
        foreach ($item in $c.cdt_tree) { $cdtList += ('"{0}"' -f $item) }
        $cdtListStr = $cdtList -join ", "
        
        $compList = @()
        foreach ($item in $c.competitive_set) { $compList += ('"{0}"' -f $item) }
        $compListStr = $compList -join ", "
        
        $wsList = @()
        foreach ($item in $c.white_spaces) { $wsList += ('"{0}"' -f $item) }
        $wsListStr = $wsList -join ", "

        $cityList = @()
        foreach ($item in $c.cities) { $cityList += ('"{0}"' -f $item) }
        $cityListStr = $cityList -join ", "

        $bestList = @()
        foreach ($item in $c.best_sellers) { $bestList += ('"{0}"' -f $item) }
        $bestListStr = $bestList -join ", "

        $futureList = @()
        foreach ($item in $c.future_sources) { $futureList += ('"{0}"' -f $item) }
        $futureListStr = $futureList -join ", "
        
        $coastalRiskStr = if ($c.coastal_churn_risk) { "true" } else { "false" }
        $clientJSON = '      {' + "`n" +
                      '        "name": "' + $c.name + '",' + "`n" +
                      '        "country": "' + $c.country + '",' + "`n" +
                      '        "cities": [ ' + $cityListStr + ' ],' + "`n" +
                      '        "best_sellers": [ ' + $bestListStr + ' ],' + "`n" +
                      '        "future_sources": [ ' + $futureListStr + ' ],' + "`n" +
                      '        "menu_hierarchy": [ ' + $menuListStr + ' ],' + "`n" +
                      '        "cdt_focus": "' + $c.cdt_focus + '",' + "`n" +
                      '        "cdt_tree": [ ' + $cdtListStr + ' ],' + "`n" +
                      '        "own_brand_weight": ' + $c.own_brand_weight + ',' + "`n" +
                      '        "traffic_score": ' + $c.traffic_score + ',' + "`n" +
                      '        "crm_lead_score": ' + $c.crm_lead_score + ',' + "`n" +
                      '        "crm_suggested_pitch": "' + $c.crm_suggested_pitch + '",' + "`n" +
                      '        "crm_next_action": "' + $c.crm_next_action + '",' + "`n" +
                      '        "coastal_churn_risk": ' + $coastalRiskStr + ',' + "`n" +
                      '        "competitive_set": [ ' + $compListStr + ' ],' + "`n" +
                      '        "jtbd": {' + "`n" +
                      '          "persona": "' + $c.jtbd.persona + '",' + "`n" +
                      '          "job": "' + $c.jtbd.job + '",' + "`n" +
                      '          "pain_points": "' + $c.jtbd.pain_points + '",' + "`n" +
                      '          "triggers": "' + $c.jtbd.triggers + '"' + "`n" +
                      '        },' + "`n" +
                      '        "white_spaces": [ ' + $wsListStr + ' ]' + "`n" +
                      '      }'
        $clientJSONList += $clientJSON
    }
    
    $allClientsJSON = $clientJSONList -join ",`n"
    
    $trendJSONList = @()
    foreach ($t in $weekData.trends) {
        $trendJSON = '      {"name": "' + $t.name + '", "x": ' + $t.x + ', "y": ' + $t.y + ', "phase": "' + $t.phase + '"}'
        $trendJSONList += $trendJSON
    }
    $allTrendsJSON = $trendJSONList -join ",`n"
    
    $weekJSON = '{' + "`n" +
                '    "dominant_trend": "' + $weekData.dominant_trend + '",' + "`n" +
                '    "total_whitespaces": ' + $weekData.total_whitespaces + ',' + "`n" +
                '    "trends": [' + "`n" +
                $allTrendsJSON + "`n" +
                '    ],' + "`n" +
                '    "clients": [' + "`n" +
                $allClientsJSON + "`n" +
                '    ]' + "`n" +
                '  }'
    return $weekJSON
}

function Convert-HistoryToJSON {
    param($currentDate, $historyObj)
    
    $historyWeeksJSON = @()
    foreach ($dateKey in $historyObj.Keys) {
        $weekJSON = Convert-WeekToJSON -weekData $historyObj[$dateKey]
        $historyWeeksJSON += ('    "{0}": {1}' -f $dateKey, $weekJSON)
    }
    $allWeeksJSON = $historyWeeksJSON -join ",`n"
    
    $fullJSON = '{' + "`n" +
                '  "current_date": "' + $currentDate + '",' + "`n" +
                '  "history": {' + "`n" +
                $allWeeksJSON + "`n" +
                '  }' + "`n" +
                '}'
    return $fullJSON
}

# --- GUARDAR Y ACTUALIZAR ---

$formattedJson = Convert-HistoryToJSON -currentDate $todayStr -historyObj $history

# Guardar data.json
[System.IO.File]::WriteAllText("data.json", $formattedJson, (New-Object System.Text.UTF8Encoding($false)))

# Inyectar en archivos HTML usando reemplazo de subcadena exacto
$htmlPaths = @("index.html")
foreach ($htmlPath in $htmlPaths) {
    if (Test-Path $htmlPath) {
        $htmlContent = Get-Content -Path $htmlPath -Raw -Encoding utf8
        
        $startTag = '<script id="market-data" type="application/json">'
        $endTag = '</script>'
        
        $startIdx = $htmlContent.IndexOf($startTag)
        if ($startIdx -ne -1) {
            $endIdx = $htmlContent.IndexOf($endTag, $startIdx)
            if ($endIdx -ne -1) {
                $before = $htmlContent.Substring(0, $startIdx + $startTag.Length)
                $after = $htmlContent.Substring($endIdx)
                $newHtml = $before + "`n" + $formattedJson + "`n" + $after
                
                [System.IO.File]::WriteAllText($htmlPath, $newHtml, (New-Object System.Text.UTF8Encoding($false)))
                Write-Host "Inyectada nueva data JSON en $htmlPath (metodo de subcadena seguro)" -ForegroundColor Green
            } else {
                Write-Host "Error: No se encontro la etiqueta de cierre en $htmlPath" -ForegroundColor Red
            }
        } else {
            Write-Host "Error: No se encontro la etiqueta de inicio en $htmlPath" -ForegroundColor Red
        }
    } else {
        Write-Host "Aviso: No se encuentra $htmlPath, omitiendo." -ForegroundColor Yellow
    }
}

# Generar README.md (reporte estatico basado en la semana actual)
$readmeContent = @()
$readmeContent += "# Inteligencia de Canales Digitales de Muebles RTA"
$readmeContent += ""
$readmeContent += "Ultima actualizacion semanal: " + $todayStr + " | Analista Principal: Amelia RTA"
$readmeContent += ""
$readmeContent += "Tendencia Dominante de Mercado: " + $dominantTrend
$readmeContent += "Total Alertas de Oportunidad (Espacios en Blanco): " + $totalWhitespaces
$readmeContent += ""
$readmeContent += "## Resumen de Visualizaciones del Dashboard"
$readmeContent += "- Matriz de Ciclo de Vida de Tendencias: Mapeo de categorias en fases de Introduccion, Crecimiento, Madurez o Declive."
$readmeContent += "- Trafico Digital vs. Presencia de Marca Propia: Comportamiento de penetracion de marca propia en relacion al volumen de trafico digital."
$readmeContent += ""
$readmeContent += "Para explorar las visualizaciones interactivas de Chart.js y aplicar filtros dinamicos, abre el archivo index.html en tu navegador."
$readmeContent += ""
$readmeContent += "---"
$readmeContent += "## Analisis Detallado por Cliente (11 Canales)"

foreach ($c in $processedClients) {
    $cName = $c.name
    $cWeight = $c.own_brand_weight
    $cTraffic = $c.traffic_score
    $cCountry = $c.country
    $cCities = $c.cities -join ", "
    $readmeContent += ""
    $readmeContent += "### " + $cName
    $readmeContent += "- **Pais:** " + $cCountry + " | **Ciudades Cobertura:** " + $cCities
    $readmeContent += "- **Peso Estimado de Marca Propia:** " + $cWeight + "% | **Indice de Trafico Digital:** " + $cTraffic + "/100"
    $readmeContent += ""
    $readmeContent += "#### Productos Mas Vendidos / Potenciados"
    foreach ($item in $c.best_sellers) {
        $readmeContent += "- " + $item
    }
    $readmeContent += ""
    $readmeContent += "#### Fuentes Futuras de Monitoreo Recomendadas"
    foreach ($item in $c.future_sources) {
        $readmeContent += "- " + $item
    }
    $readmeContent += ""
    $readmeContent += "#### Arquitectura y Jerarquia del Menu (Filtrado sin Ruido)"
    foreach ($item in $c.menu_hierarchy) {
        $readmeContent += "- " + $item
    }
    
    $readmeContent += ""
    $readmeContent += "#### Arbol de Decision de Compra (CDT) Digital"
    $cFocus = $c.cdt_focus
    $readmeContent += "- Enfoque Principal: " + $cFocus
    foreach ($item in $c.cdt_tree) {
        $readmeContent += "  - " + $item
    }
    
    $readmeContent += ""
    $readmeContent += "#### Set Competitivo Principal"
    $compString = $c.competitive_set -join ", "
    $readmeContent += "- " + $compString
    
    $jt = $c.jtbd
    $p = $jt.persona
    $j = $jt.job
    $dp = $jt.pain_points
    $tr = $jt.triggers
    $readmeContent += ""
    $readmeContent += "#### Perfil Buyer Persona (Jobs-To-Be-Done)"
    $readmeContent += "- Arquetipo: " + $p
    $readmeContent += "- Trabajo a Realizar (Job): " + $j
    $readmeContent += "- Puntos de Dolor (Pains): " + $dp
    $readmeContent += "- Disparador de Compra (Trigger): " + $tr
    
    $readmeContent += ""
    $readmeContent += "#### Alertas de Espacio en Blanco (Oportunidades de Catalogo)"
    if ($c.white_spaces.Count -gt 0) {
        foreach ($ws in $c.white_spaces) {
            $readmeContent += "- ALERTA: " + $ws
        }
    } else {
        $readmeContent += "- No se detectan alertas criticas en stock de tableros RH o ensamble rapido."
    }
    $readmeContent += ""
    $readmeContent += "---"
}

$readmeContent += ""
$readmeContent += "## Arquitectura del Sistema de Automatizacion"
$readmeContent += "Este repositorio se actualiza autonomamente cada lunes a las 00:00 UTC."
$readmeContent += ""
$readmeContent += '```mermaid'
$readmeContent += 'graph TD'
$readmeContent += '    A[Cron Job GitHub Actions] -->|Ejecuta| B(actualizador_rta.py)'
$readmeContent += '    B --> C[Scraping Simulado & Ingesta]'
$readmeContent += '    C --> D[Filtro Antirruido Regex]'
$readmeContent += '    D --> E[Clasificacion CDT/JTBD & Deteccion de Espacios]'
$readmeContent += '    E --> F[Inyeccion de JSON en index.html]'
$readmeContent += '    E --> G[Reescritura de README.md]'
$readmeContent += '    F & G --> H[Git Commit & Auto Push]'
$readmeContent += '```'

# Escribir README.md
$readmeContent | Out-File -FilePath "README.md" -Encoding utf8
Write-Host "Generado reporte estatico README.md" -ForegroundColor Green

Write-Host "Proceso finalizado con exito." -ForegroundColor Cyan
