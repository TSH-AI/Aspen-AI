# 35 Sensitivity Blocks

This chapter describes the input language for defining sensitivity blocks.  

Use the SENSITIVITY paragraph to:  

Identify the flowsheet variables to be tabulated or to be used in FORTRAN expressions or inline FORTRAN statements, and equivalence them to FORTRAN variables using the DEFINE or VECTOR-DEF sentences.   
Select or compute the variables to be tabulated, using the TABULATE sentence and optional inline FORTRAN statements.   
Identify the feed stream or block input variables to be varied to generate the table, using the VARY sentence. Sensitivity blocks can have up to five varied variables when the plot sentence is not included. When you request plots, only one VARY sentence is allowed.  

You can use the SENSITIVITY paragraph to select values for each variable to be varied. You can select values by entering:  

A list of values.   
Lower and upper limits. Then enter either the number of equally-spaced points between the limits or the size of the increment between points. Use the RANGE statement for this purpose.  

# SENSITIVITY Block Paragraph  

# Input Language for SENSITIVITY  

SENSITIVITY sblockid   
DESCRIPTION "a sensitivity description - up to 64 characters in quotes"   
F FORTRAN declaration statements   
DEFINE fvar vartype     keyword $\mathbf { \bar { \rho } } = \mathbf { \rho }$ value   
VECTOR-DEF farray vectype     keyword $\mathbf { \bar { \rho } } = \mathbf { \rho }$ value   
F Executable FORTRAN statements   
TABULATE colno "expression" COL-LABEL $\mathbf { \lambda } =$ "line1". . ."line4" & UNIT-LABEL $\mathbf { \lambda } =$ "line5" "line6"   
VARY vartype keyword $\circleddash$ value   
RANGE keyword $\mathbf { \bar { \rho } } = \mathbf { \rho }$ value  

Keywords:  

<html><body><table><tr><td>LIST</td><td>LOWER</td><td>UPPER NPOINT</td><td>INCR</td></tr><tr><td>REINIT BLOCKS : PLOT</td><td>ALL [blockid -list keyword=value</td><td>STREAMS:</td><td>ALL sid -list</td></tr><tr><td>Optional keywords: COLUMNS</td><td>X-AXIS X-SCALE</td><td>Y-SCALE</td><td>PLOT-HEADING</td></tr><tr><td colspan="4">WIDE GRID INTERPOLATE PARAM keyword=value</td></tr><tr><td colspan="4">Optional keywords:</td></tr><tr><td colspan="4">WIDE HIGH-PRECISION BASE-CASE</td></tr><tr><td colspan="4">BLOCK-OPTIONS keyWOrd=value</td></tr></table></body></html>  

Keywords:  

# VAR-LEVEL TVAR-LEVEL  

# Input Language Description for SENSITIVITY  

sblockid Sensitivity block ID  

# DESCRIPTION  

A string of up to 64 characters enclosed in quotes. Aspen Plus prints this description in the header section of the SENSITIVITY block report.  

DEFINE, VECTOR-DEF  

Use to access a flowsheet variable and equivalence it to the FORTRAN variable fvar, which is used in the subsequent FORTRAN statements or the TABULATE or RANGE expressions to represent the flowsheet variable. VECTOR-DEF is similar to DEFINE except that VECTORDEF equivalences an entire stream or block profile results to the FORTRAN array, farray. A SENSITIVITY paragraph must contain at least one DEFINE or VECTOR-DEF sentence. See Chapters 29 and 30 for a complete discussion of the DEFINE and VECTOR-DEF sentences.  

# FORTRAN statements  

A FORTRAN statement is any valid FORTRAN statement subject to the restrictions discussed in the Aspen Plus User Guide. You can use FORTRAN comments (not shown). FORTRAN statements are needed only if the tabulated results or RANGE values are too complex to be represented by the TABULATE and RANGE expressions.  

# TABULATE  

Use to define the tabulated results. Enter one TABULATE sentence for each tabulated result, to generate one column in the sensitivity table. You can also use TABULATE to supply column headings for tabulated results. Column headings consist of six lines of eight characters each. The first four lines (COL-LABEL) identify the tabulated results. The last two lines (UNIT-LABEL) display the units of tabulated results. If the tabulated results expression is a single FORTRAN variable defined by a DEFINE sentence, then Aspen Plus automatically generates UNIT-LABEL. Otherwise, you must enter the UNIT-LABEL or leave it blank.  

colno. Table column number. Column number 1 is the first column after the columns for the varied variables.   
expression .. Any valid FORTRAN arithmetic expression enclosed in quotes ("). It is used to compute the tabulated values. Typically, expression is a single FORTRAN variable name, in which case you can omit the quotes.   
line1. . .line4 .. Column heading used to identify tabulated results. A string of up to eight characters enclosed in quotes (").   
line5. . .line6 .. Column heading used to display units of tabulated results. A string of up to eight characters enclosed in quotes (").  

VARY  

Use to identify the flowsheet variables that are to be varied to generate the table. Only block input and process feed stream variables can be varied. You must enter one VARY sentence and one RANGE sentence for each varied variable. A sensitivity block can have up to five VARY and RANGE sentences when a PLOT sentence is not included. When you request plotting, only one VARY sentence is allowed. See Chapters 29 and 30 for a complete discussion of the VARY sentence.  

RANGE  

Use to specify values for the varied variables. Aspen Plus generates one row of the table for each possible combination of varied variable values. You can use only one of the keywords LIST, NPOINT, INCR in a RANGE statement.  

LIST List of varied variable values   
LOWER. Lower limit of the varied variable range. It can be a constant or FORTRAN expression in terms of FORTRAN variables.   
UPPER. Upper limit of the varied variable range. It can be a constant or FORTRAN expression in terms of FORTRAN variables.   
NPOINT Number of points including LOWER and UPPER. It can also be any valid FORTRAN arithmetic expression in quotes.   
INCR . Increment size between intermediate points. It can also be any valid FORTRAN arithmetic expression in quotes.  

REINIT  

Use to reset convergence and unit operation restart flags. (See Chapter 45.) Also use to restore tear streams or streams manipulated by design specifications or by FORTRAN blocks to their initial values, and to reset any other flowsheet stream to zero flow.  

Normally, REINIT is not used, since it is usually most efficient to begin calculations for a new row evaluation with the results of the previous row evaluation.  

blockid-list... List of convergence and unit operation blocks for which the restart feature is suppressed when a new row evaluation begins. When restart is suppressed for a block, the initialization algorithm for the convergence method or unit operation model is invoked at the beginning of each row evaluation. IDs can be hierarchical; see Chapter 9 for naming conventions and restrictions. Enter ALL to reinitialize all blocks. (Default $\ c =$ no blocks are reinitialized)  

sid-list List of streams whose initial values are restored when a new row evaluation begins. IDs can be hierarchical; see Chapter 9 for naming conventions and restrictions. Enter ALL to reinitialize all streams. (Default $\mathbf { \sigma } =$ no streams are reinitialized)  

PLOT  

Use to generate print-plots of sensitivity block results. Only one VARY sentence is allowed when plots are produced. The variable named in the $\mathsf { X }$ -AXIS keyword is the independent variable for the plots. The column numbers specified in the PLOT sentence are the dependent variables for the plots. Up to five columns can be placed on a single plot. If you list more than five columns in a PLOT sentence, Aspen Plus will produce multiple plots.  

COLUMNS. List of column numbers from the TABULATE sentences for the dependent variables to be plotted. (Default $\ c =$ all columns)   
X-AXIS. Column number from the TABULATE sentence to be used as the independent variable for the plots. (Default $\ c =$ variable named in VARY sentence)   
X-SCALE. X-SCALE $\mathbf { \tau } =$ STANDARD Uses linear scale on horizontal axis of plots (Default) X-SCALE $\mathbf { \tau } =$ INVERSE Uses inverse scale on horizontal axis of plots   
Y-SCALE. Y-SCALE $\mathbf { \lambda } =$ STANDARD Uses linear scale on vertical axis of plots (Default) Y-SCALE $\mathbf { \lambda } =$ INVERSE Uses inverse scale on vertical axis of plots Y-SCALE $\mathbf { \lambda } =$ LOG Uses logarithmic scale on vertical axis of plots  

PLOT-HEADING.. Heading up to 64 characters included in quotes, printed at the top of the print-plot WIDE, GRID, . Plot options. Use to override the defaults established by the INTERPOLATE PLOT-OPTIONS paragraph. (See Chapter 46.)  

PARAM  

Use to specify the format of the table of results and execution options.  

WIDE WIDE=NO Generated tables are limited to 80 columns wide (Default) WIDE $\dot { \mathbf { \zeta } } = \dot { \mathbf { \zeta } }$ YES Generated tables are greater than 80 columns wide   
HIGH-PRECISION .. ..  HIGH-PRECISION $\mathbf { \tau } =$ YES Prints seven significant digits HIGH-PRECISION $= N O$ Prints five significant digits (Default)  

BASE-CASE.. Base-case execution options:  

BASE-CASE $\mathbf { \lambda } =$ LAST Executes base-case last (Default) BASE-CASE $\mathbf { \lambda } =$ FIRST Executes base-case first BASE-CASE $\mathbf { \lambda } =$ NO Does not execute base-case  

BLOCK-OPTIONS  

Use to override diagnostic message levels for the history file and the terminal, established by the DIAGNOSTICS paragraph (see Chapter 45).  

VAR-LEVEL Sets the level of diagnostics printed in the history file for FORTRAN variables that are used in the DEFINE and VECTOR-DEF sentences (default is set by HISTORY-VAR-LEVEL in the DIAGNOSTICS paragraph).   
TVAR-LEVEL Sets the level of diagnostics printed to the terminal for FORTRAN variables that are used in the DEFINE and VECTOR-DEF sentences (default is set by TERMINAL VAR-LEVEL in the DIAGNOSTICS paragraph).  
