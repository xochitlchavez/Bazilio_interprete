grammar Bazilio;

/* ---------- Reglas del Parser ---------- */
programa : procedimiento+ EOF ;
 
procedimiento : PROC_ID VAR* bloque ;
 
bloque : INICIO instruccion* FIN ;
 
instruccion
    : VAR ASIGNA expr                            # Asignacion
    | LEE VAR                                    # Lectura
    | ESCRIBE (TEXTO | expr)*                    # Escritura
    | TOCA expr                                  # Reproduccion
    | PROC_ID expr*                              # Invocacion
    | SI expr bloque (SINO bloque)?              # Condicional
    | MIENTRAS expr bloque                       # Iteracion
    | VAR AGREGA expr                            # Agregado
    | CORTA VAR '[' expr ']'                     # Corte
    ;
 
expr
    : expr '[' expr ']'                          # Indice
    | LONG expr                                  # Longitud
    | expr op=(POR | ENTRE | MODULO) expr        # MulDiv
    | expr op=(MAS | MENOS) expr                 # SumaResta
    | expr op=(MENOR | MAYOR | MENORIGUAL | MAYORIGUAL) expr    # Relacional
    | expr op=(IGUAL | DISTINTO) expr            # Igualdad
    | '(' expr ')'                               # Parentesis
    | '{' (expr (',' expr)*)? '}'                # Lista
    | ENTERO                                     # Entero
    | NOTA                                       # Nota
    | VAR                                        # Variable
    ;

/* ---------- Símbolos ---------- */
INICIO : '|:' ;
FIN    : ':|' ;
ASIGNA : '<-' ;
LEE    : '<?>' ;
ESCRIBE: '<w>' ;
TOCA   : 'toca' ;
AGREGA : '<<' ;
CORTA  : '8<' ;
LONG   : '#' ;
 
MAS : '+' ;  MENOS : '-' ;  POR : '*' ;  ENTRE : '/' ;  MODULO : '%' ;
IGUAL : '=' ;  DISTINTO : '/=' ;
MENOR : '<' ;  MAYOR : '>' ;  MENORIGUAL : '<=' ;  MAYORIGUAL : '>=';
 
/* ---------- Palabras reservadas ---------- */
SI      : 'if' ;
SINO    : 'else' ;
MIENTRAS: 'while' ;
 
/* ---------- Valores e identificadores ---------- */
TEXTO   : '"' ~["\r\n]* '"' | '\u201C' ~[\u201D\r\n]* '\u201D' ;
ENTERO  : [0-9]+ ;
NOTA    : [A-G] [0-8]? ;
PROC_ID : [A-Z] [a-zA-Z0-9_]* ;
VAR     : [a-z] [a-zA-Z0-9_]* ;
 
COMENTARIO : ( '###' .*? '###' | '~~~' .*? '~~~' ) -> skip ;
ESPACIOS   : [ \t\r\n]+ -> skip ;