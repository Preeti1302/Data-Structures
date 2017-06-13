#!/usr/bin/env python3

"""
This script is to help automate the on-boarding of projects using Globalyzer's pull-request workflow.
"""

import os
import sys 
import json
from json import JSONDecoder
import optparse
from shutil import copytree
from distutils.sysconfig import project_base
from string import Template
import re 

__version__ = 1.0

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class copyDirectory(object):
    #Run all the functions through this function
    def runCommandLine(self):
        desc = """This is a command-line tool for initializing a new project configuration based off of the master project template directory: "1_MASTER_PROJ_TEMPLATE".
The result should be a directory, named after your project, containing the configuration files required for the pull-request workflow."""
        usage = "%prog -p adsk.ph-js-pr-test \\\n\t\t\t -g 'i18n/ph-js-pr-testing' \
\\\n\t\t\t -r {\"scans\": [[\"java_dir\",\"js_ph_java_rules\",\"js_ph@autodesk.com\"],\n\t\t\t\t\t[\"python_dir\",\"python_rules\",\"js_ph_gz@autodesk.com\"],\n\t\t\t\t\t[\"c++_dir\",\"C++_rules\",\"js_ph@autodesk.com\"]] }"
        p = optparse.OptionParser(description=desc,
                                prog='create_project.py',
                                version='create_project.py %s' % __version__,
                                usage=usage)
        #Parser option to take Project name as input from User
        p.add_option("-p", "--project_name",
                     dest='project_name',
                     help="Provide a unique project name starting with \'adsk.\' and \
including your initials and a project identifier. \
Valid characters may include (regex): [.a-zA-Z_0-9-]")
        #Parser option to take Github Repository name as input from User
        p.add_option("-g", "--github_repo",
                     dest='github_repo',
                     help="Provide the Github Repository name.")
        #Parser option to take Ruleset name as input from User
        p.add_option("-r", "--ruleset_name",
                     action='store',
                     type='string',
                     dest='ruleset_name_scan',
                     help="This option is provided to you to perform single scan or complex scans. Provide the data with a key named 'scans'. Format of the data is provided in the usage")
                                    
        (options, arguments) = p.parse_args()
        
        if options.project_name is not None and len(options.project_name)<=20:
            project_name = options.project_name
            #if project_name.startswith('adsk.') and re.search(r'^[.a-zA-Z_0-9-]*$' , project_name):
            github_repo = options.github_repo
            ruleset_info = options.ruleset_name_scan
            xml_output = self.custom_xml_configuration(ruleset_info)
            #print("Return value: %s" % list(xml_output))
            
            output_of_copying= self.copyTemplate(project_name, github_repo)
            if output_of_copying == "Success":
                #print("XML:::::: %s"  % xml_output)
                self.swap_Variables(project_name , github_repo ,  xml_output)
                print("Your Project Directory %s is successfully created along with swapped variables !!" % project_name)
            elif output_of_copying == "Exists" :
                print("\n ********Project name needs to be unique*********\n\nThis project name already exists!! ")
            else:
                print("\n\nChange the name according to standard format!! \n\nProject name should start with prefix 'adsk.' and then the name of the project \n\n No spaces allowed. Allowed characters are: . a-z A-Z _ 0-9 - * \n\nExample:'adsk.project_name'")
          
        else:
            print("\n\nPlease enter the project name  ! \n\n Maximum 20 characters allowed")
            p.print_usage() 

    #Function that facilitates to make copy of the directory 
    def copyTemplate(self , project_name , github_repo):
        if project_name.startswith('adsk.') and re.search(r'^[.a-zA-Z_0-9-]*$' , project_name):
            path_newProject = os.path.join(BASE_DIR , project_name)
            template_dir = os.path.join(BASE_DIR,"1_MASTER_PROJ_TEMPLATE")
            #print(self.options.project_name)
            if os.path.exists(path_newProject):
                return "Exists"
            else:
                copytree(template_dir, path_newProject)
                return "Success"
        else:
            return "Validation error"
    
    #Swapping place-holders for RUN_SCAN.sh
    def configure_RUNSCAN(self , project_name):
        file_RUN_SCAN = os.path.join(os.path.join(BASE_DIR , project_name), '1-RUN-SCAN.sh')
         
        with open(file_RUN_SCAN, 'r') as file1:
            src = Template( file1.read() )
            d = { 'PROJECT_NAME': project_name }
            result = src.safe_substitute(d)
            #print(result)
            file1.closed
            with open(file_RUN_SCAN, 'w') as file1:
                file1.write(result)
                file1.closed
        
        return result
    
    #Swapping place-holders for projectDef.xml
    def configure_projDef(self ,project_name , github_repo , xml_output):
        file_Projdef = os.path.join(os.path.join(BASE_DIR , project_name), 'projdef.xml')
         
        with open(file_Projdef, 'r') as file2:
                src = Template( file2.read()) 
                d = { 'PROJECT_NAME': project_name , 'XML_TEMPLATE': xml_output}
                result = src.safe_substitute(d)
                file2.closed
                with open(file_Projdef, 'w') as file2:
                    file2.write(result)
                    file2.closed
        
        return result
    
    #Swapping place-holders for Sonar Properties
    def configure_SONAR(self , project_name , github_repo ):
        file_SONAR = os.path.join(os.path.join(BASE_DIR , project_name), 'sonar-project-template.properties')
        with open(file_SONAR, 'r') as file3:
            src = Template( file3.read())
            d = { 'PROJECT_NAME': project_name , 'GITHUB_REPO' : github_repo}
            result = src.safe_substitute(d)
            #print(result)
            file3.closed
            with open(file_SONAR, 'w') as file3:
                file3.write(result)
                file3.closed
        
        return result
        
 
    #Swap the place-holders with the variables   
    def swap_Variables(self , project_name , github_repo , xml_output ):
        self.configure_RUNSCAN(project_name)
        self.configure_projDef(project_name, github_repo,  xml_output)
        self.configure_SONAR(project_name, github_repo)
    
    #Function that allows customization of xml according to different rulesets 
    def custom_xml_configuration(self , ruleset_info):
        try:
            #print("Ruleset Info : %s" % ruleset_info) 
            scanner_information = json.loads(ruleset_info)
            #print("Scanner Info: %s" % scanner_information['scans'])
            results = {}
            #e.g: ["/2","preeti_ruless", "preeti.patil@autodesk.com"]
            for scan_info in scanner_information['scans']:
                #print("Scan Info = %s" % scan_info)
                if len(scan_info) != 3:
                    print("ERROR: invalid data structure!")
                    sys.exit()
                    
                key_combination = "::".join(scan_info[-2:])
                if key_combination in results:
                    results[key_combination].append(scan_info[0])
                else:
                    results[key_combination] = [scan_info[0]]
            sorted_keys = sorted(list(results.keys()))
            #print("[Sorted list of keys] %s " % sorted_keys)
            xml_output = ""
            for key in sorted_keys:
                #print("Current key: %s" % key)
                results[key] = list(set(results[key]))
                sorted_keys = sorted(list(results.keys()))
                ruleset_name = key.split("::")[0]
                ruleset_owner = key.split("::")[1]
                sorted_dir_list = sorted(results[key])
                items_xml = ""
                #print("Sorted list : %s " %sorted_dir_list)
                for i in sorted_dir_list:
                    items_xml = items_xml + ("""<item>%s</item>""" % i)

                    items_xml_newlines = items_xml.replace("><", ">\n            <")

                xml_output = xml_output + ("""\
    <scan>
        <scan-name>%s_scan</scan-name>
        <ruleset-name>%s</ruleset-name>
        <ruleset-owner>%s</ruleset-owner>
        <scan-items>
            %s
        </scan-items>
    </scan>\n""" % (ruleset_name, ruleset_name, ruleset_owner, items_xml_newlines))
            return  xml_output
        
        except json.decoder.JSONDecodeError:
            print("Faced a Decode Error ")  
#Main Function        
def main():    
    c = copyDirectory()
    c.runCommandLine()  

if __name__ == "__main__":
    main()
