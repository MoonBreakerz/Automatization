describe("Funcionalidade: Filtrar produtos por preço", () => {
  before(() => {
    cy.visit("https://www.saucedemo.com/");
    cy.get("#user-name").type("standard_user");
    cy.get("#password").type("secret_sauce");
    cy.get("#login-button").click();
    cy.url().should("include", "inventory.html");
  });

  it("Cenário: Filtrar produtos pelo preço mais baixo", () => {
    cy.get(".product_sort_container").select("lohi");

    cy.get(".inventory_item_price").then((precos) => {
      const precosDosProdutos = Array.from(precos).map((el) =>
        parseFloat(el.textContent.replace("$", ""))
      );

      const produtosOrdenados = [...precosDosProdutos].sort((a, b) => a - b);
      expect(precosDosProdutos).to.deep.equal(produtosOrdenados);
    });
  });

  it("Cenário: Filtrar produtos pelo preço mais alto", () => {
    cy.get(".product_sort_container").select("hilo");
    cy.get(".inventory_item_price").then((precos) => {
      const precosDosProdutos = Array.from(precos).map((el) =>
        parseFloat(el.textContent.replace("$", ""))
      );

      const produtosOrdenados = [...precosDosProdutos].sort((a, b) => b - a);
      expect(precosDosProdutos).to.deep.equal(produtosOrdenados);
    });
  });
});
