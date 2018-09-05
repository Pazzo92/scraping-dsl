import distutils.core
import os
import re
import scrapy.cmdline

from dsl.base_generator import BaseGenerator
from dsl.root import BASE_PATH, SRC_DIR


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


    def generate_application(self, location=""):
        # path to django templates
        base_source_path = os.path.join('program')
        necessary_source_path = os.path.join(SRC_DIR, 'templates',
                                             'necessary_files')

        if not location:
            outputlocation = BASE_PATH
        else:
            outputlocation = location

        # path to the target folder
        base_path = os.path.join(outputlocation, 'products')
        spiders_path = os.path.join(base_path, 'spiders')
        
        folder_gen_list = [base_path,spiders_path]
        # create and copy
        self.init_folder_structure(folder_gen_list)
        # generate files
        self.generate_program(base_source_path, spiders_path, base_path)
        
        self.copy_necessary_files(necessary_source_path, outputlocation)
        # post gen events
        self.generate_main(base_source_path,outputlocation)

    def generate_program(self, base_source_path, spiders_path, program_path):
        # program files
        
        file_gen_list = {'__init__', 'items', 'middlewares', 'settings'}

        # generate the basic files
        for e in file_gen_list:
            self.generate(base_source_path + '/t{e}.tx'.format(e=e), '{e}.py'.format(e=e),
                          {'model': self.model, 'model_main': self.model_main}, program_path)
            
        self.generate(base_source_path+'/tpipelines.tx','pipelines.py', {'model': self.model_main}, program_path)
            
        spiders_file_gen_list = {'__init__', 'spider_gigatron', 'spider_winwin'}
            
        for e in spiders_file_gen_list:
            self.generate(base_source_path + '/spiders' +  '/t{e}.tx'.format(e=e), '{e}.py'.format(e=e),
                          {'model': self.model, 'model_main': self.model_main}, program_path + '/spiders')
            
    def generate_main(self, base_path, program_path):
       
        self.generate(base_path+'/tmain.tx','main.py', {'model_main': self.model_main}, program_path)
        
        os.chdir(program_path)
        os.system('python ./main.py')