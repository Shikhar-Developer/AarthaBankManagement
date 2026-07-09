def configureControllers(container):
    container.welcomePageController.setUp()
    container.registrationController.setup()
    container.loginController.setup()
    container.rolesController.setup()
