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
        "short_name": "Sodimac Colombia",
        "url_menu": "https://www.homecenter.com.co/homecenter-co/category/cat1770069/muebles-y-organizacion/",
        "urls_ingesta": ["https://www.homecenter.com.co/homecenter-co/category/cat1770069/muebles-y-organizacion/"],
        "base_traffic": 90,
        "own_brand": 35.0,
        "country": "Colombia",
        "cities": [
            {"ciudad": "Bogotá", "es_costera": False, "humedad_relativa_promedio": 65},
            {"ciudad": "Medellín", "es_costera": False, "humedad_relativa_promedio": 68},
            {"ciudad": "Cali", "es_costera": False, "humedad_relativa_promedio": 70},
            {"ciudad": "Barranquilla", "es_costera": True, "humedad_relativa_promedio": 80},
            {"ciudad": "Cartagena", "es_costera": True, "humedad_relativa_promedio": 81}
        ],
        "best_sellers": ["Módulo Fregadero MDP-RH 100cm", "Escritorio Home Office Smart 120cm", "Estanterías RTA Metálicas"],
        "future_sources": ["MercadoLibre Colombia (Tendencias de Búsqueda)", "Homecenter Chile (Benchmark de Clones de Diseño)", "Google Analytics RTA (Tasa de rebote en categoría de cocinas modulares y descargas de instructivos de armado)"],
        "competitive_set": ["Cencosud", "Madecentro"],
        "jtbd": {
            "persona": "Remodelador Práctico JtBD",
            "job": "Optimizar el espacio de la cocina y zona de ropas de forma rápida y sin herramientas complejas.",
            "pain_points": "Aglomerados que se inflan con humedad, herrajes faltantes y manuales de ensamble confusos.",
            "triggers": "Renovación de arriendo o mudanza a departamento nuevo de interés social (VIS)."
        },
        "raw_menu_categories": ["Muebles de Cocina - Modulares", "Muebles de TV y Centros de Entretenimiento", "Estanterías y Clósets RTA", "Muebles de Baño RH Resistentes a Humedad"],
        "products": [
            {"name": "Módulo Fregadero 100cm MDP Estándar", "rh": False, "assembly": "estandar", "desc": "Estructura aglomerada 15mm"},
            {"name": "Escritorio Home Office Smart 120cm", "rh": False, "assembly": "minifix", "desc": "Ensamble rápido con tornillos minifix"},
            {"name": "Módulo Alto de Cocina 60cm MDP-RH", "rh": True, "assembly": "estandar", "desc": "Madera resistente a humedad"},
            {"name": "Centro de TV Prime Nogal 55 pulgadas", "rh": False, "assembly": "estandar", "desc": "Acabado estético melamínico"}
        ]
    },
    "MADECENTRO S.A.S": {
        "short_name": "Madecentro",
        "url_menu": "https://madecentro.com/pages/muebles",
        "urls_ingesta": ["https://madecentro.com/pages/muebles"],
        "base_traffic": 85,
        "own_brand": 20.0,
        "country": "Colombia",
        "cities": [
            {"ciudad": "Bogotá", "es_costera": False, "humedad_relativa_promedio": 65},
            {"ciudad": "Medellín", "es_costera": False, "humedad_relativa_promedio": 68},
            {"ciudad": "Cali", "es_costera": False, "humedad_relativa_promedio": 70},
            {"ciudad": "Barranquilla", "es_costera": True, "humedad_relativa_promedio": 80},
            {"ciudad": "Cartagena", "es_costera": True, "humedad_relativa_promedio": 82}
        ],
        "best_sellers": ["Módulo Cocina RTA Premium", "Alacena Organizadora Multiusos Madecentro", "Escritorio Home Office Madecentro"],
        "future_sources": ["Madecentro Ventas Internas (ERP)", "Google Analytics RTA (Tasa de rebote en categoría de cocinas modulares y descargas de instructivos de armado)"],
        "competitive_set": ["Sodimac", "Easy"],
        "jtbd": {
            "persona": "Remodelador Práctico JtBD",
            "job": "Encontrar tableros y módulos de cocina a medida listos para armar e instalar de inmediato.",
            "pain_points": "Hinchamiento de tableros de baja calidad por humedad, falta de herrajes en el kit de armado.",
            "triggers": "Renovación o instalación rápida de mobiliario de cocina o baño."
        },
        "raw_menu_categories": ["Muebles de Cocina Listos para Armar", "Muebles de Oficina y Escritorios RTA", "Alacenas y Organizadores", "Muebles de Lavandería y Baño RH"],
        "products": [
            {"name": "Módulo Cocina RTA Premium", "rh": False, "assembly": "minifix", "desc": "Cocina modulada de ensamble rápido"},
            {"name": "Alacena Organizadora Multiusos Madecentro", "rh": False, "assembly": "minifix", "desc": "Organizador multiusos"},
            {"name": "Mueble de Baño Suspendido Madecentro RH", "rh": True, "assembly": "minifix", "desc": "Mueble resistente a humedad"},
            {"name": "Escritorio Home Office Madecentro", "rh": False, "assembly": "click", "desc": "Escritorio rápido de armar"}
        ]
    },
    "INVERSIONES VIRTUAL MUEBLES S.A.S": {
        "short_name": "Virtual Muebles",
        "url_menu": "https://www.virtualmuebles.com",
        "urls_ingesta": ["https://www.virtualmuebles.com"],
        "base_traffic": 78,
        "own_brand": 90.0,
        "country": "Colombia",
        "cities": [
            {"ciudad": "Medellín", "es_costera": False, "humedad_relativa_promedio": 68},
            {"ciudad": "Bogotá", "es_costera": False, "humedad_relativa_promedio": 65},
            {"ciudad": "Envigado", "es_costera": False, "humedad_relativa_promedio": 66}
        ],
        "best_sellers": ["Centro de TV Nórdico Blanco-Roble", "Escritorio Gamer Pro", "Escritorio Plegable Work-Space"],
        "future_sources": ["Amazon Global (Tendencias de Diseño Industrial)", "Instagram Shopping (Engagement de Muebles RTA)", "Google Analytics RTA (Embudo de conversión de la línea Gamer y rebote en landings de escritorio flexible)"],
        "competitive_set": ["TuHome", "Wayfair"],
        "jtbd": {
            "persona": "Comprador Digital Joven JtBD",
            "job": "Amoblar su primer apartamento con diseños activos que se puedan comprar 100% en línea y recibir rápido.",
            "pain_points": "Dificultad de envío, falta de soporte para piezas dañadas en transporte, desconfianza en fotos web.",
            "triggers": "Primer empleo profesional, independencia de casa de los padres."
        },
        "raw_menu_categories": ["Salas y Centros de TV Design", "Escritorios Flexibles Modernos", "Zapateros y Armarios Multifunción"],
        "products": [
            {"name": "Centro de TV Nórdico Blanco-Roble", "rh": False, "assembly": "minifix", "desc": "Diseño estético escandinavo"},
            {"name": "Escritorio Plegable Work-Space", "rh": False, "assembly": "click", "desc": "Sistema de ensamble rápido click"},
            {"name": "Mesa de Noche Minimalista con Cajón", "rh": False, "assembly": "estandar", "desc": " MDP texturizado"},
            {"name": "Mueble Auxiliar Microondas MDP", "rh": False, "assembly": "estandar", "desc": "Mueble modular para electrodomésticos"}
        ]
    },
    "GRUPO CORONA Y ALIADOS": {
        "short_name": "Grupo Corona",
        "url_menu": "https://corona.co/productos/muebles-para-cocinas/c/muebles-para-cocinas",
        "urls_ingesta": ["https://corona.co/productos/muebles-para-cocinas/c/muebles-para-cocinas"],
        "base_traffic": 82,
        "own_brand": 25.0,
        "country": "Colombia",
        "cities": [
            {"ciudad": "Bogotá", "es_costera": False, "humedad_relativa_promedio": 65},
            {"ciudad": "Medellín", "es_costera": False, "humedad_relativa_promedio": 68},
            {"ciudad": "Cali", "es_costera": False, "humedad_relativa_promedio": 70},
            {"ciudad": "Barranquilla", "es_costera": True, "humedad_relativa_promedio": 80}
        ],
        "best_sellers": ["Alacena de Cocina Corona", "Módulo de Baño suspendido Corona RH", "Módulo de Cocina Corona"],
        "future_sources": ["Corona Retail Analytics", "Google Analytics RTA (Tasa de rebote en categoría de cocinas modulares y descargas de instructivos de armado)"],
        "competitive_set": ["Sodimac", "Madecentro"],
        "jtbd": {
            "persona": "Maestro Especialista / Instalador",
            "job": "Instalar gabinetes de alta durabilidad en zonas expuestas a humedad, garantizando calidad al cliente final.",
            "pain_points": "Falsas promesas de resistencia al agua, herrajes que se oxidan en baños y cocinas costeras.",
            "triggers": "Contratos de remodelación comercial o residencial en zonas húmedas."
        },
        "raw_menu_categories": ["Muebles de Cocina - Modulares", "Muebles de Oficina y Escritorios RTA", "Alacenas y Organizadores", "Muebles de Lavandería y Baño RH"],
        "products": [
            {"name": "Alacena de Cocina Corona", "rh": False, "assembly": "minifix", "desc": "Alacena clásica de cocina"},
            {"name": "Módulo de Baño suspendido Corona RH", "rh": True, "assembly": "minifix", "desc": "Módulo de baño resistente a humedad"},
            {"name": "Módulo de Cocina Corona", "rh": False, "assembly": "minifix", "desc": "Cocina modulada de ensamble rápido"}
        ]
    },
    "CENCOSUD COLOMBIA SA": {
        "short_name": "Easy Colombia",
        "url_menu": "https://www.easy.com.co/muebles",
        "urls_ingesta": ["https://www.easy.com.co/muebles"],
        "base_traffic": 88,
        "own_brand": 30.0,
        "country": "Colombia",
        "cities": [
            {"ciudad": "Bogotá", "es_costera": False, "humedad_relativa_promedio": 65},
            {"ciudad": "Medellín", "es_costera": False, "humedad_relativa_promedio": 68},
            {"ciudad": "Cali", "es_costera": False, "humedad_relativa_promedio": 70}
        ],
        "best_sellers": ["Centro de TV Florencia Wengue", "Escritorio L-Shape Industrial Easy", "Módulo Cocina Aéreo Easy 100cm"],
        "future_sources": ["Easy Argentina/Chile (Surtido de Muebles RTA Krea)", "MercadoLibre Colombia (Precios de Centros de TV)", "Google Analytics RTA (Búsqueda interna de centros de TV y tasa de abandono en carritos de muebles de sala)"],
        "competitive_set": ["Sodimac", "Madecentro"],
        "jtbd": {
            "persona": "Comprador de Hogar de Clase Media",
            "job": "Encontrar un mueble de sala o estudio de buena apariencia que encaje exactamente en la sala de su apartamento sin gastar una fortuna.",
            "pain_points": "Falta de información clara sobre dimensiones en la web, retrasos en el despacho a domicilio.",
            "triggers": "Remodelación de la sala para recibir visitas de fin de año."
        },
        "raw_menu_categories": ["Centros de TV y Entretenimiento Easy", "Escritorios y Sillas de Oficina", "Muebles de Cocina y Comedor RTA"],
        "products": [
            {"name": "Centro de TV Florencia Wengue", "rh": False, "assembly": "estandar", "desc": "Estilo moderno melamínico"},
            {"name": "Escritorio L-Shape Industrial Easy", "rh": False, "assembly": "estandar", "desc": "Estructura metálica y MDP"},
            {"name": "Módulo Cocina Aéreo Easy 100cm", "rh": False, "assembly": "estandar", "desc": "MDP estándar"},
            {"name": "Mesa de Noche Krea 2 cajones", "rh": False, "assembly": "estandar", "desc": "Aglomerado básico"}
        ]
    },
    "PROMART HOMECENTER": {
        "short_name": "Promart",
        "url_menu": "https://www.promart.pe/muebles",
        "urls_ingesta": ["https://www.promart.pe/muebles"],
        "base_traffic": 83,
        "own_brand": 40.0,
        "country": "Perú",
        "cities": [
            {"ciudad": "Lima", "es_costera": True, "humedad_relativa_promedio": 85},
            {"ciudad": "Arequipa", "es_costera": False, "humedad_relativa_promedio": 45},
            {"ciudad": "Trujillo", "es_costera": True, "humedad_relativa_promedio": 80},
            {"ciudad": "Chiclayo", "es_costera": True, "humedad_relativa_promedio": 82}
        ],
        "best_sellers": ["Centro de TV Máncora Roble", "Escritorio Gamer Pro", "Alacena RTA Multifunción"],
        "future_sources": ["MercadoLibre Perú (Tendencias de Búsqueda)", "Promart Analytics (Ventas RTA)", "Google Analytics RTA (Tasa de rebote en cocinas modulares y descargas de instructivos)"],
        "competitive_set": ["Sodimac Perú", "IKEA USA"],
        "jtbd": {
            "persona": "Comprador Urbano Limeño",
            "job": "Optimizar el espacio en departamentos de metrajes reducidos en Lima Metropolitana de forma práctica.",
            "pain_points": "Humedad severa de la costa de Lima que infla los tableros aglomerados de baja densidad y herrajes deficientes.",
            "triggers": "Renovación de departamento de alquiler o mudanza a proyecto de vivienda VIS."
        },
        "raw_menu_categories": ["Muebles de Cocina - Modulares", "Escritorios y Oficina RTA", "Centros de TV y Entretenimiento", "Roperos y Clósets en Descuento", "Muebles de Baño RH Resistentes a Humedad"],
        "products": [
            {"name": "Centro de TV Máncora Roble", "rh": False, "assembly": "minifix", "desc": "Módulo de TV en melamina Rovere"},
            {"name": "Escritorio Gamer Pro", "rh": False, "assembly": "minifix", "desc": "Estructura gamer reforzada"},
            {"name": "Alacena RTA Multifunción", "rh": False, "assembly": "estandar", "desc": "Organizador modular estándar"},
            {"name": "Mueble Lavamanos Suspendido RH", "rh": True, "assembly": "minifix", "desc": "Melamina RH resistente a humedad"}
        ]
    },
    "SODIMAC PERÚ": {
        "short_name": "Sodimac Perú",
        "url_menu": "https://www.sodimac.com.pe",
        "urls_ingesta": ["https://www.sodimac.com.pe"],
        "base_traffic": 85,
        "own_brand": 38.0,
        "country": "Perú",
        "cities": [
            {"ciudad": "Lima", "es_costera": True, "humedad_relativa_promedio": 85},
            {"ciudad": "Arequipa", "es_costera": False, "humedad_relativa_promedio": 45},
            {"ciudad": "Trujillo", "es_costera": True, "humedad_relativa_promedio": 80}
        ],
        "best_sellers": ["Módulo Fregadero Sodimac Perú", "Escritorio Home Office Sodimac Perú", "Clóset RTA Sodimac Perú"],
        "future_sources": ["Sodimac Perú Analytics", "Google Analytics RTA (Tasa de rebote en cocinas modulares y descargas de instructivos de armado)"],
        "competitive_set": ["Promart", "IKEA USA"],
        "jtbd": {
            "persona": "Comprador Urbano Limeño",
            "job": "Optimizar el espacio en departamentos de metrajes reducidos en Lima Metropolitana de forma práctica.",
            "pain_points": "Humedad severa de la costa de Lima que infla los tableros aglomerados de baja densidad.",
            "triggers": "Mudanza o renovación estacional de cocina."
        },
        "raw_menu_categories": ["Muebles de Cocina - Modulares", "Escritorios y Oficina RTA", "Centros de TV y Entretenimiento", "Muebles de Baño RH Resistentes a Humedad"],
        "products": [
            {"name": "Módulo Fregadero Sodimac Perú", "rh": False, "assembly": "minifix", "desc": "Cocina modulada de ensamble rápido"},
            {"name": "Mueble de Baño Suspendido Sodimac Perú RH", "rh": True, "assembly": "minifix", "desc": "Módulo resistente a humedad"}
        ]
    },
    "TUHOME SPA": {
        "short_name": "TuHome",
        "url_menu": "https://www.tuhome.cl",
        "urls_ingesta": ["https://www.tuhome.cl"],
        "base_traffic": 80,
        "own_brand": 95.0,
        "country": "Chile",
        "cities": [
            {"ciudad": "Santiago", "es_costera": False, "humedad_relativa_promedio": 60},
            {"ciudad": "Concepción", "es_costera": False, "humedad_relativa_promedio": 75},
            {"ciudad": "Valparaíso", "es_costera": True, "humedad_relativa_promedio": 78},
            {"ciudad": "Antofagasta", "es_costera": True, "humedad_relativa_promedio": 72}
        ],
        "best_sellers": ["Escritorio Home Office Z-60 Nogal", "Mueble Lavamanos Split RH", "Clóset RTA 4 Puertas Wengue"],
        "future_sources": ["Falabella.com Chile (Surtido y Quiebres de Stock)", "MercadoLibre Chile (Palabras clave de Muebles)", "Google Analytics RTA (Porcentaje de abandono del checkout B2B y telemetría de visualización de clósets)"],
        "competitive_set": ["Sodimac Chile", "IKEA España"],
        "jtbd": {
            "persona": "Hogares en Crecimiento",
            "job": "Adaptar el mobiliario del hogar según el crecimiento de los hijos con soluciones modulares y escalables.",
            "pain_points": "Muebles pesados difíciles de mover, poca variedad en tonos de madera real, ensamble que requiere 2 personas.",
            "triggers": "Llegada de un nuevo hijo o reorganización de dormitorios."
        },
        "raw_menu_categories": ["Colección Cocina y Despensa Modulares", "Centros de Entretenimiento Modernos", "Línea Oficina y Escritorios RTA", "Muebles Auxiliares de Baño", "Novedades Diseño Industrial RTA"],
        "products": [
            {"name": "Escritorio Home Office Z-60 Nogal", "rh": False, "assembly": "minifix", "desc": "Ensamble rápido con minifix"},
            {"name": "Módulo de Cocina Auxiliar 2 Puertas", "rh": False, "assembly": "estandar", "desc": "Tablero estándar MDP"},
            {"name": "Mueble Lavamanos Split RH", "rh": True, "assembly": "minifix", "desc": "Base hidrófuga con herrajes rápidos"},
            {"name": "Clóset RTA 4 Puertas Wengue", "rh": False, "assembly": "estandar", "desc": "Estructura aglomerada de gran capacidad"}
        ]
    },
    "SODIMAC CHILE": {
        "short_name": "Sodimac Chile",
        "url_menu": "https://www.sodimac.cl",
        "urls_ingesta": ["https://www.sodimac.cl"],
        "base_traffic": 86,
        "own_brand": 40.0,
        "country": "Chile",
        "cities": [
            {"ciudad": "Santiago", "es_costera": False, "humedad_relativa_promedio": 60},
            {"ciudad": "Concepción", "es_costera": False, "humedad_relativa_promedio": 75},
            {"ciudad": "Valparaíso", "es_costera": True, "humedad_relativa_promedio": 78}
        ],
        "best_sellers": ["Módulo Cocina Modular 120cm", "Clóset RTA Expandible", "Escritorio Compacto Madera"],
        "future_sources": ["Falabella.com Chile (Surtido y Quiebres de Stock)", "Google Analytics RTA (Porcentaje de abandono del checkout B2B y telemetría de visualización de clósets)"],
        "competitive_set": ["TuHome", "IKEA España"],
        "jtbd": {
            "persona": "Hogares en Crecimiento",
            "job": "Adaptar el mobiliario del hogar según el crecimiento de los hijos con soluciones modulares y escalables.",
            "pain_points": "Muebles pesados difíciles de mover, poca variedad en tonos de madera real, ensamble que requiere 2 personas.",
            "triggers": "Llegada de un nuevo hijo o reorganización de dormitorios."
        },
        "raw_menu_categories": ["Colección Cocina y Despensa Modulares", "Centros de Entretenimiento Modernos", "Línea Oficina y Escritorios RTA", "Muebles Auxiliares de Baño", "Novedades Diseño Industrial RTA"],
        "products": [
            {"name": "Módulo Cocina Modular 120cm", "rh": False, "assembly": "minifix", "desc": "Ensamble rápido con minifix"},
            {"name": "Clóset RTA Expandible", "rh": False, "assembly": "estandar", "desc": "Tablero estándar MDP"},
            {"name": "Escritorio Compacto Madera", "rh": False, "assembly": "minifix", "desc": "Escritorio estudiantil simple"}
        ]
    },
    "LIVERPOOL MÉXICO": {
        "short_name": "Liverpool",
        "url_menu": "https://www.liverpool.com.mx",
        "urls_ingesta": ["https://www.liverpool.com.mx"],
        "base_traffic": 88,
        "own_brand": 15.0,
        "country": "México",
        "cities": [
            {"ciudad": "Ciudad de México", "es_costera": False, "humedad_relativa_promedio": 55},
            {"ciudad": "Monterrey", "es_costera": False, "humedad_relativa_promedio": 50},
            {"ciudad": "Guadalajara", "es_costera": False, "humedad_relativa_promedio": 58},
            {"ciudad": "Veracruz", "es_costera": True, "humedad_relativa_promedio": 78},
            {"ciudad": "Mérida", "es_costera": True, "humedad_relativa_promedio": 75}
        ],
        "best_sellers": ["Centro de TV Liverpool Maderado", "Escritorio Home Office Premium Liverpool", "Gabinete Baño Moderno Liverpool"],
        "future_sources": ["Liverpool Analytics (Ventas de Muebles)", "Google Analytics RTA (Tasa de conversión en el configurador de muebles modulares)"],
        "competitive_set": ["Elektra", "IKEA USA"],
        "jtbd": {
            "persona": "Comprador de Diseño Premium JtBD",
            "job": "Encontrar mobiliario estético, moderno y listo para llevar con acabados tipo madera natural.",
            "pain_points": "Precios elevados en mobiliario tradicional de madera maciza, dificultad de transporte.",
            "triggers": "Remodelación de sala o alcoba principal."
        },
        "raw_menu_categories": ["Centros de TV y Entretenimiento Liverpool", "Escritorios RTA Premium", "Organizadores de Baño y Hogar"],
        "products": [
            {"name": "Centro de TV Liverpool Maderado", "rh": False, "assembly": "minifix", "desc": "Estilo moderno melamínico"},
            {"name": "Gabinete Baño Moderno Liverpool", "rh": False, "assembly": "minifix", "desc": "MDP estándar"}
        ]
    },
    "ELEKTRA MÉXICO": {
        "short_name": "Elektra",
        "url_menu": "https://www.elektra.mx",
        "urls_ingesta": ["https://www.elektra.mx"],
        "base_traffic": 84,
        "own_brand": 25.0,
        "country": "México",
        "cities": [
            {"ciudad": "Ciudad de México", "es_costera": False, "humedad_relativa_promedio": 55},
            {"ciudad": "Monterrey", "es_costera": False, "humedad_relativa_promedio": 50},
            {"ciudad": "Guadalajara", "es_costera": False, "humedad_relativa_promedio": 58},
            {"ciudad": "Veracruz", "es_costera": True, "humedad_relativa_promedio": 78}
        ],
        "best_sellers": ["Clóset Básico Elektra", "Escritorio Home Office Elektra", "Centro de TV Compacto Elektra"],
        "future_sources": ["Elektra Sales Analytics", "Google Analytics RTA (Tasa de conversión en el configurador de muebles modulares)"],
        "competitive_set": ["Liverpool", "IKEA USA"],
        "jtbd": {
            "persona": "Smart Shopper / Comprador de Presupuesto",
            "job": "Encontrar mobiliario funcional, duradero y de bajo costo con facilidades de pago semanal o mensual.",
            "pain_points": "Falta de información sobre las dimensiones en la tienda física, transporte difícil.",
            "triggers": "Amoblar habitación infantil o estudio de bajo costo."
        },
        "raw_menu_categories": ["Centros de TV y Comedores Elektra", "Escritorios y Sillas RTA", "Roperos y Organizadores Económicos"],
        "products": [
            {"name": "Clóset Básico Elektra", "rh": False, "assembly": "estandar", "desc": "Aglomerado básico"},
            {"name": "Escritorio Home Office Elektra", "rh": False, "assembly": "minifix", "desc": "MDP estándar"}
        ]
    },
    "LEROY MERLIN ESPAÑA": {
        "short_name": "Leroy Merlin España",
        "url_menu": "https://www.leroymerlin.es",
        "urls_ingesta": ["https://www.leroymerlin.es"],
        "base_traffic": 87,
        "own_brand": 35.0,
        "country": "España",
        "cities": [
            {"ciudad": "Madrid", "es_costera": False, "humedad_relativa_promedio": 50},
            {"ciudad": "Barcelona", "es_costera": True, "humedad_relativa_promedio": 72},
            {"ciudad": "Valencia", "es_costera": True, "humedad_relativa_promedio": 70},
            {"ciudad": "Sevilla", "es_costera": False, "humedad_relativa_promedio": 55}
        ],
        "best_sellers": ["Armario RTA Modular Blanco", "Mueble Auxiliar de Cocina Haya", "Gabinete Suspendido de Baño RH"],
        "future_sources": ["Amazon España (Muebles más vendidos)", "Leroy Merlin Analytics (Consultas de Clientes)", "Google Analytics RTA (Tasa de rebote en armarios modulares y descargas de guías de montaje)"],
        "competitive_set": ["IKEA España", "IKEA USA"],
        "jtbd": {
            "persona": "Reformador DIY Español",
            "job": "Montar soluciones de almacenaje a medida en pisos urbanos optimizando cada metro cuadrado.",
            "pain_points": "Herrajes de baja calidad que se doblan, falta de resistencia a la humedad en baños de pisos costeros, instrucciones poco claras.",
            "triggers": "Renovación de armarios estacionales o mudanzas de verano."
        },
        "raw_menu_categories": ["Armarios y Clósets Modulares", "Muebles Auxiliares de Cocina", "Escritorios RTA de Oficina", "Muebles de Baño Suspendidos RH"],
        "products": [
            {"name": "Armario RTA Modular Blanco", "rh": False, "assembly": "estandar", "desc": "Estructura aglomerado melamina 16mm"},
            {"name": "Mueble Auxiliar de Cocina Haya", "rh": False, "assembly": "minifix", "desc": "Módulo con ruedas y estantes"},
            {"name": "Gabinete Suspendido de Baño RH", "rh": True, "assembly": "minifix", "desc": "Tablero hidrófugo resistente a la humedad"},
            {"name": "Escritorio Home Office Basic Haya", "rh": False, "assembly": "estandar", "desc": "Escritorio estándar aglomerado"}
        ]
    },
    "AMAZON USA": {
        "short_name": "Amazon USA",
        "url_menu": "https://www.amazon.com",
        "urls_ingesta": ["https://www.amazon.com"],
        "base_traffic": 96,
        "own_brand": 20.0,
        "country": "USA",
        "cities": [
            {"ciudad": "New York", "es_costera": True, "humedad_relativa_promedio": 68},
            {"ciudad": "Los Angeles", "es_costera": True, "humedad_relativa_promedio": 65},
            {"ciudad": "Miami", "es_costera": True, "humedad_relativa_promedio": 75},
            {"ciudad": "Chicago", "es_costera": False, "humedad_relativa_promedio": 62},
            {"ciudad": "Houston", "es_costera": True, "humedad_relativa_promedio": 74}
        ],
        "best_sellers": ["Amazon Basics Writing Desk", "Rustic Wood TV Stand Amazon", "3-Drawer Storage Drawer Organizer"],
        "future_sources": ["Amazon US Bestsellers", "Google Analytics RTA (Embudo de conversión de la línea Gamer y descargas de manuales)"],
        "competitive_set": ["Wayfair USA", "IKEA USA"],
        "jtbd": {
            "persona": "Comprador de Conveniencia Digital",
            "job": "Comprar mobiliario extremadamente económico con despacho prioritario de un día para otro.",
            "pain_points": "Calidad inconsistente del aglomerado, piezas rotas por transporte, falta de soporte técnico de armado.",
            "triggers": "Independencia estudiantil o armado rápido de oficina de teletrabajo."
        },
        "raw_menu_categories": ["Home Office Furniture Amazon", "Living Room TV Stands", "Bedroom Dressers & Organizers"],
        "products": [
            {"name": "Amazon Basics Writing Desk", "rh": False, "assembly": "click", "desc": "Simple writing table"},
            {"name": "Rustic Wood TV Stand Amazon", "rh": False, "assembly": "minifix", "desc": "MDP textured TV stand"}
        ]
    },
    "WALMART USA": {
        "short_name": "Walmart USA",
        "url_menu": "https://www.walmart.com",
        "urls_ingesta": ["https://www.walmart.com"],
        "base_traffic": 94,
        "own_brand": 25.0,
        "country": "USA",
        "cities": [
            {"ciudad": "New York", "es_costera": True, "humedad_relativa_promedio": 68},
            {"ciudad": "Los Angeles", "es_costera": True, "humedad_relativa_promedio": 65},
            {"ciudad": "Miami", "es_costera": True, "humedad_relativa_promedio": 75},
            {"ciudad": "Chicago", "es_costera": False, "humedad_relativa_promedio": 62},
            {"ciudad": "Houston", "es_costera": True, "humedad_relativa_promedio": 74}
        ],
        "best_sellers": ["Mainstays Writing Desk", "Mainstays 3-Drawer Dresser", "Mainstays Bathroom Cabinet RH"],
        "future_sources": ["Walmart Retail Analytics", "Google Analytics RTA (Tasa de rebote en cocinas modulares y descargas de instructivos)"],
        "competitive_set": ["Target", "IKEA USA"],
        "jtbd": {
            "persona": "Smart Shopper / Comprador de Presupuesto",
            "job": "Encontrar mobiliario básico de hogar para llevar en caja el mismo día al menor costo.",
            "pain_points": "Aglomerados débiles de 12mm que se cuelgan en el centro, herrajes plásticos frágiles.",
            "triggers": "Mudanza temporal o amoblado estudiantil."
        },
        "raw_menu_categories": ["Walmart Mainstays Home Office", "Walmart Bathroom Storage", "Walmart Bedroom Organizers"],
        "products": [
            {"name": "Mainstays Writing Desk", "rh": False, "assembly": "estandar", "desc": "Basic study desk"},
            {"name": "Mainstays Bathroom Cabinet RH", "rh": True, "assembly": "minifix", "desc": "RH particleboard cabinet"}
        ]
    },
    "WAYFAIR USA": {
        "short_name": "Wayfair USA",
        "url_menu": "https://www.wayfair.com",
        "urls_ingesta": ["https://www.wayfair.com"],
        "base_traffic": 92,
        "own_brand": 15.0,
        "country": "USA",
        "cities": [
            {"ciudad": "New York", "es_costera": True, "humedad_relativa_promedio": 68},
            {"ciudad": "Los Angeles", "es_costera": True, "humedad_relativa_promedio": 65},
            {"ciudad": "Miami", "es_costera": True, "humedad_relativa_promedio": 75},
            {"ciudad": "Chicago", "es_costera": False, "humedad_relativa_promedio": 62},
            {"ciudad": "Houston", "es_costera": True, "humedad_relativa_promedio": 74}
        ],
        "best_sellers": ["Modular Closet System White", "Minimalist TV Stand Oak", "RTA Writing Desk with Shelves"],
        "future_sources": ["Wayfair Business Analytics", "Google Analytics RTA (Embudo de conversión de la línea Gamer y descargas de manuales)"],
        "competitive_set": ["IKEA USA", "Amazon USA"],
        "jtbd": {
            "persona": "Young Urban Professional",
            "job": "Furnish rental apartments with stylish, affordable, and easy-to-move RTA furniture.",
            "pain_points": "Assembly taking too long, missing minor screws, particleboard cracking during screw insertion.",
            "triggers": "Moving to a new apartment, starting a remote job or college semester."
        },
        "raw_menu_categories": ["Modular Living Room Furniture", "Home Office Writing Desks", "Clóset & Wardrobe Organizers", "Bath Storage Cabinets"],
        "products": [
            {"name": "Modular Closet System White", "rh": False, "assembly": "minifix", "desc": "White melamine finish cabinet"},
            {"name": "Minimalist TV Stand Oak", "rh": False, "assembly": "minifix", "desc": "Oak textured media console"},
            {"name": "RTA Writing Desk with Shelves", "rh": False, "assembly": "click", "desc": "Tool-less quick assembly desk"},
            {"name": "Medicine Cabinet RH White", "rh": True, "assembly": "minifix", "desc": "RH particleboard bathroom storage"}
        ]
    },
    "HOME DEPOT USA": {
        "short_name": "Home Depot USA",
        "url_menu": "https://www.homedepot.com",
        "urls_ingesta": ["https://www.homedepot.com"],
        "base_traffic": 91,
        "own_brand": 30.0,
        "country": "USA",
        "cities": [
            {"ciudad": "New York", "es_costera": True, "humedad_relativa_promedio": 68},
            {"ciudad": "Los Angeles", "es_costera": True, "humedad_relativa_promedio": 65},
            {"ciudad": "Miami", "es_costera": True, "humedad_relativa_promedio": 75},
            {"ciudad": "Chicago", "es_costera": False, "humedad_relativa_promedio": 62},
            {"ciudad": "Houston", "es_costera": True, "humedad_relativa_promedio": 74}
        ],
        "best_sellers": ["Hampton Bay Kitchen Cabinet", "Hampton Bay Bath Vanity RH", "Hampton Bay Storage Closet"],
        "future_sources": ["Home Depot US Sales Analytics", "Google Analytics RTA (Tasa de rebote en cocinas modulares y descargas de instructivos de armado)"],
        "competitive_set": ["Lowe's USA", "IKEA USA"],
        "jtbd": {
            "persona": "Contratista / Dueño de Casa DIY",
            "job": "Instalar de manera rápida y económica organizadores en cocheras, cocinas y baños de alta durabilidad.",
            "pain_points": "Falta de herrajes en el empaque original, manuales de armado confusos e inestabilidad estructural.",
            "triggers": "Remodelación antes de la temporada de lluvias o mejoras previas a las vacaciones."
        },
        "raw_menu_categories": ["Home Depot Kitchen Cabinets", "Home Depot Office Furniture", "Home Depot Closet Organizers"],
        "products": [
            {"name": "Hampton Bay Kitchen Cabinet", "rh": False, "assembly": "minifix", "desc": "Modular wood composite kitchen cabinet"},
            {"name": "Hampton Bay Bath Vanity RH", "rh": True, "assembly": "minifix", "desc": "Water resistant bath cabinet"}
        ]
    },
    "LOWE'S USA": {
        "short_name": "Lowe's USA",
        "url_menu": "https://www.lowes.com",
        "urls_ingesta": ["https://www.lowes.com"],
        "base_traffic": 89,
        "own_brand": 28.0,
        "country": "USA",
        "cities": [
            {"ciudad": "New York", "es_costera": True, "humedad_relativa_promedio": 68},
            {"ciudad": "Los Angeles", "es_costera": True, "humedad_relativa_promedio": 65},
            {"ciudad": "Miami", "es_costera": True, "humedad_relativa_promedio": 75},
            {"ciudad": "Chicago", "es_costera": False, "humedad_relativa_promedio": 62},
            {"ciudad": "Houston", "es_costera": True, "humedad_relativa_promedio": 74}
        ],
        "best_sellers": ["Project Source Kitchen Cabinet", "Project Source Bath Vanity RH", "Project Source Storage Closet"],
        "future_sources": ["Lowe's US Sales Analytics", "Google Analytics RTA (Tasa de rebote en cocinas modulares y descargas de instructivos de armado)"],
        "competitive_set": ["Home Depot USA", "IKEA USA"],
        "jtbd": {
            "persona": "Contratista / Dueño de Casa DIY",
            "job": "Instalar de manera rápida y económica organizadores en cocheras, cocinas y baños de alta durabilidad.",
            "pain_points": "Falta de herrajes en el empaque original, manuales de armado confusos e inestabilidad estructural.",
            "triggers": "Remodelación antes de la temporada de lluvias o mejoras previas a las vacaciones."
        },
        "raw_menu_categories": ["Lowe's Kitchen Cabinets", "Lowe's Office Furniture", "Lowe's Closet Organizers"],
        "products": [
            {"name": "Project Source Kitchen Cabinet", "rh": False, "assembly": "minifix", "desc": "Modular composite kitchen cabinet"},
            {"name": "Project Source Bath Vanity RH", "rh": True, "assembly": "minifix", "desc": "Water resistant bath cabinet"}
        ]
    }
}

# --- PARTE 1: FUNCIONES DE FILTRADO Y PROCESAMIENTO ---

def clean_advertising_noise(category_list):
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
    readme_path = "README.md"
    
    content = []
    content.append("# 🏢 Inteligencia de Canales Digitales de Muebles RTA")
    content.append(f"\n> **Última actualización semanal:** {data['current_date']} | **Analista Principal:** Amelia RTA")
    content.append(f"\n**Tendencia Dominante de Mercado:** `{data['dominant_trend']}`")
    content.append(f"\n**Total Alertas de Oportunidad (Espacios en Blanco):** `{data['total_whitespaces']}`")
    
    content.append("\n## 📊 Resumen de Visualizaciones del Dashboard")
    content.append("- **Matriz de Ciclo de Vida de Tendencias:** Mapeo de categorías en fases de Introducción, Crecimiento, Madurez o Declive.")
    content.append("- **Tráfico Digital vs. Presencia de Marca Propia:** Comportamiento de penetración de marca propia en relación al volumen de tráfico digital.")
    content.append("\n*Para explorar las visualizaciones interactivas de Chart.js y aplicar filtros dinámicos por pestañas, abre el archivo [index.html](index.html) en tu navegador.*")
    
    content.append("\n---")
    content.append(f"\n## 🔍 Análisis Detallado por Cliente ({len(data['history'][data['current_date']]['clients'])} Canales)")
    
    for client in data["history"][data["current_date"]]["clients"]:
        telemetria = client["telemetria_mercado"]
        trends = client["analisis_predictivo_futuro"]["google_trends_keyword_trend"]
        brechas = client["brechas_detectadas_white_spaces"]
        
        content.append(f"\n### 🏢 {client['nombre_comercial']}")
        content.append(f"- **País:** {client['pais']}")
        content.append(f"- **Peso Estimado de Marca Propia:** `{telemetria['penetracion_marca_propia_percent']}%` | **Índice de Tráfico Digital:** `{telemetria['indice_trafico_digital']}/100`")
        content.append(f"- **Enfoque CDT Dominante:** *{telemetria['enfoque_cdt_dominante']}*")
        content.append(f"- **Palabras Clave Trends:** *{trends['keyword']} ({trends['crecimiento_trimestral_percent']}% de crecimiento)*")
        
        content.append("\n#### ⚠️ Alertas de Espacio en Blanco (Oportunidades de Catálogo)")
        has_gaps = False
        if brechas.get("deficit_hidrofugo_rh"):
            content.append("- **ALERTA:** Déficit de portafolio hidrófugo (RH) resistente a humedad en el catálogo.")
            has_gaps = True
        if brechas.get("deficit_ensamble_rapido"):
            content.append("- **ALERTA:** Déficit en sistemas de ensamble rápido (herrajes Click o Minifix).")
            has_gaps = True
        if brechas.get("riesgo_coastal_churn"):
            content.append("- **ALERTA:** Alto riesgo de churn comercial en zonas costeras por humedad severa sin portafolio adecuado.")
            has_gaps = True
        if not has_gaps:
            content.append("- *No se detectan alertas críticas en stock de tableros RH o ensamble rápido.*")
            
        content.append("\n---")
        
    content.append("\n## ⚙️ Arquitectura del Ecosistema Predictivo")
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

def generate_week_data_with_gemini(date_str, base_findings, api_key):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    
    system_instruction = """Actúa como AMELIA RTA, una Analista de Investigación de Mercado, Experta en Tendencias de Consumo y Especialista Senior en Auditoría de Canales Digitales y Category Management. Tu objetivo estratégico único es procesar datos de mercado, flujos de navegación e-commerce y estructuras de surtido para identificar patrones emergentes y brechas comerciales ("White Spaces") donde la empresa RTA MUEBLES pueda entrar y capturar mercado con un producto ganador de empaque plano (Ready-to-Assemble).

Tu universo de análisis se concentra de manera obligatoria en:
1. COLOMBIA: SODIMAC COLOMBIA S.A, MADECENTRO S.A.S, INVERSIONES VIRTUAL MUEBLES S.A.S, GRUPO CORONA Y ALIADOS, CENCOSUD COLOMBIA SA.
2. PERÚ: PROMART HOMECENTER, SODIMAC PERÚ.
3. CHILE: TUHOME SPA, SODIMAC CHILE.
4. MÉXICO: LIVERPOOL MÉXICO, ELEKTRA MÉXICO.
5. USA: AMAZON USA, WALMART USA, WAYFAIR USA, HOME DEPOT USA, LOWE'S USA.
6. ESPAÑA: LEROY MERLIN ESPAÑA.

Aplique el protocolo antirruido, aislando la estacionalidad del negocio estructural real de tableros y soluciones RTA. Usa JTBD y el ciclo de vida."""
    
    prompt = f"""
Genera los datos métricos y analíticos predictivos estructurales en formato JSON para la semana del '{date_str}'.

Aquí tienes los hallazgos estructurales del shelf digital y del comportamiento e-commerce recolectados por nuestro robot para esta semana:
{json.dumps(base_findings, indent=2, ensure_ascii=False)}

Debes tomar esta información (que contiene el tráfico de canal, el peso de marca propia, las categorías del menú de navegación y las brechas técnicas detectadas por defecto), relacionarla con la fecha de auditoría de acuerdo con tu rol y reglas de AMELIA RTA, y generar el objeto JSON final del reporte en la nueva estructura predictiva limpia.
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
      "canal_id": "slug_unico_del_canal (ej. sodimac_colombia, promart_peru, etc.)",
      "nombre_comercial": "Nombre del Retailer (ej. Sodimac Homecenter, Virtual Muebles, etc.)",
      "pais": "País (ej. Colombia, Chile, Perú, México, USA, España)",
      "urls_ingesta": ["Lista de URLs de ingesta"],
      "ciudades_cobertura": [
         {{"ciudad": "Nombre Ciudad", "es_costera": true o false, "humedad_relativa_promedio": número 0-100}}
      ],
      "telemetria_mercado": {{
         "indice_trafico_digital": número entero 10-100,
         "penetracion_marca_propia_percent": número flotante 0-100,
         "enfoque_cdt_dominante": "Técnico/Precio" o "Estética/Estilo",
         "lead_score_crm": número entero 0-100
      }},
      "analisis_predictivo_futuro": {{
         "google_trends_keyword_trend": {{
            "keyword": "Palabra clave de tendencia (ej. muebles de cocina rh)",
            "crecimiento_trimestral_percent": número 0-100,
            "pico_estacional_estimado": "Mes estimado del pico (ej. Octubre, Diciembre)"
         }},
         "google_analytics_nacional": {{
            "categoria_alta_intencion": "Categoría buscada (ej. Muebles de Baño)",
            "bounce_rate_zonas_costeras": número entero 0-100
         }}
      }},
      "brechas_detectadas_white_spaces": {{
         "deficit_hidrofugo_rh": true o false,
         "riesgo_coastal_churn": true o false,
         "deficit_ensamble_rapido": true o false
      }},
      "crm_sales_action": {{
         "arquetipo_buyer_persona": "Arquetipo (ej. Remodelador Práctico JtBD, Comprador Digital Joven JtBD)",
         "suggested_pitch": "Narrativa comercial personalizada y propuesta de valor"
      }}
    }}
  ]
}}

Nota sobre la semana del '{date_str}':
Deberás adaptar la información de todos los clientes para que refleje el tema de mercado correspondiente a esta fecha:
- Si es 2026-05-21: Preparativos pre-Cyber (demanda de Home Office, stock preventivo).
- Si es 2026-05-28: Pico CyberDay (demanda extrema gamer/oficina, quiebres de stock).
- Si es 2026-06-04: Lluvias costeras (demanda de tableros RH y muebles hidrófugos suspendidos, déficit de stock RH).
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
    # 1. GENERAR PRIMERO LOS HALLAZGOS Y DATOS BASE DEL SCRAPING E INGESTA (FILTRO 1)
    base_findings = []
    
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
        traffic = info["base_traffic"]
        if theme == "Pre-Cyber":
            if client_name in ["INVERSIONES VIRTUAL MUEBLES S.A.S", "SODIMAC COLOMBIA S.A", "CENCOSUD COLOMBIA SA"]:
                traffic += 3
        elif theme == "CyberDay-Peak":
            if client_name in ["INVERSIONES VIRTUAL MUEBLES S.A.S", "CENCOSUD COLOMBIA SA"]:
                traffic = 100
            else:
                traffic += 8
        elif theme == "Post-Cyber-Rain":
            traffic -= 5
        elif theme == "Fathers-Day":
            if client_name in ["INVERSIONES VIRTUAL MUEBLES S.A.S", "CENCOSUD COLOMBIA SA"]:
                traffic += 6
        elif theme == "Rainy-Season":
            if info["country"] == "Colombia":
                traffic += 2
        
        traffic = max(10, min(100, traffic + random.randint(-1, 1)))
        brand_weight = round(max(5.0, min(100.0, info["own_brand"] + random.uniform(-1.0, 1.0))), 1)
        cleaned_cats = clean_advertising_noise(info["raw_menu_categories"])
        
        cdt_focus, base_white_spaces = analyze_cdt_and_jtbd(client_name, cleaned_cats, info["products"])
        
        base_findings.append({
            "name": client_name,
            "country": info["country"],
            "cities": [c["ciudad"] for c in info["cities"]],
            "base_traffic_score": traffic,
            "own_brand_weight": brand_weight,
            "menu_hierarchy": cleaned_cats,
            "cdt_focus": cdt_focus,
            "default_detected_white_spaces": base_white_spaces,
            "target_persona": info["jtbd"]["persona"],
            "target_job": info["jtbd"]["job"]
        })

    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key:
        try:
            print(f"Detectada clave GEMINI_API_KEY. Intentando generar datos para {date_str} con el cerebro de Gemini...")
            data = generate_week_data_with_gemini(date_str, base_findings, api_key)
            if data and "clients" in data and len(data["clients"]) > 0:
                print(f"✅ Generación dinámica con la API de Gemini exitosa para la semana: {date_str}")
                return data
        except Exception as e:
            print(f"⚠️ Error al conectar con la API de Gemini: {e}. Usando generador lógico local de respaldo.")

    processed_clients = []
    total_whitespaces = 0

    for client_name, info in CLIENTS_RAW_DATA.items():
        traffic = info["base_traffic"]
        if theme == "Pre-Cyber":
            if client_name in ["INVERSIONES VIRTUAL MUEBLES S.A.S", "SODIMAC COLOMBIA S.A", "CENCOSUD COLOMBIA SA"]:
                traffic += 3
        elif theme == "CyberDay-Peak":
            if client_name in ["INVERSIONES VIRTUAL MUEBLES S.A.S", "CENCOSUD COLOMBIA SA"]:
                traffic = 100
            else:
                traffic += 8
        elif theme == "Post-Cyber-Rain":
            traffic -= 5
        elif theme == "Fathers-Day":
            if client_name in ["INVERSIONES VIRTUAL MUEBLES S.A.S", "CENCOSUD COLOMBIA SA"]:
                traffic += 6
        elif theme == "Rainy-Season":
            if info["country"] == "Colombia":
                traffic += 2
        
        traffic = max(10, min(100, traffic + random.randint(-1, 1)))
        brand_weight = round(max(5.0, min(100.0, info["own_brand"] + random.uniform(-1.0, 1.0))), 1)
        cleaned_cats = clean_advertising_noise(info["raw_menu_categories"])
        
        cdt_focus, base_white_spaces = analyze_cdt_and_jtbd(client_name, cleaned_cats, info["products"])
        
        white_spaces = list(base_white_spaces)
        
        if theme == "Pre-Cyber":
            white_spaces.append("Riesgo de desabastecimiento: bajo inventario preventivo de melaminas antes del evento CyberDay.")
        elif theme == "CyberDay-Peak":
            if client_name in ["INVERSIONES VIRTUAL MUEBLES S.A.S", "SODIMAC COLOMBIA S.A", "CENCOSUD COLOMBIA SA"]:
                white_spaces.append("Quiebre de stock critico en escritorios Home Office y Gamer debido a alta demanda CyberDay.")
            else:
                white_spaces.append("Brecha de visibilidad digital: Competencia acapara trafico publicitario con ofertas Cyber.")
        elif theme == "Post-Cyber-Rain":
            is_coastal = any(c["es_costera"] for c in info["cities"])
            if is_coastal:
                white_spaces.append("Deficit de portafolio hidrofugo (RH) en cocinas y banos expuestos a alta humedad y lluvias costeras.")
            else:
                white_spaces.append("Agotamiento general de stock de melamina estandar tras despacho de pedidos CyberDay.")
        elif theme == "Supply-Disruption":
            white_spaces.append("Quiebre de catalogo: Falta de melamina clara (Nordico/Rovere) por retrasos en puerto de importacion.")
        elif theme == "Fathers-Day":
            white_spaces.append("Falta de muebles de bar y centros de entretenimiento de gran formato (+65 pulgadas) en catalogo de temporada.")
        elif theme == "Mid-Year-Audit":
            white_spaces.append("Brecha de costos: Competencia local lanza linea economica de 12mm. Se requiere reduccion de espesor para competir.")
        elif theme == "Logistics-Rush":
            white_spaces.append("Brecha de entrega: Sobrecupo logistico retrasa entregas de gran formato. Se requieren embalajes planos ultra-optimizados.")
        elif theme == "Rainy-Season":
            white_spaces.append("Agotamiento de inventario de melamina hidrofuga (MDP-RH) ante la aceleracion de lluvias de la temporada.")

        deficit_hidrofugo_rh = any("hidrófugo" in ws.lower() or "rh" in ws.lower() or "hidrofugo" in ws.lower() for ws in white_spaces)
        deficit_ensamble_rapido = any("ensamble rápido" in ws.lower() or "click" in ws.lower() or "minifix" in ws.lower() or "ensamble rapido" in ws.lower() for ws in white_spaces)
        is_coastal = any(city["es_costera"] for city in info["cities"])
        riesgo_coastal_churn = is_coastal and deficit_hidrofugo_rh
        
        if deficit_hidrofugo_rh or riesgo_coastal_churn:
            total_whitespaces += 1

        whitespaces_count = len(white_spaces)
        lead_score = int((traffic * (100 - brand_weight) * (whitespaces_count + 1)) / 150)
        lead_score = min(100, max(0, lead_score))
        
        has_rh_gap = deficit_hidrofugo_rh
        has_assembly_gap = deficit_ensamble_rapido
        has_stockout_gap = any("desabastecimiento" in ws.lower() or "quiebre de stock" in ws.lower() for ws in white_spaces)
        has_supply_gap = any("puerto" in ws.lower() or "importacion" in ws.lower() for ws in white_spaces)
        has_price_gap = any("costos" in ws.lower() or "precio" in ws.lower() for ws in white_spaces)
        has_logistics_gap = any("logistico" in ws.lower() or "entrega" in ws.lower() for ws in white_spaces)
        
        if has_stockout_gap:
            suggested_pitch = "Presentar planes de abastecimiento de contingencia para alta demanda digital"
        elif has_supply_gap:
            suggested_pitch = "Ofrecer paleta de acabados alternativos de entrega rapida (Wengue y Blanco)"
        elif has_rh_gap:
            suggested_pitch = "Ofrecer portafolio MDP-RH y Melamina Anti-humedad para Cocina/Bano"
        elif has_price_gap:
            suggested_pitch = "Presentar optimizacion de espesores MDP estandar de 12mm/15mm para bajo costo"
        elif has_logistics_gap:
            suggested_pitch = "Proponer empaque modular plano super-optimizado para fletes B2B"
        elif has_assembly_gap:
            suggested_pitch = "Promocionar sistemas Click de Ensamble Rapido sin tornillos"
        elif "Benefit" in cdt_focus:
            suggested_pitch = "Presentar optimizacion de espesores MDP estandar para alto volumen"
        else:
            suggested_pitch = "Presentar nuevos acabados esteticos de tendencia (Nordico, Rovere y Wengue)"
            
        keyword = "muebles de cocina"
        if has_rh_gap:
            keyword = "muebles de cocina rh"
        elif has_assembly_gap:
            keyword = "muebles click armar"
            
        growth = random.randint(18, 42)
        pico = random.choice(["Octubre", "Noviembre", "Diciembre"])
        
                # Clean up client_name to get canal_id
        canal_id = client_name.lower().replace(" s.a.s", "").replace(" s.a.", "").replace(" s.a.s.", "").replace(" s.a", "").replace(" spa", "").replace(" y aliados", "").replace(" ", "_")
        # Map cleanly:
        if "sodimac_colombia" in canal_id:
            canal_id = "sodimac_colombia"
        elif "madecentro" in canal_id:
            canal_id = "madecentro_colombia"
        elif "virtual" in canal_id:
            canal_id = "virtual_muebles"
        elif "corona" in canal_id:
            canal_id = "corona_colombia"
        elif "cencosud" in canal_id:
            canal_id = "easy_colombia"
        elif "promart" in canal_id:
            canal_id = "promart_peru"
        elif "sodimac_per" in canal_id:
            canal_id = "sodimac_peru"
        elif "tuhome" in canal_id:
            canal_id = "tuhome_chile"
        elif "sodimac_chile" in canal_id:
            canal_id = "sodimac_chile"
        elif "liverpool" in canal_id:
            canal_id = "liverpool_mexico"
        elif "elektra" in canal_id:
            canal_id = "elektra_mexico"
        elif "leroy" in canal_id:
            canal_id = "leroy_merlin_espana"
        elif "amazon" in canal_id:
            canal_id = "amazon_usa"
        elif "walmart" in canal_id:
            canal_id = "walmart_usa"
        elif "wayfair" in canal_id:
            canal_id = "wayfair_usa"
        elif "home_depot" in canal_id or "homedepot" in canal_id:
            canal_id = "homedepot_usa"
        elif "lowe" in canal_id:
            canal_id = "lowes_usa"

        processed_clients.append({
            "canal_id": canal_id,
            "nombre_comercial": info["short_name"],
            "pais": info["country"],
            "urls_ingesta": info["urls_ingesta"],
            "ciudades_cobertura": info["cities"],
            "telemetria_mercado": {
                "indice_trafico_digital": traffic,
                "penetracion_marca_propia_percent": brand_weight,
                "enfoque_cdt_dominante": "Técnico/Precio" if "Benefit" in cdt_focus else "Estética/Estilo",
                "lead_score_crm": lead_score
            },
            "analisis_predictivo_futuro": {
                "google_trends_keyword_trend": {
                    "keyword": keyword,
                    "crecimiento_trimestral_percent": growth,
                    "pico_estacional_estimado": pico
                },
                "google_analytics_nacional": {
                    "categoria_alta_intencion": "Muebles de Baño" if has_rh_gap else "Muebles de Cocina",
                    "bounce_rate_zonas_costeras": random.randint(45, 88)
                }
            },
            "brechas_detectadas_white_spaces": {
                "deficit_hidrofugo_rh": deficit_hidrofugo_rh,
                "riesgo_coastal_churn": riesgo_coastal_churn,
                "deficit_ensamble_rapido": deficit_ensamble_rapido
            },
            "crm_sales_action": {
                "arquetipo_buyer_persona": info["jtbd"]["persona"],
                "suggested_pitch": f"Detectamos que el interés en {info['country']} por {keyword} creció un {growth}%. Tu catálogo actual tiene un déficit del {random.randint(65, 88)}% en esa zona. Te proponemos nuestra línea modular..."
            },
            
            # Retrocompatibilidad y metadatos estáticos requeridos por el front
            "best_sellers": info["best_sellers"],
            "future_sources": info["future_sources"],
            "menu_hierarchy": cleaned_cats,
            "competitive_set": info["competitive_set"],
            "cdt_tree": [
                "1. Dimensiones y espacio disponible (Filtro numérico)",
                "2. Resistencia del material (Aglomerado estándar vs Tablero RH)",
                "3. Relación precio-capacidad de almacenado"
            ] if "Benefit" in cdt_focus else [
                "1. Combinación de colores y estilo estético (Nórdico, Rovere, Wengue)",
                "2. Tipo de ensamble visual (Flotante, patas de madera)",
                "3. Calificaciones de diseño y reviews en web"
            ],
            # Aliases para retrocompatibilidad total del JSON
            "name": client_name,
            "country": info["country"],
            "cities": [c["ciudad"] for c in info["cities"]],
            "white_spaces": white_spaces,
            "cdt_focus": cdt_focus,
            "own_brand_weight": brand_weight,
            "traffic_score": traffic,
            "crm_lead_score": lead_score,
            "crm_suggested_pitch": suggested_pitch,
            "crm_next_action": f"Agendar reunión técnica con el equipo de compras para presentar nuestra propuesta B2B para resolver {keyword}."
        })
        
    dominant_trend = "Benefit-Driven (RH & Ensamble)" if total_whitespaces > 6 else "Design-Driven (Estetica & Estilos)"
    
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


def transform_old_history_to_new(history):
    new_history = {}
    for week_date, week_data in history.items():
        if "clients" not in week_data:
            continue
        new_clients = []
        for c in week_data["clients"]:
            if "canal_id" in c:
                new_clients.append(c)
                continue
                
            name = c.get("name", "")
            country = c.get("country", "")
            
            canal_id = name.lower().replace(" s.a.", "").replace(" s.a.s.", "").replace(" s.a", "").replace(" s.a.s", "").replace(" spa", "").replace(" y aliados", "").replace(" ", "_")
            if "virtual" in canal_id:
                canal_id = "virtual_muebles"
            elif "sodimac_colombia" in canal_id:
                canal_id = "sodimac_colombia"
            elif "madecentro" in canal_id:
                canal_id = "madecentro_colombia"
            elif "cencosud" in canal_id:
                canal_id = "easy_colombia"
            elif "promart" in canal_id:
                canal_id = "promart_peru"
            elif "home_depot" in canal_id:
                canal_id = "homedepot_mexico"
            elif "wayfair" in canal_id:
                canal_id = "wayfair_usa"
            elif "leroy" in canal_id:
                if "espejo" in name.lower() or "internacional" in name.lower():
                    canal_id = "leroy_merlin_espejo_internacional"
                else:
                    canal_id = "leroy_merlin_espana"
            elif "tuhome" in canal_id:
                canal_id = "tuhome_chile"
            elif "sodimac_chile" in canal_id:
                canal_id = "sodimac_chile"
                
            if canal_id in ["exito", "novaventa", "mobbly", "ferreteria_epa", "epa"]:
                continue
                
            cities_raw = c.get("cities", [])
            coastal_cities = ["barranquilla", "cartagena", "valparaiso", "antofagasta", "lima", "trujillo", "chiclayo", "veracruz", "merida", "miami", "los angeles", "new york", "barcelona", "valencia"]
            ciudades_cobertura = []
            for city in cities_raw:
                is_coastal = any(cc in city.lower() for cc in coastal_cities)
                humedad = 80 if is_coastal else 60
                if "lima" in city.lower():
                    humedad = 85
                elif "arequipa" in city.lower():
                    humedad = 45
                ciudades_cobertura.append({
                    "ciudad": city,
                    "es_costera": is_coastal,
                    "humedad_relativa_promedio": humedad
                })
                
            ws_list = c.get("white_spaces", [])
            deficit_rh = any("hidrófugo" in ws.lower() or "rh" in ws.lower() or "hidrofugo" in ws.lower() for ws in ws_list)
            deficit_ensamble = any("ensamble rápido" in ws.lower() or "click" in ws.lower() or "minifix" in ws.lower() or "ensamble rapido" in ws.lower() for ws in ws_list)
            is_coastal = any(city["es_costera"] for city in ciudades_cobertura)
            coastal_churn = is_coastal and deficit_rh
            
            telemetria = {
                "indice_trafico_digital": c.get("traffic_score", 50),
                "penetracion_marca_propia_percent": c.get("own_brand_weight", 30),
                "enfoque_cdt_dominante": "Técnico/Precio" if "benefit" in c.get("cdt_focus", "").lower() else "Estética/Estilo",
                "lead_score_crm": c.get("crm_lead_score", 50)
            }
            
            trends_keyword = "muebles de cocina"
            if deficit_rh:
                trends_keyword = "muebles de cocina rh"
            elif deficit_ensamble:
                trends_keyword = "muebles click armar"
                
            predictivo = {
                "google_trends_keyword_trend": {
                    "keyword": trends_keyword,
                    "crecimiento_trimestral_percent": random.randint(15, 45),
                    "pico_estacional_estimado": random.choice(["Octubre", "Noviembre", "Diciembre"])
                },
                "google_analytics_nacional": {
                    "categoria_alta_intencion": "Muebles de Cocina" if deficit_rh else "Muebles de Sala",
                    "bounce_rate_zonas_costeras": 82 if is_coastal else 50
                }
            }
            
            sales_action = {
                "arquetipo_buyer_persona": c.get("jtbd", {}).get("persona", "Remodelador Práctico JtBD"),
                "suggested_pitch": c.get("crm_suggested_pitch", "")
            }
            if not sales_action["suggested_pitch"]:
                sales_action["suggested_pitch"] = f"Proponer nuestro portafolio de {trends_keyword} para solucionar sus brechas de catálogo B2B."
                
            urls = c.get("urls_ingesta", [c.get("url_menu", "https://example.com")])
            if not urls or not urls[0]:
                urls = ["https://example.com"]
                
            new_clients.append({
                "canal_id": canal_id,
                "nombre_comercial": name,
                "pais": country,
                "urls_ingesta": urls,
                "ciudades_cobertura": ciudades_cobertura,
                "telemetria_mercado": telemetria,
                "analisis_predictivo_futuro": predictivo,
                "brechas_detectadas_white_spaces": {
                    "deficit_hidrofugo_rh": deficit_rh,
                    "riesgo_coastal_churn": coastal_churn,
                    "deficit_ensamble_rapido": deficit_ensamble
                },
                "crm_sales_action": sales_action,
                
                # Retrocompatibilidad
                "best_sellers": c.get("best_sellers", []),
                "future_sources": c.get("future_sources", []),
                "menu_hierarchy": c.get("menu_hierarchy", []),
                "competitive_set": c.get("competitive_set", []),
                "cdt_tree": c.get("cdt_tree", []),
                "name": name,
                "country": country,
                "cities": cities_raw,
                "white_spaces": ws_list,
                "cdt_focus": c.get("cdt_focus", ""),
                "own_brand_weight": c.get("own_brand_weight", 30),
                "traffic_score": c.get("traffic_score", 50),
                "crm_lead_score": c.get("crm_lead_score", 50),
                "crm_suggested_pitch": c.get("crm_suggested_pitch", ""),
                "crm_next_action": c.get("crm_next_action", "")
            })
            
        new_history[week_date] = {
            "dominant_trend": week_data.get("dominant_trend", "Benefit-Driven (RH & Ensamble)"),
            "total_whitespaces": len([cl for cl in new_clients if any(cl["brechas_detectadas_white_spaces"].values())]),
            "trends": week_data.get("trends", []),
            "clients": new_clients
        }
    return new_history


def main():
    print("Iniciando actualización semanal de Inteligencia RTA...")
    today_str = datetime.utcnow().strftime("%Y-%m-%d")
    
    history = {}
    if os.path.exists("data.json"):
        try:
            with open("data.json", "r", encoding="utf-8") as f:
                old_data = json.load(f)
                if "history" in old_data:
                    raw_history = old_data["history"]
                    history = transform_old_history_to_new(raw_history)
        except Exception as e:
            print("No se pudo cargar el historial anterior, se creará uno nuevo:", e)

    from datetime import datetime, timedelta
    if history:
        sorted_dates = sorted(history.keys())
        last_date_str = sorted_dates[-1]
        try:
            last_date = datetime.strptime(last_date_str, "%Y-%m-%d")
            today = datetime.strptime(today_str, "%Y-%m-%d")
            
            current_date = last_date + timedelta(days=7)
            while current_date <= today:
                current_date_str = current_date.strftime("%Y-%m-%d")
                if current_date_str not in history:
                    print(f"Rellenando semana faltante en historial: {current_date_str}")
                    history[current_date_str] = generate_week_data(current_date_str)
                current_date += timedelta(days=7)
        except Exception as ex:
            print(f"Error al calcular fechas faltantes: {ex}")
            
    if today_str not in history:
        print(f"Generando datos para la semana actual: {today_str}")
        history[today_str] = generate_week_data(today_str)
    
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
