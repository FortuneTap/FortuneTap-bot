from lxml import etree
from playwright.async_api import async_playwright
from domain.character import Character

async def get_rendered_html(url):
    """Usa Playwright para obtener el HTML renderizado de una página."""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url)
        
        # Esperar hasta que el nombre del personaje esté visible en la página
        await page.wait_for_selector("#sheet-desktop-header > div.MuiGrid-root.MuiGrid-container.MuiGrid-item.MuiGrid-grid-xs-6.grid-block.header-character-container.css-yjeeko > div.MuiGrid-root.MuiGrid-container.MuiGrid-item.grid-block.header-character-name-container.css-jjdzd4 > div:nth-child(1) > div.MuiGrid-root.MuiGrid-item.text-block.character-name.css-1ipveys", timeout=30000)
        
        # Obtener el contenido HTML de la página después de la carga completa
        html_content = await page.content()
        await browser.close()
        
        return html_content

async def import_character_data(url):
    """Función que obtiene y parsea los datos del personaje desde Demiplane usando XPath."""
    html_content = await get_rendered_html(url)
    tree = etree.HTML(html_content)

    # Extraer el nombre del personaje (adaptar XPath si es necesario)
    name = tree.xpath("//div[contains(@class, 'character-name')]/text()")
    name = name[0].strip() if name else "Unknown Character"

    # Diccionario para almacenar los datos del personaje
    attributes = {}
    skills = {}

    # Diccionario de rutas XPath para cada atributo
    attribute_xpaths = {
        "strength": "//div[contains(@class, 'attribute-box-strength')]//div[contains(@class, 'attribute-value') and contains(@class, 'text-block__text')]/text()",
        "speed": "//div[contains(@class, 'attribute-box-speed')]//div[contains(@class, 'attribute-value') and contains(@class, 'text-block__text')]/text()",
        "defense_physical": "//div[contains(@class, 'defense-box-physical')]//div[contains(@class, 'defense-value') and contains(@class, 'text-block__text')]/text()",
        "defense_cognitive": "//div[contains(@class, 'defense-box-cognitive')]//div[contains(@class, 'defense-value') and contains(@class, 'text-block__text')]/text()",
        "defense_spiritual": "//div[contains(@class, 'defense-box-spiritual')]//div[contains(@class, 'defense-value') and contains(@class, 'text-block__text')]/text()",
        "movement": "//div[contains(@class, 'statistic-box--movement')]//div[contains(@class, 'statistic-value')]/text()",
        "recovery_die": "//div[contains(@class, 'statistic-box--recovery-die')]//div[contains(@class, 'statistic-value')]/text()",
        "senses_range": "//div[contains(@class, 'statistic-box--senses-range')]//div[contains(@class, 'statistic-value')]/text()",
        "health": "//div[contains(@class, 'max-hit-point-indicator')]/text()",
        "focus": "//div[contains(@class, 'resource-box-focus')]//div[contains(@class, 'resource-max') and contains(@class, 'text-block__text')]/text()",
        "investiture": "//div[contains(@class, 'resource-box-investiture')]//div[contains(@class, 'resource-max') and contains(@class, 'text-block__text')]/text()"
    }

    # Extraer y almacenar cada atributo usando XPath
    for attr, path in attribute_xpaths.items():
        result = tree.xpath(path)
        attributes[attr] = result[0].strip() if result else "N/A"

    # Extraer habilidades (skills) usando XPath
    skill_rows = tree.xpath("//div[contains(@class, 'skill-row')]")
    for row in skill_rows:
        skill_name = row.xpath(".//div[contains(@class, 'skill-name')]/text()")
        skill_value = row.xpath(".//div[contains(@class, 'skill-modifier')]/text()")
        if skill_name and skill_value:
            skills[skill_name[0].strip()] = skill_value[0].strip()

    character = Character(name=name, attributes=attributes, skills=skills)
    return character
