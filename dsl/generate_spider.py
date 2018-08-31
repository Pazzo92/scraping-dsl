import distutils.core

import os
import re
import scrapy

from dsl.base_generator import BaseGenerator
from dsl.root import BASE_PATH, SRC_DIR


class SpiderGenerator(BaseGenerator):
    def __init__(self, model):
        BaseGenerator.__init__(self, model)
        pass

    @staticmethod
    def init_folder_structure(folder_list):
        for folder in folder_list:
            if not os.path.exists(folder):
                os.makedirs(folder)
    @staticmethod
    def call_post_gen_script(base_path):
        os.chdir(base_path)
        scrapy.cmdline.execute(argv=['scrapy', 'crawl', 'winwin_laptops'])


    def generate_application(self, location=""):
        # path to django templates
        base_source_path = os.path.join('program')

        if not location:
            outputlocation = BASE_PATH
        else:
            outputlocation = location

        # path to the target folder
        base_path = os.path.join(outputlocation, 'products_mining')
        spiders_path = os.path.join(base_path, 'spiders')
        
        folder_gen_list = [base_path,spiders_path]
        # create and copy
        self.init_folder_structure(folder_gen_list)
        # generate files
        self.generate_program(base_source_path, spiders_path, base_path)

        # post gen events
        # self.call_post_gen_script(base_path)

    def generate_program(self, base_source_path, spiders_path, program_path):
        # program files
        
        file_gen_list = {'__init__', 'items', 'middlewares', 'pipelines', 'settings'}

        # generate the basic files
        for e in file_gen_list:
            self.generate(base_source_path + '/t{e}.tx'.format(e=e), '{e}.py'.format(e=e),
                          {'model': self.model}, program_path)
            
        spiders_file_gen_list = {'__init__', 'spiders'}
            
        for e in spiders_file_gen_list:
            self.generate(base_source_path + '/spiders' +  '/t{e}.tx'.format(e=e), '{e}.py'.format(e=e),
                          {'model': self.model}, program_path + '/spiders')
            
        