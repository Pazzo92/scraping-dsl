"""
Created on 06.12.2015.

@author: xx
"""

import os

from dsl.execute import execute
from dsl.generate_spider import SpiderGenerator
from dsl.root import SRC_DIR

def main(type,location="", filename="", output="", debug=False):
    
    model_path = os.path.join(os.path.join(SRC_DIR, "language"), type+'_type.rbt')
        
    file = open(model_path,'r')
    file_content = file.read().split("---")
    model_str = file_content[0]
    custom_code = file_content[1]
    custom_code += "\nyield " + type

    model = execute(os.path.join(SRC_DIR, "language"), 'type.tx', type+'_type.rbt', debug, debug , model_str)

    model_main = execute(os.path.join(SRC_DIR, "language"), 'products_mining.tx', type+'_program.rbt', debug, debug)
    
    generator = SpiderGenerator(model, model_main)
    generator.generate_application(type, custom_code)
    
if __name__ == '__main__':
    
    # DEFINE THE TYPE OF THE SCRAPING ITEM
    type = "poslanik"
    main(type, False)
