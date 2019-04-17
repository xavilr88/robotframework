
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ARGUMENT ARGUMENTS ASSIGN COMMENT_HEADER DATA DEFAULT_TAGS DOCUMENTATION END EOS ERROR FOR FORCE_TAGS FOR_SEPARATOR KEYWORD KEYWORD_HEADER LIBRARY METADATA NAME NON_DATA_TOKENS OLD_FOR_INDENT RESOURCE RETURN SETTING_HEADER SETUP SUITE_SETUP SUITE_TEARDOWN TAGS TEARDOWN TEMPLATE TESTCASE_HEADER TEST_SETUP TEST_TEARDOWN TEST_TEMPLATE TEST_TIMEOUT TIMEOUT VARIABLE VARIABLES VARIABLE_HEADERdatafile : sectionssections : section\n                    | sections sectionsection : setting_section\n                   | variable_section\n                   | testcase_section\n                   | keyword_section\n        setting_section : SETTING_HEADER EOS settingssettings : setting\n                    | settings settingsetting : documentation_setting EOS\n                   | suite_setup_setting EOS\n                   | suite_teardown_setting EOS\n                   | metadata_setting EOS\n                   | test_setup_setting EOS\n                   | test_teardown_setting EOS\n                   | test_template_setting EOS\n                   | test_timeout_setting EOS\n                   | force_tags_setting EOS\n                   | default_tags_setting EOS\n                   | library_setting EOS\n                   | resource_setting EOS\n                   | variables_setting EOS\n                   | setup_setting EOS\n                   | teardown_setting EOS\n                   | template_setting EOS\n                   | timeout_setting EOS\n                   | tags_setting EOS\n                   | arguments_setting EOS\n                   | return_setting EOSdocumentation_setting : DOCUMENTATION argumentssuite_setup_setting : SUITE_SETUP argumentssuite_teardown_setting : SUITE_TEARDOWN argumentsmetadata_setting : METADATA argumentstest_setup_setting : TEST_SETUP argumentstest_teardown_setting : TEST_TEARDOWN argumentstest_template_setting : TEST_TEMPLATE argumentstest_timeout_setting : TEST_TIMEOUT argumentsforce_tags_setting : FORCE_TAGS argumentsdefault_tags_setting : DEFAULT_TAGS argumentslibrary_setting : LIBRARY argumentsresource_setting : RESOURCE argumentsvariables_setting : VARIABLES argumentssetup_setting : SETUP argumentsteardown_setting : TEARDOWN argumentstemplate_setting : TEMPLATE argumentstimeout_setting : TIMEOUT argumentstags_setting : TAGS argumentsarguments_setting : ARGUMENTS argumentsreturn_setting : RETURN argumentsvariable_section : VARIABLE_HEADER EOS variablesvariables : variable\n                    | variables variablevariable : VARIABLE arguments EOS\n                    | VARIABLE EOStestcase_section : TESTCASE_HEADER EOS testskeyword_section : KEYWORD_HEADER EOS keywordstests : test\n                | tests testkeywords : keyword\n                    | keywords keywordtest : NAME EOS\n               | NAME EOS body_itemskeyword : NAME EOS\n                    | NAME EOS body_itemsbody_items : body_item\n                      | body_items body_item\n        body_item : forloop\n                     | setting\n                     | step\n                     | templatearguments\n        step : KEYWORD EOS\n                | KEYWORD arguments EOSstep : assignments KEYWORD EOS\n                | assignments KEYWORD arguments EOSforloop : for_header for_body END EOS\n                   | for_header\n                   | END EOSfor_header : FOR arguments FOR_SEPARATOR arguments EOS\n                      | FOR arguments FOR_SEPARATOR EOS\n                      | FOR arguments EOS\n                      | FOR EOSfor_body : step\n                    | for_body step\n        templatearguments : arguments EOSassignments : ASSIGN\n                     | assignments ASSIGNarguments : ARGUMENT\n                     | arguments ARGUMENT'
    
_lr_action_items = {'SETTING_HEADER':([0,2,3,4,5,6,7,12,17,18,59,60,62,63,65,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,110,112,113,114,115,116,118,119,120,121,122,123,124,125,132,133,136,137,139,143,146,147,150,151,152,154,155,],[8,8,-2,-4,-5,-6,-7,-3,-8,-9,-51,-52,-56,-58,-57,-60,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-53,-55,-59,-62,-61,-64,-54,-63,-66,-68,-69,-70,-71,-77,-65,-67,-78,-72,-85,-82,-73,-74,-81,-76,-75,-80,-79,]),'VARIABLE_HEADER':([0,2,3,4,5,6,7,12,17,18,59,60,62,63,65,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,110,112,113,114,115,116,118,119,120,121,122,123,124,125,132,133,136,137,139,143,146,147,150,151,152,154,155,],[9,9,-2,-4,-5,-6,-7,-3,-8,-9,-51,-52,-56,-58,-57,-60,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-53,-55,-59,-62,-61,-64,-54,-63,-66,-68,-69,-70,-71,-77,-65,-67,-78,-72,-85,-82,-73,-74,-81,-76,-75,-80,-79,]),'TESTCASE_HEADER':([0,2,3,4,5,6,7,12,17,18,59,60,62,63,65,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,110,112,113,114,115,116,118,119,120,121,122,123,124,125,132,133,136,137,139,143,146,147,150,151,152,154,155,],[10,10,-2,-4,-5,-6,-7,-3,-8,-9,-51,-52,-56,-58,-57,-60,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-53,-55,-59,-62,-61,-64,-54,-63,-66,-68,-69,-70,-71,-77,-65,-67,-78,-72,-85,-82,-73,-74,-81,-76,-75,-80,-79,]),'KEYWORD_HEADER':([0,2,3,4,5,6,7,12,17,18,59,60,62,63,65,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,110,112,113,114,115,116,118,119,120,121,122,123,124,125,132,133,136,137,139,143,146,147,150,151,152,154,155,],[11,11,-2,-4,-5,-6,-7,-3,-8,-9,-51,-52,-56,-58,-57,-60,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-53,-55,-59,-62,-61,-64,-54,-63,-66,-68,-69,-70,-71,-77,-65,-67,-78,-72,-85,-82,-73,-74,-81,-76,-75,-80,-79,]),'$end':([1,2,3,4,5,6,7,12,17,18,59,60,62,63,65,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,110,112,113,114,115,116,118,119,120,121,122,123,124,125,132,133,136,137,139,143,146,147,150,151,152,154,155,],[0,-1,-2,-4,-5,-6,-7,-3,-8,-9,-51,-52,-56,-58,-57,-60,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-53,-55,-59,-62,-61,-64,-54,-63,-66,-68,-69,-70,-71,-77,-65,-67,-78,-72,-85,-82,-73,-74,-81,-76,-75,-80,-79,]),'EOS':([8,9,10,11,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,61,64,67,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,111,117,126,127,128,130,138,140,142,144,148,149,153,],[13,14,15,16,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,112,114,116,-31,-88,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,118,-89,136,137,139,143,146,147,150,151,152,154,155,]),'DOCUMENTATION':([13,17,18,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,114,116,119,120,121,122,123,124,125,132,133,136,137,139,143,146,147,150,151,152,154,155,],[39,39,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,39,39,39,-66,-68,-69,-70,-71,-77,39,-67,-78,-72,-85,-82,-73,-74,-81,-76,-75,-80,-79,]),'SUITE_SETUP':([13,17,18,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,114,116,119,120,121,122,123,124,125,132,133,136,137,139,143,146,147,150,151,152,154,155,],[40,40,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,40,40,40,-66,-68,-69,-70,-71,-77,40,-67,-78,-72,-85,-82,-73,-74,-81,-76,-75,-80,-79,]),'SUITE_TEARDOWN':([13,17,18,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,114,116,119,120,121,122,123,124,125,132,133,136,137,139,143,146,147,150,151,152,154,155,],[41,41,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,41,41,41,-66,-68,-69,-70,-71,-77,41,-67,-78,-72,-85,-82,-73,-74,-81,-76,-75,-80,-79,]),'METADATA':([13,17,18,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,114,116,119,120,121,122,123,124,125,132,133,136,137,139,143,146,147,150,151,152,154,155,],[42,42,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,42,42,42,-66,-68,-69,-70,-71,-77,42,-67,-78,-72,-85,-82,-73,-74,-81,-76,-75,-80,-79,]),'TEST_SETUP':([13,17,18,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,114,116,119,120,121,122,123,124,125,132,133,136,137,139,143,146,147,150,151,152,154,155,],[43,43,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,43,43,43,-66,-68,-69,-70,-71,-77,43,-67,-78,-72,-85,-82,-73,-74,-81,-76,-75,-80,-79,]),'TEST_TEARDOWN':([13,17,18,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,114,116,119,120,121,122,123,124,125,132,133,136,137,139,143,146,147,150,151,152,154,155,],[44,44,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,44,44,44,-66,-68,-69,-70,-71,-77,44,-67,-78,-72,-85,-82,-73,-74,-81,-76,-75,-80,-79,]),'TEST_TEMPLATE':([13,17,18,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,114,116,119,120,121,122,123,124,125,132,133,136,137,139,143,146,147,150,151,152,154,155,],[45,45,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,45,45,45,-66,-68,-69,-70,-71,-77,45,-67,-78,-72,-85,-82,-73,-74,-81,-76,-75,-80,-79,]),'TEST_TIMEOUT':([13,17,18,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,114,116,119,120,121,122,123,124,125,132,133,136,137,139,143,146,147,150,151,152,154,155,],[46,46,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,46,46,46,-66,-68,-69,-70,-71,-77,46,-67,-78,-72,-85,-82,-73,-74,-81,-76,-75,-80,-79,]),'FORCE_TAGS':([13,17,18,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,114,116,119,120,121,122,123,124,125,132,133,136,137,139,143,146,147,150,151,152,154,155,],[47,47,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,47,47,47,-66,-68,-69,-70,-71,-77,47,-67,-78,-72,-85,-82,-73,-74,-81,-76,-75,-80,-79,]),'DEFAULT_TAGS':([13,17,18,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,114,116,119,120,121,122,123,124,125,132,133,136,137,139,143,146,147,150,151,152,154,155,],[48,48,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,48,48,48,-66,-68,-69,-70,-71,-77,48,-67,-78,-72,-85,-82,-73,-74,-81,-76,-75,-80,-79,]),'LIBRARY':([13,17,18,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,114,116,119,120,121,122,123,124,125,132,133,136,137,139,143,146,147,150,151,152,154,155,],[49,49,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,49,49,49,-66,-68,-69,-70,-71,-77,49,-67,-78,-72,-85,-82,-73,-74,-81,-76,-75,-80,-79,]),'RESOURCE':([13,17,18,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,114,116,119,120,121,122,123,124,125,132,133,136,137,139,143,146,147,150,151,152,154,155,],[50,50,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,50,50,50,-66,-68,-69,-70,-71,-77,50,-67,-78,-72,-85,-82,-73,-74,-81,-76,-75,-80,-79,]),'VARIABLES':([13,17,18,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,114,116,119,120,121,122,123,124,125,132,133,136,137,139,143,146,147,150,151,152,154,155,],[51,51,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,51,51,51,-66,-68,-69,-70,-71,-77,51,-67,-78,-72,-85,-82,-73,-74,-81,-76,-75,-80,-79,]),'SETUP':([13,17,18,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,114,116,119,120,121,122,123,124,125,132,133,136,137,139,143,146,147,150,151,152,154,155,],[52,52,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,52,52,52,-66,-68,-69,-70,-71,-77,52,-67,-78,-72,-85,-82,-73,-74,-81,-76,-75,-80,-79,]),'TEARDOWN':([13,17,18,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,114,116,119,120,121,122,123,124,125,132,133,136,137,139,143,146,147,150,151,152,154,155,],[53,53,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,53,53,53,-66,-68,-69,-70,-71,-77,53,-67,-78,-72,-85,-82,-73,-74,-81,-76,-75,-80,-79,]),'TEMPLATE':([13,17,18,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,114,116,119,120,121,122,123,124,125,132,133,136,137,139,143,146,147,150,151,152,154,155,],[54,54,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,54,54,54,-66,-68,-69,-70,-71,-77,54,-67,-78,-72,-85,-82,-73,-74,-81,-76,-75,-80,-79,]),'TIMEOUT':([13,17,18,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,114,116,119,120,121,122,123,124,125,132,133,136,137,139,143,146,147,150,151,152,154,155,],[55,55,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,55,55,55,-66,-68,-69,-70,-71,-77,55,-67,-78,-72,-85,-82,-73,-74,-81,-76,-75,-80,-79,]),'TAGS':([13,17,18,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,114,116,119,120,121,122,123,124,125,132,133,136,137,139,143,146,147,150,151,152,154,155,],[56,56,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,56,56,56,-66,-68,-69,-70,-71,-77,56,-67,-78,-72,-85,-82,-73,-74,-81,-76,-75,-80,-79,]),'ARGUMENTS':([13,17,18,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,114,116,119,120,121,122,123,124,125,132,133,136,137,139,143,146,147,150,151,152,154,155,],[57,57,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,57,57,57,-66,-68,-69,-70,-71,-77,57,-67,-78,-72,-85,-82,-73,-74,-81,-76,-75,-80,-79,]),'RETURN':([13,17,18,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,114,116,119,120,121,122,123,124,125,132,133,136,137,139,143,146,147,150,151,152,154,155,],[58,58,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,58,58,58,-66,-68,-69,-70,-71,-77,58,-67,-78,-72,-85,-82,-73,-74,-81,-76,-75,-80,-79,]),'VARIABLE':([14,59,60,110,112,118,],[61,61,-52,-53,-55,-54,]),'NAME':([15,16,62,63,65,66,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,113,114,115,116,119,120,121,122,123,124,125,132,133,136,137,139,143,146,147,150,151,152,154,155,],[64,67,64,-58,67,-60,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-59,-62,-61,-64,-63,-66,-68,-69,-70,-71,-77,-65,-67,-78,-72,-85,-82,-73,-74,-81,-76,-75,-80,-79,]),'ARGUMENT':([39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,61,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,111,114,116,117,119,120,121,122,123,124,125,127,128,130,132,133,136,137,138,139,140,142,143,146,147,148,149,150,151,152,153,154,155,],[90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,117,-88,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,90,90,-89,90,-66,-68,-69,-70,-71,-77,90,117,90,90,-67,-78,-72,117,-85,90,117,-82,-73,-74,117,90,-81,-76,-75,117,-80,-79,]),'END':([69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,114,116,119,120,121,122,123,124,125,132,133,134,135,136,137,139,143,145,146,147,150,151,152,154,155,],[-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,126,126,126,-66,-68,-69,-70,-71,-77,126,-67,144,-83,-78,-72,-85,-82,-84,-73,-74,-81,-76,-75,-80,-79,]),'KEYWORD':([69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,114,116,119,120,121,122,123,124,125,129,131,132,133,134,135,136,137,139,141,143,145,146,147,150,151,152,154,155,],[-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,127,127,127,-66,-68,-69,-70,-71,127,140,-86,127,-67,127,-83,-78,-72,-85,-87,-82,-84,-73,-74,-81,-76,-75,-80,-79,]),'FOR':([69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,114,116,119,120,121,122,123,124,125,132,133,136,137,139,143,146,147,150,151,152,154,155,],[-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,130,130,130,-66,-68,-69,-70,-71,-77,130,-67,-78,-72,-85,-82,-73,-74,-81,-76,-75,-80,-79,]),'ASSIGN':([69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,114,116,119,120,121,122,123,124,125,129,131,132,133,134,135,136,137,139,141,143,145,146,147,150,151,152,154,155,],[-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,131,131,131,-66,-68,-69,-70,-71,131,141,-86,131,-67,131,-83,-78,-72,-85,-87,-82,-84,-73,-74,-81,-76,-75,-80,-79,]),'FOR_SEPARATOR':([90,117,142,],[-88,-89,149,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'datafile':([0,],[1,]),'sections':([0,],[2,]),'section':([0,2,],[3,12,]),'setting_section':([0,2,],[4,4,]),'variable_section':([0,2,],[5,5,]),'testcase_section':([0,2,],[6,6,]),'keyword_section':([0,2,],[7,7,]),'settings':([13,],[17,]),'setting':([13,17,114,116,119,132,],[18,68,122,122,122,122,]),'documentation_setting':([13,17,114,116,119,132,],[19,19,19,19,19,19,]),'suite_setup_setting':([13,17,114,116,119,132,],[20,20,20,20,20,20,]),'suite_teardown_setting':([13,17,114,116,119,132,],[21,21,21,21,21,21,]),'metadata_setting':([13,17,114,116,119,132,],[22,22,22,22,22,22,]),'test_setup_setting':([13,17,114,116,119,132,],[23,23,23,23,23,23,]),'test_teardown_setting':([13,17,114,116,119,132,],[24,24,24,24,24,24,]),'test_template_setting':([13,17,114,116,119,132,],[25,25,25,25,25,25,]),'test_timeout_setting':([13,17,114,116,119,132,],[26,26,26,26,26,26,]),'force_tags_setting':([13,17,114,116,119,132,],[27,27,27,27,27,27,]),'default_tags_setting':([13,17,114,116,119,132,],[28,28,28,28,28,28,]),'library_setting':([13,17,114,116,119,132,],[29,29,29,29,29,29,]),'resource_setting':([13,17,114,116,119,132,],[30,30,30,30,30,30,]),'variables_setting':([13,17,114,116,119,132,],[31,31,31,31,31,31,]),'setup_setting':([13,17,114,116,119,132,],[32,32,32,32,32,32,]),'teardown_setting':([13,17,114,116,119,132,],[33,33,33,33,33,33,]),'template_setting':([13,17,114,116,119,132,],[34,34,34,34,34,34,]),'timeout_setting':([13,17,114,116,119,132,],[35,35,35,35,35,35,]),'tags_setting':([13,17,114,116,119,132,],[36,36,36,36,36,36,]),'arguments_setting':([13,17,114,116,119,132,],[37,37,37,37,37,37,]),'return_setting':([13,17,114,116,119,132,],[38,38,38,38,38,38,]),'variables':([14,],[59,]),'variable':([14,59,],[60,110,]),'tests':([15,],[62,]),'test':([15,62,],[63,113,]),'keywords':([16,],[65,]),'keyword':([16,65,],[66,115,]),'arguments':([39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,61,114,116,119,127,130,132,140,149,],[89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,111,128,128,128,138,142,128,148,153,]),'body_items':([114,116,],[119,132,]),'body_item':([114,116,119,132,],[120,120,133,133,]),'forloop':([114,116,119,132,],[121,121,121,121,]),'step':([114,116,119,125,132,134,],[123,123,123,135,123,145,]),'templatearguments':([114,116,119,132,],[124,124,124,124,]),'for_header':([114,116,119,132,],[125,125,125,125,]),'assignments':([114,116,119,125,132,134,],[129,129,129,129,129,129,]),'for_body':([125,],[134,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> datafile","S'",1,None,None,None),
  ('datafile -> sections','datafile',1,'p_datafile','parser.py',18),
  ('sections -> section','sections',1,'p_sections','parser.py',22),
  ('sections -> sections section','sections',2,'p_sections','parser.py',23),
  ('section -> setting_section','section',1,'p_section','parser.py',27),
  ('section -> variable_section','section',1,'p_section','parser.py',28),
  ('section -> testcase_section','section',1,'p_section','parser.py',29),
  ('section -> keyword_section','section',1,'p_section','parser.py',30),
  ('setting_section -> SETTING_HEADER EOS settings','setting_section',3,'p_setting_section','parser.py',35),
  ('settings -> setting','settings',1,'p_settings','parser.py',39),
  ('settings -> settings setting','settings',2,'p_settings','parser.py',40),
  ('setting -> documentation_setting EOS','setting',2,'p_setting','parser.py',44),
  ('setting -> suite_setup_setting EOS','setting',2,'p_setting','parser.py',45),
  ('setting -> suite_teardown_setting EOS','setting',2,'p_setting','parser.py',46),
  ('setting -> metadata_setting EOS','setting',2,'p_setting','parser.py',47),
  ('setting -> test_setup_setting EOS','setting',2,'p_setting','parser.py',48),
  ('setting -> test_teardown_setting EOS','setting',2,'p_setting','parser.py',49),
  ('setting -> test_template_setting EOS','setting',2,'p_setting','parser.py',50),
  ('setting -> test_timeout_setting EOS','setting',2,'p_setting','parser.py',51),
  ('setting -> force_tags_setting EOS','setting',2,'p_setting','parser.py',52),
  ('setting -> default_tags_setting EOS','setting',2,'p_setting','parser.py',53),
  ('setting -> library_setting EOS','setting',2,'p_setting','parser.py',54),
  ('setting -> resource_setting EOS','setting',2,'p_setting','parser.py',55),
  ('setting -> variables_setting EOS','setting',2,'p_setting','parser.py',56),
  ('setting -> setup_setting EOS','setting',2,'p_setting','parser.py',57),
  ('setting -> teardown_setting EOS','setting',2,'p_setting','parser.py',58),
  ('setting -> template_setting EOS','setting',2,'p_setting','parser.py',59),
  ('setting -> timeout_setting EOS','setting',2,'p_setting','parser.py',60),
  ('setting -> tags_setting EOS','setting',2,'p_setting','parser.py',61),
  ('setting -> arguments_setting EOS','setting',2,'p_setting','parser.py',62),
  ('setting -> return_setting EOS','setting',2,'p_setting','parser.py',63),
  ('documentation_setting -> DOCUMENTATION arguments','documentation_setting',2,'p_documentation','parser.py',67),
  ('suite_setup_setting -> SUITE_SETUP arguments','suite_setup_setting',2,'p_suite_setup','parser.py',71),
  ('suite_teardown_setting -> SUITE_TEARDOWN arguments','suite_teardown_setting',2,'p_suite_teardown','parser.py',75),
  ('metadata_setting -> METADATA arguments','metadata_setting',2,'p_metadata','parser.py',79),
  ('test_setup_setting -> TEST_SETUP arguments','test_setup_setting',2,'p_test_setup','parser.py',83),
  ('test_teardown_setting -> TEST_TEARDOWN arguments','test_teardown_setting',2,'p_test_teardown','parser.py',87),
  ('test_template_setting -> TEST_TEMPLATE arguments','test_template_setting',2,'p_test_template','parser.py',91),
  ('test_timeout_setting -> TEST_TIMEOUT arguments','test_timeout_setting',2,'p_test_timeout','parser.py',95),
  ('force_tags_setting -> FORCE_TAGS arguments','force_tags_setting',2,'p_force_tags','parser.py',99),
  ('default_tags_setting -> DEFAULT_TAGS arguments','default_tags_setting',2,'p_default_tags','parser.py',103),
  ('library_setting -> LIBRARY arguments','library_setting',2,'p_library','parser.py',107),
  ('resource_setting -> RESOURCE arguments','resource_setting',2,'p_resource','parser.py',112),
  ('variables_setting -> VARIABLES arguments','variables_setting',2,'p_variables_import','parser.py',117),
  ('setup_setting -> SETUP arguments','setup_setting',2,'p_setup','parser.py',122),
  ('teardown_setting -> TEARDOWN arguments','teardown_setting',2,'p_teardown','parser.py',126),
  ('template_setting -> TEMPLATE arguments','template_setting',2,'p_template','parser.py',130),
  ('timeout_setting -> TIMEOUT arguments','timeout_setting',2,'p_timeout','parser.py',134),
  ('tags_setting -> TAGS arguments','tags_setting',2,'p_tags','parser.py',138),
  ('arguments_setting -> ARGUMENTS arguments','arguments_setting',2,'p_arguments_setting','parser.py',142),
  ('return_setting -> RETURN arguments','return_setting',2,'p_return','parser.py',146),
  ('variable_section -> VARIABLE_HEADER EOS variables','variable_section',3,'p_variable_section','parser.py',150),
  ('variables -> variable','variables',1,'p_variables','parser.py',154),
  ('variables -> variables variable','variables',2,'p_variables','parser.py',155),
  ('variable -> VARIABLE arguments EOS','variable',3,'p_variable','parser.py',159),
  ('variable -> VARIABLE EOS','variable',2,'p_variable','parser.py',160),
  ('testcase_section -> TESTCASE_HEADER EOS tests','testcase_section',3,'p_testcase_section','parser.py',165),
  ('keyword_section -> KEYWORD_HEADER EOS keywords','keyword_section',3,'p_keyword_section','parser.py',169),
  ('tests -> test','tests',1,'p_tests','parser.py',173),
  ('tests -> tests test','tests',2,'p_tests','parser.py',174),
  ('keywords -> keyword','keywords',1,'p_keywords','parser.py',178),
  ('keywords -> keywords keyword','keywords',2,'p_keywords','parser.py',179),
  ('test -> NAME EOS','test',2,'p_test','parser.py',183),
  ('test -> NAME EOS body_items','test',3,'p_test','parser.py',184),
  ('keyword -> NAME EOS','keyword',2,'p_keyword','parser.py',191),
  ('keyword -> NAME EOS body_items','keyword',3,'p_keyword','parser.py',192),
  ('body_items -> body_item','body_items',1,'p_body_items','parser.py',199),
  ('body_items -> body_items body_item','body_items',2,'p_body_items','parser.py',200),
  ('body_item -> forloop','body_item',1,'p_body_item','parser.py',205),
  ('body_item -> setting','body_item',1,'p_body_item','parser.py',206),
  ('body_item -> step','body_item',1,'p_body_item','parser.py',207),
  ('body_item -> templatearguments','body_item',1,'p_body_item','parser.py',208),
  ('step -> KEYWORD EOS','step',2,'p_step','parser.py',214),
  ('step -> KEYWORD arguments EOS','step',3,'p_step','parser.py',215),
  ('step -> assignments KEYWORD EOS','step',3,'p_step_with_assignment','parser.py',222),
  ('step -> assignments KEYWORD arguments EOS','step',4,'p_step_with_assignment','parser.py',223),
  ('forloop -> for_header for_body END EOS','forloop',4,'p_forloop','parser.py',230),
  ('forloop -> for_header','forloop',1,'p_forloop','parser.py',231),
  ('forloop -> END EOS','forloop',2,'p_forloop','parser.py',232),
  ('for_header -> FOR arguments FOR_SEPARATOR arguments EOS','for_header',5,'p_for_header','parser.py',241),
  ('for_header -> FOR arguments FOR_SEPARATOR EOS','for_header',4,'p_for_header','parser.py',242),
  ('for_header -> FOR arguments EOS','for_header',3,'p_for_header','parser.py',243),
  ('for_header -> FOR EOS','for_header',2,'p_for_header','parser.py',244),
  ('for_body -> step','for_body',1,'p_for_body','parser.py',256),
  ('for_body -> for_body step','for_body',2,'p_for_body','parser.py',257),
  ('templatearguments -> arguments EOS','templatearguments',2,'p_templatearguments','parser.py',262),
  ('assignments -> ASSIGN','assignments',1,'p_assignments','parser.py',266),
  ('assignments -> assignments ASSIGN','assignments',2,'p_assignments','parser.py',267),
  ('arguments -> ARGUMENT','arguments',1,'p_arguments','parser.py',271),
  ('arguments -> arguments ARGUMENT','arguments',2,'p_arguments','parser.py',272),
]
