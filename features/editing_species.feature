Feature: Store species details
  In order to track the the different species being
  planted, the user can create and save the details
  of individual species.

  Scenario: Saving a species adds it to the list
     Given we have navigated to the species details page
      When we fill in the form
        And we click the save button
      Then the species is displayed on the species list page