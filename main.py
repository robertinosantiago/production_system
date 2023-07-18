from memory import Memory
from rules import Rule
from inference import InferenceEngine
from phase01_checks import Phase01Checks
from error import Error
from type_error import TypeError

from datetime import datetime

import logging
import time


def main():
    logging.basicConfig(level=logging.INFO)
    
    wm = Memory()
    engine = InferenceEngine()
    phase01checks = Phase01Checks()
    type_error = TypeError()
    
    
    engine.add_rule(
        Rule(
            name = 'Nenhum numero',
            condition=lambda wm: phase01checks.zero_numbers(wm),
            action=type_error.not_valid
        )
    )
    
    engine.add_rule(
        Rule(
            name = 'Mais de um numero',
            condition=lambda wm: phase01checks.more_numbers(wm),
            action=type_error.not_valid
        )
    )
    
    engine.add_rule(
        Rule(
            name = 'Apenas um numero',
            condition=lambda wm: phase01checks.one_number(wm),
            action=type_error.valid
        )
    )
    
    engine.add_rule(
        Rule(
            name = 'Juncao de termos',
            condition=lambda wm: phase01checks.union_terms(wm),
            action=type_error.error_rule_deficiency
        )
    )
    
    engine.add_rule(
        Rule(
            name = 'Troca de operadores',
            condition=lambda wm: phase01checks.switched_operators(wm),
            action=type_error.error_operator_usage
        )
    )
    
    engine.add_rule(
        Rule(
            name = 'Resposta errada',
            condition=lambda wm: phase01checks.wrong_answer(wm),
            action=type_error.error_domain_deficiency
        )
    )
    
    engine.add_rule(
        Rule(
            name = 'Demora para responder',
            condition=lambda wm: phase01checks.long_time(wm),
            action=type_error.error_misinterpretation_language
        )
    )
    
    engine.add_rule(
        Rule(
            name = 'Resposta correta',
            condition=lambda wm: phase01checks.is_correct(wm),
            action=type_error.error_misinterpretation_language
        )
    )
    

    wm.add_fact('last_execution', datetime.now())
    time.sleep(5)    

    wm.add_fact('expression', '5+1-2=4')
    wm.add_fact('result', [3])
    
    engine.execute_rules(wm)
    
    print("Erros encontrados:")
    for e in wm.get_fact('errors'):
        print(e)
    
main()
