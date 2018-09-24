'''
Created on 06.12.2015.

@author: xx
'''

import os
import re

import pydot
from textx.export import metamodel_export, model_export
from textx.metamodel import metamodel_from_file
from scraping_dsl.root import SRC_DIR


def execute(path, grammar_file_name, example_file_name, export_dot, export_png):
    """U svrhe brzeg testiranja, metoda koja prima putanju do foldera, naziv fajla gde je gramatika i naziv fajla gde je
        primer programa u nasem jeziku i indikator da li da se eksportuju .dot i .png fajlovi"""

    meta_path = os.path.join(SRC_DIR, 'language', grammar_file_name)
    meta_name = os.path.splitext(meta_path)[0]
    metamodel = metamodel_from_file(meta_path)

    if export_dot:
        metamodel_export(metamodel, meta_name + '.dot')
        if export_png:
            graph = pydot.graph_from_dot_file(meta_name + '.dot')
            graph.write_png(meta_name + '.png')

    model_path = os.path.join(path, example_file_name)
    model_name = os.path.splitext(model_path)[0]

    model = metamodel.model_from_file(model_path)
    
    
    if export_dot:
        model_export(model, model_name + '.dot')
    if export_png:
        graph = pydot.graph_from_dot_file(model_name + '.dot')
        graph.write_png(model_name + '.png')

    return model
