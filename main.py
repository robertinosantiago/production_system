from memory import Memory
from rules import Rule
from inference import InferenceEngine
from phase01_checks import Phase01Checks
import logging

def main():
    logging.basicConfig(level=logging.INFO)
    
    wm = Memory()
    engine = InferenceEngine()
    phase01checks = Phase01Checks()
    
    
    engine.add_rule(
        Rule(
            name = 'Nenhum numero',
            condition=lambda wm: True,
            action=phase01checks.zero_numbers
        )
    )
    engine.add_rule(
        Rule(
            name = 'Mais de um numero',
            condition=lambda wm: True,
            action=phase01checks.more_numbers
        )
    )
    engine.add_rule(
        Rule(
            name = 'Apenas um numero',
            condition=lambda wm: True,
            action=phase01checks.one_number
        )
    )
    engine.add_rule(
        Rule(
            name = 'Juncao de termos',
            condition=lambda wm: True,
            action=phase01checks.union_terms
        )
    )
    engine.add_rule(
        Rule(
            name = 'Troca de operadores',
            condition=lambda wm: True,
            action=phase01checks.switched_operators
        )
    )
    
    engine.add_rule(
        Rule(
            name = 'Resposta errada',
            condition=lambda wm: True,
            action=phase01checks.wrong_answer
        )
    )
    

    wm.add_fact('expression', '5+1-2=4')
    wm.add_fact('result', [2])
    
    engine.execute_rules(wm)
    
main()