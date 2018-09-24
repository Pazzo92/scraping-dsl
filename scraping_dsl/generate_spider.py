import distutils.core
import os
import re
import scrapy.cmdline
from shutil import copyfile

from scraping_dsl.base_generator import BaseGenerator
from scraping_dsl.root import BASE_PATH, SRC_DIR, EXAMPLES_PATH


class SpiderGenerator(BaseGenerator):
    def __init__(self, model, model_main):
        BaseGenerator.__init__(self, model, model_main)
        pass

    @staticmethod
    def init_folder_structure(folder_list):
        for folder in folder_list:
            if not os.path.exists(folder):
                os.makedirs(folder)
    @staticmethod
    def copy_necessary_files(necessary_source_path, base_path):
        distutils.dir_util.copy_tree(necessary_source_path, base_path)


    def generate_application(self, type, domain, custom_code=""):
        
        base_source_path = os.path.join('program')
        necessary_source_path = os.path.join(SRC_DIR, 'templates',
                                             'necessary_files')

        outputlocation = BASE_PATH
        examples_folder = os.path.join(EXAMPLES_PATH, "examples")

        # path to the target folder
        base_path = os.path.join(outputlocation, 'products')
        spiders_path = os.path.join(base_path, 'spiders')
        
        folder_gen_list = [base_path,spiders_path]
        # create and copy
        self.init_folder_structure(folder_gen_list)
        # generate files
        self.generate_program(base_source_path, spiders_path, base_path, type, domain, custom_code )
        
        self.copy_necessary_files(necessary_source_path, outputlocation)
        
          # custom py module
        module = type+"_type.py"
        copyfile(os.path.join(os.path.join(EXAMPLES_PATH, "examples"),domain+"/types/"+module), base_path+"/spiders/"+module)
        
        # post gen events
        self.generate_main(base_source_path,outputlocation, domain)
        
                          
    def generate_program(self, base_source_path, spiders_path, program_path, type, domain,  custom_code=""):
        # program files
        
        file_gen_list = {'__init__', 'items', 'middlewares', 'settings'}

        # generate the basic files
        for e in file_gen_list:
            self.generate(base_source_path + '/t{e}.tx'.format(e=e), '{e}.py'.format(e=e),
                          {'model': self.model, 'model_main': self.model_main}, program_path)
            
        self.generate(base_source_path+'/tpipelines.tx','pipelines.py', {'model': self.model_main}, program_path)
 
        spiders_file_gen_list = {'__init__', 'spider_'+domain} 
            
        for e in spiders_file_gen_list:
            self.generate(base_source_path + '/spiders' +  '/t{e}.tx'.format(e=e), '{e}.py'.format(e=e),
                          {'model': self.model, 'model_main': self.model_main}, program_path + '/spiders', custom_code)

            
    def generate_main(self, base_path, program_path, domain):

        self.generate(base_path+'/tmain.tx','main.py', {'model_main': self.model_main, 'domain' : domain}, program_path)   
        
        os.chdir(program_path)
        os.system('python ./main.py')