from playwright.sync_api import Page, expect


# Responsável: Gabriel Lessa Tramasol Machado
def test_alterna_entre_formularios_de_entrada_e_cadastro(page: Page):
    page.goto("https://local-eats-unisenac.vercel.app/")

    entrada = page.locator("#loginForm")
    cadastro = page.locator("#registerForm")
    expect(entrada).to_be_visible()

    page.get_by_role("button", name="Criar Conta", exact=True).click()

    expect(cadastro.get_by_role("button", name="Registrar", exact=True)).to_be_visible()
    expect(entrada).to_be_hidden()

    page.locator("#showLoginBtn").click()

    expect(entrada.get_by_role("button", name="Entrar", exact=True)).to_be_visible()
    expect(cadastro).to_be_hidden()
