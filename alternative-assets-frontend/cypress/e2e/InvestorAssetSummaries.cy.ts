describe('selected investors asset summaries are visible', () => {
  it('renders asset summaries and allows selection', () => {
    cy.visit('/');

    // investor row should exist
    cy.get('#investor-row-CWF', { timeout: 1000 }).should('exist');

    // click the investor row
    cy.get('#investor-row-CWF').click();

    // check for some asset summaries
    cy.get('#asset-summary-INFRASTRUCTURE', { timeout: 1000 }).should('exist');
    cy.get('#asset-summary-PRIVATE_EQUITY', { timeout: 1000 }).should('exist');
  });
});