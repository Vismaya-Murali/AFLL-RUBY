
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "DO END EQUALS EQUALS_TO IDENTIFIER LPAREN NUMBER PLUS PUTS RPAREN STRING UNTIL WHILEstatement : WHILE expression statements ENDstatement : UNTIL expression DO statements ENDstatements : statement statements\n                  | statement\n                  | emptyexpression : expression PLUS expression\n                  | IDENTIFIER\n                  | NUMBER\n                  | LPAREN expression RPAREN\n                  | expression EQUALS expression\n                  | expression '-' expression\n                  | expression '*' expression\n                  | expression '/' expression\n    statement : PUTS STRING\n                 | IDENTIFIER EQUALS_TO expressionempty :"
    
_lr_action_items = {'WHILE':([0,6,7,8,11,19,22,23,24,25,26,27,28,29,31,33,],[2,2,-7,-8,-14,2,2,-15,-1,-6,-10,-11,-12,-13,-9,-2,]),'UNTIL':([0,6,7,8,11,19,22,23,24,25,26,27,28,29,31,33,],[3,3,-7,-8,-14,3,3,-15,-1,-6,-10,-11,-12,-13,-9,-2,]),'PUTS':([0,6,7,8,11,19,22,23,24,25,26,27,28,29,31,33,],[4,4,-7,-8,-14,4,4,-15,-1,-6,-10,-11,-12,-13,-9,-2,]),'IDENTIFIER':([0,2,3,6,7,8,9,11,12,14,15,16,17,18,19,22,23,24,25,26,27,28,29,31,33,],[5,7,7,5,-7,-8,7,-14,7,7,7,7,7,7,5,5,-15,-1,-6,-10,-11,-12,-13,-9,-2,]),'$end':([1,7,8,11,23,24,25,26,27,28,29,31,33,],[0,-7,-8,-14,-15,-1,-6,-10,-11,-12,-13,-9,-2,]),'NUMBER':([2,3,9,12,14,15,16,17,18,],[8,8,8,8,8,8,8,8,8,]),'LPAREN':([2,3,9,12,14,15,16,17,18,],[9,9,9,9,9,9,9,9,9,]),'STRING':([4,],[11,]),'EQUALS_TO':([5,],[12,]),'PLUS':([6,7,8,10,21,23,25,26,27,28,29,31,],[14,-7,-8,14,14,14,14,14,14,14,14,-9,]),'EQUALS':([6,7,8,10,21,23,25,26,27,28,29,31,],[15,-7,-8,15,15,15,15,15,15,15,15,-9,]),'-':([6,7,8,10,21,23,25,26,27,28,29,31,],[16,-7,-8,16,16,16,16,16,16,16,16,-9,]),'*':([6,7,8,10,21,23,25,26,27,28,29,31,],[17,-7,-8,17,17,17,17,17,17,17,17,-9,]),'/':([6,7,8,10,21,23,25,26,27,28,29,31,],[18,-7,-8,18,18,18,18,18,18,18,18,-9,]),'END':([6,7,8,11,13,19,20,22,23,24,25,26,27,28,29,30,31,32,33,],[-16,-7,-8,-14,24,-4,-5,-16,-15,-1,-6,-10,-11,-12,-13,-3,-9,33,-2,]),'DO':([7,8,10,25,26,27,28,29,31,],[-7,-8,22,-6,-10,-11,-12,-13,-9,]),'RPAREN':([7,8,21,25,26,27,28,29,31,],[-7,-8,31,-6,-10,-11,-12,-13,-9,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,6,19,22,],[1,19,19,19,]),'expression':([2,3,9,12,14,15,16,17,18,],[6,10,21,23,25,26,27,28,29,]),'statements':([6,19,22,],[13,30,32,]),'empty':([6,19,22,],[20,20,20,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> WHILE expression statements END','statement',4,'p_statement_while','UNTIL.py',64),
  ('statement -> UNTIL expression DO statements END','statement',5,'p_statement_until','UNTIL.py',68),
  ('statements -> statement statements','statements',2,'p_statements','UNTIL.py',72),
  ('statements -> statement','statements',1,'p_statements','UNTIL.py',73),
  ('statements -> empty','statements',1,'p_statements','UNTIL.py',74),
  ('expression -> expression PLUS expression','expression',3,'p_expression','UNTIL.py',82),
  ('expression -> IDENTIFIER','expression',1,'p_expression','UNTIL.py',83),
  ('expression -> NUMBER','expression',1,'p_expression','UNTIL.py',84),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression','UNTIL.py',85),
  ('expression -> expression EQUALS expression','expression',3,'p_expression','UNTIL.py',86),
  ('expression -> expression - expression','expression',3,'p_expression','UNTIL.py',87),
  ('expression -> expression * expression','expression',3,'p_expression','UNTIL.py',88),
  ('expression -> expression / expression','expression',3,'p_expression','UNTIL.py',89),
  ('statement -> PUTS STRING','statement',2,'p_statement','UNTIL.py',106),
  ('statement -> IDENTIFIER EQUALS_TO expression','statement',3,'p_statement','UNTIL.py',107),
  ('empty -> <empty>','empty',0,'p_empty','UNTIL.py',119),
]
