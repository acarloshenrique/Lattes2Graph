import asyncio
from playwright.async_api import async_playwright

async def get_lattes_basic_info(lattes_id):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        
        # URL base de currículos públicos
        url = f"http://lattes.cnpq.br/{lattes_id}"
        
        print(f"Buscando dados do ID: {lattes_id}...")
        try:
            await page.goto(url, timeout=30000)

            # Extração de campos fundamentais com tratamento de falhas
            try:
                nome = await page.inner_text('h2.nome', timeout=5000)
                nome = nome.strip()
            except Exception:
                print(f"Aviso: Nome não encontrado para o ID {lattes_id}")
                nome = "Nome não encontrado"

            try:
                resumo = await page.inner_text('p.resumo', timeout=5000)
                resumo = resumo.strip()[:200] + "..." # Para o "tooltip" do grafo
            except Exception:
                print(f"Aviso: Resumo não encontrado para o ID {lattes_id}")
                resumo = "Resumo não encontrado"

            # Exemplo de captura de produções (simplificado)
            try:
                producoes = await page.locator('.artigo-completo').count()
            except Exception:
                print(f"Aviso: Não foi possível contar produções para o ID {lattes_id}")
                producoes = 0

            data = {
                "id": lattes_id,
                "nome": nome,
                "resumo": resumo,
                "total_artigos": producoes
            }
        except Exception as e:
            print(f"Erro ao carregar a página para o ID {lattes_id}: {e}")
            data = {
                "id": lattes_id,
                "nome": "Erro ao carregar",
                "resumo": "Erro ao carregar",
                "total_artigos": 0
            }

        await browser.close()
        return data

# Teste rápido
if __name__ == "__main__":
    # Exemplo com um ID (substitua por um ID real para testar)
    sample_id = "0000000000000000" 
    result = asyncio.run(get_lattes_basic_info(sample_id))
    print(result)
