describe('investors are visible', () => {
  it('renders investors', () => {
    cy.visit('/');
    // verify that the investors are rendered correctly
    cy.contains('Ioo Gryffindor fund').should('be.visible');
    cy.contains('Ibx Skywalker ltd').should('be.visible');
  });
});

describe('asset summaries are not visible', () => {
  it('does not render asset summaries', () => {
    cy.visit('/');

    // first, check if the element does not exist at all
    cy.get('body').then(($body) => {
      if ($body.find('.asset-summary-NATURAL_RESOURCES').length > 0) {
        // if the element exists, then check if it is not visible
        cy.get('.asset-summary-NATURAL_RESOURCES').should('not.be.visible');
      } else {
        // otherwise, assert that it does not exist
        cy.get('.asset-summary-NATURAL_RESOURCES').should('not.exist');
      }
    });
  });
});
