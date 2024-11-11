from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_rendered_html(url):
    """Usa Selenium para obtener el HTML renderizado de una página."""
    # Configuración del navegador con Selenium
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Ejecutar en modo headless
    browser = webdriver.Chrome(options=options)

    # Navegar a la URL
    browser.get(url)

    # Esperar hasta que el nombre del personaje esté visible en la página
    WebDriverWait(browser, 30).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#sheet-desktop-header > div.MuiGrid-root.MuiGrid-container.MuiGrid-item.MuiGrid-grid-xs-6.grid-block.header-character-container.css-yjeeko > div.MuiGrid-root.MuiGrid-container.MuiGrid-item.grid-block.header-character-name-container.css-jjdzd4 > div:nth-child(1) > div.MuiGrid-root.MuiGrid-item.text-block.character-name.css-1ipveys"))
    )

    # Obtener el contenido HTML de la página después de la carga completa
    html_content = browser.page_source
    browser.quit()
    
    return html_content

def import_character_data(url):
    """Función que obtiene y parsea los datos del personaje desde Demiplane usando XPath."""
    html_content = get_rendered_html(url)
    tree = etree.HTML(html_content)

    # Diccionario para almacenar los datos del personaje
    character_data = {
        "attributes": {},
        "skills": {}
    }

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
        character_data["attributes"][attr] = result[0].strip() if result else "N/A"

    # Extraer habilidades (skills) usando XPath
    skill_rows = tree.xpath("//div[contains(@class, 'skill-row')]")
    for row in skill_rows:
        skill_name = row.xpath(".//div[contains(@class, 'skill-name')]/text()")
        skill_value = row.xpath(".//div[contains(@class, 'skill-modifier')]/text()")
        if skill_name and skill_value:
            character_data["skills"][skill_name[0].strip()] = skill_value[0].strip()

    return character_data
