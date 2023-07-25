describe("Cenário II: Maior e menor valor dos produtos", () => {
  it("Logar com o usuário standard_user", () => {
    cy.visit("https://www.saucedemo.com/");
    cy.get("#user-name").type("standard_user");
    cy.get("#password").type("secret_sauce");
    cy.get("#login-button").click();

    cy.url().should("include", "inventory.html");

    cy.get(".inventory_item_price").then((prices) => {
      const precosDosProdutos = Array.from(prices).map((el) =>
        parseFloat(el.textContent.replace("$", ""))
      );

      const menorPreco = Math.min(...precosDosProdutos);
      const indiceMenorPreco = precosDosProdutos.indexOf(menorPreco);
      const nomeProdutoMenorPreco = Cypress.$(".inventory_item_name")
        .eq(indiceMenorPreco)
        .text();
      cy.log(
        `O produto com menor valor é '${nomeProdutoMenorPreco}' e custa $${menorPreco.toFixed(2)}.`
      );

      const maiorPreco = Math.max(...precosDosProdutos);
      const indiceMaiorPreco = precosDosProdutos.indexOf(maiorPreco);
      const nomeProdutoMaiorPreco = Cypress.$(".inventory_item_name")
        .eq(indiceMaiorPreco)
        .text();
      cy.log(
        `O produto com maior valor é '${nomeProdutoMaiorPreco}' e custa $${maiorPreco.toFixed(2)}.`
      );
    });
  });
});
