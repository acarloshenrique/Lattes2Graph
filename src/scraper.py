import asyncio
from playwright.async_api import async_playwright

async def get_lattes_basic_info(lattes_id):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_context().new_page()
        
        # URL base de currículos públicos
        url = f"http://lattes.cnpq.br/{lattes_id}"
        
        print(f"Buscando dados do ID: {lattes_id}...")
        await page.goto(url)
        
        # Extração de campos fundamentais para a ontologia
        nome = await page.inner_text('h2.nome')
        resumo = await page.inner_text('p.resumo')
        
        # Exemplo de captura de produções (simplificado)
        producoes = await page.locator('.artigo-completo').count()

        data = {
            "id": lattes_id,
            "nome": nome.strip(),
            "resumo": resumo.strip()[:200] + "...", # Para o "tooltip" do grafo
            "total_artigos": producoes
        }

        await browser.close()
        return data

# Teste rápido
if __name__ == "__main__":
    # Exemplo com um ID (substitua por um ID real para testar)
    sample_id = "0000000000000000" 
    result = asyncio.run(get_lattes_basic_info(sample_id))
    print(result)
