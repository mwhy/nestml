# -*- coding: utf-8 -*-
#
# messages.py
#
# This file is part of NEST.
#
# Copyright (C) 2004 The NEST Initiative
#
# NEST is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# NEST is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with NEST.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import annotations

from typing import Tuple

from collections.abc import Iterable
from enum import Enum

from pynestml.meta_model.ast_inline_expression import ASTInlineExpression
from pynestml.meta_model.ast_function import ASTFunction


class MessageCode(Enum):
    """
    A mapping between codes and the corresponding messages.
    """
    START_PROCESSING_FILE = 0
    FUNCTION_CALL_TYPE_ERROR = 2
    TYPE_NOT_DERIVABLE = 3
    IMPLICIT_CAST = 4
    CAST_NOT_POSSIBLE = 5
    TYPE_DIFFERENT_FROM_EXPECTED = 6
    ADD_SUB_TYPE_MISMATCH = 7
    NO_VARIABLE_FOUND = 9
    SPIKE_INPUT_PORT_TYPE_NOT_DEFINED = 10
    MODEL_CONTAINS_ERRORS = 11
    START_PROCESSING_MODEL = 12
    CODE_SUCCESSFULLY_GENERATED = 13
    MODULE_SUCCESSFULLY_GENERATED = 14
    NO_CODE_GENERATED = 15
    VARIABLE_USED_BEFORE_DECLARATION = 16
    VARIABLE_DEFINED_RECURSIVELY = 17
    VALUE_ASSIGNED_TO_BUFFER = 18
    ARG_NOT_SPIKE_INPUT = 20
    NUMERATOR_NOT_ONE = 21
    ORDER_NOT_DECLARED = 22
    CONTINUOUS_INPUT_PORT_WITH_QUALIFIERS = 23
    BLOCK_NOT_CORRECT = 24
    VARIABLE_NOT_IN_STATE_BLOCK = 25
    WRONG_NUMBER_OF_ARGS = 26
    NO_RHS = 27
    SEVERAL_LHS = 28
    FUNCTION_REDECLARED = 29
    FUNCTION_NOT_DECLARED = 30
    NO_ODE = 31
    NO_INIT_VALUE = 32
    MODEL_REDECLARED = 33
    NEST_COLLISION = 34
    KERNEL_OUTSIDE_CONVOLVE = 35
    NAME_COLLISION = 36
    TYPE_NOT_SPECIFIED = 37
    NO_TYPE_ALLOWED = 38
    NO_ASSIGNMENT_ALLOWED = 39
    NOT_A_VARIABLE = 40
    MULTIPLE_KEYWORDS = 41
    VECTOR_IN_NON_VECTOR = 42
    VARIABLE_REDECLARED = 43
    SOFT_INCOMPATIBILITY = 44
    HARD_INCOMPATIBILITY = 45
    NO_RETURN = 46
    NOT_LAST_STATEMENT = 47
    SYMBOL_NOT_RESOLVED = 48
    SYNAPSE_SOLVED_BY_GSL = 49
    TYPE_MISMATCH = 50
    NEURON_SOLVED_BY_GSL = 52
    NO_UNIT = 53
    NOT_NEUROSCIENCE_UNIT = 54
    INTERNAL_WARNING = 55
    OPERATION_NOT_DEFINED = 56
    INPUT_PATH_NOT_FOUND = 58
    LEXER_ERROR = 59
    PARSER_ERROR = 60
    UNKNOWN_TARGET = 61
    VARIABLE_WITH_SAME_NAME_AS_UNIT = 62
    ANALYSING_TRANSFORMING_MODEL = 63
    ODE_NEEDS_CONSISTENT_UNITS = 64
    TEMPLATED_ARG_TYPES_INCONSISTENT = 65
    MODULE_NAME_INFO = 66
    TARGET_PATH_INFO = 67
    ODE_FUNCTION_NEEDS_CONSISTENT_UNITS = 68
    DELTA_FUNCTION_CANNOT_BE_MIXED = 69
    UNKNOWN_TYPE = 70
    ASTDATATYPE_TYPE_SYMBOL_COULD_NOT_BE_DERIVED = 71
    KERNEL_WRONG_TYPE = 72
    KERNEL_IV_WRONG_TYPE = 73
    EMIT_SPIKE_FUNCTION_BUT_NO_OUTPUT_PORT = 74
    NO_FILES_IN_INPUT_PATH = 75
    STATE_VARIABLES_NOT_INITIALZED = 76
    EQUATIONS_DEFINED_BUT_INTEGRATE_ODES_NOT_CALLED = 77
    TEMPLATE_ROOT_PATH_CREATED = 78
    VECTOR_PARAMETER_WRONG_BLOCK = 79
    VECTOR_PARAMETER_WRONG_TYPE = 80
    VECTOR_PARAMETER_WRONG_SIZE = 81
    PRIORITY_DEFINED_FOR_ONLY_ONE_EVENT_HANDLER = 82
    REPEATED_PRIORITY_VALUE = 83
    DELAY_VARIABLE = 84
    INPUT_PORT_SIZE_NOT_INTEGER = 86
    INPUT_PORT_SIZE_NOT_GREATER_THAN_ZERO = 87
    INSTALL_PATH_INFO = 88
    CREATING_INSTALL_PATH = 89
    CREATING_TARGET_PATH = 90
    INTEGRATE_ODES_WRONG_ARG = 91
    ASSIGNING_TO_INLINE = 92
    CM_NO_GATING_VARIABLES = 100
    CM_FUNCTION_MISSING = 101
    CM_VARIABLES_NOT_DECLARED = 102
    CM_FUNCTION_BAD_NUMBER_ARGS = 103
    CM_FUNCTION_BAD_RETURN_TYPE = 104
    CM_VARIABLE_NAME_MULTI_USE = 105
    CM_NO_VALUE_ASSIGNMENT = 106
    SYNS_BAD_BUFFER_COUNT = 107
    CM_NO_V_COMP = 108
    MECHS_DICTIONARY_INFO = 109
    VOID_FUNCTION_ON_RHS = 110
    NON_CONSTANT_EXPONENT = 111
    RESOLUTION_FUNC_USED = 112
    TIMESTEP_FUNCTION_LEGALLY_USED = 113
    RANDOM_FUNCTIONS_LEGALLY_USED = 113
    EXPONENT_MUST_BE_INTEGER = 114
    EMIT_SPIKE_OUTPUT_PORT_TYPE_DIFFERS = 115
    CONTINUOUS_OUTPUT_PORT_MAY_NOT_HAVE_ATTRIBUTES = 116
    INTEGRATE_ODES_ARG_HIGHER_ORDER = 117
    DELAY_VARIABLE_NOT_SPECIFIED = 118
    WEIGHT_VARIABLE_NOT_SPECIFIED = 119
    DELAY_VARIABLE_NOT_FOUND = 120
    WEIGHT_VARIABLE_NOT_FOUND = 121


class Messages:
    """
    This class contains a collection of error messages which enables a centralized maintaining and modifications of
    those.
    """

    @classmethod
    def get_start_processing_file(cls, file_path):
        """
        Returns a message indicating that processing of a file has started
        :param file_path: the path to the file
        :type file_path: str
        :return: message code tuple
        :rtype: (MessageCode,str)
        """
        message = 'Start processing \'' + file_path + '\'!'
        return MessageCode.START_PROCESSING_FILE, message

    @classmethod
    def get_input_path_not_found(cls, path):
        message = 'Input path ("%s") not found!' % (path)
        return MessageCode.INPUT_PATH_NOT_FOUND, message

    @classmethod
    def get_unknown_target_platform(cls, target: str):
        message = "Unknown target: '" + target + "'"
        return MessageCode.UNKNOWN_TARGET, message

    @classmethod
    def get_no_code_generated(cls):
        """
        Returns a message indicating that no code will be generated on this run.
        :return: a message
        :rtype: (MessageCode,str)
        """
        message = 'No target specified: no code will be generated'
        return MessageCode.NO_CODE_GENERATED, message

    @classmethod
    def get_lexer_error(cls, msg):
        message = 'Error occurred during lexing: ' + msg
        return MessageCode.LEXER_ERROR, message

    @classmethod
    def get_parser_error(cls, msg):
        message = 'Error occurred during parsing: ' + msg
        return MessageCode.PARSER_ERROR, message

    @classmethod
    def get_binary_operation_not_defined(cls, lhs, operator, rhs):
        message = 'Operation %s %s %s is not defined!' % (lhs, operator, rhs)
        return MessageCode.OPERATION_NOT_DEFINED, message

    @classmethod
    def get_binary_operation_type_could_not_be_derived(
            cls, lhs, operator, rhs, lhs_type, rhs_type):
        message = 'The type of the expression (left-hand side = \'%s\'; binary operator = \'%s\'; right-hand side = \'%s\') could not be derived: left-hand side has type \'%s\' whereas right-hand side has type \'%s\'!' % (
            lhs, operator, rhs, lhs_type, rhs_type)
        return MessageCode.TYPE_MISMATCH, message

    @classmethod
    def get_unary_operation_not_defined(cls, operator, term):
        message = 'Operation %s%s is not defined!' % (operator, term)
        return MessageCode.OPERATION_NOT_DEFINED, message

    @classmethod
    def get_convolve_needs_buffer_parameter(cls):
        message = 'Convolve requires a buffer variable as second parameter!'
        return MessageCode.CONVOLVE_NEEDS_BUFFER_PARAMETER, message

    @classmethod
    def get_implicit_magnitude_conversion(cls, lhs, rhs, conversion_factor):
        message = 'Implicit magnitude conversion from %s to %s with factor %s ' % (
            lhs.print_symbol(), rhs.print_symbol(), conversion_factor)
        return MessageCode.IMPLICIT_CAST, message

    @classmethod
    def get_function_call_implicit_cast(
            cls,
            arg_nr,
            function_call,
            expected_type,
            got_type,
            castable=False):
        """
        Returns a message indicating that an implicit cast has been performed.
        :param arg_nr: the number of the argument which is cast
        :type arg_nr: int
        :param function_call: a single function call
        :type function_call: ast_function_call
        :param expected_type: the expected type
        :type expected_type: type_symbol
        :param got_type: the got-type
        :type got_type: TypeSymbol
        :param castable: is the type castable
        :type castable: bool
        :return: a message
        :rtype: (MessageCode,str)
        """
        if not castable:
            message = str(arg_nr) + '. argument of function-call \'%s\' at is wrongly typed! Expected \'%s\',' \
                                    ' found \'%s\'!' % (function_call.get_name(), got_type.print_symbol(),
                                                        expected_type.print_symbol())
        else:
            message = str(arg_nr) + '. argument of function-call \'%s\' is wrongly typed! ' \
                                    'Implicit cast from \'%s\' to \'%s\'.' % (function_call.get_name(),
                                                                              got_type.print_symbol(),
                                                                              expected_type.print_symbol())
        return MessageCode.FUNCTION_CALL_TYPE_ERROR, message

    @classmethod
    def get_type_could_not_be_derived(cls, rhs):
        """
        Returns a message indicating that the type of the rhs rhs could not be derived.
        :param rhs: an rhs
        :type rhs: ast_expression or ast_simple_expression
        :return: a message
        :rtype: (MessageCode,str)

        """
        message = 'Type of \'%s\' could not be derived!' % rhs
        return MessageCode.TYPE_NOT_DERIVABLE, message

    @classmethod
    def get_implicit_cast_rhs_to_lhs(cls, rhs_type, lhs_type):
        """
        Returns a message indicating that the type of the lhs does not correspond to the one of the rhs, but the rhs
        can be cast down to lhs type.
        :param rhs_type: the type of the rhs
        :type rhs_type: str
        :param lhs_type: the type of the lhs
        :type lhs_type: str
        :return: a message
        :rtype:(MessageCode,str)
        """
        message = 'Implicit casting from (compatible) type \'%s\' to \'%s\'.' % (
            rhs_type, lhs_type)
        return MessageCode.IMPLICIT_CAST, message

    @classmethod
    def get_different_type_rhs_lhs(
            cls,
            rhs_expression,
            lhs_expression,
            rhs_type,
            lhs_type):
        """
        Returns a message indicating that the type of the lhs does not correspond to the one of the rhs and can not
        be cast down to a common type.
        :param rhs_expression: the rhs rhs
        :type rhs_expression: ASTExpression or ASTSimpleExpression
        :param lhs_expression: the lhs rhs
        :type lhs_expression: ast_expression or ast_simple_expression
        :param rhs_type: the type of the rhs
        :type rhs_type: type_symbol
        :param lhs_type: the type of the lhs
        :type lhs_type: TypeSymbol
        :return: a message
        :rtype:(MessageCode,str)
        """
        message = 'Type of lhs \'%s\' does not correspond to rhs \'%s\'! LHS: \'%s\', RHS: \'%s\'!' % (
            lhs_expression, rhs_expression, lhs_type.print_symbol(), rhs_type.print_symbol())
        return MessageCode.CAST_NOT_POSSIBLE, message

    @classmethod
    def get_type_different_from_expected(cls, expected_type, got_type) -> Tuple[MessageCode, str]:
        """
        Returns a message indicating that the received type is different from the expected one.
        :param expected_type: the expected type
        :param got_type: the actual type
        :return: a message
        """
        message = 'Actual type different from expected. Expected: \'%s\', got: \'%s\'!' % (
            expected_type.print_symbol(), got_type.print_symbol())
        return MessageCode.TYPE_DIFFERENT_FROM_EXPECTED, message

    @classmethod
    def get_no_variable_found(cls, variable_name):
        """
        Returns a message indicating that a variable has not been found.
        :param variable_name: the name of the variable
        :type variable_name: str
        :return: a message
        :rtype: (MessageCode,str)
        """
        assert (variable_name is not None and isinstance(variable_name, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(variable_name)
        message = 'No variable \'%s\' found!' % variable_name
        return MessageCode.NO_VARIABLE_FOUND, message

    @classmethod
    def get_input_port_type_not_defined(cls, input_port_name: str):
        """
        Returns a message indicating that a input_port type has not been defined, thus nS is assumed.
        :param input_port_name: a input_port name
        :return: a message
        :rtype: (MessageCode,str)
        """
        assert (input_port_name is not None and isinstance(input_port_name, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(
                input_port_name)
        message = 'No type declared for spiking input port \'%s\'!' % input_port_name
        return MessageCode.SPIKE_INPUT_PORT_TYPE_NOT_DEFINED, message

    @classmethod
    def get_model_contains_errors(
            cls, model_name: str) -> Tuple[MessageCode, str]:
        """
        Returns a message indicating that a model contains errors thus no code is generated.
        :param model_name: the name of the model
        :return: a message
        """
        assert (model_name is not None and isinstance(model_name, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(model_name)
        message = 'Model \'' + model_name + '\' contains errors. No code generated!'
        return MessageCode.MODEL_CONTAINS_ERRORS, message

    @classmethod
    def get_start_processing_model(
            cls, model_name: str) -> Tuple[MessageCode, str]:
        """
        Returns a message indicating that the processing of a model is started.
        :param model_name: the name of the model
        :return: a message
        """
        assert (model_name is not None and isinstance(model_name, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(model_name)
        message = 'Starts processing of the model \'' + model_name + '\''
        return MessageCode.START_PROCESSING_MODEL, message

    @classmethod
    def get_code_generated(cls, model_name: str, path: str) -> Tuple[MessageCode, str]:
        """
        Returns a message indicating that code has been successfully generated for a model in a certain path.
        :param model_name: the name of the model.
        :param path: the path to the file
        :return: a message
        """
        assert (model_name is not None and isinstance(model_name, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(model_name)
        assert (path is not None and isinstance(path, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(path)
        message = 'Successfully generated code for the model: \'' + \
            model_name + '\' in: \'' + path + '\' !'
        return MessageCode.CODE_SUCCESSFULLY_GENERATED, message

    @classmethod
    def get_module_generated(cls, path: str) -> Tuple[MessageCode, str]:
        """
        Returns a message indicating that a module has been successfully generated.
        :param path: the path to the generated file
        :return: a message
        """
        assert (path is not None and isinstance(path, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(path)
        message = 'Successfully generated NEST module code in \'' + path + '\' !'
        return MessageCode.MODULE_SUCCESSFULLY_GENERATED, message

    @classmethod
    def get_variable_used_before_declaration(cls, variable_name: str):
        """
        Returns a message indicating that a variable is used before declaration.
        :param variable_name: a variable name
        :return: a message
        :rtype: (MessageCode,str)
        """
        assert (variable_name is not None and isinstance(variable_name, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(variable_name)
        message = 'Variable \'%s\' used before declaration!' % variable_name
        return MessageCode.VARIABLE_USED_BEFORE_DECLARATION, message

    @classmethod
    def get_variable_not_defined(cls, variable_name):
        """
        Returns a message indicating that a variable is not defined .
        :param variable_name: a variable name
        :type variable_name: str
        :return: a message
        :rtype: (MessageCode,str)
        """
        assert (variable_name is not None and isinstance(variable_name, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(variable_name)
        message = 'Variable \'%s\' not defined!' % variable_name
        return MessageCode.NO_VARIABLE_FOUND, message

    @classmethod
    def get_variable_defined_recursively(cls, variable_name):
        """
        Returns a message indicating that a variable is defined recursively.
        :param variable_name: a variable name
        :type variable_name: str
        :return: a message
        :rtype: (MessageCode,str)
        """
        assert (variable_name is not None and isinstance(variable_name, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(variable_name)
        message = 'Variable \'%s\' defined recursively!' % variable_name
        return MessageCode.VARIABLE_DEFINED_RECURSIVELY, message

    @classmethod
    def get_value_assigned_to_buffer(cls, buffer_name):
        """
        Returns a message indicating that a value has been assigned to a buffer.
        :param buffer_name: a buffer name
        :type buffer_name: str
        :return: a message
        :rtype: (MessageCode,str)
        """
        assert (buffer_name is not None and isinstance(buffer_name, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(buffer_name)
        message = 'Value assigned to buffer \'%s\'!' % buffer_name
        return MessageCode.VALUE_ASSIGNED_TO_BUFFER, message

    @classmethod
    def get_first_arg_not_kernel_or_equation(cls, func_name):
        """
        Indicates that the first argument of an rhs is not an equation or kernel.
        :param func_name: the name of the function
        :type func_name: str
        :return: a message
        :rtype: (MessageCode,str)
        """
        assert (func_name is not None and isinstance(func_name, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(func_name)
        message = 'First argument of \'%s\' not a kernel or equation!' % func_name
        return MessageCode.ARG_NOT_KERNEL_OR_EQUATION, message

    @classmethod
    def get_second_arg_not_a_spike_port(
            cls, func_name: str) -> Tuple[MessageCode, str]:
        """
        Indicates that the second argument of the NESTML convolve() call is not a spiking input port.
        :param func_name: the name of the function
        :return: a message
        """
        assert (func_name is not None and isinstance(func_name, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(func_name)
        message = 'Second argument of \'%s\' not a spiking input port!' % func_name
        return MessageCode.ARG_NOT_SPIKE_INPUT, message

    @classmethod
    def get_wrong_numerator(cls, unit):
        """
        Indicates that the numerator of a unit is not 1.
        :param unit: the name of the unit
        :type unit: str
        :return: a message
        :rtype: (MessageCode,str)
        """
        assert (unit is not None and isinstance(unit, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(unit)
        message = 'Numeric numerator of unit \'%s\' not 1!' % unit
        return MessageCode.NUMERATOR_NOT_ONE, message

    @classmethod
    def get_order_not_declared(cls, lhs):
        """
        Indicates that the order has not been declared.
        :param lhs: the name of the variable
        :type lhs: str
        :return: a message
        :rtype: (MessageCode,str)
        """
        assert (lhs is not None and isinstance(lhs, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % lhs
        message = 'Order of differential equation for %s is not declared!' % lhs
        return MessageCode.ORDER_NOT_DECLARED, message

    @classmethod
    def get_continuous_input_port_specified(cls, name, keyword):
        """
        Indicates that the continuous time input port has been specified with an `inputQualifier` keyword.
        :param name: the name of the buffer
        :type name: str
        :param keyword: the keyword
        :type keyword: list(str)
        :return: a message
        :rtype: (MessageCode,str)
        """
        assert (name is not None and isinstance(name, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % name
        message = 'Continuous time input port \'%s\' specified with type keywords (%s)!' % (
            name, keyword)
        return MessageCode.CONTINUOUS_INPUT_PORT_WITH_QUALIFIERS, message

    @classmethod
    def get_block_not_defined_correctly(cls, block, missing):
        """
        Indicates that a given block has been defined several times or non.
        :param block: the name of the block which is not defined or defined multiple times.
        :type block: str
        :param missing: True if missing, False if multiple times.
        :type missing: bool
        :return: a message
        :rtype: (MessageCode,str)
        """
        assert (block is not None and isinstance(block, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(block)
        assert (missing is not None and isinstance(missing, bool)), \
            '(PyNestML.Utils.Message) Not a bool provided (%s)!' % type(missing)
        if missing:
            message = block + ' block not defined!'
        else:
            message = block + ' block defined more than once!'
        return MessageCode.BLOCK_NOT_CORRECT, message

    @classmethod
    def get_equation_var_not_in_state_block(cls, variable_name):
        """
        Indicates that a variable in the equations block is not defined in the state block.
        :param variable_name: the name of the variable of an equation which is not defined in an equations block
        :type variable_name: str
        :return: a message
        :rtype: (MessageCode,str)
        """
        assert (variable_name is not None and isinstance(variable_name, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(variable_name)
        message = 'Ode equation lhs-variable \'%s\' not defined in state block!' % variable_name
        return MessageCode.VARIABLE_NOT_IN_STATE_BLOCK, message

    @classmethod
    def get_wrong_number_of_args(cls, function_call, expected, got):
        """
        Indicates that a wrong number of arguments has been provided to the function call.
        :param function_call: a function call name
        :type function_call: str
        :param expected: the expected number of arguments
        :type expected: int
        :param got: the given number of arguments
        :type got: int
        :return: a message
        :rtype: (MessageCode,str)
        """
        assert (function_call is not None and isinstance(function_call, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(function_call)
        assert (expected is not None and isinstance(expected, int)), \
            '(PyNestML.Utils.Message) Not a int provided (%s)!' % type(expected)
        assert (got is not None and isinstance(got, int)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(got)
        message = 'Wrong number of arguments in function-call \'%s\'! Expected \'%s\', found \'%s\'.' % (
            function_call, expected, got)
        return MessageCode.WRONG_NUMBER_OF_ARGS, message

    @classmethod
    def get_no_rhs(cls, name):
        """
        Indicates that no right-hand side has been declared for the given variable.
        :param name: the name of the rhs variable
        :type name: str
        :return: a message
        :rtype: (MessageCode,str)
        """
        assert (name is not None and isinstance(name, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(name)
        message = 'Function variable \'%s\' has no right-hand side!' % name
        return MessageCode.NO_RHS, message

    @classmethod
    def get_several_lhs(cls, names):
        """
        Indicates that several left hand sides have been defined.
        :param names: a list of variables
        :type names: list(str)
        :return: a message
        :rtype: (MessageCode,str)
        """
        assert (names is not None and isinstance(names, list)), \
            '(PyNestML.Utils.Message) Not a list provided (%s)!' % type(names)
        message = 'Function declared with several variables (%s)!' % names
        return MessageCode.SEVERAL_LHS, message

    @classmethod
    def get_function_redeclared(cls, name, predefined):
        """
        Indicates that a function has been redeclared.
        :param name: the name of the function which has been redeclared.
        :type name: str
        :param predefined: True if function is predefined, otherwise False.
        :type predefined: bool
        :return: a message
        :rtype:(MessageCode,str)
        """
        assert (name is not None and isinstance(name, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(name)
        if predefined:
            message = 'Predefined function \'%s\' redeclared!' % name
        else:
            message = 'Function \'%s\' redeclared!' % name
        return MessageCode.FUNCTION_REDECLARED, message

    @classmethod
    def get_no_ode(cls, name):
        """
        Indicates that no ODE has been defined for a variable inside the state block.
        :param name: the name of the variable which does not have a defined ode
        :type name: str
        :return: a message
        :rtype: (MessageCode,str)
        """
        assert (name is not None and isinstance(name, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(name)
        message = 'Variable \'%s\' not provided with an ODE!' % name
        return MessageCode.NO_ODE, message

    @classmethod
    def get_no_init_value(cls, name):
        """
        Indicates that no initial value has been provided for a given variable.
        :param name: the name of the variable which does not have a initial value
        :type name: str
        :return: a message
        :rtype: (MessageCode,str)
        """
        assert (name is not None and isinstance(name, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(name)
        message = 'Initial value of ode variable \'%s\' not provided!' % name
        return MessageCode.NO_INIT_VALUE, message

    @classmethod
    def get_model_redeclared(cls, name: str) -> Tuple[MessageCode, str]:
        """
        Indicates that a model has been redeclared.
        :param name: the name of the model which has been redeclared.
        :return: a message
        """
        assert (name is not None and isinstance(name, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(name)
        assert (name is not None and isinstance(name, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(name)
        message = 'Model \'%s\' redeclared!' % name
        return MessageCode.MODEL_REDECLARED, message

    @classmethod
    def get_nest_collision(cls, name):
        """
        Indicates that a collision between a user defined function and a nest function occurred.
        :param name: the name of the function which collides to nest
        :type name: str
        :return: a message
        :rtype: (MessageCode,str)
        """
        assert (name is not None and isinstance(name, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(name)
        message = 'Function \'%s\' collides with NEST namespace!' % name
        return MessageCode.NEST_COLLISION, message

    @classmethod
    def get_kernel_outside_convolve(cls, name):
        """
        Indicates that a kernel variable has been used outside a convolve call.
        :param name: the name of the kernel
        :type name: str
        :return: message
        :rtype: (MessageCode,str)
        """
        assert (name is not None and isinstance(name, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(name)
        message = 'Kernel \'%s\' used outside convolve!' % name
        return MessageCode.KERNEL_OUTSIDE_CONVOLVE, message

    @classmethod
    def get_compilation_unit_name_collision(cls, name, art1, art2):
        """
        Indicates that a name collision with the same model inside two artifacts.
        :param name: the name of the model which leads to collision
        :type name: str
        :param art1: the first artifact name
        :type art1: str
        :param art2: the second artifact name
        :type art2: str
        :return: a message
        :rtype: (MessageCode,str)
        """
        assert (name is not None and isinstance(name, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(name)
        assert (art1 is not None and isinstance(art1, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(art1)
        assert (art2 is not None and isinstance(art2, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(art2)
        message = 'Name collision of \'%s\' in \'%s\' and \'%s\'!' % (
            name, art1, art2)
        return MessageCode.NAME_COLLISION, message

    @classmethod
    def get_data_type_not_specified(cls, name):
        """
        Indicates that for a given element no type has been specified.
        :param name: the name of the variable for which a type has not been specified.
        :type name: str
        :return: a message
        :rtype: (MessageCode,str)
        """
        assert (name is not None and isinstance(name, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(name)
        message = 'Data type of \'%s\' at not specified!' % name
        return MessageCode.TYPE_NOT_SPECIFIED, message

    @classmethod
    def get_not_type_allowed(cls, name):
        """
        Indicates that a type for the given element is not allowed.
        :param name: the name of the element for which a type is not allowed.
        :type name: str
        :return: a message
        :rtype: (MessageCode,str)
        """
        assert (name is not None and isinstance(name, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(name)
        message = 'No data type allowed for \'%s\'!' % name
        return MessageCode.NO_TYPE_ALLOWED, message

    @classmethod
    def get_assignment_not_allowed(cls, name):
        """
        Indicates that an assignment to the given element is not allowed.
        :param name: the name of variable to which an assignment is not allowed.
        :type name: str
        :return: a message
        :rtype: (MessageCode,str)
        """
        assert (name is not None and isinstance(name, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(name)
        message = 'Assignment to \'%s\' not allowed!' % name
        return MessageCode.NO_ASSIGNMENT_ALLOWED, message

    @classmethod
    def get_not_a_variable(cls, name):
        """
        Indicates that a given name does not represent a variable.
        :param name: the name of the variable
        :type name: str
        :return: a message
        :rtype: (MessageCode,str)
        """
        assert (name is not None and isinstance(name, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(name)
        message = '\'%s\' not a variable!' % name
        return MessageCode.NOT_A_VARIABLE, message

    @classmethod
    def get_multiple_keywords(cls, keyword):
        """
        Indicates that a buffer has been declared with multiple keywords of the same type, e.g., inhibitory inhibitory
        :param keyword: the keyword which has been used multiple times
        :type keyword: str
        :return: a message
        :rtype: (MessageCode,str)
        """
        assert (keyword is not None and isinstance(keyword, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(keyword)
        message = 'Buffer specified with multiple \'%s\' keywords!' % keyword
        return MessageCode.MULTIPLE_KEYWORDS, message

    @classmethod
    def get_vector_in_non_vector(cls, vector, non_vector):
        """
        Indicates that a vector has been used in a non-vector declaration.
        :param vector: the vector variable
        :type vector: str
        :param non_vector: the non-vector lhs
        :type non_vector: list(str)
        :return: a message
        :rtype: (MessageCode,str)
        """
        assert (vector is not None and isinstance(vector, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(vector)
        assert (non_vector is not None and isinstance(non_vector, list)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(non_vector)
        message = 'Vector value \'%s\' used in a non-vector declaration of variables \'%s\'!' % (
            vector, non_vector)
        return MessageCode.VECTOR_IN_NON_VECTOR, message

    @classmethod
    def get_variable_redeclared(cls, name, predefined):
        """
        Indicates that a given variable has been redeclared. A redeclaration can happen with user defined
        functions or with predefined functions (second parameter).
        :param name: the name of the variable
        :type name: str
        :param predefined: True if a pre-defined variable has been redeclared, otherwise False.
        :type predefined: bool
        :return: a message
        :rtype: (MessageCode,str)
        """
        assert (name is not None and isinstance(name, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(name)
        assert (predefined is not None and isinstance(predefined, bool)), \
            '(PyNestML.Utils.Message) Not a bool provided (%s)!' % type(predefined)
        if predefined:
            message = 'Predefined variable \'%s\' redeclared!' % name
        else:
            message = 'Variable \'%s\' redeclared !' % name
        return MessageCode.VARIABLE_REDECLARED, message

    @classmethod
    def get_no_return(cls):
        """
        Indicates that a given function has no return statement although required.
        :return: a message
        :rtype: (MessageCode,str)
        """
        message = 'Return statement expected!'
        return MessageCode.NO_RETURN, message

    @classmethod
    def get_not_last_statement(cls, name):
        """
        Indicates that given statement is not the last statement in a block, e.g., in the case that a return
        statement is not the last statement.
        :param name: the statement.
        :type name: str
        :return: a message
        :rtype: (MessageCode,str)
        """
        assert (name is not None and isinstance(name, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(name)
        message = '\'%s\' not the last statement!' % name
        return MessageCode.NOT_LAST_STATEMENT, message

    @classmethod
    def get_function_not_declared(cls, name):
        """
        Indicates that a function, which is not declared, has been used.
        :param name: the name of the function.
        :type name: str
        :return: a message
        :rtype: (MessageCode,str)
        """
        assert (name is not None and isinstance(name, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(name)
        message = 'Function \'%s\' is not declared!' % name
        return MessageCode.FUNCTION_NOT_DECLARED, message

    @classmethod
    def get_could_not_resolve(cls, name):
        """
        Indicates that the handed over name could not be resolved to a symbol.
        :param name: the name which could not be resolved
        :type name: str
        :return: a message
        :rtype: (MessageCode,str)
        """
        assert (name is not None and isinstance(name, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(name)
        message = 'Could not resolve symbol \'%s\'!' % name
        return MessageCode.SYMBOL_NOT_RESOLVED, message

    @classmethod
    def get_unit_does_not_exist(cls, name):
        """
        Indicates that a unit does not exist.
        :param name: the name of the unit.
        :type name: str
        :return: a new code,message tuple
        :rtype: (MessageCode,str)
        """
        assert (name is not None and isinstance(name, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(name)
        message = 'Unit does not exist (%s).' % name
        return MessageCode.NO_UNIT, message

    @classmethod
    def get_not_neuroscience_unit_used(cls, name):
        """
        Indicates that a non-neuroscientific unit, e.g., kg, has been used. Those units can not be converted to
        a corresponding representation in the simulation and are therefore represented by the factor 1.
        :param name: the name of the variable
        :type name: str
        :return: a nes code,message tuple
        :rtype: (MessageCode,str)
        """
        assert (name is not None and isinstance(name, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(name)
        message = 'Not convertible unit \'%s\' used, 1 assumed as factor!' % name
        return MessageCode.NOT_NEUROSCIENCE_UNIT, message

    @classmethod
    def get_ode_needs_consistent_units(cls, name, differential_order, lhs_type, rhs_type):
        assert (name is not None and isinstance(name, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(name)
        message = 'ODE definition for \''
        if differential_order > 1:
            message += 'd^' + str(differential_order) + ' ' + \
                name + ' / dt^' + str(differential_order) + '\''
        if differential_order > 0:
            message += 'd ' + name + ' / dt\''
        else:
            message += '\'' + str(name) + '\''
        message += ' has inconsistent units: expected \'' + \
            lhs_type.print_symbol() + '\', got \'' + rhs_type.print_symbol() + '\''
        return MessageCode.ODE_NEEDS_CONSISTENT_UNITS, message

    @classmethod
    def get_ode_function_needs_consistent_units(
            cls, name, declared_type, expression_type):
        assert (name is not None and isinstance(name, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(name)
        message = 'ODE function definition for \'' + name + '\' has inconsistent units: expected \'' + \
            declared_type.print_symbol() + '\', got \'' + expression_type.print_symbol() + '\''
        return MessageCode.ODE_FUNCTION_NEEDS_CONSISTENT_UNITS, message

    @classmethod
    def get_variable_with_same_name_as_type(cls, name):
        """
        Indicates that a variable has been declared with the same name as a physical unit, e.g. "V mV"
        :param name: the name of the variable
        :type name: str
        :return: a tuple containing message code and message text
        :rtype: (MessageCode,str)
        """
        assert (name is not None and isinstance(name, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(name)
        message = 'Variable \'%s\' has the same name as a physical unit!' % name
        return MessageCode.VARIABLE_WITH_SAME_NAME_AS_UNIT, message

    @classmethod
    def get_analysing_transforming_model(cls, name):
        """
        Indicates start of code generation
        :param name: the name of the model
        :type name: ASTModel
        :return: a code, message tuple
        :rtype: (MessageCode,str)
        """
        assert (name is not None and isinstance(name, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(name)
        message = 'Analysing/transforming model \'%s\'' % name
        return MessageCode.ANALYSING_TRANSFORMING_MODEL, message

    @classmethod
    def get_assigning_to_inline(cls):
        """
        Cannot assign to inline expression
        :param name: the name of the neuron model
        :return: a code, message tuple
        :rtype: (MessageCode,str)
        """
        message = "Cannot assign to inline expression."
        return MessageCode.ASSIGNING_TO_INLINE, message

    @classmethod
    def templated_arg_types_inconsistent(cls, function_name, failing_arg_idx, other_args_idx, failing_arg_type_str, other_type_str):
        """
        For templated function arguments, indicates inconsistency between (formal) template argument types and actual derived types.
        :param name: the name of the model
        :type name: ASTModel
        :return: a code, message tuple
        :rtype: (MessageCode,str)
        """
        message = 'In function \'' + function_name + '\': actual derived type of templated parameter ' + \
            str(failing_arg_idx + 1) + ' is \'' + failing_arg_type_str + '\', which is inconsistent with that of parameter(s) ' + \
            ', '.join([str(_ + 1) for _ in other_args_idx]) + \
            ', which has/have type \'' + other_type_str + '\''
        return MessageCode.TEMPLATED_ARG_TYPES_INCONSISTENT, message

    @classmethod
    def delta_function_cannot_be_mixed(cls):
        """
        Delta function cannot be mixed with expressions.
        """
        message = "delta function cannot be mixed with expressions"
        return MessageCode.DELTA_FUNCTION_CANNOT_BE_MIXED, message

    @classmethod
    def delta_function_one_arg(cls, deltafunc):
        """
        Delta function takes exactly one argument.
        :param deltafunc: the delta function node
        :type name: ASTFunctionCall
        """
        message = "delta function takes exactly one argument (time *t*); instead found " + ", ".join([
            str(arg) for arg in deltafunc.get_args()])
        return MessageCode.DELTA_FUNCTION_CANNOT_BE_MIXED, message

    @classmethod
    def unknown_type(cls, provided_type_str):
        """
        Unknown type or unit literal.
        :param provided_type_str: the provided type as a string
        :type provided_type_str: str
        """
        message = "Unknown type or unit literal: " + provided_type_str
        return MessageCode.UNKNOWN_TYPE, message

    @classmethod
    def astdatatype_type_symbol_could_not_be_derived(cls):
        """
        Unknown type or unit literal.
        :param provided_type_str: the provided type as a string
        :type provided_type_str: str
        """
        message = "ASTDataType type symbol could not be derived"
        return MessageCode.ASTDATATYPE_TYPE_SYMBOL_COULD_NOT_BE_DERIVED, message

    @classmethod
    def get_emit_spike_function_but_no_output_port(cls):
        """
        Indicates that an emit_spike() function was called, but no spiking output port has been defined.
        :return: a (code, message) tuple
        :rtype: (MessageCode, str)
        """
        message = 'emit_spike() function was called, but no spiking output port has been defined!'
        return MessageCode.EMIT_SPIKE_FUNCTION_BUT_NO_OUTPUT_PORT, message

    @classmethod
    def get_output_port_type_differs(cls) -> Tuple[MessageCode, str]:
        """
        Indicates that an emit_spike() function was called, but with different parameter types than the output port was defined with.
        """
        message = 'emit_spike() function was called, but with different parameter types than the output port was defined with!'
        return MessageCode.EMIT_SPIKE_OUTPUT_PORT_TYPE_DIFFERS, message

    @classmethod
    def get_kernel_wrong_type(cls,
                              kernel_name: str,
                              differential_order: int,
                              actual_type: str) -> Tuple[MessageCode,
                                                         str]:
        """
        Returns a message indicating that the type of a kernel is wrong.
        :param kernel_name: the name of the kernel
        :param differential_order: differential order of the kernel left-hand side, e.g. 2 if the kernel is g''
        :param actual_type: the name of the actual type that was found in the model
        """
        assert (kernel_name is not None and isinstance(kernel_name, str)), \
            '(PyNestML.Utils.Message) Not a string provided (%s)!' % type(kernel_name)
        if differential_order == 0:
            expected_type_str = "real or int"
        else:
            assert differential_order > 0
            expected_type_str = "s**-%d" % differential_order
        message = 'Kernel \'%s\' was found to be of type \'%s\' (should be %s)!' % (
            kernel_name, actual_type, expected_type_str)
        return MessageCode.KERNEL_WRONG_TYPE, message

    @classmethod
    def get_kernel_iv_wrong_type(cls,
                                 iv_name: str,
                                 actual_type: str,
                                 expected_type: str) -> Tuple[MessageCode,
                                                              str]:
        """
        Returns a message indicating that the type of a kernel initial value is wrong.
        :param iv_name: the name of the state variable with an initial value
        :param actual_type: the name of the actual type that was found in the model
        :param expected_type: the name of the type that was expected
        """
        message = 'Initial value \'%s\' was found to be of type \'%s\' (should be %s)!' % (
            iv_name, actual_type, expected_type)
        return MessageCode.KERNEL_IV_WRONG_TYPE, message

    @classmethod
    def get_no_files_in_input_path(cls, path: str):
        message = "No files found matching '*.nestml' in provided input path '" + path + "'"
        return MessageCode.NO_FILES_IN_INPUT_PATH, message

    @classmethod
    def get_state_variables_not_initialized(cls, var_name: str):
        message = "The variable \'%s\' is not initialized." % var_name
        return MessageCode.STATE_VARIABLES_NOT_INITIALZED, message

    @classmethod
    def get_equations_defined_but_integrate_odes_not_called(cls):
        message = "Equations defined but integrate_odes() not called"
        return MessageCode.EQUATIONS_DEFINED_BUT_INTEGRATE_ODES_NOT_CALLED, message

    @classmethod
    def get_template_root_path_created(cls, templates_root_dir: str):
        message = "Given template root path is not an absolute path. " \
                  "Creating the absolute path with default templates directory '" + \
            templates_root_dir + "'"
        return MessageCode.TEMPLATE_ROOT_PATH_CREATED, message

    @classmethod
    def get_vector_parameter_wrong_block(cls, var, block):
        message = "The vector parameter '" + var + "' is declared in the wrong block '" + block + "'. " \
                  "The vector parameter can only be declared in parameters or internals block."
        return MessageCode.VECTOR_PARAMETER_WRONG_BLOCK, message

    @classmethod
    def get_vector_parameter_wrong_type(cls, var):
        message = "The vector parameter '" + var + "' is of the wrong type. " \
                  "The vector parameter can be only of type integer."
        return MessageCode.VECTOR_PARAMETER_WRONG_TYPE, message

    @classmethod
    def get_vector_parameter_wrong_size(cls, var, value):
        message = "The vector parameter '" + var + "' has value '" + value + "' " \
                  "which is less than or equal to 0."
        return MessageCode.VECTOR_PARAMETER_WRONG_SIZE, message

    @classmethod
    def get_priority_defined_for_only_one_receive_block(cls, event_handler_port_name: str):
        message = "Priority defined for only one event handler (" + event_handler_port_name + ")"
        return MessageCode.PRIORITY_DEFINED_FOR_ONLY_ONE_EVENT_HANDLER, message

    @classmethod
    def get_repeated_priorty_value(cls):
        message = "Priority values for event handlers need to be unique"
        return MessageCode.REPEATED_PRIORITY_VALUE, message

    @classmethod
    def get_function_is_delay_variable(cls, func):
        message = "Function '" + func + "' is not a function but a delay variable."
        return MessageCode.DELAY_VARIABLE, message

    @classmethod
    def get_no_gating_variables(
            cls,
            cm_inline_expr: ASTInlineExpression,
            ion_channel_name: str):
        """
        Indicates that if you defined an inline expression inside the equations block
        that uses no kernels / has no convolution calls
        then then there must be at least one variable name that ends with _{x}
        For example an inline "Na" must have at least one variable ending with "_Na"
        :return: a message
        :rtype: (MessageCode,str)
        """

        message = "No gating variables found inside declaration of '" + \
            cm_inline_expr.variable_name + "', "
        message += "\nmeaning no variable ends with the suffix '_" + \
            ion_channel_name + "' here. "
        message += "This suffix indicates that a variable is a gating variable. "
        message += "At least one gating variable is expected to exist."

        return MessageCode.CM_NO_GATING_VARIABLES, message

    @classmethod
    def get_cm_inline_expression_variable_used_mulitple_times(
            cls,
            cm_inline_expr: ASTInlineExpression,
            bad_variable_name: str,
            ion_channel_name: str):
        message = "Variable name '" + bad_variable_name + \
            "' seems to be used multiple times"
        message += "' inside inline expression '" + cm_inline_expr.variable_name + "'. "
        message += "\nVariables are not allowed to occur multiple times here."

        return MessageCode.CM_VARIABLE_NAME_MULTI_USE, message

    @classmethod
    def get_expected_cm_function_missing(
            cls,
            ion_channel_name: str,
            variable_name: str,
            function_name: str):
        message = "Implementation of a function called '" + function_name + "' not found. "
        message += "It is expected because of variable '" + \
            variable_name + "' in the ion channel '" + ion_channel_name + "'"
        return MessageCode.CM_FUNCTION_MISSING, message

    @classmethod
    def get_expected_cm_function_wrong_args_count(
            cls, ion_channel_name: str, variable_name, astfun: ASTFunction):
        message = "Function '" + astfun.name + \
            "' is expected to have exactly one Argument. "
        message += "It is related to variable '" + variable_name + \
            "' in the ion channel '" + ion_channel_name + "'"
        return MessageCode.CM_FUNCTION_BAD_NUMBER_ARGS, message

    @classmethod
    def get_expected_cm_function_bad_return_type(
            cls, ion_channel_name: str, astfun: ASTFunction) -> Tuple[MessageCode, str]:
        message = "'" + ion_channel_name + "' channel function '" + \
            astfun.name + "' must return real. "
        return MessageCode.CM_FUNCTION_BAD_RETURN_TYPE, message

    @classmethod
    def get_expected_cm_variables_missing_in_blocks(cls,
                                                    missing_variable_to_proper_block: Iterable,
                                                    expected_variables_to_reason: dict) -> Tuple[MessageCode, str]:
        message = "The following variables not found:\n"
        for missing_var, proper_location in missing_variable_to_proper_block.items():
            message += "Variable with name '" + missing_var
            message += "' not found but expected to exist inside of " + \
                proper_location + " because of position "
            message += str(
                expected_variables_to_reason[missing_var].get_source_position()) + "\n"
        return MessageCode.CM_VARIABLES_NOT_DECLARED, message

    @classmethod
    def get_cm_variable_value_missing(cls, varname: str) -> Tuple[MessageCode, str]:
        message = "The following variable has no value assinged: " + varname + "\n"
        return MessageCode.CM_NO_VALUE_ASSIGNMENT, message

    @classmethod
    def get_v_comp_variable_value_missing(cls, neuron_name: str, missing_variable_name) -> Tuple[MessageCode, str]:
        message = "Missing state variable '" + missing_variable_name
        message += "' inside of neuron '" + neuron_name + "'. "
        message += "You have passed NEST_COMPARTMENTAL flag to the generator, thereby activating compartmental mode."
        message += "In this mode, such variable must be declared in the state block.\n"
        message += "This variable represents the dynamically calculated value of membrane potential "
        message += "and should be utilized in your equations for voltage activated ion channels."
        return MessageCode.CM_NO_V_COMP, message

    @classmethod
    def get_syns_bad_buffer_count(cls, buffers: set, synapse_name: str) -> Tuple[MessageCode, str]:
        message = "Synapse `\'%s\' uses the following input buffers: %s" % (
            synapse_name, buffers)
        message += " However exaxtly one spike input buffer per synapse is allowed."
        return MessageCode.SYNS_BAD_BUFFER_COUNT, message

    @classmethod
    def get_input_port_size_not_integer(cls, port_name: str) -> Tuple[MessageCode, str]:
        message = "The size of the input port " + port_name + " is not of integer type."
        return MessageCode.INPUT_PORT_SIZE_NOT_INTEGER, message

    @classmethod
    def get_input_port_size_not_greater_than_zero(cls, port_name: str) -> Tuple[MessageCode, str]:
        message = "The size of the input port " + port_name + " must be greater than zero."
        return MessageCode.INPUT_PORT_SIZE_NOT_GREATER_THAN_ZERO, message

    @classmethod
    def get_target_path_info(cls, target_dir: str) -> Tuple[MessageCode, str]:
        message = "Target platform code will be generated in directory: '" + target_dir + "'"
        return MessageCode.TARGET_PATH_INFO, message

    @classmethod
    def get_install_path_info(cls, install_path: str) -> Tuple[MessageCode, str]:
        message = "Target platform code will be installed in directory: '" + install_path + "'"
        return MessageCode.INSTALL_PATH_INFO, message

    @classmethod
    def get_creating_target_path(cls, target_path: str) -> Tuple[MessageCode, str]:
        message = "Creating target directory: '" + target_path + "'"
        return MessageCode.CREATING_TARGET_PATH, message

    @classmethod
    def get_creating_install_path(cls, install_path: str) -> Tuple[MessageCode, str]:
        message = "Creating installation directory: '" + install_path + "'"
        return MessageCode.CREATING_INSTALL_PATH, message

    @classmethod
    def get_integrate_odes_wrong_arg(cls, arg: str) -> Tuple[MessageCode, str]:
        message = "Parameter provided to integrate_odes() function is not a state variable: '" + arg + "'"
        return MessageCode.INTEGRATE_ODES_WRONG_ARG, message

    @classmethod
    def get_integrate_odes_arg_higher_order(cls, arg: str) -> Tuple[MessageCode, str]:
        message = "Parameter provided to integrate_odes() function is a state variable of higher order: '" + arg + "'"
        return MessageCode.INTEGRATE_ODES_ARG_HIGHER_ORDER, message

    @classmethod
    def get_mechs_dictionary_info(cls, chan_info, syns_info, conc_info, con_in_info) -> Tuple[MessageCode, str]:
        message = ""
        message += "chan_info:\n" + chan_info + "\n"
        message += "syns_info:\n" + syns_info + "\n"
        message += "conc_info:\n" + conc_info + "\n"
        message += "con_in_info:\n" + con_in_info + "\n"

        return MessageCode.MECHS_DICTIONARY_INFO, message

    @classmethod
    def get_fixed_timestep_func_used(cls):
        message = "Model contains a call to fixed-timestep functions (``resolution()`` and/or ``steps()``). This restricts the model to being compatible only with fixed-timestep simulators. Consider eliminating ``resolution()`` and ``steps()`` from the model, and using ``timestep()`` instead."
        return MessageCode.RESOLUTION_FUNC_USED, message

    @classmethod
    def get_void_function_on_rhs(cls, function_name: str) -> Tuple[MessageCode, str]:
        r"""
        Construct an error message indicating that a void function cannot be used on a RHS.
        :param function_name: the offending function
        :return: the error message
        """
        message = "Function " + function_name + " with the return-type 'void' cannot be used in expressions."
        return MessageCode.VOID_FUNCTION_ON_RHS, message

    @classmethod
    def get_timestep_function_legally_used(cls):
        message = "``timestep()`` function may appear only inside the ``update`` block."
        return MessageCode.TIMESTEP_FUNCTION_LEGALLY_USED, message

    @classmethod
    def get_ternary_mismatch(cls, if_true_text: str, if_not_text: str) -> Tuple[MessageCode, str]:
        r"""
        construct an error message indicating that an a comparison operation has incompatible operands
        :param if_true_text: plain text of the positive branch of the ternary operator
        :param if_not_text: plain text of the negative branch of the ternary operator
        :return: the error message
        """
        message = "Mismatched conditional alternatives " + if_true_text + " and " + if_not_text + "-> Assuming real."

        return MessageCode.TYPE_DIFFERENT_FROM_EXPECTED, message

    @classmethod
    def get_mismatch(cls) -> Tuple[MessageCode, str]:
        r"""
        construct an error message indicating that an a comparison operation has incompatible operands
        :return: the error message
        """
        message = "The ternary operator condition must be boolean."

        return MessageCode.TYPE_DIFFERENT_FROM_EXPECTED, message

    @classmethod
    def get_comparison(cls, message_code: MessageCode) -> Tuple[MessageCode, str]:
        r"""
        construct an error message indicating that an a comparison operation has incompatible operands
        :return: the error message
        """
        message = "Operands of logical comparison operator not compatible."

        return message_code, message

    @classmethod
    def get_unit_base(cls) -> Tuple[MessageCode, str]:
        """
        construct an error message indicating that a non-int type was given as exponent to a unit type
        :return: the error message
        """
        message = "With a Unit base, the exponent must be an integer."

        return MessageCode.EXPONENT_MUST_BE_INTEGER, message

    @classmethod
    def get_non_constant_exponent(cls) -> Tuple[MessageCode, str]:
        """
        construct an error message indicating that the exponent given to a unit base is not a constant value
        :return: the error message
        """
        message = "Cannot calculate value of exponent. Must be a constant value!"

        return MessageCode.NON_CONSTANT_EXPONENT, message

    @classmethod
    def get_random_functions_legally_used(cls, name):
        message = "The function '" + name + "' can only be used in the update, onReceive, or onCondition blocks."
        return MessageCode.RANDOM_FUNCTIONS_LEGALLY_USED, message

    @classmethod
    def get_continuous_output_port_cannot_have_attributes(cls):
        message = "continuous time output port may not have attributes."
        return MessageCode.CONTINUOUS_OUTPUT_PORT_MAY_NOT_HAVE_ATTRIBUTES, message

    @classmethod
    def get_delay_variable_not_specified(cls) -> Tuple[MessageCode, str]:
        message = "Delay variable is not specified for synapse model. Please see https://nestml.readthedocs.io/en/latest/running/running_nest.html#dendritic-delay-and-synaptic-weight"

        return MessageCode.DELAY_VARIABLE_NOT_SPECIFIED, message

    @classmethod
    def get_weight_variable_not_specified(cls) -> Tuple[MessageCode, str]:
        message = "Weight variable is not specified for synapse model. Please see https://nestml.readthedocs.io/en/latest/running/running_nest.html#dendritic-delay-and-synaptic-weight"

        return MessageCode.WEIGHT_VARIABLE_NOT_SPECIFIED, message

    @classmethod
    def get_delay_variable_not_found(cls, variable_name: str) -> Tuple[MessageCode, str]:
        message = "Delay variable '" + variable_name + "' not found in synapse. Please see https://nestml.readthedocs.io/en/latest/running/running_nest.html#dendritic-delay-and-synaptic-weight"

        return MessageCode.DELAY_VARIABLE_NOT_FOUND, message

    @classmethod
    def get_weight_variable_not_found(cls, variable_name: str) -> Tuple[MessageCode, str]:
        message = "Weight variable '" + variable_name + "' not found in synapse. Please see https://nestml.readthedocs.io/en/latest/running/running_nest.html#dendritic-delay-and-synaptic-weight"

        return MessageCode.WEIGHT_VARIABLE_NOT_FOUND, message
