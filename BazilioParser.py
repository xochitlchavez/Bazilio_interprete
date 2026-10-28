# Generated from Bazilio.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,37,126,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,4,0,12,8,
        0,11,0,12,0,13,1,0,1,0,1,1,1,1,5,1,20,8,1,10,1,12,1,23,9,1,1,1,1,
        1,1,2,1,2,5,2,29,8,2,10,2,12,2,32,9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,5,3,44,8,3,10,3,12,3,47,9,3,1,3,1,3,1,3,1,3,5,3,53,
        8,3,10,3,12,3,56,9,3,1,3,1,3,1,3,1,3,1,3,3,3,63,8,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,78,8,3,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,91,8,4,10,4,12,4,94,9,4,3,4,96,
        8,4,1,4,1,4,1,4,1,4,3,4,102,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,121,8,4,10,4,12,4,124,9,
        4,1,4,0,1,8,5,0,2,4,6,8,0,4,1,0,19,21,1,0,17,18,1,0,24,27,1,0,22,
        23,147,0,11,1,0,0,0,2,17,1,0,0,0,4,26,1,0,0,0,6,77,1,0,0,0,8,101,
        1,0,0,0,10,12,3,2,1,0,11,10,1,0,0,0,12,13,1,0,0,0,13,11,1,0,0,0,
        13,14,1,0,0,0,14,15,1,0,0,0,15,16,5,0,0,1,16,1,1,0,0,0,17,21,5,34,
        0,0,18,20,5,35,0,0,19,18,1,0,0,0,20,23,1,0,0,0,21,19,1,0,0,0,21,
        22,1,0,0,0,22,24,1,0,0,0,23,21,1,0,0,0,24,25,3,4,2,0,25,3,1,0,0,
        0,26,30,5,8,0,0,27,29,3,6,3,0,28,27,1,0,0,0,29,32,1,0,0,0,30,28,
        1,0,0,0,30,31,1,0,0,0,31,33,1,0,0,0,32,30,1,0,0,0,33,34,5,9,0,0,
        34,5,1,0,0,0,35,36,5,35,0,0,36,37,5,10,0,0,37,78,3,8,4,0,38,39,5,
        11,0,0,39,78,5,35,0,0,40,45,5,12,0,0,41,44,5,31,0,0,42,44,3,8,4,
        0,43,41,1,0,0,0,43,42,1,0,0,0,44,47,1,0,0,0,45,43,1,0,0,0,45,46,
        1,0,0,0,46,78,1,0,0,0,47,45,1,0,0,0,48,49,5,13,0,0,49,78,3,8,4,0,
        50,54,5,34,0,0,51,53,3,8,4,0,52,51,1,0,0,0,53,56,1,0,0,0,54,52,1,
        0,0,0,54,55,1,0,0,0,55,78,1,0,0,0,56,54,1,0,0,0,57,58,5,28,0,0,58,
        59,3,8,4,0,59,62,3,4,2,0,60,61,5,29,0,0,61,63,3,4,2,0,62,60,1,0,
        0,0,62,63,1,0,0,0,63,78,1,0,0,0,64,65,5,30,0,0,65,66,3,8,4,0,66,
        67,3,4,2,0,67,78,1,0,0,0,68,69,5,35,0,0,69,70,5,14,0,0,70,78,3,8,
        4,0,71,72,5,15,0,0,72,73,5,35,0,0,73,74,5,1,0,0,74,75,3,8,4,0,75,
        76,5,2,0,0,76,78,1,0,0,0,77,35,1,0,0,0,77,38,1,0,0,0,77,40,1,0,0,
        0,77,48,1,0,0,0,77,50,1,0,0,0,77,57,1,0,0,0,77,64,1,0,0,0,77,68,
        1,0,0,0,77,71,1,0,0,0,78,7,1,0,0,0,79,80,6,4,-1,0,80,81,5,16,0,0,
        81,102,3,8,4,10,82,83,5,3,0,0,83,84,3,8,4,0,84,85,5,4,0,0,85,102,
        1,0,0,0,86,95,5,5,0,0,87,92,3,8,4,0,88,89,5,6,0,0,89,91,3,8,4,0,
        90,88,1,0,0,0,91,94,1,0,0,0,92,90,1,0,0,0,92,93,1,0,0,0,93,96,1,
        0,0,0,94,92,1,0,0,0,95,87,1,0,0,0,95,96,1,0,0,0,96,97,1,0,0,0,97,
        102,5,7,0,0,98,102,5,32,0,0,99,102,5,33,0,0,100,102,5,35,0,0,101,
        79,1,0,0,0,101,82,1,0,0,0,101,86,1,0,0,0,101,98,1,0,0,0,101,99,1,
        0,0,0,101,100,1,0,0,0,102,122,1,0,0,0,103,104,10,9,0,0,104,105,7,
        0,0,0,105,121,3,8,4,10,106,107,10,8,0,0,107,108,7,1,0,0,108,121,
        3,8,4,9,109,110,10,7,0,0,110,111,7,2,0,0,111,121,3,8,4,8,112,113,
        10,6,0,0,113,114,7,3,0,0,114,121,3,8,4,7,115,116,10,11,0,0,116,117,
        5,1,0,0,117,118,3,8,4,0,118,119,5,2,0,0,119,121,1,0,0,0,120,103,
        1,0,0,0,120,106,1,0,0,0,120,109,1,0,0,0,120,112,1,0,0,0,120,115,
        1,0,0,0,121,124,1,0,0,0,122,120,1,0,0,0,122,123,1,0,0,0,123,9,1,
        0,0,0,124,122,1,0,0,0,13,13,21,30,43,45,54,62,77,92,95,101,120,122
    ]

class BazilioParser ( Parser ):

    grammarFileName = "Bazilio.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "'('", "')'", "'{'", "','", 
                     "'}'", "'|:'", "':|'", "'<-'", "'<?>'", "'<w>'", "'toca'", 
                     "'<<'", "'8<'", "'#'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'='", "'/='", "'<'", "'>'", "'<='", "'>='", 
                     "'if'", "'else'", "'while'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "INICIO", "FIN", "ASIGNA", "LEE", "ESCRIBE", "TOCA", 
                      "AGREGA", "CORTA", "LONG", "MAS", "MENOS", "POR", 
                      "ENTRE", "MODULO", "IGUAL", "DISTINTO", "MENOR", "MAYOR", 
                      "MENORIGUAL", "MAYORIGUAL", "SI", "SINO", "MIENTRAS", 
                      "TEXTO", "ENTERO", "NOTA", "PROC_ID", "VAR", "COMENTARIO", 
                      "ESPACIOS" ]

    RULE_programa = 0
    RULE_procedimiento = 1
    RULE_bloque = 2
    RULE_instruccion = 3
    RULE_expr = 4

    ruleNames =  [ "programa", "procedimiento", "bloque", "instruccion", 
                   "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    INICIO=8
    FIN=9
    ASIGNA=10
    LEE=11
    ESCRIBE=12
    TOCA=13
    AGREGA=14
    CORTA=15
    LONG=16
    MAS=17
    MENOS=18
    POR=19
    ENTRE=20
    MODULO=21
    IGUAL=22
    DISTINTO=23
    MENOR=24
    MAYOR=25
    MENORIGUAL=26
    MAYORIGUAL=27
    SI=28
    SINO=29
    MIENTRAS=30
    TEXTO=31
    ENTERO=32
    NOTA=33
    PROC_ID=34
    VAR=35
    COMENTARIO=36
    ESPACIOS=37

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BazilioParser.EOF, 0)

        def procedimiento(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazilioParser.ProcedimientoContext)
            else:
                return self.getTypedRuleContext(BazilioParser.ProcedimientoContext,i)


        def getRuleIndex(self):
            return BazilioParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = BazilioParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.procedimiento()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==34):
                    break

            self.state = 15
            self.match(BazilioParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProcedimientoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROC_ID(self):
            return self.getToken(BazilioParser.PROC_ID, 0)

        def bloque(self):
            return self.getTypedRuleContext(BazilioParser.BloqueContext,0)


        def VAR(self, i:int=None):
            if i is None:
                return self.getTokens(BazilioParser.VAR)
            else:
                return self.getToken(BazilioParser.VAR, i)

        def getRuleIndex(self):
            return BazilioParser.RULE_procedimiento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProcedimiento" ):
                listener.enterProcedimiento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProcedimiento" ):
                listener.exitProcedimiento(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcedimiento" ):
                return visitor.visitProcedimiento(self)
            else:
                return visitor.visitChildren(self)




    def procedimiento(self):

        localctx = BazilioParser.ProcedimientoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_procedimiento)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.match(BazilioParser.PROC_ID)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==35:
                self.state = 18
                self.match(BazilioParser.VAR)
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INICIO(self):
            return self.getToken(BazilioParser.INICIO, 0)

        def FIN(self):
            return self.getToken(BazilioParser.FIN, 0)

        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazilioParser.InstruccionContext)
            else:
                return self.getTypedRuleContext(BazilioParser.InstruccionContext,i)


        def getRuleIndex(self):
            return BazilioParser.RULE_bloque

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque" ):
                listener.enterBloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque" ):
                listener.exitBloque(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = BazilioParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_bloque)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(BazilioParser.INICIO)
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 52881831936) != 0):
                self.state = 27
                self.instruccion()
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 33
            self.match(BazilioParser.FIN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BazilioParser.RULE_instruccion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IteracionContext(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MIENTRAS(self):
            return self.getToken(BazilioParser.MIENTRAS, 0)
        def expr(self):
            return self.getTypedRuleContext(BazilioParser.ExprContext,0)

        def bloque(self):
            return self.getTypedRuleContext(BazilioParser.BloqueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIteracion" ):
                listener.enterIteracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIteracion" ):
                listener.exitIteracion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIteracion" ):
                return visitor.visitIteracion(self)
            else:
                return visitor.visitChildren(self)


    class AsignacionContext(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(BazilioParser.VAR, 0)
        def ASIGNA(self):
            return self.getToken(BazilioParser.ASIGNA, 0)
        def expr(self):
            return self.getTypedRuleContext(BazilioParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)


    class CorteContext(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CORTA(self):
            return self.getToken(BazilioParser.CORTA, 0)
        def VAR(self):
            return self.getToken(BazilioParser.VAR, 0)
        def expr(self):
            return self.getTypedRuleContext(BazilioParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCorte" ):
                listener.enterCorte(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCorte" ):
                listener.exitCorte(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCorte" ):
                return visitor.visitCorte(self)
            else:
                return visitor.visitChildren(self)


    class EscrituraContext(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ESCRIBE(self):
            return self.getToken(BazilioParser.ESCRIBE, 0)
        def TEXTO(self, i:int=None):
            if i is None:
                return self.getTokens(BazilioParser.TEXTO)
            else:
                return self.getToken(BazilioParser.TEXTO, i)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazilioParser.ExprContext)
            else:
                return self.getTypedRuleContext(BazilioParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEscritura" ):
                listener.enterEscritura(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEscritura" ):
                listener.exitEscritura(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEscritura" ):
                return visitor.visitEscritura(self)
            else:
                return visitor.visitChildren(self)


    class LecturaContext(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LEE(self):
            return self.getToken(BazilioParser.LEE, 0)
        def VAR(self):
            return self.getToken(BazilioParser.VAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLectura" ):
                listener.enterLectura(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLectura" ):
                listener.exitLectura(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLectura" ):
                return visitor.visitLectura(self)
            else:
                return visitor.visitChildren(self)


    class AgregadoContext(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(BazilioParser.VAR, 0)
        def AGREGA(self):
            return self.getToken(BazilioParser.AGREGA, 0)
        def expr(self):
            return self.getTypedRuleContext(BazilioParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgregado" ):
                listener.enterAgregado(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgregado" ):
                listener.exitAgregado(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAgregado" ):
                return visitor.visitAgregado(self)
            else:
                return visitor.visitChildren(self)


    class ReproduccionContext(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TOCA(self):
            return self.getToken(BazilioParser.TOCA, 0)
        def expr(self):
            return self.getTypedRuleContext(BazilioParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReproduccion" ):
                listener.enterReproduccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReproduccion" ):
                listener.exitReproduccion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReproduccion" ):
                return visitor.visitReproduccion(self)
            else:
                return visitor.visitChildren(self)


    class InvocacionContext(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PROC_ID(self):
            return self.getToken(BazilioParser.PROC_ID, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazilioParser.ExprContext)
            else:
                return self.getTypedRuleContext(BazilioParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInvocacion" ):
                listener.enterInvocacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInvocacion" ):
                listener.exitInvocacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInvocacion" ):
                return visitor.visitInvocacion(self)
            else:
                return visitor.visitChildren(self)


    class CondicionalContext(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SI(self):
            return self.getToken(BazilioParser.SI, 0)
        def expr(self):
            return self.getTypedRuleContext(BazilioParser.ExprContext,0)

        def bloque(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazilioParser.BloqueContext)
            else:
                return self.getTypedRuleContext(BazilioParser.BloqueContext,i)

        def SINO(self):
            return self.getToken(BazilioParser.SINO, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicional" ):
                listener.enterCondicional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicional" ):
                listener.exitCondicional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicional" ):
                return visitor.visitCondicional(self)
            else:
                return visitor.visitChildren(self)



    def instruccion(self):

        localctx = BazilioParser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_instruccion)
        self._la = 0 # Token type
        try:
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = BazilioParser.AsignacionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.match(BazilioParser.VAR)
                self.state = 36
                self.match(BazilioParser.ASIGNA)
                self.state = 37
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = BazilioParser.LecturaContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.match(BazilioParser.LEE)
                self.state = 39
                self.match(BazilioParser.VAR)
                pass

            elif la_ == 3:
                localctx = BazilioParser.EscrituraContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 40
                self.match(BazilioParser.ESCRIBE)
                self.state = 45
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 43
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [31]:
                            self.state = 41
                            self.match(BazilioParser.TEXTO)
                            pass
                        elif token in [3, 5, 16, 32, 33, 35]:
                            self.state = 42
                            self.expr(0)
                            pass
                        else:
                            raise NoViableAltException(self)
                 
                    self.state = 47
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                pass

            elif la_ == 4:
                localctx = BazilioParser.ReproduccionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 48
                self.match(BazilioParser.TOCA)
                self.state = 49
                self.expr(0)
                pass

            elif la_ == 5:
                localctx = BazilioParser.InvocacionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 50
                self.match(BazilioParser.PROC_ID)
                self.state = 54
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 51
                        self.expr(0) 
                    self.state = 56
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                pass

            elif la_ == 6:
                localctx = BazilioParser.CondicionalContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 57
                self.match(BazilioParser.SI)
                self.state = 58
                self.expr(0)
                self.state = 59
                self.bloque()
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==29:
                    self.state = 60
                    self.match(BazilioParser.SINO)
                    self.state = 61
                    self.bloque()


                pass

            elif la_ == 7:
                localctx = BazilioParser.IteracionContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 64
                self.match(BazilioParser.MIENTRAS)
                self.state = 65
                self.expr(0)
                self.state = 66
                self.bloque()
                pass

            elif la_ == 8:
                localctx = BazilioParser.AgregadoContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 68
                self.match(BazilioParser.VAR)
                self.state = 69
                self.match(BazilioParser.AGREGA)
                self.state = 70
                self.expr(0)
                pass

            elif la_ == 9:
                localctx = BazilioParser.CorteContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 71
                self.match(BazilioParser.CORTA)
                self.state = 72
                self.match(BazilioParser.VAR)
                self.state = 73
                self.match(BazilioParser.T__0)
                self.state = 74
                self.expr(0)
                self.state = 75
                self.match(BazilioParser.T__1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BazilioParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class IndiceContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazilioParser.ExprContext)
            else:
                return self.getTypedRuleContext(BazilioParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndice" ):
                listener.enterIndice(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndice" ):
                listener.exitIndice(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndice" ):
                return visitor.visitIndice(self)
            else:
                return visitor.visitChildren(self)


    class ListaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazilioParser.ExprContext)
            else:
                return self.getTypedRuleContext(BazilioParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista" ):
                listener.enterLista(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista" ):
                listener.exitLista(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLista" ):
                return visitor.visitLista(self)
            else:
                return visitor.visitChildren(self)


    class VariableContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(BazilioParser.VAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)


    class RelacionalContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazilioParser.ExprContext)
            else:
                return self.getTypedRuleContext(BazilioParser.ExprContext,i)

        def MENOR(self):
            return self.getToken(BazilioParser.MENOR, 0)
        def MAYOR(self):
            return self.getToken(BazilioParser.MAYOR, 0)
        def MENORIGUAL(self):
            return self.getToken(BazilioParser.MENORIGUAL, 0)
        def MAYORIGUAL(self):
            return self.getToken(BazilioParser.MAYORIGUAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelacional" ):
                listener.enterRelacional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelacional" ):
                listener.exitRelacional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelacional" ):
                return visitor.visitRelacional(self)
            else:
                return visitor.visitChildren(self)


    class EnteroContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ENTERO(self):
            return self.getToken(BazilioParser.ENTERO, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntero" ):
                listener.enterEntero(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntero" ):
                listener.exitEntero(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEntero" ):
                return visitor.visitEntero(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazilioParser.ExprContext)
            else:
                return self.getTypedRuleContext(BazilioParser.ExprContext,i)

        def POR(self):
            return self.getToken(BazilioParser.POR, 0)
        def ENTRE(self):
            return self.getToken(BazilioParser.ENTRE, 0)
        def MODULO(self):
            return self.getToken(BazilioParser.MODULO, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class ParentesisContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(BazilioParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParentesis" ):
                listener.enterParentesis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParentesis" ):
                listener.exitParentesis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentesis" ):
                return visitor.visitParentesis(self)
            else:
                return visitor.visitChildren(self)


    class LongitudContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LONG(self):
            return self.getToken(BazilioParser.LONG, 0)
        def expr(self):
            return self.getTypedRuleContext(BazilioParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLongitud" ):
                listener.enterLongitud(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLongitud" ):
                listener.exitLongitud(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLongitud" ):
                return visitor.visitLongitud(self)
            else:
                return visitor.visitChildren(self)


    class NotaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOTA(self):
            return self.getToken(BazilioParser.NOTA, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNota" ):
                listener.enterNota(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNota" ):
                listener.exitNota(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNota" ):
                return visitor.visitNota(self)
            else:
                return visitor.visitChildren(self)


    class IgualdadContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazilioParser.ExprContext)
            else:
                return self.getTypedRuleContext(BazilioParser.ExprContext,i)

        def IGUAL(self):
            return self.getToken(BazilioParser.IGUAL, 0)
        def DISTINTO(self):
            return self.getToken(BazilioParser.DISTINTO, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIgualdad" ):
                listener.enterIgualdad(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIgualdad" ):
                listener.exitIgualdad(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIgualdad" ):
                return visitor.visitIgualdad(self)
            else:
                return visitor.visitChildren(self)


    class SumaRestaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazilioParser.ExprContext)
            else:
                return self.getTypedRuleContext(BazilioParser.ExprContext,i)

        def MAS(self):
            return self.getToken(BazilioParser.MAS, 0)
        def MENOS(self):
            return self.getToken(BazilioParser.MENOS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSumaResta" ):
                listener.enterSumaResta(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSumaResta" ):
                listener.exitSumaResta(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSumaResta" ):
                return visitor.visitSumaResta(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BazilioParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                localctx = BazilioParser.LongitudContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 80
                self.match(BazilioParser.LONG)
                self.state = 81
                self.expr(10)
                pass
            elif token in [3]:
                localctx = BazilioParser.ParentesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 82
                self.match(BazilioParser.T__2)
                self.state = 83
                self.expr(0)
                self.state = 84
                self.match(BazilioParser.T__3)
                pass
            elif token in [5]:
                localctx = BazilioParser.ListaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 86
                self.match(BazilioParser.T__4)
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 47244705832) != 0):
                    self.state = 87
                    self.expr(0)
                    self.state = 92
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==6:
                        self.state = 88
                        self.match(BazilioParser.T__5)
                        self.state = 89
                        self.expr(0)
                        self.state = 94
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 97
                self.match(BazilioParser.T__6)
                pass
            elif token in [32]:
                localctx = BazilioParser.EnteroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 98
                self.match(BazilioParser.ENTERO)
                pass
            elif token in [33]:
                localctx = BazilioParser.NotaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 99
                self.match(BazilioParser.NOTA)
                pass
            elif token in [35]:
                localctx = BazilioParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 100
                self.match(BazilioParser.VAR)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 122
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 120
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = BazilioParser.MulDivContext(self, BazilioParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 103
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 104
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3670016) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 105
                        self.expr(10)
                        pass

                    elif la_ == 2:
                        localctx = BazilioParser.SumaRestaContext(self, BazilioParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 106
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 107
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==17 or _la==18):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 108
                        self.expr(9)
                        pass

                    elif la_ == 3:
                        localctx = BazilioParser.RelacionalContext(self, BazilioParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 109
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 110
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 251658240) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 111
                        self.expr(8)
                        pass

                    elif la_ == 4:
                        localctx = BazilioParser.IgualdadContext(self, BazilioParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 112
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 113
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==22 or _la==23):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 114
                        self.expr(7)
                        pass

                    elif la_ == 5:
                        localctx = BazilioParser.IndiceContext(self, BazilioParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 115
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 116
                        self.match(BazilioParser.T__0)
                        self.state = 117
                        self.expr(0)
                        self.state = 118
                        self.match(BazilioParser.T__1)
                        pass

             
                self.state = 124
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 11)
         




