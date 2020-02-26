# ci-test
This is a test to configure CI with Github.

## About the package
The package is a simple calculator with a unit tests which will serve to validate the source code.
The calculator has the following operations defined:
- Add
- Subtract
- Multiply
- Divide

## CI Strategy
The main idea is to create a workflow to deploy the package and run the unit tests to validate the build.
As a stretch goal, we will attempt to add a code style check if time permits.
The current CI implementation follows these steps:
- Pull package
- Install package dependencies
- Test package using its included tst directory
- Upload test results for analysis
# This change comes from master