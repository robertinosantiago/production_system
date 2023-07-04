import logging
import re

class Phase01Checks:
    
    def __init__(self):
        pass
        
    
    def zero_numbers(self, wm, rule_name):
        expression = wm.get_fact('expression')
        result = wm.get_fact('result')
        
        logging.info(f'Executando a regra: {rule_name}')
                
        if len(result) == 0:
            wm.add_fact('valid', False)
            logging.info(f'Confirmado regra: {rule_name}')
        
    def more_numbers(self, wm, rule_name):
        expression = wm.get_fact('expression')
        result = wm.get_fact('result')
        
        logging.info(f'Executando a regra: {rule_name}')
        
        if len(result) > 1:
            wm.add_fact('valid', False)
            logging.info(f'Confirmado regra: {rule_name}')
            
    def one_number(self, wm, rule_name):
        expression = wm.get_fact('expression')
        result = wm.get_fact('result')
        
        logging.info(f'Executando a regra: {rule_name}')
        
        if len(result) == 1:
            wm.add_fact('valid', True)
            logging.info(f'Confirmado regra: {rule_name}')
        
    
    def union_terms(self, wm, rule_name):
        expression = wm.get_fact('expression')
        result = wm.get_fact('result')
        
        logging.info(f'Executando a regra: {rule_name}')
        
        valid = wm.get_fact('valid')
                
        if not valid:
            part1, part2 = expression.split('=')
            
            r = re.compile(r'[^0-9]')
            numbers_expression = r.sub('', part1).strip()
                        
            result = ''.join(str(e) for e in result).strip()
             
            if result == numbers_expression:
                logging.info(f'Confirmado regra: {rule_name}')
                wm.add_fact('error_type', 'diretamente_identificaveis')
                wm.add_fact('error_subtype', 'deficiencia_regra')
    
    def switched_operators(self, wm, rule_name):
        expression = wm.get_fact('expression')
        result = wm.get_fact('result')
        
        logging.info(f'Executando a regra: {rule_name}')
        
        valid = wm.get_fact('valid')
        
        if valid:
            result = int(result[0])
            part1, part2 = expression.split('=')
            
            count_plus = part1.count('+')
            count_minus = part1.count('-')
            
            is_switched = False
            
            if count_plus + count_minus == 1:
                n1, op, n2 = part1
                n1 = int(n1)
                n2 = int(n2)
                if op == '+':
                    if n1 - n2 == result:
                        is_switched = True
                else:
                    if n1 + n2 == result:
                        is_switched = True
            else:
                n1, op1, n2, op2, n3 = part1
                n1 = int(n1)
                n2 = int(n2)
                n3 = int(n3)
                
                if op1 == '+':
                    if n1 - n2 + n3 == result:
                        is_switched = True
                    if n1 - n2 - n3 == result:
                        is_switched = True
                    if op2 == '+':
                        if n1 + n2 - n3 == result:
                            is_switched = True
                    else:
                        if n1 + n2 + n3 == result:
                            is_switched = True
                elif op1 == '-':
                    if n1 + n2 + n3 == result:
                        is_switched = True
                    if n1 + n2 - n3 == result:
                        is_switched = True
                    if op2 == '+':
                        if n1 - n2 - n3 == result:
                            is_switched = True
                    else:
                        if n1 - n2 + n3 == result:
                            is_switched = True
            
            if (is_switched):
                logging.info(f'Confirmado regra: {rule_name}')
                wm.add_fact('error_type', 'diretamente_identificaveis')
                wm.add_fact('error_subtype', 'uso_operador')
                
    def wrong_answer(self, wm, rule_name):
        expression = wm.get_fact('expression')
        result = wm.get_fact('result')
        
        logging.info(f'Executando a regra: {rule_name}')
        
        valid = wm.get_fact('valid')
            
        if valid:
            result = int(result[0])
            part1, part2 = expression.split('=')
            n = int(part2[0])
            
            if n != result:
                logging.info(f'Confirmado regra: {rule_name}')
                wm.add_fact('error_type', 'diretamente_identificaveis')
                wm.add_fact('error_subtype', 'deficiencia_dominio')
        
