describe("Funcionalidade: Adicionar e excluir produtos do carrinho", () => {
  before(() => {
    cy.visit("https://www.saucedemo.com/");
    cy.get("#user-name").type("standard_user");
    cy.get("#password").type("secret_sauce");
    cy.get("#login-button").click();
    cy.url().should("include", "inventory.html");
  });
  
  it("Cenário: Adicionar todos os produtos ao carrinho e excluir os dois de menores valores", () => {
    cy.visit("https://www.saucedemo.com/inventory.html");
    cy.get(".inventory_item").then((produtos) => {
      const quantidadeProdutos = produtos.length;

      cy.get(".btn_inventory").click({ multiple: true });

      cy.get(".shopping_cart_badge").should("have.text", String(quantidadeProdutos));

      cy.get(".shopping_cart_link").click();

      cy.get(".cart_item")
        .find(".inventory_item_price")
        .then((precos) => {
          const precosDosProdutos = Array.from(precos).map((el) =>
            parseFloat(el.textContent.replace("$", ""))
          );

          const indicesMenoresValores = [];
          for (let i = 0; i < 2; i++) {
            const menorPreco = Math.min(...precosDosProdutos);
            const indiceMenorPreco = precosDosProdutos.indexOf(menorPreco);
            indicesMenoresValores.push(indiceMenorPreco);
            precosDosProdutos.splice(indiceMenorPreco, 1, Number.MAX_VALUE);
          }

          cy.get(".cart_item").eq(indicesMenoresValores[0]).find(".cart_button").click();
          cy.get(".cart_item").eq(indicesMenoresValores[1] - 1).find(".cart_button").click();

          cy.get(".shopping_cart_badge").should("have.text", String(quantidadeProdutos - 2));
        });
    });
  });
});
