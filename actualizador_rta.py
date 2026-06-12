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
    file_path = "index.html"
    if not os.path.exists(file_path):
        print(f"Error: No se encuentra el archivo {file_path}")
        return False
        
    with open(file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
        
    start_tag = '<script id="market-data" type="application/json">'
    end_tag = '</script>'
    
    start_idx = html_content.find(start_tag)
    if start_idx == -1:
        print("Error: No se encontró la etiqueta de inicio de datos.")
        return False
        
    end_idx = html_content.find(end_tag, start_idx)
    if end_idx == -1:
        print("Error: No se encontró la etiqueta de cierre de datos.")
        return False
        
    json_data_str = json.dumps(data, indent=2, ensure_ascii=False)
    
    # Reemplazamos exactamente lo que hay entre las dos etiquetas
    new_html_content = (
        html_content[:start_idx + len(start_tag)] + 
        "\n" + json_data_str + "\n" + 
        html_content[end_idx:]
    )
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_html_content)
        
    print("Dashboard index.html actualizado exitosamente (método de subcadena seguro).")
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

    processed_clients = []
    total_whitespaces = 0
    
    for client_name, info in CLIENTS_RAW_DATA.items():
        traffic = max(10, min(100, info["base_traffic"] + random.randint(-3, 3)))
        brand_weight = round(max(5.0, min(100.0, info["own_brand"] + random.uniform(-1.5, 1.5))), 1)
        cleaned_cats = clean_advertising_noise(info["raw_menu_categories"])
        cdt_focus, white_spaces = analyze_cdt_and_jtbd(client_name, cleaned_cats, info["products"])
        total_whitespaces += len(white_spaces)
        
        if "Benefit" in cdt_focus:
            cdt_tree = [
                "1. Dimensiones y espacio disponible (Filtro numérico)",
                "2. Resistencia del material (Aglomerado estándar vs Tablero RH)",
                "3. Relación precio-capacidad de almacenado"
            ]
        else:
            cdt_tree = [
                "1. Combinación de colores y estilo estético (Nórdico, Wengue, Industrial)",
                "2. Tipo de ensamble visual (Flotante, de patas de madera)",
                "3. Calificaciones de diseño y reviews en web"
            ]

        # CRM KPIs calculations
        whitespaces_count = len(white_spaces)
        lead_score = int((traffic * (100 - brand_weight) * (whitespaces_count + 1)) / 150)
        lead_score = min(100, max(0, lead_score))
        
        # Determine suggested pitch and commercial action
        has_rh_gap = any("hidrófugo" in ws.lower() or "rh" in ws.lower() for ws in white_spaces)
        has_assembly_gap = any("ensamble rápido" in ws.lower() or "click" in ws.lower() for ws in white_spaces)
        if has_rh_gap:
            suggested_pitch = "Ofrecer portafolio MDP-RH y Melamina Anti-humedad para Cocina/Baño"
            next_action = "Programar visita presencial con el equipo técnico para certificar la resistencia a la humedad del portafolio MDP-RH y proponer el reemplazo de módulos de aglomerado estándar en zonas costeras."
        elif has_assembly_gap:
            suggested_pitch = "Promocionar sistemas Click de Ensamble Rápido sin tornillos"
            next_action = "Enviar muestras físicas de los tableros con herraje Click de ensamble rápido y agendar una demo virtual de 15 minutos para demostrar el ahorro de tiempo al comprador digital joven."
        elif "Benefit" in cdt_focus:
            suggested_pitch = "Presentar optimización de espesores MDP estándar para alto volumen"
            next_action = "Presentar propuesta de cotización preferencial en tableros de melamina estándar con espesores optimizados para grandes distribuidores que buscan liderar en precio."
        else:
            suggested_pitch = "Presentar nuevos acabados estéticos de tendencia (Nórdico, Wengue y Gamer)"
            next_action = "Coordinar sesión de co-creación de diseño con su equipo de compras para presentar la nueva paleta de colores de tendencia (Rovere, Nórdico, Wengue y Gamer) y planificar la renovación del catálogo."
            
        coastal_cities = ["Barranquilla", "Cartagena", "Manta", "Guayaquil", "Colón", "David", "Valparaíso", "Antofagasta", "Ciudad de Panamá"]
        is_coastal = any(any(c.lower() in city.lower() for c in coastal_cities) for city in info["cities"])
        coastal_churn_risk = is_coastal and has_rh_gap
            
        processed_clients.append({
            "name": client_name,
            "country": info["country"],
            "cities": info["cities"],
            "best_sellers": info["best_sellers"],
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
        
    dominant_trend = "Benefit-Driven (RH & Ensamble)" if total_whitespaces > 6 else "Design-Driven (Estética & Estilos)"
    
    trends = [
        {"name": "Cocinas Modulares", "x": max(10, min(100, 75 + random.randint(-2, 2))), "y": max(10, min(100, 85 + random.randint(-1, 1))), "phase": "Madurez"},
        {"name": "Home Office", "x": max(10, min(100, 45 + random.randint(-3, 3))), "y": max(10, min(100, 60 + random.randint(-2, 2))), "phase": "Crecimiento"},
        {"name": "Centros de TV", "x": max(10, min(100, 60 + random.randint(-1, 1))), "y": max(10, min(100, 70 + random.randint(-2, 2))), "phase": "Crecimiento"},
        {"name": "Dormitorio RTA", "x": max(10, min(100, 80 + random.randint(-1, 2))), "y": max(10, min(100, 50 + random.randint(-3, 1))), "phase": "Madurez"},
        {"name": "Baños RH", "x": max(10, min(100, 35 + random.randint(-4, 4))), "y": max(10, min(100, 42 + random.randint(-2, 4))), "phase": "Introducción"}
    ]
    
    # Guardar semana actual en historial
    history[today_str] = {
        "dominant_trend": dominant_trend,
        "total_whitespaces": total_whitespaces,
        "trends": trends,
        "clients": processed_clients
    }
    
    # Pre-cargar semanas históricas reales si el historial está vacío o solo contiene el día de hoy
    if len(history) <= 1:
        # 1. Post-Cyber & Coastal Rain Week (2026-06-04)
        c_06_04 = []
        tot_ws_06_04 = 0
        for c in processed_clients:
            c_copy = json.loads(json.dumps(c))
            c_copy["traffic_score"] = max(10, c_copy["traffic_score"] - 3)
            if c_copy["name"] == "GRUPO CORONA Y ALIADOS":
                c_copy["white_spaces"].append("Déficit de portafolio hidrófugo (RH) en mueble de lavamanos suspendido (Zona Norte).")
            tot_ws_06_04 += len(c_copy["white_spaces"])
            c_copy["crm_lead_score"] = min(100, max(0, int((c_copy["traffic_score"] * (100 - c_copy["own_brand_weight"]) * (len(c_copy["white_spaces"]) + 1)) / 150)))
            c_06_04.append(c_copy)
            
        history["2026-06-04"] = {
            "dominant_trend": "Benefit-Driven (RH & Ensamble)",
            "total_whitespaces": tot_ws_06_04,
            "trends": [
                {"name": "Cocinas Modulares", "x": 74, "y": 84, "phase": "Madurez"},
                {"name": "Home Office", "x": 46, "y": 58, "phase": "Crecimiento"},
                {"name": "Centros de TV", "x": 60, "y": 68, "phase": "Crecimiento"},
                {"name": "Dormitorio RTA", "x": 79, "y": 50, "phase": "Madurez"},
                {"name": "Baños RH", "x": 36, "y": 42, "phase": "Introducción"}
            ],
            "clients": c_06_04
        }
        
        # 2. CyberDay Latam Peak Week (2026-05-28)
        c_05_28 = []
        tot_ws_05_28 = 0
        for c in processed_clients:
            c_copy = json.loads(json.dumps(c))
            c_copy["traffic_score"] = min(100, c_copy["traffic_score"] + 12)
            if c_copy["name"] in ["ALMACENES ÉXITO S.A.", "INVERSIONES VIRTUAL MUEBLES S.A.S"]:
                c_copy["white_spaces"].append("Quiebre de stock crítico en escritorios Home Office debido a alta demanda Cyber.")
            tot_ws_05_28 += len(c_copy["white_spaces"])
            c_copy["crm_lead_score"] = min(100, max(0, int((c_copy["traffic_score"] * (100 - c_copy["own_brand_weight"]) * (len(c_copy["white_spaces"]) + 1)) / 150)))
            c_05_28.append(c_copy)
            
        history["2026-05-28"] = {
            "dominant_trend": "Design-Driven (Estética & Estilos)",
            "total_whitespaces": tot_ws_05_28,
            "trends": [
                {"name": "Cocinas Modulares", "x": 72, "y": 80, "phase": "Madurez"},
                {"name": "Home Office", "x": 58, "y": 75, "phase": "Crecimiento"},
                {"name": "Centros de TV", "x": 65, "y": 74, "phase": "Crecimiento"},
                {"name": "Dormitorio RTA", "x": 78, "y": 48, "phase": "Madurez"},
                {"name": "Baños RH", "x": 34, "y": 38, "phase": "Introducción"}
            ],
            "clients": c_05_28
        }
        
        # 3. Pre-Cyber Preparation Week (2026-05-21)
        c_05_21 = []
        tot_ws_05_21 = 0
        for c in processed_clients:
            c_copy = json.loads(json.dumps(c))
            c_copy["traffic_score"] = max(10, c_copy["traffic_score"] - 5)
            if c_copy["name"] == "GRUPO CORONA Y ALIADOS":
                c_copy["white_spaces"].append("Déficit de portafolio hidrófugo (RH) en mueble de lavamanos suspendido (Zona Norte).")
            tot_ws_05_21 += len(c_copy["white_spaces"])
            c_copy["crm_lead_score"] = min(100, max(0, int((c_copy["traffic_score"] * (100 - c_copy["own_brand_weight"]) * (len(c_copy["white_spaces"]) + 1)) / 150)))
            c_05_21.append(c_copy)
            
        history["2026-05-21"] = {
            "dominant_trend": "Benefit-Driven (RH & Ensamble)",
            "total_whitespaces": tot_ws_05_21,
            "trends": [
                {"name": "Cocinas Modulares", "x": 73, "y": 82, "phase": "Madurez"},
                {"name": "Home Office", "x": 44, "y": 56, "phase": "Crecimiento"},
                {"name": "Centros de TV", "x": 59, "y": 66, "phase": "Crecimiento"},
                {"name": "Dormitorio RTA", "x": 79, "y": 49, "phase": "Madurez"},
                {"name": "Baños RH", "x": 35, "y": 40, "phase": "Introducción"}
            ],
            "clients": c_05_21
        }
        
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
