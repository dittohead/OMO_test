OMO Test

resources.py - ids, labels, etc
testHelper.py - classes with actions, identifiers setters, getters and other
loginTest.py - test suite for described sceneario
requirements.txt - nuff said:)

For launching tests:
 * Set path to apk file in desired capabilities (in suite)
 * Connect real device/AVD
 * Run appium server
 * $>python3 -m unittest loginTest.LoginTestSuite
 * Wait for execution
 
Know issues:
 * MainActivity start on splash, so I can't handle disappearing of splash screen
 * For unknown reasons WebDriverWait.until not working for elements, located as xpath,
 
 So sorry for using dumb sleep