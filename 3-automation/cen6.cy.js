describe("Funcionalidade: Verificar detalhes de um produto", () => {
  before(() => {
    cy.visit("https://www.saucedemo.com/");
    cy.get("#user-name").type("standard_user");
    cy.get("#password").type("secret_sauce");
    cy.get("#login-button").click();

    cy.url().should("include", "inventory.html");
  });	
  
  it("Cenário: Verificar detalhes de um produto específico", () => {
    cy.get(".inventory_item_name").first().then((produto) => {
      const nomeProduto = produto.text();

      cy.get(".inventory_item_name").first().click();

      cy.url().should("include", "inventory-item.html");
      cy.get(".inventory_item_name").should("have.text", nomeProduto);
    });
  });

  it("Cenário: Verificar informações do produto na página de detalhes", () => {
    cy.get(".inventory_item_name").first().click();

    cy.get(".inventory_details_name").should("be.visible");
    cy.get(".inventory_details_desc").should("be.visible");
    cy.get(".inventory_details_price").should("be.visible");
  });

  it("Cenário: Adicionar produto ao carrinho a partir da página de detalhes", () => {
    cy.get(".inventory_item_name").first().click();

    cy.get(".btn_inventory").click();

    cy.get(".shopping_cart_badge").should("have.text", "1");
  });

  it("Cenário: Voltar para a página de inventário a partir da página de detalhes", () => {
    cy.get(".inventory_item_name").first().click();

    cy.get(".inventory_details_back_button").click();

    cy.url().should("include", "inventory.html");
  });
});
