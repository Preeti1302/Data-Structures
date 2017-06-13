#!/usr/bin/env python3

import unittest
import os
import json
from json import JSONDecoder
from shutil import rmtree
from string import Template
from create_project import copyDirectory, BASE_DIR

class TestCreateProject(unittest.TestCase):
    
    def setUp(self):
        self.copyObject = copyDirectory()
        self.new_path = 'adsk.preetiproj' 
        self.result_exists = self.copyObject.copyTemplate(self.new_path, 'i18n/preeti_corner')
        self.assertEqual.__self__.maxDiff = None
        
    def tearDown(self):
        clean_dir_created_1 = os.path.join(BASE_DIR , 'adsk.preetiproj1')
        rmtree(clean_dir_created_1 , ignore_errors='True')
        clean_dir_created_2 = os.path.join(BASE_DIR , 'adsk.project_name_for_testing')
        rmtree(clean_dir_created_2 , ignore_errors='True')
        clean_dir_created_2 = os.path.join(BASE_DIR , 'adsk.project_name_for_testing1')
        rmtree(clean_dir_created_2 , ignore_errors='True')
        clean_dir_created_1 = os.path.join(BASE_DIR , 'adsk.preetiproj')
        rmtree(clean_dir_created_1 , ignore_errors='True')
        unittest.TestCase.tearDown(self)
    
    #Check existence of project    
    def test_copy_template_exists(self):
        #print(self.result_exists)
        if self.result_exists == 'Success':
            self.result_exists = self.copyObject.copyTemplate(self.new_path, 'i18n/preeti_corner')
            self.test_copy_template_exists()
        else:
            self.assertEqual(self.result_exists, 'Exists') 
            #print("Test Successful in checking if project exists")
        
    
    #check successful creation of project    
    def test_copy_template_success(self):    
        new_path_success = 'adsk.preetiproj1' 
        result_success = self.copyObject.copyTemplate(new_path_success, 'i18n/preeti_corner')
        self.assertEqual(result_success, 'Success') and self.assertNotEqual(result_success,'Exists') and self.assertNotEqual(result_success,'Validation error')
        #print("Test Successful in checking if project is successfully created")
     
    #Check for all validations   
    def test_project_name_startswith_adsk_and_dot_validation(self):    
        result_valid_name = self.copyObject.copyTemplate('adskpreetiproj1', 'i18n/preeti_corner')
        self.assertEqual(result_valid_name, 'Validation error')
        
    def test_project_name_should_not_have_whitespace_validation(self): 
        result_valid_name = self.copyObject.copyTemplate('adsk preetiproj1', 'i18n/preeti_corner')
        self.assertEqual(result_valid_name, 'Validation error')
        
    def test_project_name_has_no_underscore_validation(self): 
        result_valid_name = self.copyObject.copyTemplate('adsk_preetiproj1', 'i18n/preeti_corner')
        self.assertEqual(result_valid_name, 'Validation error')
    
    def test_projecy_name_should_start_with_adsk_validation(self):      
        result_valid_name = self.copyObject.copyTemplate('newadskpreetiproj1', 'i18n/preeti_corner')
        self.assertEqual(result_valid_name, 'Validation error')   
    
    #check all variables are well swapped
    def test_swap_variables(self):
        test_sample_correct_xml = """\
    <scan>
        <scan-name>preeti_rules_scan</scan-name>
        <ruleset-name>preeti_rules</ruleset-name>
        <ruleset-owner>preeti.patil@autodesk.com</ruleset-owner>
        <scan-items>
            <item>/2</item>
        </scan-items>
    </scan>
    <scan>
        <scan-name>robs_rules_scan</scan-name>
        <ruleset-name>robs_rules</ruleset-name>
        <ruleset-owner>rob.orsini@autodesk.com</ruleset-owner>
        <scan-items>
            <item>/3</item>
        </scan-items>
    </scan>\n"""

        self.copyObject.copyTemplate('adsk.project_name_for_testing', 'adsk_github_name')
        
        result_test_runScan = self.copyObject.configure_RUNSCAN('adsk.project_name_for_testing')
        result_test_projdef = self.copyObject.configure_projDef('adsk.project_name_for_testing', 'i18n/preeti_corner', test_sample_correct_xml)
        result_test_sonar = self.copyObject.configure_SONAR('adsk.project_name_for_testing', 'i18n/preeti_corner')
        
        file_RUN_SCAN = os.path.join(os.path.join(BASE_DIR , 'adsk.project_name_for_testing'), '1-RUN-SCAN.sh')
        file_Projdef = os.path.join(os.path.join(BASE_DIR , 'adsk.project_name_for_testing'), 'projdef.xml')
        file_SONAR = os.path.join(os.path.join(BASE_DIR , 'adsk.project_name_for_testing'), 'sonar-project-template.properties')
        
        with open(file_RUN_SCAN, 'r') as file1:
            src_RUN_SCAN = Template( file1.read())
            resultFile1 = src_RUN_SCAN.template
            self.assertEqual(result_test_runScan, resultFile1)
        with open(file_Projdef, 'r') as file2:
            src_Projdef = Template( file2.read())
            resultFile2 = src_Projdef.template
            self.assertEqual(result_test_projdef, resultFile2)
        with open(file_SONAR, 'r') as file3:
            src_Sonar = Template( file3.read())
            resultFile3 = src_Sonar.template
            self.assertEqual(result_test_sonar, resultFile3)
    
    #Check for correct XML construction    
    def test_check_for_construction_of_correct_xml(self):
        #print("Before Data")
        data = "{\"scans\": [[\"2\",\"preeti_rules\",\"preeti.patil@autodesk.com\"],[\"3\",\"robs_rules\",\"rob.orsini@autodesk.com\"],[\"2\",\"preeti_rules\",\"preeti.patil@autodesk.com\"]]}"
        #print("After")
        test_xml_result = self.copyObject.custom_xml_configuration(data)
        #print("XML :::::::::::::::::::::\n %s " % test_xml_result)
        test_sample_correct_xml = """\
    <scan>
        <scan-name>preeti_rules_scan</scan-name>
        <ruleset-name>preeti_rules</ruleset-name>
        <ruleset-owner>preeti.patil@autodesk.com</ruleset-owner>
        <scan-items>
            <item>2</item>
        </scan-items>
    </scan>
    <scan>
        <scan-name>robs_rules_scan</scan-name>
        <ruleset-name>robs_rules</ruleset-name>
        <ruleset-owner>rob.orsini@autodesk.com</ruleset-owner>
        <scan-items>
            <item>3</item>
        </scan-items>
    </scan>\n"""

        self.assertEquals(test_xml_result, test_sample_correct_xml)

    #Check for correct XML construction if multiple scan items are provided
    def test_check_for_construction_of_correct_xml_with_multi_scan_items(self):
        data = "{\"scans\": [[\"java_dir\",\"preeti_rules\",\"preeti.patil@autodesk.com\"],[\"python_dir\",\"robs_rules\",\"rob.orsini@autodesk.com\"],[\"c++_dir\",\"preeti_rules\",\"preeti.patil@autodesk.com\"]]}"
        test_xml_result = self.copyObject.custom_xml_configuration(data)
        #print("XML :::::::::::::::::::::\n %s " % test_xml_result)
        test_sample_correct_xml = """\
    <scan>
        <scan-name>preeti_rules_scan</scan-name>
        <ruleset-name>preeti_rules</ruleset-name>
        <ruleset-owner>preeti.patil@autodesk.com</ruleset-owner>
        <scan-items>
            <item>c++_dir</item>
            <item>java_dir</item>
        </scan-items>
    </scan>
    <scan>
        <scan-name>robs_rules_scan</scan-name>
        <ruleset-name>robs_rules</ruleset-name>
        <ruleset-owner>rob.orsini@autodesk.com</ruleset-owner>
        <scan-items>
            <item>python_dir</item>
        </scan-items>
    </scan>\n"""
        self.assertEquals(test_xml_result, test_sample_correct_xml)


    def test_check_for_construction_of_correct_xml_with_one_rule(self):
        data = "{\"scans\" : [[\"/\",\"preeti_rules\", \"preeti.patil@autodesk.com\"]]}"
        test_xml_result = self.copyObject.custom_xml_configuration(data)
        #print("XML :::::::::::::::::::::\n %s " % test_xml_result)
        test_sample_correct_xml = """\
    <scan>
        <scan-name>preeti_rules_scan</scan-name>
        <ruleset-name>preeti_rules</ruleset-name>
        <ruleset-owner>preeti.patil@autodesk.com</ruleset-owner>
        <scan-items>
            <item>/</item>
        </scan-items>
    </scan>\n"""
        self.assertEquals(test_xml_result, test_sample_correct_xml)


    def test_check_for_construction_of_correct_xml_with_one_rule_with_newlines(self):
        data = "\n[[\"/\n/\n/\",\"preeti_rules\", \"preeti.patil@autodesk.com\"]]"
        test_xml_result = self.copyObject.custom_xml_configuration(data)   
        self.assertRaises(json.decoder.JSONDecodeError)
         
          
if __name__ == '__main__':             
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCreateProject)
    unittest.TextTestRunner(verbosity=2).run(suite)        


