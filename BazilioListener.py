# Generated from Bazilio.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BazilioParser import BazilioParser
else:
    from BazilioParser import BazilioParser

# This class defines a complete listener for a parse tree produced by BazilioParser.
class BazilioListener(ParseTreeListener):

    # Enter a parse tree produced by BazilioParser#programa.
    def enterPrograma(self, ctx:BazilioParser.ProgramaContext):
        pass

    # Exit a parse tree produced by BazilioParser#programa.
    def exitPrograma(self, ctx:BazilioParser.ProgramaContext):
        pass


    # Enter a parse tree produced by BazilioParser#procedimiento.
    def enterProcedimiento(self, ctx:BazilioParser.ProcedimientoContext):
        pass

    # Exit a parse tree produced by BazilioParser#procedimiento.
    def exitProcedimiento(self, ctx:BazilioParser.ProcedimientoContext):
        pass


    # Enter a parse tree produced by BazilioParser#bloque.
    def enterBloque(self, ctx:BazilioParser.BloqueContext):
        pass

    # Exit a parse tree produced by BazilioParser#bloque.
    def exitBloque(self, ctx:BazilioParser.BloqueContext):
        pass


    # Enter a parse tree produced by BazilioParser#Asignacion.
    def enterAsignacion(self, ctx:BazilioParser.AsignacionContext):
        pass

    # Exit a parse tree produced by BazilioParser#Asignacion.
    def exitAsignacion(self, ctx:BazilioParser.AsignacionContext):
        pass


    # Enter a parse tree produced by BazilioParser#Lectura.
    def enterLectura(self, ctx:BazilioParser.LecturaContext):
        pass

    # Exit a parse tree produced by BazilioParser#Lectura.
    def exitLectura(self, ctx:BazilioParser.LecturaContext):
        pass


    # Enter a parse tree produced by BazilioParser#Escritura.
    def enterEscritura(self, ctx:BazilioParser.EscrituraContext):
        pass

    # Exit a parse tree produced by BazilioParser#Escritura.
    def exitEscritura(self, ctx:BazilioParser.EscrituraContext):
        pass


    # Enter a parse tree produced by BazilioParser#Reproduccion.
    def enterReproduccion(self, ctx:BazilioParser.ReproduccionContext):
        pass

    # Exit a parse tree produced by BazilioParser#Reproduccion.
    def exitReproduccion(self, ctx:BazilioParser.ReproduccionContext):
        pass


    # Enter a parse tree produced by BazilioParser#Invocacion.
    def enterInvocacion(self, ctx:BazilioParser.InvocacionContext):
        pass

    # Exit a parse tree produced by BazilioParser#Invocacion.
    def exitInvocacion(self, ctx:BazilioParser.InvocacionContext):
        pass


    # Enter a parse tree produced by BazilioParser#Condicional.
    def enterCondicional(self, ctx:BazilioParser.CondicionalContext):
        pass

    # Exit a parse tree produced by BazilioParser#Condicional.
    def exitCondicional(self, ctx:BazilioParser.CondicionalContext):
        pass


    # Enter a parse tree produced by BazilioParser#Iteracion.
    def enterIteracion(self, ctx:BazilioParser.IteracionContext):
        pass

    # Exit a parse tree produced by BazilioParser#Iteracion.
    def exitIteracion(self, ctx:BazilioParser.IteracionContext):
        pass


    # Enter a parse tree produced by BazilioParser#Agregado.
    def enterAgregado(self, ctx:BazilioParser.AgregadoContext):
        pass

    # Exit a parse tree produced by BazilioParser#Agregado.
    def exitAgregado(self, ctx:BazilioParser.AgregadoContext):
        pass


    # Enter a parse tree produced by BazilioParser#Corte.
    def enterCorte(self, ctx:BazilioParser.CorteContext):
        pass

    # Exit a parse tree produced by BazilioParser#Corte.
    def exitCorte(self, ctx:BazilioParser.CorteContext):
        pass


    # Enter a parse tree produced by BazilioParser#Indice.
    def enterIndice(self, ctx:BazilioParser.IndiceContext):
        pass

    # Exit a parse tree produced by BazilioParser#Indice.
    def exitIndice(self, ctx:BazilioParser.IndiceContext):
        pass


    # Enter a parse tree produced by BazilioParser#Lista.
    def enterLista(self, ctx:BazilioParser.ListaContext):
        pass

    # Exit a parse tree produced by BazilioParser#Lista.
    def exitLista(self, ctx:BazilioParser.ListaContext):
        pass


    # Enter a parse tree produced by BazilioParser#Variable.
    def enterVariable(self, ctx:BazilioParser.VariableContext):
        pass

    # Exit a parse tree produced by BazilioParser#Variable.
    def exitVariable(self, ctx:BazilioParser.VariableContext):
        pass


    # Enter a parse tree produced by BazilioParser#Relacional.
    def enterRelacional(self, ctx:BazilioParser.RelacionalContext):
        pass

    # Exit a parse tree produced by BazilioParser#Relacional.
    def exitRelacional(self, ctx:BazilioParser.RelacionalContext):
        pass


    # Enter a parse tree produced by BazilioParser#Entero.
    def enterEntero(self, ctx:BazilioParser.EnteroContext):
        pass

    # Exit a parse tree produced by BazilioParser#Entero.
    def exitEntero(self, ctx:BazilioParser.EnteroContext):
        pass


    # Enter a parse tree produced by BazilioParser#MulDiv.
    def enterMulDiv(self, ctx:BazilioParser.MulDivContext):
        pass

    # Exit a parse tree produced by BazilioParser#MulDiv.
    def exitMulDiv(self, ctx:BazilioParser.MulDivContext):
        pass


    # Enter a parse tree produced by BazilioParser#Parentesis.
    def enterParentesis(self, ctx:BazilioParser.ParentesisContext):
        pass

    # Exit a parse tree produced by BazilioParser#Parentesis.
    def exitParentesis(self, ctx:BazilioParser.ParentesisContext):
        pass


    # Enter a parse tree produced by BazilioParser#Longitud.
    def enterLongitud(self, ctx:BazilioParser.LongitudContext):
        pass

    # Exit a parse tree produced by BazilioParser#Longitud.
    def exitLongitud(self, ctx:BazilioParser.LongitudContext):
        pass


    # Enter a parse tree produced by BazilioParser#Nota.
    def enterNota(self, ctx:BazilioParser.NotaContext):
        pass

    # Exit a parse tree produced by BazilioParser#Nota.
    def exitNota(self, ctx:BazilioParser.NotaContext):
        pass


    # Enter a parse tree produced by BazilioParser#Igualdad.
    def enterIgualdad(self, ctx:BazilioParser.IgualdadContext):
        pass

    # Exit a parse tree produced by BazilioParser#Igualdad.
    def exitIgualdad(self, ctx:BazilioParser.IgualdadContext):
        pass


    # Enter a parse tree produced by BazilioParser#SumaResta.
    def enterSumaResta(self, ctx:BazilioParser.SumaRestaContext):
        pass

    # Exit a parse tree produced by BazilioParser#SumaResta.
    def exitSumaResta(self, ctx:BazilioParser.SumaRestaContext):
        pass



del BazilioParser