import os
import copy


from typing import Sequence, Optional, Mapping, Any

from pynestml.cocos.co_cos_manager import CoCosManager
from pynestml.codegeneration.code_generator import CodeGenerator

from pynestml.visitors.ast_parent_visitor import ASTParentVisitor


from pynestml.codegeneration.code_generator import CodeGenerator
from pynestml.codegeneration.nest_code_generator import NESTCodeGenerator
from pynestml.codegeneration.printers.cpp_expression_printer import CppExpressionPrinter
from pynestml.codegeneration.printers.cpp_printer import CppPrinter
from pynestml.codegeneration.printers.c_simple_expression_printer import CSimpleExpressionPrinter
from pynestml.codegeneration.printers.gsl_variable_printer import GSLVariablePrinter
from pynestml.codegeneration.printers.ode_toolbox_expression_printer import ODEToolboxExpressionPrinter
from pynestml.codegeneration.printers.ode_toolbox_function_call_printer import ODEToolboxFunctionCallPrinter
from pynestml.codegeneration.printers.ode_toolbox_variable_printer import ODEToolboxVariablePrinter

from pynestml.codegeneration.printers.spinnaker_c_function_call_printer import SpinnakerCFunctionCallPrinter
from pynestml.codegeneration.printers.spinnaker_c_type_symbol_printer import SpinnakerCTypeSymbolPrinter
from pynestml.codegeneration.printers.spinnaker_c_variable_printer import SpinnakerCVariablePrinter
from pynestml.codegeneration.printers.spinnaker_gsl_function_call_printer import SpinnakerGSLFunctionCallPrinter


from pynestml.codegeneration.printers.constant_printer import ConstantPrinter
from pynestml.codegeneration.printers.python_expression_printer import PythonExpressionPrinter
from pynestml.codegeneration.printers.python_standalone_printer import PythonStandalonePrinter
from pynestml.codegeneration.printers.python_stepping_function_function_call_printer import PythonSteppingFunctionFunctionCallPrinter
from pynestml.codegeneration.printers.python_stepping_function_variable_printer import PythonSteppingFunctionVariablePrinter
from pynestml.codegeneration.printers.python_variable_printer import PythonVariablePrinter
from pynestml.codegeneration.printers.spinnaker_python_function_call_printer import SpinnakerPythonFunctionCallPrinter
from pynestml.codegeneration.printers.spinnaker_python_simple_expression_printer import SpinnakerPythonSimpleExpressionPrinter
from pynestml.codegeneration.printers.spinnaker_python_type_symbol_printer import SpinnakerPythonTypeSymbolPrinter
from pynestml.codegeneration.python_standalone_code_generator import PythonStandaloneCodeGenerator
from pynestml.meta_model.ast_model import ASTModel
from pynestml.visitors.ast_symbol_table_visitor import ASTSymbolTableVisitor


class CustomNESTCodeGenerator(NESTCodeGenerator):
    def setup_printers(self):
        self._constant_printer = ConstantPrinter()

        # C/Spinnaker API printers
        self._type_symbol_printer = SpinnakerCTypeSymbolPrinter()
        self._nest_variable_printer = SpinnakerCVariablePrinter(expression_printer=None, with_origin=True,
                                                                with_vector_parameter=True)
        self._nest_function_call_printer = SpinnakerCFunctionCallPrinter(None)
        self._nest_function_call_printer_no_origin = SpinnakerCFunctionCallPrinter(None)

        self._printer = CppExpressionPrinter(
            simple_expression_printer=CSimpleExpressionPrinter(variable_printer=self._nest_variable_printer,
                                                               constant_printer=self._constant_printer,
                                                               function_call_printer=self._nest_function_call_printer))
        self._nest_variable_printer._expression_printer = self._printer
        self._nest_function_call_printer._expression_printer = self._printer
        self._nest_printer = CppPrinter(expression_printer=self._printer)

        self._nest_variable_printer_no_origin = SpinnakerCVariablePrinter(None, with_origin=False,
                                                                          with_vector_parameter=False)
        self._printer_no_origin = CppExpressionPrinter(
            simple_expression_printer=CSimpleExpressionPrinter(variable_printer=self._nest_variable_printer_no_origin,
                                                               constant_printer=self._constant_printer,
                                                               function_call_printer=self._nest_function_call_printer_no_origin))
        self._nest_variable_printer_no_origin._expression_printer = self._printer_no_origin
        self._nest_function_call_printer_no_origin._expression_printer = self._printer_no_origin

        # GSL printers
        self._gsl_variable_printer = GSLVariablePrinter(None)
        self._gsl_function_call_printer = SpinnakerGSLFunctionCallPrinter(None)

        self._gsl_printer = CppExpressionPrinter(
            simple_expression_printer=CSimpleExpressionPrinter(variable_printer=self._gsl_variable_printer,
                                                               constant_printer=self._constant_printer,
                                                               function_call_printer=self._gsl_function_call_printer))
        self._gsl_function_call_printer._expression_printer = self._gsl_printer

        # ODE-toolbox printers
        self._ode_toolbox_variable_printer = ODEToolboxVariablePrinter(None)
        self._ode_toolbox_function_call_printer = ODEToolboxFunctionCallPrinter(None)
        self._ode_toolbox_printer = ODEToolboxExpressionPrinter(
            simple_expression_printer=CSimpleExpressionPrinter(
                variable_printer=self._ode_toolbox_variable_printer,
                constant_printer=self._constant_printer,
                function_call_printer=self._ode_toolbox_function_call_printer))
        self._ode_toolbox_variable_printer._expression_printer = self._ode_toolbox_printer
        self._ode_toolbox_function_call_printer._expression_printer = self._ode_toolbox_printer



class CustomPythonStandaloneCodeGenerator(PythonStandaloneCodeGenerator):
    def setup_printers(self):
        super().setup_printers()

        self._type_symbol_printer = SpinnakerPythonTypeSymbolPrinter()
        self._constant_printer = ConstantPrinter()

        # Python/mini simulation environment API printers
        self._nest_variable_printer = PythonVariablePrinter(expression_printer=None, with_origin=False,
                                                            with_vector_parameter=True)
        self._nest_function_call_printer = SpinnakerPythonFunctionCallPrinter(None)
        self._nest_function_call_printer_no_origin = SpinnakerPythonFunctionCallPrinter(None)

        self._printer = PythonExpressionPrinter(simple_expression_printer=SpinnakerPythonSimpleExpressionPrinter(
            variable_printer=self._nest_variable_printer,
            constant_printer=self._constant_printer,
            function_call_printer=self._nest_function_call_printer))
        self._nest_variable_printer._expression_printer = self._printer
        self._nest_function_call_printer._expression_printer = self._printer
        self._nest_printer = PythonStandalonePrinter(expression_printer=self._printer)

        self._nest_variable_printer_no_origin = PythonVariablePrinter(None, with_origin=False,
                                                                      with_vector_parameter=False)
        self._printer_no_origin = PythonExpressionPrinter(
            simple_expression_printer=SpinnakerPythonSimpleExpressionPrinter(
                variable_printer=self._nest_variable_printer_no_origin,
                constant_printer=self._constant_printer,
                function_call_printer=self._nest_function_call_printer_no_origin))
        self._nest_variable_printer_no_origin._expression_printer = self._printer_no_origin
        self._nest_function_call_printer_no_origin._expression_printer = self._printer_no_origin

        # GSL printers
        self._gsl_variable_printer = PythonSteppingFunctionVariablePrinter(None)
        self._gsl_function_call_printer = PythonSteppingFunctionFunctionCallPrinter(None)
        self._gsl_printer = PythonExpressionPrinter(simple_expression_printer=SpinnakerPythonSimpleExpressionPrinter(
            variable_printer=self._gsl_variable_printer,
            constant_printer=self._constant_printer,
            function_call_printer=self._gsl_function_call_printer))
        self._gsl_function_call_printer._expression_printer = self._gsl_printer
        self._gsl_variable_printer._expression_printer = self._gsl_printer

class Spinnaker2CodeGenerator(CodeGenerator):
    """
    Code generator for Spinnaker 2
    """

    _default_options = {
        # "neuron_synapse_pairs": [],
        "templates": {
            "path": os.path.join(os.path.realpath(os.path.join(os.path.dirname(__file__), "resources_spinnaker2"))),
            "model_templates": {
                "neuron":  ["@NEURON_NAME@.py.jinja2",
                            "@NEURON_NAME@.c.jinja2",
                            "@NEURON_NAME@.h.jinja2",
                            "decay.h.jinja2",
                            "global_params.h.jinja2",
                            "neuron.c.jinja2",
                            "neuron.h.jinja2",
                            "neuron_model.h.jinja2",
                            "neuron_model_@NEURON_NAME@_impl.c.jinja2",
                            "neuron_model_@NEURON_NAME@_impl.h.jinja2",
                            "param_defs.h.jinja2",
                            "population_table.h.jinja2",
                            "regions.h.jinja2",
                            "simulation.h.jinja2",
                            "synapse_row.h.jinja2",
                            "synapses.c.jinja2",
                            "synapses.h.jinja2",
                            ],
            },
            "module_templates": []
        }
    }

    def __init__(self, options: Optional[Mapping[str, Any]] = None):
        super().__init__(options)

        options_cpp = copy.deepcopy(NESTCodeGenerator._default_options)
        # options_cpp["neuron_synapse_pairs"] = self._options["neuron_synapse_pairs"]
        options_cpp["templates"]["model_templates"]["neuron"] = [fname for fname in
                                                                 self._options["templates"]["model_templates"]["neuron"]
                                                                 if ((fname.endswith(".h.jinja2") or fname.endswith(".c.jinja2")
                                                                      or ("Makefile" in fname)) and "@NEURON_NAME@" in fname)]
        # options_cpp["templates"]["model_templates"]["synapse"] = [fname for fname in
        #                                                           self._options["templates"]["model_templates"]["synapse"]
        #                                                           if ((fname.endswith(".h.jinja2") or fname.endswith(".c.jinja2") or ("Makefile" in fname)) and "@SYNAPSE_NAME@" in fname)]
        # options_cpp["nest_version"] = "<not available>"
        # options_cpp["templates"]["module_templates"] = self._options["templates"]["module_templates"]
        options_cpp["templates"]["path"] = self._options["templates"]["path"]
        self.codegen_cpp = CustomNESTCodeGenerator(options_cpp)

        options_py = copy.deepcopy(PythonStandaloneCodeGenerator._default_options)
        options_py["templates"]["model_templates"]["neuron"] = [fname for fname in
                                                                self._options["templates"]["model_templates"]["neuron"]
                                                                if (fname.endswith(".py.jinja2")) and ("@NEURON_NAME@" in fname or fname == "__init__.py.jinja2")]
        # options_py["templates"]["model_templates"]["synapse"] = [fname for fname in
        #                                                          self._options["templates"]["model_templates"][
        #                                                              "synapse"] if (fname.endswith(".py.jinja2")) and "@SYNAPSE_NAME@" in fname]
        options_py["nest_version"] = "<not available>"
        options_py["templates"]["module_templates"] = []
        options_py["templates"]["path"] = self._options["templates"]["path"]
        self.codegen_py = CustomPythonStandaloneCodeGenerator(options_py)

    def generate_code(self, models: Sequence[ASTModel]) -> None:
        cloned_models = []
        for model in models:
            cloned_model = model.clone()
            cloned_model.accept(ASTParentVisitor())
            cloned_model.accept(ASTSymbolTableVisitor())
            CoCosManager.check_cocos(cloned_model)
            cloned_models.append(cloned_model)

        self.codegen_cpp.generate_code(cloned_models)
        self.codegen_py.generate_code(cloned_models)
