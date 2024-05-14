def failte_ainm() -> str:
    print("== Fáilte go Crochadóir ==")
    print("Cad is ainm duit?")
    return input()

def taispean_crochadoir(iarrachtai):
    ceimeanna = [  # cuid deireanach: ceann, corp, dhá lámh, agus dhá chos
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # ceann, corp, dhá lámh, agus cos amháin
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # ceann, corp agus dhá lámh
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # ceann, corp agus lámh amháin
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # ceann agus corp
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # ceann
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # rud ar bith
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return ceimeanna[iarrachtai]