from error import Error

import logging

class TypeError:
    
    TYPE_DIRECTLY_IDENTIFIABLE = 'Diretamente identificáveis'
    TYPE_MISINTERPRETATION_LANGUAGE = 'Interpretação equivocada da linguagem'
    TYPE_INDIRECTLY_IDENTIFIABLE = 'Indiretamente identificáveis'
    TYPE_UNCATEGORIZED_SOLUTION = 'Solução não-categorizável'

    SUBTYPE_DOMAIN_DEFICIENCY = 'Erro de deficiência no domínio ou uso inadequado de dados'
    SUBTYPE_OPERATOR_USAGE = 'Erro referente a uso de operador'
    SUBTYPE_RULE_DEFICIECY = 'Erro de deficiência de regra, teorema ou definição'
    SUBTYPE_NONE = ''
    
    def __init__(self):
        pass
    
    def __add_error_in_wm__(self, error, wm, rule_name, function_name):
        logging.info(f'A regra {rule_name} disparou a funçao {function_name}')
        errors = wm.get_fact('errors')
        errors.append(error)
        wm.add_fact('errors', errors)
    
    def not_valid(self, wm, rule_name):
        logging.info(f'A regra {rule_name} disparou a funçao not_valid')
        wm.add_fact('valid', False)
        
    def valid(self, wm, rule_name):
        logging.info(f'A regra {rule_name} disparou a funçao valid')
        wm.add_fact('valid', True)
        
    def error_rule_deficiency(self, wm, rule_name):
        error = Error(
                type=TypeError.TYPE_DIRECTLY_IDENTIFIABLE,
                subtype=TypeError.SUBTYPE_RULE_DEFICIECY
            )
        self.__add_error_in_wm__(error, wm, rule_name, 'error_rule_deficiency')
        
        
    def error_operator_usage(self, wm, rule_name):
        error = Error(
                type=TypeError.TYPE_DIRECTLY_IDENTIFIABLE,
                subtype=TypeError.SUBTYPE_OPERATOR_USAGE
            )
        self.__add_error_in_wm__(error, wm, rule_name, 'error_operator_usage')
        
    def error_domain_deficiency(self, wm, rule_name):
        error = Error(
                type=TypeError.TYPE_DIRECTLY_IDENTIFIABLE,
                subtype=TypeError.SUBTYPE_DOMAIN_DEFICIENCY
            )
        self.__add_error_in_wm__(error, wm, rule_name, 'error_domain_deficiency')
        
    def error_misinterpretation_language(self, wm, rule_name):
        error = Error(
                type=TypeError.TYPE_MISINTERPRETATION_LANGUAGE,
                subtype= TypeError.SUBTYPE_NONE
            )
        self.__add_error_in_wm__(error, wm, rule_name, 'error_misinterpretation_language')
    
    def error_indirectly_identifiable(self, wm, rule_name):
        error = Error(
                type=TypeError.TYPE_INDIRECTLY_IDENTIFIABLE,
                subtype= TypeError.SUBTYPE_NONE
            )
        self.__add_error_in_wm__(error, wm, rule_name, 'error_indirectly_identifiable')
        
    def error_uncategorized_solution(self, wm, rule_name):
        error = Error(
                type=TypeError.TYPE_UNCATEGORIZED_SOLUTION,
                subtype= TypeError.SUBTYPE_NONE
            )
        self.__add_error_in_wm__(error, wm, rule_name, 'error_uncategorized_solution')