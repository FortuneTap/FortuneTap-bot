from fastapi import FastAPI
from playwright.async_api import async_playwright

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to Playwright Scraper on Railway"}

@app.get("/scrape")
async def scrape(url: str):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url)
        content = await page.content()
        await browser.close()
    return {"content": content}