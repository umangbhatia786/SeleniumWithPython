Feature: Change_Notepad_Font_Size

@NotePad
Scenario Outline: Change Font Size of a text in Notepad
  Then I write some <Text> into the NotePad Console
  And I open Font window from Format Dropdown in Menu
  And I change the Font Size as <Size> and click ok
  Then I close the Notepad without saving any changes

  Examples:
  | ScenarioName                      | Text | Size | 
  | "TC_01_Customer Search_EE PayM"   | "This is a sample text line1"   | "14"   | 