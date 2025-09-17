# Localización Venezolana para Odoo - Módulos de Integración de Datos

![Versión de Odoo](https://img.shields.io/badge/Odoo-18.0-blueviolet)
![Versión de Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Licencia](https://img.shields.io/badge/licencia-GPL--3-green.svg)

## Introducción

En el contexto venezolano, la validación y obtención de datos fiscales y de identidad de ciudadanos o empresas es un proceso manual y propenso a errores. Este proyecto nace para solucionar ese problema creando un ecosistema de módulos para Odoo 18 que **construyen y exponen una API local** para consultar información de ciudadanos venezolanos, utilizando una base de datos offline del CNE.

El objetivo es simple: **eficiencia, precisión y autonomía.** Al introducir una Cédula de Identidad en Odoo, los datos del contacto se autocompletan de forma instantánea, segura y sin depender de servicios externos inestables.

<!-- ### ¡En Acción!

**[GRABAR Y AÑADIR UN GIF AQUÍ]**

*   **Paso 1:** Ve a la sección "Releases" de este repositorio y sube un video corto (`.mp4` o `.mov`) mostrando el módulo en acción.
*   **Paso 2:** Copia el link y pégalo aquí para que se vea una vista previa del video.
*   **Opcional:** Usa una herramienta como "ScreenToGif" para grabar un GIF rápido del `onchange` funcionando y pégalo aquí. ¡Es la forma más efectiva de mostrar tu trabajo!
-->

---
### Componentes del Ecosistema

| Módulo | Responsabilidad Principal | Estado Actual |
| :--- | :--- | :--- |
| **`l10n_ve_data_cne`** | Almacena la base de datos de ciudadanos (CNE) y sus modelos relacionados (estados, municipios, etc.). | 🚧 En Desarrollo |
| **`l10n_ve_api_provider`**| Expone un `controller` para crear una API RESTful (`/api/v1/persona/...`) que consulta la base de datos local. | 📝 Planificado |
| **`l10n_ve_res_partner_seniat`**| Hereda `res.partner` para añadir el `onchange` que consume nuestra API local y autocompleta los datos. | 🚀 Funcional (Enfocado ahora en datos locales) |

---

## Instalación

1.  Clonar el repositorio en tu carpeta de `addons` de Odoo:
    ```bash
    git clone https://github.com/zerodaty/l10n_ve_integration_seniat.git
    ```
2.  Asegurarte de que la ruta a esta carpeta esté en tu `addons_path` del archivo `odoo.conf`.
3.  Reiniciar el servicio de Odoo.
4.  Ir al menú de `Apps`, buscar y instalar los módulos deseados (empezando por `l10n_ve_data_cne`).

---

## Autor

*   **Frany Velásquez**
*   **GitHub:** [@zerodaty](https://github.com/zerodaty)
*   **LinkedIn:** [https://www.linkedin.com/in/franyvelas/]
