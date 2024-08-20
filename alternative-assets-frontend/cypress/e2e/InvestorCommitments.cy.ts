describe('selected asset commitment details are visible', () => {
  it('renders asset commitment details', () => {
    cy.visit('/');

    // investor row should exist
    cy.get('#investor-row-MJF', { timeout: 1000 }).should('exist');

    // click the investor row
    cy.get('#investor-row-MJF').click();

    // check for some asset summaries
    cy.get('#asset-summary-INFRASTRUCTURE', { timeout: 1000 }).should('exist');
    cy.get('#asset-summary-PRIVATE_EQUITY', { timeout: 1000 }).should('exist');

    // select an asset summary
    cy.get('#asset-summary-INFRASTRUCTURE').click();

    // we know that this row should exist in the commitments table for MJF > INFRASTRUCTURE
    cy.get('#commitment-8969f468-7404-466b-a9f1-2a6336ea1232', { timeout: 1000 }).should('exist');
  });
});