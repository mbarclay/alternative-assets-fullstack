describe('investors are visible', () => {
  it('renders asset summaries and allows selection', () => {
    cy.visit('/');
    // verify that the investors are rendered correctly
    cy.contains('Ioo Gryffindor fund').should('be.visible');
    cy.contains('Ibx Skywalker ltd').should('be.visible');
  });
});
