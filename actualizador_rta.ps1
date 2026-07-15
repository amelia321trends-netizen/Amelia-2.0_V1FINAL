$ClientsData = [ordered]@{
    "SODIMAC COLOMBIA S.A" = @{
        short_name = "Sodimac Colombia"
        url_menu = "https://www.homecenter.com.co/homecenter-co/category/cat1770069/muebles-y-organizacion/"
        urls_ingesta = @("https://www.homecenter.com.co/homecenter-co/category/cat1770069/muebles-y-organizacion/")
        base_traffic = 90
        own_brand = 35.0
        country = "Colombia"
        cities = @(
            @{ ciudad = "Bogota"; es_costera = $false; humedad_relativa_promedio = 65 },
            @{ ciudad = "Medellin"; es_costera = $false; humedad_relativa_promedio = 68 },
            @{ ciudad = "Cali"; es_costera = $false; humedad_relativa_promedio = 70 },
            @{ ciudad = "Barranquilla"; es_costera = $true; humedad_relativa_promedio = 80 },
            @{ ciudad = "Cartagena"; es_costera = $true; humedad_relativa_promedio = 81 }
        )
        best_sellers = @("Módulo Fregadero MDP-RH 100cm", "Escritorio Home Office Smart 120cm", "Estanterías RTA Metálicas")
        future_sources = @("MercadoLibre Colombia (Tendencias de Búsqueda)", "Homecenter Chile (Benchmark de Clones de Diseño)", "Google Analytics RTA (Tasa de rebote en categoría de cocinas modulares y descargas de instructivos de armado)")
        competitive_set = @("Cencosud", "Madecentro")
        jtbd = @{
            persona = "Remodelador Práctico JtBD"
            job = "Optimizar el espacio de la cocina y zona de ropas de forma rápida y sin herramientas complejas."
            pain_points = "Aglomerados que se inflan con humedad, herrajes faltantes y manuales de ensamble confusos."
            triggers = "Renovación de arriendo o mudanza a departamento nuevo de interés social (VIS)."
        }
        raw_menu_categories = @("Muebles de Cocina - Modulares", "Muebles de TV y Centros de Entretenimiento", "Estanterías y Clósets RTA", "Muebles de Baño RH Resistentes a Humedad")
        products = @(
            @{ name = "Módulo Fregadero 100cm MDP Estándar"; rh = $false; assembly = "estandar"; desc = "Estructura aglomerada 15mm" },
            @{ name = "Escritorio Home Office Smart 120cm"; rh = $false; assembly = "minifix"; desc = "Ensamble rápido con tornillos minifix" },
            @{ name = "Módulo Alto de Cocina 60cm MDP-RH"; rh = $true; assembly = "estandar"; desc = "Madera resistente a humedad" },
            @{ name = "Centro de TV Prime Nogal 55 pulgadas"; rh = $false; assembly = "estandar"; desc = "Acabado estético melamínico" }
        )
    }
    "MADECENTRO S.A.S" = @{
        short_name = "Madecentro"
        url_menu = "https://madecentro.com/pages/muebles"
        urls_ingesta = @("https://madecentro.com/pages/muebles")
        base_traffic = 85
        own_brand = 20.0
        country = "Colombia"
        cities = @(
            @{ ciudad = "Bogota"; es_costera = $false; humedad_relativa_promedio = 65 },
            @{ ciudad = "Medellin"; es_costera = $false; humedad_relativa_promedio = 68 },
            @{ ciudad = "Cali"; es_costera = $false; humedad_relativa_promedio = 70 },
            @{ ciudad = "Barranquilla"; es_costera = $true; humedad_relativa_promedio = 80 },
            @{ ciudad = "Cartagena"; es_costera = $true; humedad_relativa_promedio = 82 }
        )
        best_sellers = @("Módulo Cocina RTA Premium", "Alacena Organizadora Multiusos Madecentro", "Escritorio Home Office Madecentro")
        future_sources = @("Madecentro Ventas Internas (ERP)", "Google Analytics RTA (Tasa de rebote en categoría de cocinas modulares y descargas de instructivos de armado)")
        competitive_set = @("Sodimac", "Easy")
        jtbd = @{
            persona = "Remodelador Práctico JtBD"
            job = "Encontrar tableros y módulos de cocina a medida listos para armar e instalar de inmediato."
            pain_points = "Hinchamiento de tableros de baja calidad por humedad, falta de herrajes en el kit de armado."
            triggers = "Renovación o instalación rápida de mobiliario de cocina o baño."
        }
        raw_menu_categories = @("Muebles de Cocina Listos para Armar", "Muebles de Oficina y Escritorios RTA", "Alacenas y Organizadores", "Muebles de Lavandería y Baño RH")
        products = @(
            @{ name = "Módulo Cocina RTA Premium"; rh = $false; assembly = "minifix"; desc = "Cocina modulada de ensamble rápido" },
            @{ name = "Alacena Organizadora Multiusos Madecentro"; rh = $false; assembly = "minifix"; desc = "Organizador multiusos" },
            @{ name = "Mueble de Baño Suspendido Madecentro RH"; rh = $true; assembly = "minifix"; desc = "Mueble resistente a humedad" },
            @{ name = "Escritorio Home Office Madecentro"; rh = $false; assembly = "click"; desc = "Escritorio rápido de armar" }
        )
    }
    "INVERSIONES VIRTUAL MUEBLES S.A.S" = @{
        short_name = "Virtual Muebles"
        url_menu = "https://www.virtualmuebles.com"
        urls_ingesta = @("https://www.virtualmuebles.com")
        base_traffic = 78
        own_brand = 90.0
        country = "Colombia"
        cities = @(
            @{ ciudad = "Medellin"; es_costera = $false; humedad_relativa_promedio = 68 },
            @{ ciudad = "Bogota"; es_costera = $false; humedad_relativa_promedio = 65 },
            @{ ciudad = "Envigado"; es_costera = $false; humedad_relativa_promedio = 66 }
        )
        best_sellers = @("Centro de TV Nórdico Blanco-Roble", "Escritorio Gamer Pro", "Escritorio Plegable Work-Space")
        future_sources = @("Amazon Global (Tendencias de Diseño Industrial)", "Instagram Shopping (Engagement de Muebles RTA)", "Google Analytics RTA (Embudo de conversión de la línea Gamer y rebote en landings de escritorio flexible)")
        competitive_set = @("TuHome", "Wayfair")
        jtbd = @{
            persona = "Comprador Digital Joven JtBD"
            job = "Amoblar su primer apartamento con diseños activos que se puedan comprar 100% en línea y recibir rápido."
            pain_points = "Dificultad de envío, falta de soporte para piezas dañadas en transporte, desconfianza en fotos web."
            triggers = "Primer empleo profesional, independencia de casa de los padres."
        }
        raw_menu_categories = @("Salas y Centros de TV Design", "Escritorios Flexibles Modernos", "Zapateros y Armarios Multifunción")
        products = @(
            @{ name = "Centro de TV Nórdico Blanco-Roble"; rh = $false; assembly = "minifix"; desc = "Diseño estético escandinavo" },
            @{ name = "Escritorio Plegable Work-Space"; rh = $false; assembly = "click"; desc = "Sistema de ensamble rápido click" },
            @{ name = "Mesa de Noche Minimalista con Cajón"; rh = $false; assembly = "estandar"; desc = " MDP texturizado" },
            @{ name = "Mueble Auxiliar Microondas MDP"; rh = $false; assembly = "estandar"; desc = "Mueble modular para electrodomésticos" }
        )
    }
    "GRUPO CORONA Y ALIADOS" = @{
        short_name = "Grupo Corona"
        url_menu = "https://corona.co/productos/muebles-para-cocinas/c/muebles-para-cocinas"
        urls_ingesta = @("https://corona.co/productos/muebles-para-cocinas/c/muebles-para-cocinas")
        base_traffic = 82
        own_brand = 25.0
        country = "Colombia"
        cities = @(
            @{ ciudad = "Bogota"; es_costera = $false; humedad_relativa_promedio = 65 },
            @{ ciudad = "Medellin"; es_costera = $false; humedad_relativa_promedio = 68 },
            @{ ciudad = "Cali"; es_costera = $false; humedad_relativa_promedio = 70 },
            @{ ciudad = "Barranquilla"; es_costera = $true; humedad_relativa_promedio = 80 }
        )
        best_sellers = @("Alacena de Cocina Corona", "Módulo de Baño suspendido Corona RH", "Módulo de Cocina Corona")
        future_sources = @("Corona Retail Analytics", "Google Analytics RTA (Tasa de rebote en categoría de cocinas modulares y descargas de instructivos de armado)")
        competitive_set = @("Sodimac", "Madecentro")
        jtbd = @{
            persona = "Maestro Especialista / Instalador"
            job = "Instalar gabinetes de alta durabilidad en zonas expuestas a humedad, garantizando calidad al cliente final."
            pain_points = "Falsas promesas de resistencia al agua, herrajes que se oxidan en baños y cocinas costeras."
            triggers = "Contratos de remodelación comercial o residencial en zonas húmedas."
        }
        raw_menu_categories = @("Muebles de Cocina - Modulares", "Muebles de Oficina y Escritorios RTA", "Alacenas y Organizadores", "Muebles de Lavandería y Baño RH")
        products = @(
            @{ name = "Alacena de Cocina Corona"; rh = $false; assembly = "minifix"; desc = "Alacena clásica de cocina" },
            @{ name = "Módulo de Baño suspendido Corona RH"; rh = $true; assembly = "minifix"; desc = "Módulo de baño resistente a humedad" },
            @{ name = "Módulo de Cocina Corona"; rh = $false; assembly = "minifix"; desc = "Cocina modulada de ensamble rápido" }
        )
    }
    "CENCOSUD COLOMBIA SA" = @{
        short_name = "Easy Colombia"
        url_menu = "https://www.easy.com.co/muebles"
        urls_ingesta = @("https://www.easy.com.co/muebles")
        base_traffic = 88
        own_brand = 30.0
        country = "Colombia"
        cities = @(
            @{ ciudad = "Bogota"; es_costera = $false; humedad_relativa_promedio = 65 },
            @{ ciudad = "Medellin"; es_costera = $false; humedad_relativa_promedio = 68 },
            @{ ciudad = "Cali"; es_costera = $false; humedad_relativa_promedio = 70 }
        )
        best_sellers = @("Centro de TV Florencia Wengue", "Escritorio L-Shape Industrial Easy", "Módulo Cocina Aéreo Easy 100cm")
        future_sources = @("Easy Argentina/Chile (Surtido de Muebles RTA Krea)", "MercadoLibre Colombia (Precios de Centros de TV)", "Google Analytics RTA (Búsqueda interna de centros de TV y tasa de abandono en carritos de muebles de sala)")
        competitive_set = @("Sodimac", "Madecentro")
        jtbd = @{
            persona = "Comprador de Hogar de Clase Media"
            job = "Encontrar un mueble de sala o estudio de buena apariencia que encaje exactamente en la sala de su apartamento sin gastar una fortuna."
            pain_points = "Falta de información clara sobre dimensiones en la web, retrasos en el despacho a domicilio."
            triggers = "Remodelación de la sala para recibir visitas de fin de año."
        }
        raw_menu_categories = @("Centros de TV y Entretenimiento Easy", "Escritorios y Sillas de Oficina", "Muebles de Cocina y Comedor RTA")
        products = @(
            @{ name = "Centro de TV Florencia Wengue"; rh = $false; assembly = "estandar"; desc = "Estilo moderno melamínico" },
            @{ name = "Escritorio L-Shape Industrial Easy"; rh = $false; assembly = "estandar"; desc = "Estructura metálica y MDP" },
            @{ name = "Módulo Cocina Aéreo Easy 100cm"; rh = $false; assembly = "estandar"; desc = "MDP estándar" },
            @{ name = "Mesa de Noche Krea 2 cajones"; rh = $false; assembly = "estandar"; desc = "Aglomerado básico" }
        )
    }
    "PROMART HOMECENTER" = @{
        short_name = "Promart"
        url_menu = "https://www.promart.pe/muebles"
        urls_ingesta = @("https://www.promart.pe/muebles")
        base_traffic = 83
        own_brand = 40.0
        country = "Perú"
        cities = @(
            @{ ciudad = "Lima"; es_costera = $true; humedad_relativa_promedio = 85 },
            @{ ciudad = "Arequipa"; es_costera = $false; humedad_relativa_promedio = 45 },
            @{ ciudad = "Trujillo"; es_costera = $true; humedad_relativa_promedio = 80 },
            @{ ciudad = "Chiclayo"; es_costera = $true; humedad_relativa_promedio = 82 }
        )
        best_sellers = @("Centro de TV Máncora Roble", "Escritorio Gamer Pro", "Alacena RTA Multifunción")
        future_sources = @("MercadoLibre Perú (Tendencias de Búsqueda)", "Promart Analytics (Ventas RTA)", "Google Analytics RTA (Tasa de rebote en cocinas modulares y descargas de instructivos)")
        competitive_set = @("Sodimac Perú", "IKEA USA")
        jtbd = @{
            persona = "Comprador Urbano Limeño"
            job = "Optimizar el espacio en departamentos de metrajes reducidos en Lima Metropolitana de forma práctica."
            pain_points = "Humedad severa de la costa de Lima que infla los tableros aglomerados de baja densidad y herrajes deficientes."
            triggers = "Renovación de departamento de alquiler o mudanza a proyecto de vivienda VIS."
        }
        raw_menu_categories = @("Muebles de Cocina - Modulares", "Escritorios y Oficina RTA", "Centros de TV y Entretenimiento", "Roperos y Clósets en Descuento", "Muebles de Baño RH Resistentes a Humedad")
        products = @(
            @{ name = "Centro de TV Máncora Roble"; rh = $false; assembly = "minifix"; desc = "Módulo de TV en melamina Rovere" },
            @{ name = "Escritorio Gamer Pro"; rh = $false; assembly = "minifix"; desc = "Estructura gamer reforzada" },
            @{ name = "Alacena RTA Multifunción"; rh = $false; assembly = "estandar"; desc = "Organizador modular estándar" },
            @{ name = "Mueble Lavamanos Suspendido RH"; rh = $true; assembly = "minifix"; desc = "Melamina RH resistente a humedad" }
        )
    }
    "SODIMAC PERÚ" = @{
        short_name = "Sodimac Perú"
        url_menu = "https://www.sodimac.com.pe"
        urls_ingesta = @("https://www.sodimac.com.pe")
        base_traffic = 85
        own_brand = 38.0
        country = "Perú"
        cities = @(
            @{ ciudad = "Lima"; es_costera = $true; humedad_relativa_promedio = 85 },
            @{ ciudad = "Arequipa"; es_costera = $false; humedad_relativa_promedio = 45 },
            @{ ciudad = "Trujillo"; es_costera = $true; humedad_relativa_promedio = 80 }
        )
        best_sellers = @("Módulo Fregadero Sodimac Perú", "Escritorio Home Office Sodimac Perú", "Clóset RTA Sodimac Perú")
        future_sources = @("Sodimac Perú Analytics", "Google Analytics RTA (Tasa de rebote en cocinas modulares y descargas de instructivos de armado)")
        competitive_set = @("Promart", "IKEA USA")
        jtbd = @{
            persona = "Comprador Urbano Limeño"
            job = "Optimizar el espacio en departamentos de metrajes reducidos en Lima Metropolitana de forma práctica."
            pain_points = "Humedad severa de la costa de Lima que infla los tableros aglomerados de baja densidad."
            triggers = "Mudanza o renovación estacional de cocina."
        }
        raw_menu_categories = @("Muebles de Cocina - Modulares", "Escritorios y Oficina RTA", "Centros de TV y Entretenimiento", "Muebles de Baño RH Resistentes a Humedad")
        products = @(
            @{ name = "Módulo Fregadero Sodimac Perú"; rh = $false; assembly = "minifix"; desc = "Cocina modulada de ensamble rápido" },
            @{ name = "Mueble de Baño Suspendido Sodimac Perú RH"; rh = $true; assembly = "minifix"; desc = "Módulo resistente a humedad" }
        )
    }
    "TUHOME SPA" = @{
        short_name = "TuHome"
        url_menu = "https://www.tuhome.cl"
        urls_ingesta = @("https://www.tuhome.cl")
        base_traffic = 80
        own_brand = 95.0
        country = "Chile"
        cities = @(
            @{ ciudad = "Santiago"; es_costera = $false; humedad_relativa_promedio = 60 },
            @{ ciudad = "Concepcion"; es_costera = $false; humedad_relativa_promedio = 75 },
            @{ ciudad = "Valparaiso"; es_costera = $true; humedad_relativa_promedio = 78 },
            @{ ciudad = "Antofagasta"; es_costera = $true; humedad_relativa_promedio = 72 }
        )
        best_sellers = @("Escritorio Home Office Z-60 Nogal", "Mueble Lavamanos Split RH", "Clóset RTA 4 Puertas Wengue")
        future_sources = @("Falabella.com Chile (Surtido y Quiebres de Stock)", "MercadoLibre Chile (Palabras clave de Muebles)", "Google Analytics RTA (Porcentaje de abandono del checkout B2B y telemetría de visualización de clósets)")
        competitive_set = @("Sodimac Chile", "IKEA España")
        jtbd = @{
            persona = "Hogares en Crecimiento"
            job = "Adaptar el mobiliario del hogar según el crecimiento de los hijos con soluciones modulares y escalables."
            pain_points = "Muebles pesados difíciles de mover, poca variedad en tonos de madera real, ensamble que requiere 2 personas."
            triggers = "Llegada de un nuevo hijo o reorganización de dormitorios."
        }
        raw_menu_categories = @("Colección Cocina y Despensa Modulares", "Centros de Entretenimiento Modernos", "Línea Oficina y Escritorios RTA", "Muebles Auxiliares de Baño", "Novedades Diseño Industrial RTA")
        products = @(
            @{ name = "Escritorio Home Office Z-60 Nogal"; rh = $false; assembly = "minifix"; desc = "Ensamble rápido con minifix" },
            @{ name = "Módulo de Cocina Auxiliar 2 Puertas"; rh = $false; assembly = "estandar"; desc = "Tablero estándar MDP" },
            @{ name = "Mueble Lavamanos Split RH"; rh = $true; assembly = "minifix"; desc = "Base hidrófuga con herrajes rápidos" },
            @{ name = "Clóset RTA 4 Puertas Wengue"; rh = $false; assembly = "estandar"; desc = "Estructura aglomerada de gran capacidad" }
        )
    }
    "SODIMAC CHILE" = @{
        short_name = "Sodimac Chile"
        url_menu = "https://www.sodimac.cl"
        urls_ingesta = @("https://www.sodimac.cl")
        base_traffic = 86
        own_brand = 40.0
        country = "Chile"
        cities = @(
            @{ ciudad = "Santiago"; es_costera = $false; humedad_relativa_promedio = 60 },
            @{ ciudad = "Concepcion"; es_costera = $false; humedad_relativa_promedio = 75 },
            @{ ciudad = "Valparaiso"; es_costera = $true; humedad_relativa_promedio = 78 }
        )
        best_sellers = @("Módulo Cocina Modular 120cm", "Clóset RTA Expandible", "Escritorio Compacto Madera")
        future_sources = @("Falabella.com Chile (Surtido y Quiebres de Stock)", "Google Analytics RTA (Porcentaje de abandono del checkout B2B y telemetría de visualización de clósets)")
        competitive_set = @("TuHome", "IKEA España")
        jtbd = @{
            persona = "Hogares en Crecimiento"
            job = "Adaptar el mobiliario del hogar según el crecimiento de los hijos con soluciones modulares y escalables."
            pain_points = "Muebles pesados difíciles de mover, poca variedad en tonos de madera real, ensamble que requiere 2 personas."
            triggers = "Llegada de un nuevo hijo o reorganización de dormitorios."
        }
        raw_menu_categories = @("Colección Cocina y Despensa Modulares", "Centros de Entretenimiento Modernos", "Línea Oficina y Escritorios RTA", "Muebles Auxiliares de Baño", "Novedades Diseño Industrial RTA")
        products = @(
            @{ name = "Módulo Cocina Modular 120cm"; rh = $false; assembly = "minifix"; desc = "Ensamble rápido con minifix" },
            @{ name = "Clóset RTA Expandible"; rh = $false; assembly = "estandar"; desc = "Tablero estándar MDP" },
            @{ name = "Escritorio Compacto Madera"; rh = $false; assembly = "minifix"; desc = "Escritorio estudiantil simple" }
        )
    }
    "LIVERPOOL MÉXICO" = @{
        short_name = "Liverpool"
        url_menu = "https://www.liverpool.com.mx"
        urls_ingesta = @("https://www.liverpool.com.mx")
        base_traffic = 88
        own_brand = 15.0
        country = "México"
        cities = @(
            @{ ciudad = "Ciudad de Mexico"; es_costera = $false; humedad_relativa_promedio = 55 },
            @{ ciudad = "Monterrey"; es_costera = $false; humedad_relativa_promedio = 50 },
            @{ ciudad = "Guadalajara"; es_costera = $false; humedad_relativa_promedio = 58 },
            @{ ciudad = "Veracruz"; es_costera = $true; humedad_relativa_promedio = 78 },
            @{ ciudad = "Merida"; es_costera = $true; humedad_relativa_promedio = 75 }
        )
        best_sellers = @("Centro de TV Liverpool Maderado", "Escritorio Home Office Premium Liverpool", "Gabinete Baño Moderno Liverpool")
        future_sources = @("Liverpool Analytics (Ventas de Muebles)", "Google Analytics RTA (Tasa de conversión en el configurador de muebles modulares)")
        competitive_set = @("Elektra", "IKEA USA")
        jtbd = @{
            persona = "Comprador de Diseño Premium JtBD"
            job = "Encontrar mobiliario estético, moderno y listo para llevar con acabados tipo madera natural."
            pain_points = "Precios elevados en mobiliario tradicional de madera maciza, dificultad de transporte."
            triggers = "Remodelación de sala o alcoba principal."
        }
        raw_menu_categories = @("Centros de TV y Entretenimiento Liverpool", "Escritorios RTA Premium", "Organizadores de Baño y Hogar")
        products = @(
            @{ name = "Centro de TV Liverpool Maderado"; rh = $false; assembly = "minifix"; desc = "Estilo moderno melamínico" },
            @{ name = "Gabinete Baño Moderno Liverpool"; rh = $false; assembly = "minifix"; desc = "MDP estándar" }
        )
    }
    "ELEKTRA MÉXICO" = @{
        short_name = "Elektra"
        url_menu = "https://www.elektra.mx"
        urls_ingesta = @("https://www.elektra.mx")
        base_traffic = 84
        own_brand = 25.0
        country = "México"
        cities = @(
            @{ ciudad = "Ciudad de Mexico"; es_costera = $false; humedad_relativa_promedio = 55 },
            @{ ciudad = "Monterrey"; es_costera = $false; humedad_relativa_promedio = 50 },
            @{ ciudad = "Guadalajara"; es_costera = $false; humedad_relativa_promedio = 58 },
            @{ ciudad = "Veracruz"; es_costera = $true; humedad_relativa_promedio = 78 }
        )
        best_sellers = @("Clóset Básico Elektra", "Escritorio Home Office Elektra", "Centro de TV Compacto Elektra")
        future_sources = @("Elektra Sales Analytics", "Google Analytics RTA (Tasa de conversión en el configurador de muebles modulares)")
        competitive_set = @("Liverpool", "IKEA USA")
        jtbd = @{
            persona = "Smart Shopper / Comprador de Presupuesto"
            job = "Encontrar mobiliario funcional, duradero y de bajo costo con facilidades de pago semanal o mensual."
            pain_points = "Falta de información sobre las dimensiones en la tienda física, transporte difícil."
            triggers = "Amoblar habitación infantil o estudio de bajo costo."
        }
        raw_menu_categories = @("Centros de TV y Comedores Elektra", "Escritorios y Sillas RTA", "Roperos y Organizadores Económicos")
        products = @(
            @{ name = "Clóset Básico Elektra"; rh = $false; assembly = "estandar"; desc = "Aglomerado básico" },
            @{ name = "Escritorio Home Office Elektra"; rh = $false; assembly = "minifix"; desc = "MDP estándar" }
        )
    }
    "LEROY MERLIN ESPAÑA" = @{
        short_name = "Leroy Merlin España"
        url_menu = "https://www.leroymerlin.es"
        urls_ingesta = @("https://www.leroymerlin.es")
        base_traffic = 87
        own_brand = 35.0
        country = "España"
        cities = @(
            @{ ciudad = "Madrid"; es_costera = $false; humedad_relativa_promedio = 50 },
            @{ ciudad = "Barcelona"; es_costera = $true; humedad_relativa_promedio = 72 },
            @{ ciudad = "Valencia"; es_costera = $true; humedad_relativa_promedio = 70 },
            @{ ciudad = "Sevilla"; es_costera = $false; humedad_relativa_promedio = 55 }
        )
        best_sellers = @("Armario RTA Modular Blanco", "Mueble Auxiliar de Cocina Haya", "Gabinete Suspendido de Baño RH")
        future_sources = @("Amazon España (Muebles más vendidos)", "Leroy Merlin Analytics (Consultas de Clientes)", "Google Analytics RTA (Tasa de rebote en armarios modulares y descargas de guías de montaje)")
        competitive_set = @("IKEA España", "IKEA USA")
        jtbd = @{
            persona = "Reformador DIY Español"
            job = "Montar soluciones de almacenaje a medida en pisos urbanos optimizando cada metro cuadrado."
            pain_points = "Herrajes de baja calidad que se doblan, falta de resistencia a la humedad en baños de pisos costeros, instrucciones poco claras."
            triggers = "Renovación de armarios estacionales o mudanzas de verano."
        }
        raw_menu_categories = @("Armarios y Clósets Modulares", "Muebles Auxiliares de Cocina", "Escritorios RTA de Oficina", "Muebles de Baño Suspendidos RH")
        products = @(
            @{ name = "Armario RTA Modular Blanco"; rh = $false; assembly = "estandar"; desc = "Estructura aglomerado melamina 16mm" },
            @{ name = "Mueble Auxiliar de Cocina Haya"; rh = $false; assembly = "minifix"; desc = "Módulo con ruedas y estantes" },
            @{ name = "Gabinete Suspendido de Baño RH"; rh = $true; assembly = "minifix"; desc = "Tablero hidrófugo resistente a la humedad" },
            @{ name = "Escritorio Home Office Basic Haya"; rh = $false; assembly = "estandar"; desc = "Escritorio estándar aglomerado" }
        )
    }
    "AMAZON USA" = @{
        short_name = "Amazon USA"
        url_menu = "https://www.amazon.com"
        urls_ingesta = @("https://www.amazon.com")
        base_traffic = 96
        own_brand = 20.0
        country = "USA"
        cities = @(
            @{ ciudad = "New York"; es_costera = $true; humedad_relativa_promedio = 68 },
            @{ ciudad = "Los Angeles"; es_costera = $true; humedad_relativa_promedio = 65 },
            @{ ciudad = "Miami"; es_costera = $true; humedad_relativa_promedio = 75 },
            @{ ciudad = "Chicago"; es_costera = $false; humedad_relativa_promedio = 62 },
            @{ ciudad = "Houston"; es_costera = $true; humedad_relativa_promedio = 74 }
        )
        best_sellers = @("Amazon Basics Writing Desk", "Rustic Wood TV Stand Amazon", "3-Drawer Storage Drawer Organizer")
        future_sources = @("Amazon US Bestsellers", "Google Analytics RTA (Embudo de conversión de la línea Gamer y descargas de manuales)")
        competitive_set = @("Wayfair USA", "IKEA USA")
        jtbd = @{
            persona = "Comprador de Conveniencia Digital"
            job = "Comprar mobiliario extremadamente económico con despacho prioritario de un día para otro."
            pain_points = "Calidad inconsistente del aglomerado, piezas rotas por transporte, falta de soporte técnico de armado."
            triggers = "Independencia estudiantil o armado rápido de oficina de teletrabajo."
        }
        raw_menu_categories = @("Home Office Furniture Amazon", "Living Room TV Stands", "Bedroom Dressers & Organizers")
        products = @(
            @{ name = "Amazon Basics Writing Desk"; rh = $false; assembly = "click"; desc = "Simple writing table" },
            @{ name = "Rustic Wood TV Stand Amazon"; rh = $false; assembly = "minifix"; desc = "MDP textured TV stand" }
        )
    }
    "WALMART USA" = @{
        short_name = "Walmart USA"
        url_menu = "https://www.walmart.com"
        urls_ingesta = @("https://www.walmart.com")
        base_traffic = 94
        own_brand = 25.0
        country = "USA"
        cities = @(
            @{ ciudad = "New York"; es_costera = $true; humedad_relativa_promedio = 68 },
            @{ ciudad = "Los Angeles"; es_costera = $true; humedad_relativa_promedio = 65 },
            @{ ciudad = "Miami"; es_costera = $true; humedad_relativa_promedio = 75 },
            @{ ciudad = "Chicago"; es_costera = $false; humedad_relativa_promedio = 62 },
            @{ ciudad = "Houston"; es_costera = $true; humedad_relativa_promedio = 74 }
        )
        best_sellers = @("Mainstays Writing Desk", "Mainstays 3-Drawer Dresser", "Mainstays Bathroom Cabinet RH")
        future_sources = @("Walmart Retail Analytics", "Google Analytics RTA (Tasa de rebote en cocinas modulares y descargas de instructivos)")
        competitive_set = @("Target", "IKEA USA")
        jtbd = @{
            persona = "Smart Shopper / Comprador de Presupuesto"
            job = "Encontrar mobiliario básico de hogar para llevar en caja el mismo día al menor costo."
            pain_points = "Aglomerados débiles de 12mm que se cuelgan en el centro, herrajes plásticos frágiles."
            triggers = "Mudanza temporal o amoblado estudiantil."
        }
        raw_menu_categories = @("Walmart Mainstays Home Office", "Walmart Bathroom Storage", "Walmart Bedroom Organizers")
        products = @(
            @{ name = "Mainstays Writing Desk"; rh = $false; assembly = "estandar"; desc = "Basic study desk" },
            @{ name = "Mainstays Bathroom Cabinet RH"; rh = $true; assembly = "minifix"; desc = "RH particleboard cabinet" }
        )
    }
    "WAYFAIR USA" = @{
        short_name = "Wayfair USA"
        url_menu = "https://www.wayfair.com"
        urls_ingesta = @("https://www.wayfair.com")
        base_traffic = 92
        own_brand = 15.0
        country = "USA"
        cities = @(
            @{ ciudad = "New York"; es_costera = $true; humedad_relativa_promedio = 68 },
            @{ ciudad = "Los Angeles"; es_costera = $true; humedad_relativa_promedio = 65 },
            @{ ciudad = "Miami"; es_costera = $true; humedad_relativa_promedio = 75 },
            @{ ciudad = "Chicago"; es_costera = $false; humedad_relativa_promedio = 62 },
            @{ ciudad = "Houston"; es_costera = $true; humedad_relativa_promedio = 74 }
        )
        best_sellers = @("Modular Closet System White", "Minimalist TV Stand Oak", "RTA Writing Desk with Shelves")
        future_sources = @("Wayfair Business Analytics", "Google Analytics RTA (Embudo de conversión de la línea Gamer y descargas de manuales)")
        competitive_set = @("IKEA USA", "Amazon USA")
        jtbd = @{
            persona = "Young Urban Professional"
            job = "Furnish rental apartments with stylish, affordable, and easy-to-move RTA furniture."
            pain_points = "Assembly taking too long, missing minor screws, particleboard cracking during screw insertion."
            triggers = "Moving to a new apartment, starting a remote job or college semester."
        }
        raw_menu_categories = @("Modular Living Room Furniture", "Home Office Writing Desks", "Clóset & Wardrobe Organizers", "Bath Storage Cabinets")
        products = @(
            @{ name = "Modular Closet System White"; rh = $false; assembly = "minifix"; desc = "White melamine finish cabinet" },
            @{ name = "Minimalist TV Stand Oak"; rh = $false; assembly = "minifix"; desc = "Oak textured media console" },
            @{ name = "RTA Writing Desk with Shelves"; rh = $false; assembly = "click"; desc = "Tool-less quick assembly desk" },
            @{ name = "Medicine Cabinet RH White"; rh = $true; assembly = "minifix"; desc = "RH particleboard bathroom storage" }
        )
    }
    "HOME DEPOT USA" = @{
        short_name = "Home Depot USA"
        url_menu = "https://www.homedepot.com"
        urls_ingesta = @("https://www.homedepot.com")
        base_traffic = 91
        own_brand = 30.0
        country = "USA"
        cities = @(
            @{ ciudad = "New York"; es_costera = $true; humedad_relativa_promedio = 68 },
            @{ ciudad = "Los Angeles"; es_costera = $true; humedad_relativa_promedio = 65 },
            @{ ciudad = "Miami"; es_costera = $true; humedad_relativa_promedio = 75 },
            @{ ciudad = "Chicago"; es_costera = $false; humedad_relativa_promedio = 62 },
            @{ ciudad = "Houston"; es_costera = $true; humedad_relativa_promedio = 74 }
        )
        best_sellers = @("Hampton Bay Kitchen Cabinet", "Hampton Bay Bath Vanity RH", "Hampton Bay Storage Closet")
        future_sources = @("Home Depot US Sales Analytics", "Google Analytics RTA (Tasa de rebote en cocinas modulares y descargas de instructivos de armado)")
        competitive_set = @("Lowe's USA", "IKEA USA")
        jtbd = @{
            persona = "Contratista / Dueño de Casa DIY"
            job = "Instalar de manera rápida y económica organizadores en cocheras, cocinas y baños de alta durabilidad."
            pain_points = "Falta de herrajes en el empaque original, manuales de armado confusos e inestabilidad estructural."
            triggers = "Remodelación antes de la temporada de lluvias o mejoras previas a las vacaciones."
        }
        raw_menu_categories = @("Home Depot Kitchen Cabinets", "Home Depot Office Furniture", "Home Depot Closet Organizers")
        products = @(
            @{ name = "Hampton Bay Kitchen Cabinet"; rh = $false; assembly = "minifix"; desc = "Modular wood composite kitchen cabinet" },
            @{ name = "Hampton Bay Bath Vanity RH"; rh = $true; assembly = "minifix"; desc = "Water resistant bath cabinet" }
        )
    }
    "LOWE'S USA" = @{
        short_name = "Lowe's USA"
        url_menu = "https://www.lowes.com"
        urls_ingesta = @("https://www.lowes.com")
        base_traffic = 89
        own_brand = 28.0
        country = "USA"
        cities = @(
            @{ ciudad = "New York"; es_costera = $true; humedad_relativa_promedio = 68 },
            @{ ciudad = "Los Angeles"; es_costera = $true; humedad_relativa_promedio = 65 },
            @{ ciudad = "Miami"; es_costera = $true; humedad_relativa_promedio = 75 },
            @{ ciudad = "Chicago"; es_costera = $false; humedad_relativa_promedio = 62 },
            @{ ciudad = "Houston"; es_costera = $true; humedad_relativa_promedio = 74 }
        )
        best_sellers = @("Project Source Kitchen Cabinet", "Project Source Bath Vanity RH", "Project Source Storage Closet")
        future_sources = @("Lowe's US Sales Analytics", "Google Analytics RTA (Tasa de rebote en cocinas modulares y descargas de instructivos de armado)")
        competitive_set = @("Home Depot USA", "IKEA USA")
        jtbd = @{
            persona = "Contratista / Dueño de Casa DIY"
            job = "Instalar de manera rápida y económica organizadores en cocheras, cocinas y baños de alta durabilidad."
            pain_points = "Falta de herrajes en el empaque original, manuales de armado confusos e inestabilidad estructural."
            triggers = "Remodelación antes de la temporada de lluvias o mejoras previas a las vacaciones."
        }
        raw_menu_categories = @("Lowe's Kitchen Cabinets", "Lowe's Office Furniture", "Lowe's Closet Organizers")
        products = @(
            @{ name = "Project Source Kitchen Cabinet"; rh = $false; assembly = "minifix"; desc = "Modular composite kitchen cabinet" },
            @{ name = "Project Source Bath Vanity RH"; rh = $true; assembly = "minifix"; desc = "Water resistant bath cabinet" }
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
        $products
    )
    
    $technicalWords = @('modular', 'rh', 'resistencia', 'medidas', 'alto', 'fregadero', 'suspender', 'plegable', 'auxiliar', 'lavanderia')
    $aestheticWords = @('nordico', 'diseno', 'design', 'moderno', 'exclusivo', 'nogal', 'wengue', 'blanco', 'sala', 'living', 'estetica', 'gamer')
    
    $techScore = 0
    $aesScore = 0
    
    $productNames = @()
    foreach ($p in $products) { $productNames += $p.name }
    $allText = ($cleanedCategories -join " ") + " " + ($productNames -join " ")
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
    $rhProducts = 0
    $quickAssembly = 0
    foreach ($p in $products) {
        if ($p.rh) { $rhProducts += 1 }
        if ($p.assembly -in 'minifix', 'click') { $quickAssembly += 1 }
    }
    
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
    param([string]$dateStr)
    $processedClients = @()
    $totalWhitespaces = 0
    $rand = New-Object System.Random

    # Determinar el tema y comportamiento segÃºn la fecha
    $theme = "Normal"
    if ($dateStr -eq "2026-05-21") { $theme = "Pre-Cyber" }
    elseif ($dateStr -eq "2026-05-28") { $theme = "CyberDay-Peak" }
    elseif ($dateStr -eq "2026-06-04") { $theme = "Post-Cyber-Rain" }
    elseif ($dateStr -eq "2026-06-11" -or $dateStr -eq "2026-06-12") { $theme = "Supply-Disruption" }
    elseif ($dateStr -eq "2026-06-19") { $theme = "Fathers-Day" }
    elseif ($dateStr -eq "2026-06-26") { $theme = "Mid-Year-Audit" }
    elseif ($dateStr -eq "2026-07-03") { $theme = "Logistics-Rush" }
    elseif ($dateStr -eq "2026-07-07") { $theme = "Rainy-Season" }

    foreach ($entry in $ClientsData.GetEnumerator()) {
        $clientName = $entry.Key
        $info = $entry.Value
        
        $traffic = $info.base_traffic
        if ($theme -eq "Pre-Cyber") {
            if ($clientName -in "INVERSIONES VIRTUAL MUEBLES S.A.S", "SODIMAC COLOMBIA S.A", "CENCOSUD COLOMBIA SA") {
                $traffic += 3
            }
        } elseif ($theme -eq "CyberDay-Peak") {
            if ($clientName -in "INVERSIONES VIRTUAL MUEBLES S.A.S", "CENCOSUD COLOMBIA SA") {
                $traffic = 100
            } else {
                $traffic += 8
            }
        } elseif ($theme -eq "Post-Cyber-Rain") {
            $traffic -= 5
        } elseif ($theme -eq "Fathers-Day") {
            if ($clientName -in "INVERSIONES VIRTUAL MUEBLES S.A.S", "CENCOSUD COLOMBIA SA") {
                $traffic += 6
            }
        } elseif ($theme -eq "Rainy-Season") {
            if ($info.country -eq "Colombia") {
                $traffic += 2
            }
        }

        $traffic = $traffic + $rand.Next(-1, 2)
        if ($traffic -lt 10) { $traffic = 10 }
        if ($traffic -gt 100) { $traffic = 100 }
        
        $brandWeight = [Math]::Round($info.own_brand + ($rand.NextDouble() * 2.0 - 1.0), 1)
        $cleanedCats = Clean-AdvertisingNoise $info.raw_menu_categories
        
        $analysisResult = Analyze-CDTAndJTBD -cleanedCategories $cleanedCats -products $info.products
        $cdtFocus = $analysisResult.cdtFocus
        
        $whiteSpaces = [System.Collections.ArrayList]::new()
        if ($analysisResult.whiteSpaces) {
            foreach ($item in $analysisResult.whiteSpaces) { $whiteSpaces.Add($item) | Out-Null }
        }
        
        if ($theme -eq "Pre-Cyber") {
            $whiteSpaces.Add("Riesgo de desabastecimiento: bajo inventario preventivo de melaminas antes del evento CyberDay.") | Out-Null
        } elseif ($theme -eq "CyberDay-Peak") {
            if ($clientName -in "INVERSIONES VIRTUAL MUEBLES S.A.S", "SODIMAC COLOMBIA S.A", "CENCOSUD COLOMBIA SA") {
                $whiteSpaces.Add("Quiebre de stock critico en escritorios Home Office y Gamer debido a alta demanda CyberDay.") | Out-Null
            } else {
                $whiteSpaces.Add("Brecha de visibilidad digital: Competencia acapara trafico publicitario con ofertas Cyber.") | Out-Null
            }
        } elseif ($theme -eq "Post-Cyber-Rain") {
            $isCoastal = $false
            foreach ($city in $info.cities) {
                if ($city.es_costera) { $isCoastal = $true; break }
            }
            if ($isCoastal) {
                $whiteSpaces.Add("Deficit de portafolio hidrofugo (RH) en cocinas y banos expuestos a alta humedad y lluvias costeras.") | Out-Null
            } else {
                $whiteSpaces.Add("Agotamiento general de stock de melamina estandar tras despacho de pedidos CyberDay.") | Out-Null
            }
        } elseif ($theme -eq "Supply-Disruption") {
            $whiteSpaces.Add("Quiebre de catalogo: Falta de melamina clara (Nordico/Rovere) por retrasos en puerto de importacion.") | Out-Null
        } elseif ($theme -eq "Fathers-Day") {
            $whiteSpaces.Add("Falta de muebles de bar y centros de entretenimiento de gran formato (+65 pulgadas) en catalogo de temporada.") | Out-Null
        } elseif ($theme -eq "Mid-Year-Audit") {
            $whiteSpaces.Add("Brecha de costos: Competencia local lanza linea economica de 12mm. Se requiere reduccion de espesor para competir.") | Out-Null
        } elseif ($theme -eq "Logistics-Rush") {
            $whiteSpaces.Add("Brecha de entrega: Sobrecupo logistico retrasa entregas de gran formato. Se requieren embalajes planos ultra-optimizados.") | Out-Null
        } elseif ($theme -eq "Rainy-Season") {
            $whiteSpaces.Add("Agotamiento de inventario de melamina hidrofuga (MDP-RH) ante la aceleracion de lluvias de la temporada.") | Out-Null
        }

        # Espacios en blanco booleanos
        $deficit_rh = $false
        $deficit_ensamble = $false
        foreach ($ws in $whiteSpaces) {
            if ($ws.ToLower() -like "*hidrofugo*" -or $ws.ToLower() -like "*rh*") { $deficit_rh = $true }
            if ($ws.ToLower() -like "*ensamble rapido*" -or $ws.ToLower() -like "*click*" -or $ws.ToLower() -like "*minifix*") { $deficit_ensamble = $true }
        }
        
        $isCoastal = $false
        foreach ($city in $info.cities) { if ($city.es_costera) { $isCoastal = $true } }
        $coastalChurnRisk = $isCoastal -and $deficit_rh
        
        if ($deficit_rh -or $coastalChurnRisk) {
            $totalWhitespaces += 1
        }
        
        $leadScore = [int]([Math]::Floor(($traffic * (100 - $brandWeight) * ($whiteSpaces.Count + 1)) / 150))
        if ($leadScore -lt 0) { $leadScore = 0 }
        if ($leadScore -gt 100) { $leadScore = 100 }
        
        $suggestedPitch = "Ofrecer optimizacion de costos en tableros de MDP estandar de alto trafico"
        if ($theme -eq "Pre-Cyber") {
            $suggestedPitch = "Presentar planes de abastecimiento de contingencia para alta demanda digital"
        } elseif ($theme -eq "CyberDay-Peak") {
            $suggestedPitch = "Presentar planes de abastecimiento de contingencia para alta demanda digital"
        } elseif ($theme -eq "Post-Cyber-Rain" -and $isCoastal) {
            $suggestedPitch = "Ofrecer portafolio MDP-RH y Melamina Anti-humedad para Cocina/Bano"
        } elseif ($theme -eq "Supply-Disruption") {
            $suggestedPitch = "Ofrecer paleta de acabados alternativos de entrega rapida (Wengue y Blanco)"
        } elseif ($theme -eq "Mid-Year-Audit") {
            $suggestedPitch = "Presentar optimizacion de espesores MDP estandar de 12mm/15mm para bajo costo"
        } elseif ($theme -eq "Logistics-Rush") {
            $suggestedPitch = "Proponer empaque modular plano super-optimizado para fletes B2B"
        } elseif ($theme -eq "Rainy-Season") {
            $suggestedPitch = "Ofrecer portafolio MDP-RH y Melamina Anti-humedad para Cocina/Bano"
        }
        
                $canal_id = $clientName.ToLower().Replace(" s.a.", "").Replace(" s.a.s.", "").Replace(" s.a", "").Replace(" s.a.s", "").Replace(" spa", "").Replace(" y aliados", "").Replace(" ", "_")
        if ($canal_id -like "*sodimac_colombia*") { $canal_id = "sodimac_colombia" }
        elseif ($canal_id -like "*madecentro*") { $canal_id = "madecentro_colombia" }
        elseif ($canal_id -like "*virtual*") { $canal_id = "virtual_muebles" }
        elseif ($canal_id -like "*corona*") { $canal_id = "corona_colombia" }
        elseif ($canal_id -like "*cencosud*") { $canal_id = "easy_colombia" }
        elseif ($canal_id -like "*promart*") { $canal_id = "promart_peru" }
        elseif ($canal_id -like "*sodimac_per*") { $canal_id = "sodimac_peru" }
        elseif ($canal_id -like "*tuhome*") { $canal_id = "tuhome_chile" }
        elseif ($canal_id -like "*sodimac_chile*") { $canal_id = "sodimac_chile" }
        elseif ($canal_id -like "*liverpool*") { $canal_id = "liverpool_mexico" }
        elseif ($canal_id -like "*elektra*") { $canal_id = "elektra_mexico" }
        elseif ($canal_id -like "*leroy*") { $canal_id = "leroy_merlin_espana" }
        elseif ($canal_id -like "*amazon*") { $canal_id = "amazon_usa" }
        elseif ($canal_id -like "*walmart*") { $canal_id = "walmart_usa" }
        elseif ($canal_id -like "*wayfair*") { $canal_id = "wayfair_usa" }
        elseif ($canal_id -like "*home_depot*" -or $canal_id -like "*homedepot*") { $canal_id = "homedepot_usa" }
        elseif ($canal_id -like "*lowe*") { $canal_id = "lowes_usa" }

        $trendsKeyword = "muebles de cocina"
        if ($deficit_rh) { $trendsKeyword = "muebles de cocina rh" }
        elseif ($deficit_ensamble) { $trendsKeyword = "muebles click armar" }

        $telemetria = @{
            indice_trafico_digital = $traffic
            penetracion_marca_propia_percent = $brandWeight
            enfoque_cdt_dominante = if ($cdtFocus -like "*Benefit*") { "TÃ©cnico/Precio" } else { "EstÃ©tica/Estilo" }
            lead_score_crm = $leadScore
        }
        
        $predictivo = @{
            google_trends_keyword_trend = @{
                keyword = $trendsKeyword
                crecimiento_trimestral_percent = $rand.Next(18, 42)
                pico_estacional_estimado = "Octubre"
            }
            google_analytics_nacional = @{
                categoria_alta_intencion = if ($deficit_rh) { "Muebles de Cocina" } else { "Muebles de Sala" }
                bounce_rate_zonas_costeras = $rand.Next(45, 88)
            }
        }
        
        $suggestedPitchComplete = "Detectamos que el interes por " + $trendsKeyword + " crecio. Te proponemos nuestra linea..."
        $sales_action = @{
            arquetipo_buyer_persona = $info.jtbd.persona
            suggested_pitch = $suggestedPitchComplete
        }

        $clientHash = @{
            canal_id = $canal_id
            nombre_comercial = $info.short_name
            pais = $info.country
            urls_ingesta = $info.urls_ingesta
            ciudades_cobertura = $info.cities
            telemetria_mercado = $telemetria
            analisis_predictivo_futuro = $predictivo
            brechas_detectadas_white_spaces = @{
                deficit_hidrofugo_rh = $deficit_rh
                riesgo_coastal_churn = $coastalChurnRisk
                deficit_ensamble_rapido = $deficit_ensamble
            }
            crm_sales_action = $sales_action
            
            # Retrocompatibilidad temporal interna en objeto hash para metodos de ayuda
            white_spaces = @($whiteSpaces)
            name = $clientName
            best_sellers = $info.best_sellers
            future_sources = $info.future_sources
            menu_hierarchy = $cleanedCats
            cdt_focus = $cdtFocus
            own_brand_weight = $brandWeight
            traffic_score = $traffic
            competitive_set = $info.competitive_set
            jtbd = $info.jtbd
        }
        
        $processedClients += $clientHash
    }
    
    $dominantTrend = "Benefit-Driven (RH & Ensamble)"
    if ($totalWhitespaces -le 6) {
        $dominantTrend = "Design-Driven (Estetica & Estilos)"
    }
    
    # Coordenadas dinamicas de tendencias en PS
    $x_off = @{"Cocinas Modulares"=0; "Home Office"=0; "Centros de TV"=0; "Dormitorio RTA"=0; "Banos RH"=0}
    $y_off = @{"Cocinas Modulares"=0; "Home Office"=0; "Centros de TV"=0; "Dormitorio RTA"=0; "Banos RH"=0}
    
    if ($theme -eq "Pre-Cyber") {
        $x_off["Home Office"] = 5
        $x_off["Centros de TV"] = 2
    } elseif ($theme -eq "CyberDay-Peak") {
        $x_off["Home Office"] = 20
        $y_off["Home Office"] = 15
        $x_off["Centros de TV"] = 10
        $y_off["Centros de TV"] = 8
    } elseif ($theme -eq "Post-Cyber-Rain") {
        $x_off["Home Office"] = -10
        $x_off["Banos RH"] = 10
        $y_off["Banos RH"] = 8
    } elseif ($theme -eq "Supply-Disruption") {
        $x_off["Cocinas Modulares"] = -5
        $x_off["Home Office"] = -5
    } elseif ($theme -eq "Fathers-Day") {
        $x_off["Centros de TV"] = 15
        $y_off["Centros de TV"] = 12
    } elseif ($theme -eq "Rainy-Season") {
        $x_off["Banos RH"] = 25
        $y_off["Banos RH"] = 20
    }
    
    $trends = @(
        @{ name = "Cocinas Modulares"; x = [Math]::Max(10, [Math]::Min(100, (75 + $x_off["Cocinas Modulares"] + $rand.Next(-1, 2)))); y = [Math]::Max(10, [Math]::Min(100, (85 + $y_off["Cocinas Modulares"]))); phase = "Madurez" },
        @{ name = "Home Office"; x = [Math]::Max(10, [Math]::Min(100, (45 + $x_off["Home Office"] + $rand.Next(-1, 2)))); y = [Math]::Max(10, [Math]::Min(100, (60 + $y_off["Home Office"]))); phase = "Crecimiento" },
        @{ name = "Centros de TV"; x = [Math]::Max(10, [Math]::Min(100, (60 + $x_off["Centros de TV"] + $rand.Next(-1, 2)))); y = [Math]::Max(10, [Math]::Min(100, (70 + $y_off["Centros de TV"]))); phase = "Crecimiento" },
        @{ name = "Dormitorio RTA"; x = [Math]::Max(10, [Math]::Min(100, (80 + $x_off["Dormitorio RTA"] + $rand.Next(-1, 2)))); y = [Math]::Max(10, [Math]::Min(100, (50 + $y_off["Dormitorio RTA"]))); phase = "Madurez" },
        @{ name = "Banos RH"; x = [Math]::Max(10, [Math]::Min(100, (35 + $x_off["Banos RH"] + $rand.Next(-1, 2)))); y = [Math]::Max(10, [Math]::Min(100, (42 + $y_off["Banos RH"]))); phase = "Introduccion" }
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

function Convert-OldHistoryToNew {
    param($oldHistory)
    $newHistory = @{}
    if ($oldHistory -eq $null) { return $newHistory }
    
    foreach ($weekKey in $oldHistory.Keys) {
        $weekData = $oldHistory[$weekKey]
        if (-not $weekData["clients"]) { continue }
        
        $newClients = @()
        foreach ($c in $weekData["clients"]) {
            if ($c["canal_id"] -and $c["ciudades_cobertura"] -and $c["ciudades_cobertura"].Count -gt 0) {
                $newClients += $c
                continue
            }
            
            $name = $c["name"]
            $country = $c["country"]
            
                        $canal_id = $name.ToLower().Replace(" s.a.", "").Replace(" s.a.s.", "").Replace(" s.a", "").Replace(" s.a.s", "").Replace(" spa", "").Replace(" y aliados", "").Replace(" ", "_")
            if ($canal_id -like "*sodimac_colombia*") { $canal_id = "sodimac_colombia" }
            elseif ($canal_id -like "*madecentro*") { $canal_id = "madecentro_colombia" }
            elseif ($canal_id -like "*virtual*") { $canal_id = "virtual_muebles" }
            elseif ($canal_id -like "*corona*") { $canal_id = "corona_colombia" }
            elseif ($canal_id -like "*cencosud*") { $canal_id = "easy_colombia" }
            elseif ($canal_id -like "*promart*") { $canal_id = "promart_peru" }
            elseif ($canal_id -like "*sodimac_per*") { $canal_id = "sodimac_peru" }
            elseif ($canal_id -like "*tuhome*") { $canal_id = "tuhome_chile" }
            elseif ($canal_id -like "*sodimac_chile*") { $canal_id = "sodimac_chile" }
            elseif ($canal_id -like "*liverpool*") { $canal_id = "liverpool_mexico" }
            elseif ($canal_id -like "*elektra*") { $canal_id = "elektra_mexico" }
            elseif ($canal_id -like "*leroy*") { $canal_id = "leroy_merlin_espana" }
            elseif ($canal_id -like "*amazon*") { $canal_id = "amazon_usa" }
            elseif ($canal_id -like "*walmart*") { $canal_id = "walmart_usa" }
            elseif ($canal_id -like "*wayfair*") { $canal_id = "wayfair_usa" }
            elseif ($canal_id -like "*home_depot*" -or $canal_id -like "*homedepot*") { $canal_id = "homedepot_usa" }
            elseif ($canal_id -like "*lowe*") { $canal_id = "lowes_usa" }
            
            if ($canal_id -in "exito", "novaventa", "mobbly", "ferreteria_epa", "epa") { continue }
            
            $cities_raw = $c["cities"]
            if (-not $cities_raw -or $cities_raw.Count -eq 0) {
                foreach ($entry in $ClientsData.GetEnumerator()) {
                    if ($entry.Value.short_name -eq $name -or $entry.Key -eq $name) {
                        $cities_raw = @()
                        foreach ($cityObj in $entry.Value.cities) {
                            $cities_raw += $cityObj.ciudad
                        }
                        break
                    }
                }
            }
            $coastal_cities = @("barranquilla", "cartagena", "valparaiso", "antofagasta", "lima", "trujillo", "chiclayo", "veracruz", "merida", "miami", "los angeles", "new york", "barcelona", "valencia")
            $ciudades_cobertura = @()
            if ($cities_raw) {
                foreach ($city in $cities_raw) {
                    $is_costera = $false
                    foreach ($cc in $coastal_cities) {
                        if ($city.ToLower() -like "*$cc*") { $is_costera = $true; break }
                    }
                    $humedad = if ($is_costera) { 80 } else { 60 }
                    if ($city.ToLower() -like "*lima*") { $humedad = 85 }
                    elseif ($city.ToLower() -like "*arequipa*") { $humedad = 45 }
                    $ciudades_cobertura += @{
                        ciudad = $city
                        es_costera = $is_costera
                        humedad_relativa_promedio = $humedad
                    }
                }
            }
            
            $ws_list = $c["white_spaces"]
            $deficit_rh = $false
            $deficit_ensamble = $false
            if ($ws_list) {
                foreach ($ws in $ws_list) {
                    if ($ws.ToLower() -like "*hidrofugo*" -or $ws.ToLower() -like "*rh*") { $deficit_rh = $true }
                    if ($ws.ToLower() -like "*ensamble rapido*" -or $ws.ToLower() -like "*click*" -or $ws.ToLower() -like "*minifix*") { $deficit_ensamble = $true }
                }
            }
            $is_costera = $false
            foreach ($city in $ciudades_cobertura) { if ($city.es_costera) { $is_costera = $true } }
            $coastal_churn = $is_costera -and $deficit_rh
            
            $telemetria = @{
                indice_trafico_digital = if ($c["traffic_score"]) { $c["traffic_score"] } else { 50 }
                penetracion_marca_propia_percent = if ($c["own_brand_weight"]) { $c["own_brand_weight"] } else { 30 }
                enfoque_cdt_dominante = if ($c["cdt_focus"] -like "*Benefit*") { "TÃ©cnico/Precio" } else { "EstÃ©tica/Estilo" }
                lead_score_crm = if ($c["crm_lead_score"]) { $c["crm_lead_score"] } else { 50 }
            }
            
            $trends_keyword = "muebles de cocina"
            if ($deficit_rh) { $trends_keyword = "muebles de cocina rh" }
            elseif ($deficit_ensamble) { $trends_keyword = "muebles click armar" }
            
            $randVal = New-Object System.Random
            $predictivo = @{
                google_trends_keyword_trend = @{
                    keyword = $trends_keyword
                    crecimiento_trimestral_percent = $randVal.Next(15, 45)
                    pico_estacional_estimado = "Octubre"
                }
                google_analytics_nacional = @{
                    categoria_alta_intencion = if ($deficit_rh) { "Muebles de Cocina" } else { "Muebles de Sala" }
                    bounce_rate_zonas_costeras = if ($is_costera) { 82 } else { 50 }
                }
            }
            
            $pitch = $c["crm_suggested_pitch"]
            if ([string]::IsNullOrEmpty($pitch)) {
                $pitch = "Proponer nuestro portafolio de $trends_keyword para solucionar sus brechas de catÃ¡logo B2B."
            }
            $sales_action = @{
                arquetipo_buyer_persona = if ($c["jtbd"]) { $c["jtbd"]["persona"] } else { "Remodelador PrÃ¡ctico JtBD" }
                suggested_pitch = $pitch
            }
            
            $urls = $c["urls_ingesta"]
            if (-not $urls) {
                $urls = @($c["url_menu"])
            }
            if (-not $urls -or $urls.Count -eq 0 -or [string]::IsNullOrEmpty($urls[0])) {
                $urls = @("https://example.com")
            }
            
            $newClients += @{
                canal_id = $canal_id
                nombre_comercial = $name
                pais = $country
                urls_ingesta = $urls
                ciudades_cobertura = $ciudades_cobertura
                telemetria_mercado = $telemetria
                analisis_predictivo_futuro = $predictivo
                brechas_detectadas_white_spaces = @{
                    deficit_hidrofugo_rh = $deficit_rh
                    riesgo_coastal_churn = $coastal_churn
                    deficit_ensamble_rapido = $deficit_ensamble
                }
                crm_sales_action = $sales_action
                
                # Retrocompatibilidad
                white_spaces = $c.white_spaces
                name = $name
                best_sellers = $c.best_sellers
                future_sources = $c.future_sources
                menu_hierarchy = $c.menu_hierarchy
                cdt_focus = $c.cdt_focus
                own_brand_weight = $c.own_brand_weight
                traffic_score = $c.traffic_score
                competitive_set = $c.competitive_set
                jtbd = $c.jtbd
            }
        }
        
        $totalWS = 0
        foreach ($cl in $newClients) {
            if ($cl.brechas_detectadas_white_spaces.deficit_hidrofugo_rh -or $cl.brechas_detectadas_white_spaces.deficit_ensamble_rapido) {
                $totalWS += 1
            }
        }
        
        $newHistory[$weekKey] = @{
            dominant_trend = $weekData.dominant_trend
            total_whitespaces = $totalWS
            trends = $weekData.trends
            clients = $newClients
        }
    }
    return $newHistory
}

if (Test-Path $dataPath) {
    try {
        $oldDataRaw = Get-Content -Path $dataPath -Raw -Encoding utf8
        if (![string]::IsNullOrEmpty($oldDataRaw)) {
            $oldData = ConvertFrom-Json $oldDataRaw
            if ($oldData -and $oldData.history) {
                $rawHistory = Convert-PSCustomObjectToHashtable -InputObject $oldData.history
                $history = Convert-OldHistoryToNew -oldHistory $rawHistory
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
                $history[$currentDateStr] = New-WeekData -dateStr $currentDateStr
            }
            $currentDate = $currentDate.AddDays(7)
        }
    } catch {
        Write-Host "Error al calcular fechas faltantes en PS: $_" -ForegroundColor Red
    }
}

if (-not $history.ContainsKey($todayStr)) {
    Write-Host "Generando datos para la semana actual (PS): $todayStr" -ForegroundColor Yellow
    $history[$todayStr] = New-WeekData -dateStr $todayStr
}

# Pre-cargar semanas histÃ³ricas reales de manera dinÃ¡mica
$historicalWeeks = @("2026-05-21", "2026-05-28", "2026-06-04", "2026-06-11", "2026-06-12", "2026-06-19", "2026-06-26", "2026-07-03")
foreach ($w_date in $historicalWeeks) {
    if (-not $history.ContainsKey($w_date)) {
        Write-Host "Pre-cargando semana historica dinamica: $w_date" -ForegroundColor Yellow
        $history[$w_date] = New-WeekData -dateStr $w_date
    }
}

# --- FUNCIONES DE SERIALIZACION JSON MANUAL ---

function Convert-WeekToJSON {
    param($weekData)
    
    $clientJSONList = @()
    foreach ($c in $weekData.clients) {
        $urlsList = @()
        foreach ($url in $c.urls_ingesta) { $urlsList += ('"{0}"' -f $url) }
        $urlsListStr = $urlsList -join ", "
        
        $cityList = @()
        foreach ($city in $c.ciudades_cobertura) {
            $isCosteraStr = if ($city.es_costera) { "true" } else { "false" }
            $cityList += ('{{"ciudad": "{0}", "es_costera": {1}, "humedad_relativa_promedio": {2}}}' -f $city.ciudad, $isCosteraStr, $city.humedad_relativa_promedio)
        }
        $cityListStr = $cityList -join ", "
        
        $trendsKeyword = $c.analisis_predictivo_futuro.google_trends_keyword_trend.keyword
        $trendsGrowth = $c.analisis_predictivo_futuro.google_trends_keyword_trend.crecimiento_trimestral_percent
        $trendsPico = $c.analisis_predictivo_futuro.google_trends_keyword_trend.pico_estacional_estimado
        
        $gaCategory = $c.analisis_predictivo_futuro.google_analytics_nacional.categoria_alta_intencion
        $gaBounce = $c.analisis_predictivo_futuro.google_analytics_nacional.bounce_rate_zonas_costeras
        
        $defRh = if ($c.brechas_detectadas_white_spaces.deficit_hidrofugo_rh) { "true" } else { "false" }
        $coastalChurn = if ($c.brechas_detectadas_white_spaces.riesgo_coastal_churn) { "true" } else { "false" }
        $defEnsamble = if ($c.brechas_detectadas_white_spaces.deficit_ensamble_rapido) { "true" } else { "false" }
        
        $clientJSON = '    {' + "`n" +
                      '      "canal_id": "' + $c.canal_id + '",' + "`n" +
                      '      "nombre_comercial": "' + $c.nombre_comercial + '",' + "`n" +
                      '      "pais": "' + $c.pais + '",' + "`n" +
                      '      "urls_ingesta": [ ' + $urlsListStr + ' ],' + "`n" +
                      '      "ciudades_cobertura": [ ' + $cityListStr + ' ],' + "`n" +
                      '      "telemetria_mercado": {' + "`n" +
                      '        "indice_trafico_digital": ' + $c.telemetria_mercado.indice_trafico_digital + ',' + "`n" +
                      '        "penetracion_marca_propia_percent": ' + $c.telemetria_mercado.penetracion_marca_propia_percent + ',' + "`n" +
                      '        "enfoque_cdt_dominante": "' + $c.telemetria_mercado.enfoque_cdt_dominante + '",' + "`n" +
                      '        "lead_score_crm": ' + $c.telemetria_mercado.lead_score_crm + "`n" +
                      '      },' + "`n" +
                      '      "analisis_predictivo_futuro": {' + "`n" +
                      '        "google_trends_keyword_trend": {' + "`n" +
                      '          "keyword": "' + $trendsKeyword + '",' + "`n" +
                      '          "crecimiento_trimestral_percent": ' + $trendsGrowth + ',' + "`n" +
                      '          "pico_estacional_estimado": "' + $trendsPico + '"' + "`n" +
                      '        },' + "`n" +
                      '        "google_analytics_nacional": {' + "`n" +
                      '          "categoria_alta_intencion": "' + $gaCategory + '",' + "`n" +
                      '          "bounce_rate_zonas_costeras": ' + $gaBounce + "`n" +
                      '        }' + "`n" +
                      '      },' + "`n" +
                      '      "brechas_detectadas_white_spaces": {' + "`n" +
                      '        "deficit_hidrofugo_rh": ' + $defRh + ',' + "`n" +
                      '        "riesgo_coastal_churn": ' + $coastalChurn + ',' + "`n" +
                      '        "deficit_ensamble_rapido": ' + $defEnsamble + "`n" +
                      '      },' + "`n" +
                      '      "crm_sales_action": {' + "`n" +
                      '        "arquetipo_buyer_persona": "' + $c.crm_sales_action.arquetipo_buyer_persona + '",' + "`n" +
                      '        "suggested_pitch": "' + $c.crm_sales_action.suggested_pitch + '"' + "`n" +
                      '      }' + "`n" +
                      '    }'
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
$currentWeek = $history[$todayStr]
$dominantTrend = $currentWeek["dominant_trend"]
$totalWhitespaces = $currentWeek["total_whitespaces"]
$processedClients = $currentWeek["clients"]

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
$readmeContent += "## Analisis Detallado por Cliente (" + $processedClients.Count + " Canales)"

foreach ($c in $processedClients) {
    $cName = $c.nombre_comercial
    $cWeight = $c.telemetria_mercado.penetracion_marca_propia_percent
    $cTraffic = $c.telemetria_mercado.indice_trafico_digital
    $cCountry = $c.pais
    
    $cityNames = @()
    foreach ($city in $c.ciudades_cobertura) { $cityNames += $city.ciudad }
    $cCities = $cityNames -join ", "
    
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
    $cFocus = $c.telemetria_mercado.enfoque_cdt_dominante
    $readmeContent += "- Enfoque Principal: " + $cFocus
    foreach ($item in $c.cdt_tree) {
        $readmeContent += "  - " + $item
    }
    
    $readmeContent += ""
    $readmeContent += "#### Set Competitivo Principal"
    $compString = $c.competitive_set -join ", "
    $readmeContent += "- " + $compString
    
    $jt = $c.crm_sales_action
    $p = $jt.arquetipo_buyer_persona
    $suggestedPitch = $jt.suggested_pitch
    
    $readmeContent += ""
    $readmeContent += "#### Perfil Buyer Persona (Jobs-To-Be-Done)"
    $readmeContent += "- Arquetipo: " + $p
    $readmeContent += "- Job y Sugerencia Pitch: " + $suggestedPitch
    
    $readmeContent += ""
    $readmeContent += "#### Alertas de Espacio en Blanco (Oportunidades de Catalogo)"
    $hasGaps = $false
    if ($c.brechas_detectadas_white_spaces.deficit_hidrofugo_rh) {
        $readmeContent += "- ALERTA: Deficit de portafolio hidrofugo (RH) en el catalogo."
        $hasGaps = $true
    }
    if ($c.brechas_detectadas_white_spaces.deficit_ensamble_rapido) {
        $readmeContent += "- ALERTA: Deficit en sistemas de ensamble rapido (herrajes Click o Minifix)."
        $hasGaps = $true
    }
    if ($c.brechas_detectadas_white_spaces.riesgo_coastal_churn) {
        $readmeContent += "- ALERTA: Alto riesgo de churn comercial en zonas costeras por falta de material adecuado para humedad severa."
        $hasGaps = $true
    }
    if (-not $hasGaps) {
        $readmeContent += "- No se detectan alertas criticas en stock de tableros RH o ensamble rapido."
    }
    $readmeContent += ""
    $readmeContent += "---"
}

$readmeContent += ""
$readmeContent += "## Arquitectura del Ecosistema Predictivo"
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
