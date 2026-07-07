#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AMELIA RTA: Analista de Investigación de Mercado Senior y Especialista en Arquitectura de Datos de Canales Digitales
Script de Actualización Automática Semanal para Tendencias de Mercado Muebles RTA
"""

import os
import re
import json
import random
from datetime import datetime

# --- CONFIGURACIÓN DE CLIENTES Y PARÁMETROS ---
CLIENTS_RAW_DATA = {
    "SODIMAC COLOMBIA S.A": {
        "short_name": "Sodimac",
        "url_menu": "https://www.sodimac.com.co/sodimac-co/categoria/muebles",
        "base_traffic": 92,
        "own_brand": 45.5,
        "country": "Colombia",
        "cities": ["Bogotá", "Medellín", "Cali", "Barranquilla"],
        "best_sellers": ["Módulo Fregadero MDP-RH 100cm", "Escritorio Home Office Smart 120cm", "Estanterías RTA Metálicas"],
        "future_sources": ["MercadoLibre Colombia (Tendencias de Búsqueda)", "Homecenter Chile (Benchmark de Clones de Diseño)", "Google Analytics RTA (Tasa de rebote en categoría de cocinas modulares y descargas de instructivos de armado)"],
        "competitive_set": ["Cencosud", "Almacenes Éxito", "Corona"],
        "jtbd": {
            "persona": "Remodelador Práctico",
            "job": "Optimizar el espacio de la cocina y zona de ropas de forma rápida y sin herramientas complejas.",
            "pain_points": "Aglomerados que se inflan con humedad, herrajes faltantes y manuales de ensamble confusos.",
            "triggers": "Renovación de arriendo o mudanza a departamento nuevo de interés social (VIS)."
        },
        "raw_menu_categories": [
            "Muebles de Cocina - Modulares",
            "Ofertas Imperdibles de Cocinas",
            "Escritorios Home Office de Descuento",
            "Muebles de TV y Centros de Entretenimiento",
            "Estanterías y Clósets RTA",
            "Descuentos de Cyber en Baños",
            "Muebles de Baño RH Resistentes a Humedad",
            "Combos Dormitorio con Ofertas Especiales"
        ],
        "products": [
            {"name": "Módulo Fregadero 100cm MDP Estándar", "rh": False, "assembly": "estandar", "desc": "Estructura aglomerada 15mm"},
            {"name": "Escritorio Home Office Smart 120cm", "rh": False, "assembly": "minifix", "desc": "Ensamble rápido con tornillos minifix"},
            {"name": "Módulo Alto de Cocina 60cm MDP-RH", "rh": True, "assembly": "estandar", "desc": "Madera resistente a humedad"},
            {"name": "Centro de TV Prime Nogal 55 pulgadas", "rh": False, "assembly": "estandar", "desc": "Acabado estético melamínico"}
        ]
    },
    "INVERSIONES VIRTUAL MUEBLES S.A.S": {
        "short_name": "Virtual Muebles",
        "url_menu": "https://www.virtualmuebles.com/muebles-rta",
        "base_traffic": 78,
        "own_brand": 90.0,
        "country": "Colombia",
        "cities": ["Medellín", "Bogotá", "Envigado"],
        "best_sellers": ["Centro de TV Nórdico Blanco-Roble", "Escritorio Gamer Pro", "Escritorio Plegable Work-Space"],
        "future_sources": ["Amazon Global (Tendencias de Diseño Industrial)", "Instagram Shopping (Engagement de Muebles RTA)", "Google Analytics RTA (Embudo de conversión de la línea Gamer y rebote en landings de escritorio flexible)"],
        "competitive_set": ["TuHome", "Mobbly", "Novaventa"],
        "jtbd": {
            "persona": "Comprador Digital Joven",
            "job": "Amoblar su primer apartamento con diseños atractivos que se puedan comprar 100% en línea y recibir rápido.",
            "pain_points": "Dificultad de envío, falta de soporte para piezas dañadas en transporte, desconfianza en fotos web.",
            "triggers": "Primer empleo profesional, independencia de casa de los padres."
        },
        "raw_menu_categories": [
            "Novedades y Lanzamientos Estéticos",
            "Salas y Centros de TV Design",
            "Blackfriday Muebles de Dormitorio",
            "Escritorios Flexibles Modernos",
            "Cocinas Modulares Low Cost",
            "Ofertas de Lanzamiento Muebles Baño",
            "Zapateros y Armarios Multifunción"
        ],
        "products": [
            {"name": "Centro de TV Nórdico Blanco-Roble", "rh": False, "assembly": "minifix", "desc": "Diseño estético escandinavo"},
            {"name": "Escritorio Plegable Work-Space", "rh": False, "assembly": "click", "desc": "Sistema de ensamble rápido click"},
            {"name": "Mesa de Noche Minimalista con Cajón", "rh": False, "assembly": "estandar", "desc": " MDP texturizado"},
            {"name": "Mueble Auxiliar Microondas MDP", "rh": False, "assembly": "estandar", "desc": "Mueble modular para electrodomésticos"}
        ]
    },
    "GRUPO CORONA Y ALIADOS": {
        "short_name": "Corona",
        "url_menu": "https://www.corona.co/muebles",
        "base_traffic": 85,
        "own_brand": 35.0,
        "country": "Colombia",
        "cities": ["Bogotá", "Medellín", "Barranquilla", "Cartagena"],
        "best_sellers": ["Gabinete de Baño suspendido 60cm RH", "Alacena Organizadora Multiusos RH", "Módulo Cocina con Mesón de Acero"],
        "future_sources": ["Sodimac Constructor Portal (Precios de Contratistas)", "Corona Retail Analytics (Ventas de Baños y Cocinas)", "Google Analytics RTA (Comportamiento de búsquedas de lavamanos hidrófugos y descargas de fichas de garantía)"],
        "competitive_set": ["Sodimac", "Cencosud", "Ferretería EPA"],
        "jtbd": {
            "persona": "Maestro Especialista / Instalador",
            "job": "Instalar gabinetes de alta durabilidad en zonas expuestas a humedad, garantizando calidad al cliente final.",
            "pain_points": "Falsas promesas de resistencia al agua, herrajes que se oxidan en baños y cocinas costeras.",
            "triggers": "Contratos de remodelación comercial o residencial en zonas húmedas."
        },
        "raw_menu_categories": [
            "Muebles de Baño Certificados RH",
            "Cyber Muebles Sanitarios",
            "Cocinas Modulares con Mesón",
            "Oferta Especial de Lavaplatos RTA",
            "Organizadores y Alacenas",
            "Garantía Corona en Muebles",
            "Muebles de Lavandería Funcionales"
        ],
        "products": [
            {"name": "Gabinete de Baño suspendido 60cm RH", "rh": True, "assembly": "estandar", "desc": "Tablero RH resistente al agua"},
            {"name": "Alacena Organizadora Multiusos RH", "rh": True, "assembly": "estandar", "desc": "Estructura hidrófuga"},
            {"name": "Módulo Cocina con Mesón de Acero", "rh": False, "assembly": "estandar", "desc": "Cocina básica MDP"},
            {"name": "Mesa de Centro Estética Corona", "rh": False, "assembly": "estandar", "desc": "Melamina texturizada"}
        ]
    },
    "TUHOME SPA": {
        "short_name": "TuHome",
        "url_menu": "https://www.tuhome.cl/productos",
        "base_traffic": 80,
        "own_brand": 95.0,
        "country": "Chile",
        "cities": ["Santiago", "Concepción", "Valparaíso", "Antofagasta"],
        "best_sellers": ["Escritorio Home Office Z-60 Nogal", "Mueble Lavamanos Split RH", "Clóset RTA 4 Puertas Wengue"],
        "future_sources": ["Falabella.com Chile (Surtido y Quiebres de Stock)", "MercadoLibre Chile (Palabras clave de Muebles)", "Google Analytics RTA (Porcentaje de abandono del checkout B2B y telemetría de visualización de módulos de clóset)"],
        "competitive_set": ["Virtual Muebles", "Mobbly", "Cencosud"],
        "jtbd": {
            "persona": "Hogares en Crecimiento",
            "job": "Adaptar el mobiliario del hogar según el crecimiento de los hijos con soluciones modulares y escalables.",
            "pain_points": "Muebles pesados difíciles de mover, poca variedad en tonos de madera real, ensamble que requiere 2 personas.",
            "triggers": "Llegada de un nuevo hijo o reorganización de dormitorios."
        },
        "raw_menu_categories": [
            "Colección Cocina y Despensa Modulares",
            "Descuentos Exclusivos Dormitorio",
            "Centros de Entretenimiento Modernos",
            "Línea Oficina y Escritorios RTA",
            "Muebles Auxiliares de Baño",
            "Cyber Ofertas Muebles de Jardín",
            "Novedades Diseño Industrial RTA"
        ],
        "products": [
            {"name": "Escritorio Home Office Z-60 Nogal", "rh": False, "assembly": "minifix", "desc": "Ensamble rápido con minifix"},
            {"name": "Módulo de Cocina Auxiliar 2 Puertas", "rh": False, "assembly": "estandar", "desc": "Tablero estándar MDP"},
            {"name": "Mueble Lavamanos Split RH", "rh": True, "assembly": "minifix", "desc": "Base hidrófuga con herrajes rápidos"},
            {"name": "Clóset RTA 4 Puertas Wengue", "rh": False, "assembly": "estandar", "desc": "Estructura aglomerada de gran capacidad"}
        ]
    },
    "FERRETERIA EPA": {
        "short_name": "EPA",
        "url_menu": "https://www.epa.com.ve/muebles-rta",
        "base_traffic": 70,
        "own_brand": 30.0,
        "country": "Venezuela",
        "cities": ["Caracas", "Valencia", "Maracaibo", "Barquisimeto"],
        "best_sellers": ["Gabinete Auxiliar de Planchado MDP", "Escritorio Estudiante Basic Gris", "Módulo Cocina Fregadero 120cm"],
        "future_sources": ["MercadoLibre Venezuela (Demanda de Muebles RTA de Bajo Costo)", "EPA Costa Rica/El Salvador (Benchmarking de Precios RTA)", "Google Analytics RTA (Tasa de conversión en el configurador de muebles modulares de cocina)"],
        "competitive_set": ["Sodimac", "Novey", "Cencosud"],
        "jtbd": {
            "persona": "Auto-constructor RTA",
            "job": "Hacer mejoras funcionales en el hogar los fines de semana de forma económica.",
            "pain_points": "Falta de herramientas de ensamble en casa, tornillería incompleta en el empaque original.",
            "triggers": "Proyecto DIY (Hágalo usted mismo) de fin de semana."
        },
        "raw_menu_categories": [
            "Muebles Modulares para Cocina",
            "Armarios y Alacenas en Promoción",
            "Escritorios RTA Prácticos",
            "Cyberlunes Muebles de Sala",
            "Línea de Organizadores Económicos",
            "Muebles de Baño Básicos"
        ],
        "products": [
            {"name": "Gabinete Auxiliar de Planchado MDP", "rh": False, "assembly": "estandar", "desc": "Tablero aglomerado estándar"},
            {"name": "Escritorio Estudiante Basic Gris", "rh": False, "assembly": "estandar", "desc": "Estructura metálica y MDP"},
            {"name": "Módulo Cocina Fregadero 120cm", "rh": False, "assembly": "estandar", "desc": "No resistente a humedad"},
            {"name": "Gabinete Aéreo Baño con Espejo", "rh": False, "assembly": "estandar", "desc": "MDP estándar"}
        ]
    },
    "MOBBLY S.A.S": {
        "short_name": "Mobbly",
        "url_menu": "https://www.mobbly.com.co/rta-trends",
        "base_traffic": 65,
        "own_brand": 80.0,
        "country": "Colombia",
        "cities": ["Bogotá", "Medellín", "Cali"],
        "best_sellers": ["Escritorio Gamer Pro con Luces LED", "Mesa de TV Flotante 140cm", "Biblioteca Modular 5 Niveles"],
        "future_sources": ["Pinterest Latam (Búsquedas de Muebles Juveniles)", "TikTok Shopping (Conversión RTA en Audiencia Joven)", "Google Analytics RTA (Engagement en páginas de producto con visualización interactiva de centros de TV)"],
        "competitive_set": ["Virtual Muebles", "TuHome", "Novaventa"],
        "jtbd": {
            "persona": "Estudiante o Joven Profesional",
            "job": "Montar un espacio de estudio o trabajo estético y ergonómico con un presupuesto muy ajustado.",
            "pain_points": "Escritorios inestables, acabados que se rayan con facilidad, falta de espacio para cables.",
            "triggers": "Inicio de semestre universitario o transición a trabajo remoto."
        },
        "raw_menu_categories": [
            "Escritorios Gamer y Home Office RTA",
            "Descuento en Línea Gamer Mobbly",
            "Estanterías Modulares Libres de Ruido",
            "Mesas de TV y Centros de Diseño",
            "Cyber Muebles Dormitorio Moderno"
        ],
        "products": [
            {"name": "Escritorio Gamer Pro con Luces LED", "rh": False, "assembly": "minifix", "desc": "Diseño ergonómico juvenil"},
            {"name": "Mesa de TV Flotante 140cm", "rh": False, "assembly": "minifix", "desc": "Sistema de anclaje de pared"},
            {"name": "Biblioteca Modular 5 Niveles", "rh": False, "assembly": "estandar", "desc": "Estructura MDP texturizado"},
            {"name": "Cómoda 4 Cajones Compacta", "rh": False, "assembly": "estandar", "desc": "Melamina color roble"}
        ]
    },
    "ALMACENES ÉXITO S.A.": {
        "short_name": "Éxito",
        "url_menu": "https://www.exito.com/muebles",
        "base_traffic": 94,
        "own_brand": 25.0,
        "country": "Colombia",
        "cities": ["Medellín", "Bogotá", "Cali", "Barranquilla"],
        "best_sellers": ["Clóset RTA 3 Puertas Finlandek", "Escritorio Compacto Office Finlandek", "Gabinete Cocina Auxiliar con Ruedas"],
        "future_sources": ["Grupo Éxito Marketplace (Conversión de Canje de Puntos)", "Carrefour Brasil (Modelos RTA de Alta Frecuencia)", "Google Analytics RTA (Tráfico derivado a la categoría de dormitorio infantil y tasa de descarga de planos RTA)"],
        "competitive_set": ["Cencosud", "Sodimac", "Novaventa"],
        "jtbd": {
            "persona": "Madre de Familia / Administradora del Hogar",
            "job": "Comprar muebles para organizar los cuartos de los niños aprovechando puntos de lealtad y promociones de supermercado.",
            "pain_points": "Dificultad para coordinar la entrega con el mercado semanal, calidad inconsistente en productos importados.",
            "triggers": "Ofertas de fin de mes o acumulación de puntos de fidelidad."
        },
        "raw_menu_categories": [
            "Muebles de Dormitorio y Clósets RTA",
            "Descuentos Blackfriday Muebles",
            "Escritorios Finlandia Finlandek",
            "Cyber Ofertas Cocinas Listas",
            "Centros de Entretenimiento en Promoción",
            "Muebles Auxiliares de Cocina y Baño"
        ],
        "products": [
            {"name": "Clóset RTA 3 Puertas Finlandek", "rh": False, "assembly": "estandar", "desc": "Madera aglomerada estándar"},
            {"name": "Escritorio Compacto Office Finlandek", "rh": False, "assembly": "estandar", "desc": "Diseño simple estudiantil"},
            {"name": "Gabinete Cocina Auxiliar con Ruedas", "rh": False, "assembly": "estandar", "desc": "MDP melamínico"},
            {"name": "Mesa Auxiliar Multiusos 1 Cajón", "rh": False, "assembly": "estandar", "desc": "Finlandek RTA"}
        ]
    },
    "NOVAVENTA S.A.S": {
        "short_name": "Novaventa",
        "url_menu": "https://www.novaventa.com.co/muebles-catalogo",
        "base_traffic": 75,
        "own_brand": 15.0,
        "country": "Colombia",
        "cities": ["Medellín", "Bogotá", "Bucaramanga", "Cali"],
        "best_sellers": ["Mueble Zapatero RTA 12 Pares", "Escritorio Plegable Práctico", "Organizador Microondas con Canastillas"],
        "future_sources": ["Novaventa App (Encuestas Directas a Mamás Empresarias)", "Leonisa/Catálogo Hogar (Análisis de Surtido Competidor)", "Google Analytics RTA (Interacciones en catálogo interactivo y clics de pedido rápido de zapateros)"],
        "competitive_set": ["Almacenes Éxito", "Virtual Muebles", "Mobbly"],
        "jtbd": {
            "persona": "Mamá Empresaria / Vendedora por Catálogo",
            "job": "Ofrecer a sus vecinos de confianza muebles RTA prácticos y de bajo costo que paguen a plazos cómodos.",
            "pain_points": "Complicación en el ensamble post-venta, cajas muy pesadas para transportar, cobros difíciles si el mueble falla.",
            "triggers": "Oportunidades de catálogo mensual para aumentar ingresos extras."
        },
        "raw_menu_categories": [
            "Muebles Prácticos del Catálogo Novaventa",
            "Oferta Especial de Clósets RTA",
            "Escritorios Juveniles en Descuento",
            "Organizadores de Cocina Prácticos",
            "Cyber Muebles Auxiliares de Hogar"
        ],
        "products": [
            {"name": "Mueble Zapatero RTA 12 Pares", "rh": False, "assembly": "minifix", "desc": "Fácil ensamble por catálogo"},
            {"name": "Escritorio Plegable Práctico", "rh": False, "assembly": "click", "desc": "Sistema autoensamble sin herramientas"},
            {"name": "Organizador Microondas con Canastillas", "rh": False, "assembly": "estandar", "desc": "Estructura metálica y MDP"},
            {"name": "Estantería Multiusos 4 repisas", "rh": False, "assembly": "estandar", "desc": "Ligero y fácil de ubicar"}
        ]
    },
    "CENCOSUD COLOMBIA SA": {
        "short_name": "Cencosud",
        "url_menu": "https://www.jumbo.co/muebles-rta",
        "base_traffic": 88,
        "own_brand": 30.0,
        "country": "Colombia",
        "cities": ["Bogotá", "Medellín", "Cali", "Barranquilla"],
        "best_sellers": ["Centro de TV Florencia Wengue", "Escritorio L-Shape Industrial Easy", "Módulo Cocina Aéreo Easy 100cm"],
        "future_sources": ["Easy Argentina/Chile (Surtido de Muebles RTA Krea)", "MercadoLibre Colombia (Precios de Centros de TV)", "Google Analytics RTA (Búsqueda interna de centros de TV y tasa de abandono en carritos de muebles de sala)"],
        "competitive_set": ["Sodimac", "Almacenes Éxito", "Corona"],
        "jtbd": {
            "persona": "Comprador de Hogar de Clase Media",
            "job": "Encontrar un mueble de sala o estudio de buena apariencia que encaje exactamente en la sala de su apartamento sin gastar una fortuna.",
            "pain_points": "Falta de información clara sobre dimensiones en la web, retrasos en el despacho a domicilio.",
            "triggers": "Remodelación de la sala para recibir visitas de fin de año."
        },
        "raw_menu_categories": [
            "Centros de TV y Entretenimiento Easy",
            "Ofertas de Cyber en Muebles Easy",
            "Clósets y Cómodas RTA en Descuento",
            "Escritorios y Sillas de Oficina",
            "Muebles de Cocina y Comedor RTA",
            "Blackfriday Armarios Modulares"
        ],
        "products": [
            {"name": "Centro de TV Florencia Wengue", "rh": False, "assembly": "estandar", "desc": "Estilo moderno melamínico"},
            {"name": "Escritorio L-Shape Industrial Easy", "rh": False, "assembly": "estandar", "desc": "Estructura metálica y MDP"},
            {"name": "Módulo Cocina Aéreo Easy 100cm", "rh": False, "assembly": "estandar", "desc": "MDP estándar"},
            {"name": "Mesa de Noche Krea 2 cajones", "rh": False, "assembly": "estandar", "desc": "Aglomerado básico"}
        ]
    },
    "CORPORACIÓN FAVORITA C.A.": {
        "short_name": "Favorita",
        "url_menu": "https://www.sukasa.com/muebles-rta",
        "base_traffic": 82,
        "own_brand": 20.0,
        "country": "Ecuador",
        "cities": ["Quito", "Guayaquil", "Cuenca", "Manta"],
        "best_sellers": ["Aparador Buffet Nórdico 150cm", "Centro de Entretenimiento Rovere", "Mueble de Baño Suspendido Zen RH"],
        "future_sources": ["Sukasa Online (Tendencias de Muebles de Alta Gama)", "MercadoLibre Ecuador (Precios de Muebles RTA de Comedor)", "Google Analytics RTA (Telemetría de la línea premium y clics en el botón de contacto para proyectos de sala)"],
        "competitive_set": ["Novey", "TuHome", "Sodimac"],
        "jtbd": {
            "persona": "Hogar Moderno Ecuatoriano",
            "job": "Modernizar el comedor y la sala de estar con acabados elegantes y duraderos sin recurrir a carpinteros tradicionales.",
            "pain_points": "Poca oferta de diseños modernos en mercados locales, altos costos de importación de muebles listos.",
            "triggers": "Fiestas locales o mudanza de fin de año."
        },
        "raw_menu_categories": [
            "Muebles RTA de Diseño Exclusivo Sukasa",
            "Descuentos de Cyber en Comedores",
            "Aparadores y Centros de TV Modernos",
            "Escritorios Ejecutivos de Descuento",
            "Muebles Organizadores de Lujo"
        ],
        "products": [
            {"name": "Aparador Buffet Nórdico 150cm", "rh": False, "assembly": "minifix", "desc": "Gran acabado estético melamínico"},
            {"name": "Centro de Entretenimiento Rovere", "rh": False, "assembly": "estandar", "desc": "Estructura robusta 18mm"},
            {"name": "Mueble de Baño Suspendido Zen RH", "rh": True, "assembly": "minifix", "desc": "Módulo de baño en melamina RH"},
            {"name": "Escritorio Ejecutivo Glass & Wood", "rh": False, "assembly": "estandar", "desc": "Combinación vidrio y MDP"}
        ]
    },
    "GEO F. NOVEY S.A.": {
        "short_name": "Novey",
        "url_menu": "https://www.novey.com.pa/muebles",
        "base_traffic": 74,
        "own_brand": 35.0,
        "country": "Panamá",
        "cities": ["Ciudad de Panamá", "David", "Chitré", "Colón"],
        "best_sellers": ["Módulo Fregadero RH Novey 120cm", "Gabinete Espejo de Baño RH", "Escritorio Home Office Basic Rovere"],
        "future_sources": ["Novey.com.pa (Analytics de Búsqueda de Productos Hidrófugos)", "Amazon EE.UU. (Importación de Accesorios RTA a Panamá)", "Google Analytics RTA (Tráfico en fichas técnicas de gabinetes de baño RH y descargas de guías de resistencia)"],
        "competitive_set": ["Favorita", "Sodimac", "Ferretería EPA"],
        "jtbd": {
            "persona": "Propietario / Arrendador",
            "job": "Amoblar de forma económica e higiénica una propiedad en alquiler para proteger su valor a largo plazo.",
            "pain_points": "Daños por agua por descuido del inquilino, necesidad de reponer gabinetes deteriorados rápidamente.",
            "triggers": "Cambio de inquilino o adecuacion de departamento para Airbnb."
        },
        "raw_menu_categories": [
            "Muebles de Cocina Modular Novey",
            "Ofertas Cyber de Organizadores",
            "Muebles de Baño RH Hidrófugos",
            "Escritorios RTA de Alta Resistencia",
            "Descuentos Blackfriday Cómodas"
        ],
        "products": [
            {"name": "Módulo Fregadero RH Novey 120cm", "rh": True, "assembly": "minifix", "desc": "Tablero RH resistente a humedad"},
            {"name": "Escritorio Home Office Basic Rovere", "rh": False, "assembly": "estandar", "desc": "Tablero aglomerado estándar"},
            {"name": "Organizador Lavandería Multi-espacio", "rh": False, "assembly": "estandar", "desc": "MDP melamínico estándar"},
            {"name": "Gabinete Espejo de Baño RH", "rh": True, "assembly": "minifix", "desc": "Gabinete hidrófugo de fácil anclaje"}
        ]
    }
}

# --- PARTE 1: FUNCIONES DE FILTRADO Y PROCESAMIENTO ---

def clean_advertising_noise(category_list):
    """
    Filtro Antirruido Nativo:
    Limpia datos brutos eliminando cualquier URL o texto que contenga palabras
    promocionales mediante regex.
    """
    cleaned_list = []
    noise_pattern = re.compile(
        r'(cyber|oferta|descuento|blackfriday|promocion|combo|barato|imperdible|descuentos|rebajas|lanzamiento|low cost)', 
        re.IGNORECASE
    )
    for category in category_list:
        if not noise_pattern.search(category):
            cleaned_list.append(category.strip())
    return cleaned_list


def analyze_cdt_and_jtbd(client_name, cleaned_categories, products):
    """
    Procesamiento de Negocio: CDT y JTBD con asignación de Espacios en Blanco
    """
    technical_words = ['modular', 'rh', 'resistencia', 'medidas', 'alto', 'fregadero', 'suspender', 'plegable', 'auxiliar', 'lavanderia']
    aesthetic_words = ['nordico', 'diseno', 'design', 'moderno', 'exclusivo', 'nogal', 'wengue', 'blanco', 'sala', 'living', 'estetica', 'gamer']
    
    tech_score = 0
    aes_score = 0
    
    all_text = " ".join(cleaned_categories).lower() + " " + " ".join([p['name'] for p in products]).lower()
    
    for word in technical_words:
        tech_score += all_text.count(word)
    for word in aesthetic_words:
        aes_score += all_text.count(word)
        
    if tech_score >= aes_score:
        cdt_focus = "Benefit/Price-Driven (Atributos Técnicos & Funcionalidad)"
    else:
        cdt_focus = "Design-Driven (Estética, Acabados & Estilo de Vida)"
        
    white_spaces = []
    total_products = len(products)
    rh_products = sum(1 for p in products if p.get('rh', False))
    quick_assembly = sum(1 for p in products if p.get('assembly', '') in ['minifix', 'click'])
    
    has_wet_areas = any('cocina' in c.lower() or 'baño' in c.lower() or 'lavandería' in c.lower() for c in cleaned_categories)
    if has_wet_areas and (rh_products / total_products if total_products > 0 else 0) < 0.25:
        white_spaces.append(
            f"Escasez de portafolio hidrófugo (RH) en zonas húmedas. Solo el {int((rh_products/total_products)*100) if total_products > 0 else 0}% de los muebles de cocina/baño cuentan con propiedades hidrófugas."
        )
        
    if (quick_assembly / total_products if total_products > 0 else 0) < 0.30:
        white_spaces.append(
            f"Déficit en sistemas de ensamble rápido (Minifix o Click). El catálogo aún depende en un {int((1 - (quick_assembly/total_products))*100) if total_products > 0 else 100}% de tornillería tradicional compleja."
        )
        
    return cdt_focus, white_spaces


# --- PARTE 2: PIPELINE DE COMPILACIÓN E INYECCIÓN DE SUBCADENA ---

def update_index_html(data):
    """
    Inyecta la data JSON mediante una búsqueda y sustitución de subcadenas exacta
    basada en las etiquetas de apertura y cierre. Evita problemas de regex con PowerShell/Python.
    """
    files = ["index.html"]
    for file_path in files:
        if not os.path.exists(file_path):
            continue
            
        with open(file_path, "r", encoding="utf-8") as f:
            html_content = f.read()
            
        start_tag = '<script id="market-data" type="application/json">'
        end_tag = '</script>'
        
        start_idx = html_content.find(start_tag)
        if start_idx == -1:
            print(f"Error: No se encontró la etiqueta de inicio de datos en {file_path}.")
            continue
            
        end_idx = html_content.find(end_tag, start_idx)
        if end_idx == -1:
            print(f"Error: No se encontró la etiqueta de cierre de datos en {file_path}.")
            continue
            
        json_data_str = json.dumps(data, indent=2, ensure_ascii=False)
        
        # Reemplazamos exactamente lo que hay entre las dos etiquetas
        new_html_content = (
            html_content[:start_idx + len(start_tag)] + 
            "\n" + json_data_str + "\n" + 
            html_content[end_idx:]
        )
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_html_content)
            
        print(f"Dashboard {file_path} actualizado exitosamente (método de subcadena seguro).")
    return True


def generate_readme_report(data):
    """
    Escribe y sobrescribe el README.md del repositorio.
    """
    readme_path = "README.md"
    
    content = []
    content.append("# 🏢 Inteligencia de Canales Digitales de Muebles RTA")
    content.append(f"\n> **Última actualización semanal:** {data['update_date']} | **Analista Principal:** Amelia RTA")
    content.append(f"\n**Tendencia Dominante de Mercado:** `{data['dominant_trend']}`")
    content.append(f"\n**Total Alertas de Oportunidad (Espacios en Blanco):** `{data['total_whitespaces']}`")
    
    content.append("\n## 📊 Resumen de Visualizaciones del Dashboard")
    content.append("- **Matriz de Ciclo de Vida de Tendencias:** Mapeo de categorías en fases de Introducción, Crecimiento, Madurez o Declive.")
    content.append("- **Tráfico Digital vs. Presencia de Marca Propia:** Comportamiento de penetración de marca propia en relación al volumen de tráfico digital.")
    content.append("\n*Para explorar las visualizaciones interactivas de Chart.js y aplicar filtros dinámicos por pestañas, abre el archivo [index.html](index.html) en tu navegador.*")
    
    content.append("\n---")
    content.append("\n## 🔍 Análisis Detallado por Cliente (11 Canales)")
    
    for client in data["clients"]:
        content.append(f"\n### 🏢 {client['name']}")
        content.append(f"- **Peso Estimado de Marca Propia:** `{client['own_brand_weight']}%` | **Índice de Tráfico Digital:** `{client['traffic_score']}/100`")
        
        content.append("\n#### 🧭 Arquitectura y Jerarquía del Menú (Filtrado sin Ruido)")
        for item in client['menu_hierarchy']:
            content.append(f"- {item}")
            
        content.append("\n#### 🌳 Árbol de Decisión de Compra (CDT) Digital")
        content.append(f"- **Enfoque Principal:** *{client['cdt_focus']}*")
        for item in client['cdt_tree']:
            content.append(f"  - {item}")
            
        content.append("\n#### ⚔️ Set Competitivo Principal")
        content.append(f"- {', '.join(client['competitive_set'])}")
        
        jt = client['jtbd']
        content.append("\n#### 👤 Perfil Buyer Persona (Jobs-To-Be-Done)")
        content.append(f"- **Arquetipo:** *{jt['persona']}*")
        content.append(f"- **Trabajo a Realizar (Job):** {jt['job']}")
        content.append(f"- **Puntos de Dolor (Pains):** {jt['pain_points']}")
        content.append(f"- **Disparador de Compra (Trigger):** {jt['triggers']}")
        
        content.append("\n#### ⚠️ Alertas de Espacio en Blanco (Oportunidades de Catálogo)")
        if client['white_spaces']:
            for ws in client['white_spaces']:
                content.append(f"- **ALERTA:** {ws}")
        else:
            content.append("- *No se detectan alertas críticas en stock de tableros RH o ensamble rápido.*")
            
        content.append("\n---")
        
    content.append("\n## ⚙️ Arquitectura del Sistema de Automatización")
    content.append("Este repositorio se actualiza autónomamente cada lunes a las 00:00 UTC.")
    content.append("\n```mermaid")
    content.append("graph TD")
    content.append("    A[Cron Job GitHub Actions] -->|Ejecuta| B(actualizador_rta.py)")
    content.append("    B --> C[Scraping Simulado & Ingesta]")
    content.append("    C --> D[Filtro Antirruido Regex]")
    content.append("    D --> E[Clasificación CDT/JTBD & Detección de Espacios]")
    content.append("    E --> F[Inyección de JSON en index.html]")
    content.append("    E --> G[Reescritura de README.md]")
    content.append("    F & G --> H[Git Commit & Auto Push]")
    content.append("```")
    
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("\n".join(content))
        
    print("Reporte Markdown README.md generado exitosamente.")


# --- PARTE 3: EJECUCIÓN PRINCIPAL ---

import urllib.request
import urllib.error

def generate_week_data_with_gemini(date_str, api_key):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    
    system_instruction = """
Actúa como AMELIA RTA, una Analista de Investigación de Mercado, Experta en Tendencias de Consumo y Especialista Senior en Auditoría de Canales Digitales y Category Management. Tu objetivo estratégico único es procesar datos de mercado, flujos de navegación e-commerce y estructuras de surtido para identificar patrones emergentes y brechas comerciales ("White Spaces") donde la empresa RTA MUEBLES pueda entrar y capturar mercado con un producto ganador de empaque plano (Ready-to-Assemble).

Tu universo de análisis se concentra de manera obligatoria en:
1. CANALES ESPECIALIZADOS: SODIMAC COLOMBIA S.A, FERRETERÍA EPA S.A., CENCOSUD COLOMBIA SA, GEO F NOVEY S A.
2. CANALES ESPECIALISTAS: INVERSIONES VIRTUAL MUEBLES S.A.S, TUHOME SPA / TUHOME PERÚ SAC, MOBBLY S.A.S.
3. CANALES INDUSTRIALES: COMPAÑÍA COLOMBIANA DE CERÁMICA SAS (Grupo Corona y aliados).
4. CANALES GRAN CONSUMO Y CATÁLOGO: ALMACENES ÉXITO S.A., NOVAVENTA S.A.S., CORPORACIÓN FAVORITA C.A.

Aplica el protocolo antirruido, aislando la estacionalidad del negocio estructural real de tableros y soluciones RTA. Usa JTBD y el ciclo de vida.
"""
    
    prompt = f"""
Genera los datos métricos y analíticos estructurales en formato JSON para la semana del '{date_str}'. 
Deberás responder ÚNICAMENTE con un objeto JSON estructurado que siga el siguiente esquema, sin explicaciones ni markdown adicionales (solo texto JSON puro).

Estructura requerida del JSON de salida:
{{
  "dominant_trend": "Benefit-Driven (RH & Ensamble)" o "Design-Driven (Estetica & Estilos)" según la fecha,
  "total_whitespaces": número de brechas encontradas en total en todos los clientes,
  "trends": [
    {{"name": "Cocinas Modulares", "x": número 10-100, "y": número 10-100, "phase": "Madurez"}},
    {{"name": "Home Office", "x": número 10-100, "y": número 10-100, "phase": "Crecimiento"}},
    {{"name": "Centros de TV", "x": número 10-100, "y": número 10-100, "phase": "Crecimiento"}},
    {{"name": "Dormitorio RTA", "x": número 10-100, "y": número 10-100, "phase": "Madurez"}},
    {{"name": "Banos RH", "x": número 10-100, "y": número 10-100, "phase": "Introduccion"}}
  ],
  "clients": [
    {{
      "name": "Nombre exacto del cliente (ej. SODIMAC COLOMBIA S.A, ALMACENES ÉXITO S.A., NOVAVENTA S.A.S., etc.)",
      "country": "País (ej. Colombia, Panama, Ecuador, Chile, Peru)",
      "cities": ["Lista de ciudades"],
      "best_sellers": ["3 productos líderes de esta semana específicos al tema de la fecha"],
      "future_sources": ["Fuentes de telemetría específicas a este canal"],
      "menu_hierarchy": ["Categorías limpias sin ruido"],
      "cdt_focus": "Brand-Driven o Benefit/Price/Space-Driven",
      "cdt_tree": ["Jerarquía del árbol de decisión (1, 2, 3)"],
      "own_brand_weight": número flotante del porcentaje de marca propia (ej. 15.5),
      "traffic_score": número entero de tráfico 10-100 para la semana,
      "competitive_set": ["Competidores directos e indirectos"],
      "jtbd": {{
        "persona": "Arquetipo que compra en este canal",
        "job": "El trabajo funcional/emocional del mueble",
        "pain_points": "Puntos de dolor principales",
        "triggers": "Triggers que detonan la compra"
      }},
      "white_spaces": ["Brechas comerciales críticas específicas a la fecha"],
      "crm_lead_score": número entero de prioridad comercial 0-100,
      "crm_suggested_pitch": "Propuesta comercial o pitch de ventas para este cliente",
      "crm_next_action": "Siguiente paso de ventas recomendado en el pipeline",
      "coastal_churn_risk": true o false (si es costero y tiene brecha de portafolio hidrófugo)
    }}
  ]
}}

Nota sobre la semana del '{date_str}':
Deberás adaptar la información (best_sellers, white_spaces, crm_next_action, traffic_score, etc.) de todos los clientes para que refleje el tema de mercado correspondiente a esta fecha:
- Si es 2026-05-21: Preparativos pre-Cyber (demanda de Home Office, stock preventivo).
- Si es 2026-05-28: Pico CyberDay (demanda extrema gamer/oficina, quiebres de stock).
- Si es 2026-06-04: Lluvias costeras en la Costa Caribe/Pacífico (demanda de tableros RH y muebles hidrófugos suspendidos de baño/cocina, déficit de stock RH).
- Si es 2026-06-11 o 2026-06-12: Crisis de fletes/puerto (retraso de melaminas claras, impulso a melamina oscura Wengue/Blanco).
- Si es 2026-06-19: Campaña del Día del Padre (enfoque en centros de TV de gran formato y muebles de bar).
- Si es 2026-06-26: Auditoría de costos de mitad de año (competencia con melamina económica de 12mm, optimización de calibres).
- Si es 2026-07-03: Sobrecupo de entregas logísticas (retraso en cajas pesadas, reingeniería hacia empaque plano modular de <10cm de espesor).
- Si es 2026-07-07: Temporada de lluvias (pico de melamina hidrófuga RH, certificación de materiales).
- Si es otra fecha: Comportamiento normal según perfil base del cliente.

Responde con texto JSON crudo únicamente.
"""

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ],
        "systemInstruction": {
            "parts": [
                {"text": system_instruction}
            ]
        },
        "generationConfig": {
            "responseMimeType": "application/json",
            "temperature": 0.2
        }
    }
    
    headers = {
        "Content-Type": "application/json"
    }
    
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers=headers,
        method="POST"
    )
    
    with urllib.request.urlopen(req, timeout=35) as response:
        res_data = json.loads(response.read().decode("utf-8"))
        candidates = res_data.get("candidates", [])
        if candidates:
            text = candidates[0].get("content", {}).get("parts", [])[0].get("text", "")
            return json.loads(text.strip())
    return None

def generate_week_data(date_str):
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key:
        try:
            print(f"Detectada clave GEMINI_API_KEY. Intentando generar datos para {date_str} con el cerebro de Gemini...")
            data = generate_week_data_with_gemini(date_str, api_key)
            if data and "clients" in data and len(data["clients"]) > 0:
                print(f"✅ Generación dinámica con la API de Gemini exitosa para la semana: {date_str}")
                return data
        except Exception as e:
            print(f"⚠️ Error al conectar con la API de Gemini: {e}. Usando generador lógico local de respaldo.")

    processed_clients = []
    total_whitespaces = 0
    
    # Determinar el tema y comportamiento según la fecha
    theme = "Normal"
    if date_str == "2026-05-21":
        theme = "Pre-Cyber"
    elif date_str == "2026-05-28":
        theme = "CyberDay-Peak"
    elif date_str == "2026-06-04":
        theme = "Post-Cyber-Rain"
    elif date_str in ["2026-06-11", "2026-06-12"]:
        theme = "Supply-Disruption"
    elif date_str == "2026-06-19":
        theme = "Fathers-Day"
    elif date_str == "2026-06-26":
        theme = "Mid-Year-Audit"
    elif date_str == "2026-07-03":
        theme = "Logistics-Rush"
    elif date_str == "2026-07-07":
        theme = "Rainy-Season"

    for client_name, info in CLIENTS_RAW_DATA.items():
        # Ajustar tráfico base según el tema
        traffic = info["base_traffic"]
        if theme == "Pre-Cyber":
            if client_name in ["INVERSIONES VIRTUAL MUEBLES S.A.S", "ALMACENES ÉXITO S.A.", "SODIMAC COLOMBIA S.A"]:
                traffic += 3
        elif theme == "CyberDay-Peak":
            if client_name in ["INVERSIONES VIRTUAL MUEBLES S.A.S", "ALMACENES ÉXITO S.A.", "MOBBLY S.A.S", "CENCOSUD COLOMBIA SA"]:
                traffic = 100  # Máximo tráfico para tiendas online
            else:
                traffic += 8
        elif theme == "Post-Cyber-Rain":
            traffic -= 5
        elif theme == "Fathers-Day":
            if client_name in ["INVERSIONES VIRTUAL MUEBLES S.A.S", "MOBBLY S.A.S", "CENCOSUD COLOMBIA SA"]:
                traffic += 6
        elif theme == "Rainy-Season":
            if info["country"] == "Colombia":
                traffic += 2
        
        traffic = max(10, min(100, traffic + random.randint(-1, 1)))
        
        brand_weight = round(max(5.0, min(100.0, info["own_brand"] + random.uniform(-1.0, 1.0))), 1)
        cleaned_cats = clean_advertising_noise(info["raw_menu_categories"])
        
        # Calcular foco CDT base y espacios
        cdt_focus, base_white_spaces = analyze_cdt_and_jtbd(client_name, cleaned_cats, info["products"])
        
        # Copiar white spaces para modificarlos
        white_spaces = list(base_white_spaces)
        
        # Modificar white_spaces y best_sellers según el tema de la semana
        best_sellers = list(info["best_sellers"])
        
        if theme == "Pre-Cyber":
            white_spaces.append("Riesgo de desabastecimiento: bajo inventario preventivo de melaminas antes del evento CyberDay.")
            best_sellers = [
                "Escritorio Home Office Smart 120cm",
                "Modulo Fregadero 100cm MDP Estandar",
                "Zapatero Basico 12 Pares"
            ]
        elif theme == "CyberDay-Peak":
            if client_name in ["INVERSIONES VIRTUAL MUEBLES S.A.S", "ALMACENES EXITO S.A.", "SODIMAC COLOMBIA S.A", "CENCOSUD COLOMBIA SA"]:
                white_spaces.append("Quiebre de stock critico en escritorios Home Office y Gamer debido a alta demanda CyberDay.")
            else:
                white_spaces.append("Brecha de visibilidad digital: Competencia acapara trafico publicitario con ofertas Cyber.")
            best_sellers = [
                "Escritorio Gamer Pro con Luces LED",
                "Escritorio Plegable Work-Space",
                "Centro de TV Nordico Blanco-Roble"
            ]
        elif theme == "Post-Cyber-Rain":
            coastal_cities = ["Barranquilla", "Cartagena", "Manta", "Guayaquil", "Colon", "David", "Valparaiso", "Antofagasta", "Ciudad de Panama"]
            is_coastal = any(any(c.lower() in city.lower() for c in coastal_cities) for city in info["cities"])
            if is_coastal:
                white_spaces.append("Deficit de portafolio hidrofugo (RH) en cocinas y banos expuestos a alta humedad y lluvias costeras.")
                best_sellers = [
                    "Modulo Fregadero MDP-RH 100cm",
                    "Gabinete de Bano suspendido 60cm RH",
                    "Mueble Lavamanos Split RH"
                ]
            else:
                white_spaces.append("Agotamiento general de stock de melamina estandar tras despacho de pedidos CyberDay.")
                best_sellers = [
                    "Biblioteca Modular 5 Niveles",
                    "Estanterias RTA Metalicas",
                    "Mesa Auxiliar Multiusos"
                ]
        elif theme == "Supply-Disruption":
            white_spaces.append("Quiebre de catalogo: Falta de melamina clara (Nordico/Rovere) por retrasos en puerto de importacion.")
            best_sellers = [
                "Closet RTA 4 Puertas Wengue",
                "Centro de TV Florencia Wengue",
                "Modulo Cocina con Meson de Acero"
            ]
        elif theme == "Fathers-Day":
            white_spaces.append("Falta de muebles de bar y centros de entretenimiento de gran formato (+65 pulgadas) en catalogo de temporada.")
            best_sellers = [
                "Centro de TV Prime Nogal 55 pulgadas",
                "Mesa de TV Flotante 140cm",
                "Escritorio Gamer Pro con Luces LED"
            ]
        elif theme == "Mid-Year-Audit":
            white_spaces.append("Brecha de costos: Competencia local lanza linea economica de 12mm. Se requiere reduccion de espesor para competir.")
            best_sellers = [
                "Closet RTA 3 Puertas Finlandek",
                "Escritorio Compacto Office Finlandek",
                "Zapatero Basico 12 Pares"
            ]
        elif theme == "Logistics-Rush":
            white_spaces.append("Brecha de entrega: Sobrecupo logistico retrasa entregas de gran formato. Se requieren embalajes planos ultra-optimizados.")
            best_sellers = [
                "Zapatero RTA 12 Pares",
                "Organizador Lavanderia Multi-espacio",
                "Estanteria Multiusos 4 repisas"
            ]
        elif theme == "Rainy-Season":
            white_spaces.append("Agotamiento de inventario de melamina hidrofuga (MDP-RH) ante la aceleracion de lluvias de la temporada.")
            best_sellers = [
                "Modulo Fregadero MDP-RH 100cm",
                "Modulo Alto de Cocina 60cm MDP-RH",
                "Alacena Organizadora Multiusos RH"
            ]

        total_whitespaces += len(white_spaces)
        
        if "Benefit" in cdt_focus:
            cdt_tree = [
                "1. Dimensiones y espacio disponible (Filtro numerico)",
                "2. Resistencia del material (Aglomerado estandar vs Tablero RH)",
                "3. Relacion precio-capacidad de almacenado"
            ]
        else:
            cdt_tree = [
                "1. Combinacion de colores y estilo estetico (Nordico, Wengue, Industrial)",
                "2. Tipo de ensamble visual (Flotante, de patas de madera)",
                "3. Calificaciones de diseno y reviews en web"
            ]

        # CRM KPIs calculations
        whitespaces_count = len(white_spaces)
        lead_score = int((traffic * (100 - brand_weight) * (whitespaces_count + 1)) / 150)
        lead_score = min(100, max(0, lead_score))
        
        # Determinar pitch y accion CRM segun la brecha principal añadida por el tema
        has_rh_gap = any("hidrofugo" in ws.lower() or "rh" in ws.lower() for ws in white_spaces)
        has_assembly_gap = any("ensamble rapido" in ws.lower() or "click" in ws.lower() for ws in white_spaces)
        has_stockout_gap = any("desabastecimiento" in ws.lower() or "quiebre de stock" in ws.lower() for ws in white_spaces)
        has_supply_gap = any("puerto" in ws.lower() or "importacion" in ws.lower() for ws in white_spaces)
        has_price_gap = any("costos" in ws.lower() or "precio" in ws.lower() for ws in white_spaces)
        has_logistics_gap = any("logistico" in ws.lower() or "entrega" in ws.lower() for ws in white_spaces)
        
        if has_stockout_gap:
            suggested_pitch = "Presentar planes de abastecimiento de contingencia para alta demanda digital"
            next_action = "Enviar propuesta comercial de reserva de capacidad de produccion de tableros de oficina para cubrir los quiebres del Cyber."
        elif has_supply_gap:
            suggested_pitch = "Ofrecer paleta de acabados alternativos de entrega rapida (Wengue y Blanco)"
            next_action = "Enviar muestrarios fisicos de melamina Wengue y Blanco y agendar llamada con compras para autorizar la sustitucion temporal en catalogo."
        elif has_rh_gap:
            suggested_pitch = "Ofrecer portafolio MDP-RH y Melamina Anti-humedad para Cocina/Bano"
            next_action = "Programar visita presencial con el equipo tecnico para certificar la resistencia a la humedad del portafolio MDP-RH y proponer el reemplazo de modulos en zonas costeras."
        elif has_price_gap:
            suggested_pitch = "Presentar optimizacion de espesores MDP estandar de 12mm/15mm para bajo costo"
            next_action = "Presentar propuesta comercial de melamina de menor espesor para competir agresivamente en precios de entrada."
        elif has_logistics_gap:
            suggested_pitch = "Proponer empaque modular plano super-optimizado para optimizacion de fletes B2B"
            next_action = "Programar reunion tecnica para presentar el nuevo diseno de empaque plano modularizado que reduce el volumen logistico."
        elif has_assembly_gap:
            suggested_pitch = "Promocionar sistemas Click de Ensamble Rapido sin tornillos"
            next_action = "Enviar muestras fisicas de los tableros con herraje Click de ensamble rapido y agendar una demo virtual de 15 minutos para demostrar el ahorro de tiempo al comprador digital."
        elif "Benefit" in cdt_focus:
            suggested_pitch = "Presentar optimizacion de espesores MDP estandar para alto volumen"
            next_action = "Presentar propuesta de cotizacion preferencial en tableros de melamina estandar con espesores optimizados para grandes distribuidores."
        else:
            suggested_pitch = "Presentar nuevos acabados esteticos de tendencia (Nordico, Wengue y Gamer)"
            next_action = "Coordinar sesion de co-creacion de diseno con su equipo de compras para presentar la nueva paleta de colores de tendencia y planificar la renovacion del catalogo."
            
        coastal_cities = ["Barranquilla", "Cartagena", "Manta", "Guayaquil", "Colon", "David", "Valparaiso", "Antofagasta", "Ciudad de Panama"]
        is_coastal = any(any(c.lower() in city.lower() for c in coastal_cities) for city in info["cities"])
        coastal_churn_risk = is_coastal and has_rh_gap
            
        processed_clients.append({
            "name": client_name,
            "country": info["country"],
            "cities": info["cities"],
            "best_sellers": best_sellers,
            "future_sources": info["future_sources"],
            "menu_hierarchy": cleaned_cats,
            "cdt_focus": cdt_focus,
            "cdt_tree": cdt_tree,
            "own_brand_weight": brand_weight,
            "traffic_score": traffic,
            "competitive_set": info["competitive_set"],
            "jtbd": info["jtbd"],
            "white_spaces": white_spaces,
            "crm_lead_score": lead_score,
            "crm_suggested_pitch": suggested_pitch,
            "crm_next_action": next_action,
            "coastal_churn_risk": coastal_churn_risk
        })
        
    dominant_trend = "Benefit-Driven (RH & Ensamble)" if total_whitespaces > 6 else "Design-Driven (Estetica & Estilos)"
    
    # Mapear coordenadas de tendencias dinamicamente segun el tema de la semana
    x_offset = {"Cocinas Modulares": 0, "Home Office": 0, "Centros de TV": 0, "Dormitorio RTA": 0, "Banos RH": 0}
    y_offset = {"Cocinas Modulares": 0, "Home Office": 0, "Centros de TV": 0, "Dormitorio RTA": 0, "Banos RH": 0}
    
    if theme == "Pre-Cyber":
        x_offset["Home Office"] = 5
        x_offset["Centros de TV"] = 2
    elif theme == "CyberDay-Peak":
        x_offset["Home Office"] = 20
        y_offset["Home Office"] = 15
        x_offset["Centros de TV"] = 10
        y_offset["Centros de TV"] = 8
    elif theme == "Post-Cyber-Rain":
        x_offset["Home Office"] = -10
        x_offset["Banos RH"] = 10
        y_offset["Banos RH"] = 8
    elif theme == "Supply-Disruption":
        x_offset["Cocinas Modulares"] = -5
        x_offset["Home Office"] = -5
    elif theme == "Fathers-Day":
        x_offset["Centros de TV"] = 15
        y_offset["Centros de TV"] = 12
    elif theme == "Rainy-Season":
        x_offset["Banos RH"] = 25
        y_offset["Banos RH"] = 20
        
    trends = [
        {"name": "Cocinas Modulares", "x": max(10, min(100, 75 + x_offset["Cocinas Modulares"] + random.randint(-1, 1))), "y": max(10, min(100, 85 + y_offset["Cocinas Modulares"])), "phase": "Madurez"},
        {"name": "Home Office", "x": max(10, min(100, 45 + x_offset["Home Office"] + random.randint(-1, 1))), "y": max(10, min(100, 60 + y_offset["Home Office"])), "phase": "Crecimiento"},
        {"name": "Centros de TV", "x": max(10, min(100, 60 + x_offset["Centros de TV"] + random.randint(-1, 1))), "y": max(10, min(100, 70 + y_offset["Centros de TV"])), "phase": "Crecimiento"},
        {"name": "Dormitorio RTA", "x": max(10, min(100, 80 + x_offset["Dormitorio RTA"] + random.randint(-1, 1))), "y": max(10, min(100, 50 + y_offset["Dormitorio RTA"])), "phase": "Madurez"},
        {"name": "Banos RH", "x": max(10, min(100, 35 + x_offset["Banos RH"] + random.randint(-1, 1))), "y": max(10, min(100, 42 + y_offset["Banos RH"])), "phase": "Introduccion"}
    ]
    
    return {
        "dominant_trend": dominant_trend,
        "total_whitespaces": total_whitespaces,
        "trends": trends,
        "clients": processed_clients
    }

def main():
    print("Iniciando actualización semanal de Inteligencia RTA...")
    today_str = datetime.utcnow().strftime("%Y-%m-%d")
    
    # Cargar historial existente si existe
    history = {}
    if os.path.exists("data.json"):
        try:
            with open("data.json", "r", encoding="utf-8") as f:
                old_data = json.load(f)
                if "history" in old_data:
                    history = old_data["history"]
                    
                    # Reparar crm_next_action en el historial cargado
                    for week_date, week_data in history.items():
                        if "clients" in week_data:
                            for c in week_data["clients"]:
                                if "crm_next_action" not in c or not c["crm_next_action"]:
                                    white_spaces = c.get("white_spaces", [])
                                    cdt_focus = c.get("cdt_focus", "")
                                    has_rh_gap = any("hidrófugo" in ws.lower() or "rh" in ws.lower() for ws in white_spaces)
                                    has_assembly_gap = any("ensamble rápido" in ws.lower() or "click" in ws.lower() for ws in white_spaces)
                                    if has_rh_gap:
                                        c["crm_next_action"] = "Programar visita presencial con el equipo técnico para certificar la resistencia a la humedad del portafolio MDP-RH y proponer el reemplazo de módulos de aglomerado estándar en zonas costeras."
                                    elif has_assembly_gap:
                                        c["crm_next_action"] = "Enviar muestras físicas de los tableros con herraje Click de ensamble rápido y agendar una demo virtual de 15 minutos para demostrar el ahorro de tiempo al comprador digital joven."
                                    elif "Benefit" in cdt_focus:
                                        c["crm_next_action"] = "Presentar propuesta de cotización preferencial en tableros de melamina estándar con espesores optimizados para grandes distribuidores que buscan liderar en precio."
                                    else:
                                        c["crm_next_action"] = "Coordinar sesión de co-creación de diseño con su equipo de compras para presentar la nueva paleta de colores de tendencia (Rovere, Nórdico, Wengue y Gamer) y planificar la renovación del catálogo."
        except Exception as e:
            print("No se pudo cargar el historial anterior, se creará uno nuevo:", e)

    # Determinar si hay huecos semanales a rellenar
    from datetime import datetime, timedelta
    if history:
        sorted_dates = sorted(history.keys())
        last_date_str = sorted_dates[-1]
        try:
            last_date = datetime.strptime(last_date_str, "%Y-%m-%d")
            today = datetime.strptime(today_str, "%Y-%m-%d")
            
            # Loop agregando semanas (de 7 en 7 días) hasta hoy
            current_date = last_date + timedelta(days=7)
            while current_date <= today:
                current_date_str = current_date.strftime("%Y-%m-%d")
                if current_date_str not in history:
                    print(f"Rellenando semana faltante en historial: {current_date_str}")
                    history[current_date_str] = generate_week_data(current_date_str)
                current_date += timedelta(days=7)
        except Exception as ex:
            print(f"Error al calcular fechas faltantes: {ex}")
            
    # Asegurar que la fecha de hoy esté generada
    if today_str not in history:
        print(f"Generando datos para la semana actual: {today_str}")
        history[today_str] = generate_week_data(today_str)
    
    # Pre-cargar semanas históricas reales de manera dinámica
    historical_weeks = ["2026-05-21", "2026-05-28", "2026-06-04", "2026-06-11", "2026-06-12", "2026-06-19", "2026-06-26", "2026-07-03"]
    for w_date in historical_weeks:
        if w_date not in history:
            print(f"Pre-cargando semana histórica dinámica: {w_date}")
            history[w_date] = generate_week_data(w_date)
            
    final_data = {
        "current_date": today_str,
        "history": history
    }
    
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(final_data, f, indent=2, ensure_ascii=False)
        
    update_index_html(final_data)
    generate_readme_report(final_data)
    print("Actualización de Amelia RTA finalizada exitosamente.")


if __name__ == "__main__":
    main()
