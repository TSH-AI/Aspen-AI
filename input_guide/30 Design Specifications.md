# 30 Design Specifications  

This chapter describes the input language for defining design specifications.  

Use the DESIGN-SPEC paragraph to:  

Identify the sampled flowsheet variables and equivalence them to FORTRAN variables, by using the DEFINE or VECTOR-DEF sentences.   
Identify a flowsheet variable as the manipulated variable by using the VARY sentence.   
Supply a tolerance on the design specification by using the TOL-SPEC sentence.   
Supply upper and lower limits, and initial and maximum step sizes, for the manipulated variable, using the LIMITS sentence.   
Enter the design specification as a function of the FORTRAN variables, by using the SPEC sentence and optional inline FORTRAN statements.  

Accessed flowsheet variables, with the exception of VECTOR-DEF, are in units established by the IN-UNITS statement. You cannot specify alternative units through the use of brackets or braces. A DESIGN-SPEC can only access flowsheet objects which are global (such as property parameters) or which are contained (directly or indirectly) in the hierarchy where the DESIGN-SPEC is specified.  

# DESIGN-SPEC Paragraph  

# Input Language for DESIGN-SPEC  

DESIGN-SPEC specid   
F FORTRAN declaration statements   
DEFINE fvar vartype keyword $\mathop { \left. \sum \right.}  =$ value   
VECTOR-DEF farray vectype     keyword $\mathbf { \bar { \rho } } = \mathbf { \rho }$ value   
F Executable FORTRAN statements   
SPEC "expression1"   TO   "expression2"   
TOL-SPEC "tol"   
VARY vartype keyword $\mathbf { \bar { \Psi } } = \mathbf { \Psi }$ value   
LIMITS "lower" "upper" keyword $\mathbf { \bar { \rho } } = \mathbf { \rho }$ value  

Optional keywords for LIMITS:  

STEP-SIZE MAX-STEP-SIZE  

<html><body><table><tr><td colspan="4">EO-OPTIONS keyword=value</td></tr><tr><td colspan="4">Optional keywords:</td></tr><tr><td colspan="4">COMPS DERIV-METHOD SOLVE-METHOD INIT-ATTR vname keyword=value</td></tr><tr><td colspan="4">Optional keywords:</td></tr><tr><td colspan="4">VALUE LOWER UPPER STEP BOUND-TYPE UOM SCALE</td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4">SCRIPTS keyword=value</td></tr></table></body></html>  

Optional keywords:  

# METHOD TYPE LOCALSCRIPT GLOBALSCRIPT FILE  

# Input Language Description for DESIGN-SPEC  

specid Design specification ID  

# FORTRAN Statements  

Use in computing the design specification function and tolerance, and the manipulated variables limits. FORTRAN statements are needed only if the functions involved are too complex to be represented by the SPEC, TOL-SPEC, and LIMITS expressions. You can also use FORTRAN comments (not shown). See Chapter 31 and the Aspen Plus User Guide for a complete discussion of FORTRAN statements and expressions.  

DEFINE  

Use to access a sampled flowsheet variable and equivalence it to the FORTRAN variable fvar, which is used in subsequent FORTRAN statements or expressions to represent the flowsheet variable. There must be at least one DEFINE or VECTOR-DEF sentence in a design specification. Sampled variables are in the input units in effect for the design specification. Stream variables, stream properties, block input variables, and block results can be sampled.  

fvar . FORTRAN variable name limited to six characters. Aspen Plus will explicitly declare fvar as double precision or integer, based on the type of the accessed variable.  

vartype .. Sampled variable type:  

BLOCK-VAR  

Unit operation block variable  

<html><body><table><tr><td>PARAMETER</td><td>User-definedindirectvariable</td></tr><tr><td>STREAM-VAR</td><td>Streamvariable</td></tr><tr><td>basis-FLOW</td><td>Component flow ona MOLE,MASS,or STDVOL basis</td></tr><tr><td>basis-FRAC</td><td>Component fractionona MOLE,MASS,or STDVOL basis</td></tr><tr><td>STREAM-PROP</td><td>Stream property,defined using a PROP-SET paragraph. (See Chapter 41.)</td></tr><tr><td>INFO-VAR</td><td>Heat stream duty or work stream power</td></tr><tr><td>COMP-ATTR-VAR</td><td>Component attribute variable</td></tr><tr><td>SUBS-ATTR-VAR</td><td>Substreamattribute variable</td></tr><tr><td>CHEM-VAR</td><td>Chemistry variable</td></tr><tr><td>REACT-VAR</td><td>Reactionvariable</td></tr><tr><td>BALANCE-VAR</td><td>Balanceblockvariable</td></tr><tr><td>PRES-VAR</td><td>Pressurereliefvariable</td></tr><tr><td>UNARY-PARAM</td><td></td></tr><tr><td>UNARY-COR-EL</td><td>Unary parameter variable</td></tr><tr><td>UN-COR-VEC</td><td>Unary correlation variable</td></tr><tr><td></td><td>Unary correlation vector</td></tr><tr><td>BI-PARAM</td><td>Binary parameter variable</td></tr><tr><td>BI-COR-EL BI-COR-VEC</td><td>Binary correlation variable</td></tr><tr><td>NC-PARAM</td><td>Binary correlation vector Non-conventional component parametervariable</td></tr></table></body></html>  

VECTOR-DEF  

The remaining keywords for DEFINE depend on vartype. (See Chapter 29.)  

Similar to DEFINE except that VECTOR-DEF equivalences an entire stream or block profile result to the FORTRAN array, farray. VECTOR-DEF is useful when several variables from the same array are needed. There must be at least one DEFINE or VECTOR-DEF sentence in a design specification.  

farray. FORTRAN array name limited to five characters. Aspen Plus will explicitly declare farray as double precision or integer, based on the type of the accessed variable.  

vectype .... Sampled vector type:  

STREAM Stream vector SUBSTREAM Substream vector PROFILE Block vector COMP-ATTR Component attribute vector SUBS-ATTR Substream attribute vector  

SPEC  

The remaining keywords for VECTOR-DEF depend on vectype. (See Chapter 29.)  

Use to define the design specification function:   expression1 – expression2 = 0  

Where expression1 and expression2 are any valid FORTRAN arithmetic expressions. Typically, expression1 is a sampled flowsheet variable, and expression2 is a desired value for the variable, in which case you can omit the quotes ("). You must enter the SPEC sentence.  

TOL-SPEC  

Use to enter the design specification tolerance.   –tol $\rvert <$ expression1 – expression2 $\mathbf { \bar { \rho } } _ { < }$ tol  

Where tol is any valid FORTRAN arithmetic expression. Typically, tol is a constant, in which case you can omit the quotes ("). You must enter the TOL-SPEC sentence. Tolerance values specified in the DESIGN-SPEC paragraph are superseded by tolerance values specified in a CONVERGENCE paragraph.  

VARY  

Use to identify the manipulated variable. You can only manipulate block input or process feed stream variables. You cannot manipulate integer block input variables (for example, the feed location of a distillation column). The manipulated block or stream variable must either be a variable that you specify in the BLOCK or STREAM paragraph, or it must have a default value. The specified or default value is used as an initial estimate by the design specification. The initial guess used for a manipulated variable is the stream or block input specification for the variable. You must enter the VARY sentence. See Chapter 29 for a complete discussion of the VARY sentence. The remaining keywords for VARY depend on vartype. (See Chapter 29.)  

LIMITS  

Use to specify limits for the manipulated variable, where lower and upper are any valid FORTRAN arithmetic expressions. LIMITS expressions are evaluated before the first iteration of design specification convergence loops. They are not re-evaluated before subsequent iterations. Typically the limits are constants, in which case you can omit the quotes ("). You must enter the LIMITS sentence. You can also use the LIMITS sentence to enter initial step size and maximum step size:  

STEP-SIZE. Initial step size for the manipulated variable. Step size is defined as a fraction of the range (upper limit minus lower limit). Values entered in a CONVERGENCE paragraph supersede values entered in the DESIGN-SPEC paragraph.   
MAX-STEP-SIZE ... Maximum step size for the manipulated variable. Step size is defined as a fraction of the range (upper limit minus lower limit). Values entered in a CONVERGENCE paragraph supersede values entered in the DESIGN-SPEC paragraph.  

EO-OPTIONS  

Use to specify equation-oriented options for the Design Spec.  

COMPS Component group for a list of components which can be active in this Design Spec.  

DERIV-METHOD .... Preferred derivatives method, Analytic or Numeric. Update methods should not be used for Degree of Freedom run modes (Optimization or Reconciliation).  

DERIV-METHOD $\mathbf { \sigma } = \mathbf { \sigma }$ ANALYTICAL  

DERIV-METHOD $\mathbf { \tau } = \mathbf { \tau }$ NUMERICAL  

DERIV-METHOD $\mathbf { \tau } = \mathbf { \tau }$ UPDATE-ANALY  

Model derivatives (Jacobian) are determined from coded analytic expressions. Generally the preferred method.   
Alternate method for calculating Jacobian. Useful when there is concern that analytic derivatives are causing convergence difficulties. Usually   
slower than analytic derivatives, more subject to precision issues. (Default)   
Use Schubert method for updating Jacobian, with analytic derivatives for the Base Jacobian. Use when Jacobian calculation is rate limiting step. May result in more iterations and be less robust than calculated derivatives.   
Use Schubert method for updating Jacobian, with numerical derivatives for the Base Jacobian. Use when Jacobian calculation is rate limiting step. May result in more iterations and be less robust than calculated derivatives.  

DERIV-METHOD $\mathbf { \tau } = \mathbf { \tau }$ UPDATE-NUMER  

SOLVE-METHOD ......  

.  EO solution method. Specifies if open, closed, or neither method should be used with desired action and message level on failure.  

SOLVE-METHOD= DO-NOT-CREAT SOLVE-METHOD $\mathbf { \lambda } =$ PERTURBATION  

Ignore during EO solution. (Default)  

Closed solution method; use Perturbation layer around closed model.  

Use to specify the attributes of open variables.   
vname.. Name of the variable. (Required)   
VALUE.. Current value of the variable.   
LOWER... ...  Lower bound.   
UPPER. .  Upper bound.   
STEP .  Step bound.   
BOUND-TYPE . .  Bound type. BOUND-TYPE $\mathbf { \tau } = \mathbf { \tau }$ HARD Do not violate the upper and/or lower bounds when solving a non-square (optimization or data regression) problem. BOUND-TYPE $\mathbf { \lambda } =$ RELAXED Relax upper and/or lower bound. If the initial value is outside the bound, set the bound to the initial value. BOUND-TYPE $\mathbf { \tau } = \mathbf { \tau }$ SOFT Same as relaxed but add a penalty term to the objective to try to drive the value back to the bound.  

SCRIPTS  

SBWEIGHT . Soft bound weight.   
PHYS-QTY ... The physical quantity that the variable represents, for example, mole flow, temperature, or pressure. These types correspond to the standard Aspen Plus types.   
UOM. Units of measure (standard Aspen Plus units), based on the physical type of the variable. Internally, all values are stored in SI units.   
SCALE . Scale factor used by the solver.   
Use this sentence to specify scripts for a block.   
METHOD . Script method. Blocks support default script methods of SETUP and INIT. User may define other methods. (Required)   
TYPE Type of script (Required) TYPE $\mathbf { \tau } = \mathbf { \tau }$ LOCALSCRIPT Local Script TYPE $\mathbf { \lambda } = \mathbf { \lambda }$ GLOBALSCRIPT Global Script TYPE $\mathbf { \lambda } = \mathbf { \lambda }$ FILE File   
LOCALSCRIPT . ID of a LOCAL SCRIPT paragraph. See Chapter 48.   
GLOBALSCRIPT ...... ..  ID of a GLOBAL SCRIPT paragraph. See Chapter 48.   
FILE . Name of a file  