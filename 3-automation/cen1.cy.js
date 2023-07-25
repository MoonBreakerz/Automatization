describe("Realizar Login com o usuário standard_user", () => {
  it("Logar com o usuário standard_user", () => {
    cy.visit("https://www.saucedemo.com/");
    cy.get("#user-name").type("standard_user");
    cy.get("#password").type("secret_sauce");
    cy.get("#login-button").click();

    cy.url().should("include", "inventory.html");
  });
});

describe("Login com usuário bloqueado 'locked_out_user'", () => {
  it("Tentar fazer login com o usuário bloqueado 'locked_out_user'", () => {
    cy.visit("https://www.saucedemo.com/");
    cy.get("#user-name").type("locked_out_user");
    cy.get("#password").type("secret_sauce");
    cy.get("#login-button").click();

    cy.get("h3[data-test='error']").should(
      "have.text",
      "Epic sadface: Sorry, this user has been locked out."
    );
  });
});
