# Generated from Bazilio.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BazilioParser import BazilioParser
else:
    from BazilioParser import BazilioParser

# This class defines a complete generic visitor for a parse tree produced by BazilioParser.

class BazilioVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BazilioParser#programa.
    def visitPrograma(self, ctx:BazilioParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#procedimiento.
    def visitProcedimiento(self, ctx:BazilioParser.ProcedimientoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#bloque.
    def visitBloque(self, ctx:BazilioParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Asignacion.
    def visitAsignacion(self, ctx:BazilioParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Lectura.
    def visitLectura(self, ctx:BazilioParser.LecturaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Escritura.
    def visitEscritura(self, ctx:BazilioParser.EscrituraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Reproduccion.
    def visitReproduccion(self, ctx:BazilioParser.ReproduccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Invocacion.
    def visitInvocacion(self, ctx:BazilioParser.InvocacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Condicional.
    def visitCondicional(self, ctx:BazilioParser.CondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Iteracion.
    def visitIteracion(self, ctx:BazilioParser.IteracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Agregado.
    def visitAgregado(self, ctx:BazilioParser.AgregadoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Corte.
    def visitCorte(self, ctx:BazilioParser.CorteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Indice.
    def visitIndice(self, ctx:BazilioParser.IndiceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Lista.
    def visitLista(self, ctx:BazilioParser.ListaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Variable.
    def visitVariable(self, ctx:BazilioParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Relacional.
    def visitRelacional(self, ctx:BazilioParser.RelacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Entero.
    def visitEntero(self, ctx:BazilioParser.EnteroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#MulDiv.
    def visitMulDiv(self, ctx:BazilioParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Parentesis.
    def visitParentesis(self, ctx:BazilioParser.ParentesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Longitud.
    def visitLongitud(self, ctx:BazilioParser.LongitudContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Nota.
    def visitNota(self, ctx:BazilioParser.NotaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Igualdad.
    def visitIgualdad(self, ctx:BazilioParser.IgualdadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#SumaResta.
    def visitSumaResta(self, ctx:BazilioParser.SumaRestaContext):
        return self.visitChildren(ctx)



del BazilioParser