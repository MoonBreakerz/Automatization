describe("Cenário III: Realizar a compra de dois produtos", () => {
  it("Logar com o usuário standard_user", () => {
    cy.visit("https://www.saucedemo.com/");
    cy.get("#user-name").type("standard_user");
    cy.get("#password").type("secret_sauce");
    cy.get("#login-button").click();

    cy.url().should("include", "inventory.html");

    cy.get(".inventory_item_price")
      .then((precos) => {
        const precosDosProdutos = Array.from(precos).map((el) =>
          parseFloat(el.textContent.replace("$", ""))
        );

        const menorPreco = Math.min(...precosDosProdutos);
        const indiceMenorPreco = precosDosProdutos.indexOf(menorPreco);
        cy.get(".btn_inventory").eq(indiceMenorPreco).click();

        const maiorPreco = Math.max(...precosDosProdutos);
        const indiceMaiorPreco = precosDosProdutos.indexOf(maiorPreco);
        cy.get(".btn_inventory").eq(indiceMaiorPreco).click();

        cy.get(".shopping_cart_link").click();
      })
      .then(() => {
        cy.get("#checkout").click();
        cy.get("#first-name").type("Gabriel");
        cy.get("#last-name").type("Guedes");
        cy.get("#postal-code").type("00000-000");
        cy.get("#continue").click();
        cy.get("#finish").click();
        cy.url().should("include", "checkout-complete.html");
        cy.log("Compra realizada com sucesso!");
      });
  });
});
