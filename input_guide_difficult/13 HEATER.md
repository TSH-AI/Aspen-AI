# HEATER: Heater/Cooler  

# Input Language for HEATER  

BLOCK blockid HEATER PARAM keyword $\mathbf { \bar { \Psi } } = \mathbf { \Psi }$ value  

Keywords:  

TEMP PRES VFRAC DUTY DELT DEGSUB DEGSUP Optional keywords:  

NPHASE PHASE MAXIT TOL T-EST P-EST  

HCURVE curveno keyword=value  

Optional keywords:  

INDEP-VAR LIST NPOINT    INCR    HEADING PROPERTIES PRES-PROFILEPDROP PRINT-PLOT HIGH-PRECISION LINES X-SCALE Y-SCALEWIDE GRID INTERPOLATE  

UTILITY UTILITY-ID $\mathbf { \lambda } =$ utilityid  

# Input Language Description for HEATER  

PARAM  

<html><body><table><tr><td colspan="3">Use to specify outlet conditions of the heater.</td></tr><tr><td>TEMP..</td><td colspan="2">Temperature</td></tr><tr><td>PRES.</td><td>PRES >0</td><td>Pressure</td></tr><tr><td rowspan="4">VFRAC</td><td>PRES ≤ 0</td><td>Pressure drop (Default=0)</td></tr><tr><td>Molar vapor fraction.Enter O.0 for bubble point，1.O for dew point.</td><td></td></tr><tr><td>For subcooled or superheated vapor use TEMP,DEGSUB,or</td><td></td></tr><tr><td colspan="2">DEGSUP specifications.VFRAC is allowed only when NPHASE >1.</td></tr><tr><td>DUTY. DELT</td><td>Heat duty Temperature change</td><td></td></tr><tr><td>DEGSUB..</td><td>Degrees of subcooling</td><td></td></tr><tr><td>DEGSUP</td><td>Degrees of superheat</td><td></td></tr><tr><td>NPHASE</td><td>Number of phases in MIXED substream:</td><td></td></tr><tr><td rowspan="5"></td><td>NPHASE=1</td><td>One-phase calculation</td></tr><tr><td>NPHASE=2</td><td>Two-phase flash (Default)</td></tr><tr><td>NPHASE=3</td><td>Three-phase flash</td></tr><tr><td>Specifies the phase when NPHASE=1:</td><td></td></tr><tr><td></td><td></td></tr><tr><td rowspan="3"></td><td>PHASE=V</td><td>Vapor (Default)</td></tr><tr><td>PHASE=L Liquid</td><td></td></tr><tr><td>PHASE=S</td><td>Solid. Use for electrolytes system only.</td></tr><tr><td>MAXIT TOL.. Flash convergence tolerance. (Default=value established by the</td><td>the SIM-OPTIONS paragraph.) (See Chapter 45.)</td><td>Maximum number of flash iterations. (Default=value established by</td></tr></table></body></html>  

T-EST Temperature estimate. Use to aid convergence when PRES and either VFRAC or DUTY are specified.   
P-ES Pressure estimate. Use to aid convergence when temperature (one of TEMP, DELT, DEGSUB, or DEGSUP) and either VFRAC or DUTY are specified.  

Use to generate heating or cooling curve tables and plots. See Chapter 11 for a description of the input keywords.  

UTILITY  

Use to specify an optional utility to provide heating or cooling duty.  

UTILITY-ID .... Utility ID.  

# Accessing Variables in HEATER  

Many Aspen Plus features enable you to sample or change block variables. Chapter 29 describes how to access variables. The following tables list variable names and other information needed to sample and/or change variables for this block.  

Block Input   


<html><body><table><tr><td>Sentence Variables</td><td></td><td>ID1</td></tr><tr><td>PARAM EST</td><td>TEMP，PRES,VFRAC,DUTY,DELT,DEGSUB,DEGSUP,MAXIT,TOL,T-EST，P-</td><td>1</td></tr><tr><td>HCURVE</td><td>NPOINT，INCR，PDROP</td><td>curveno</td></tr></table></body></html>  

# Block Results  

<html><body><table><tr><td>Description</td><td>Sentence</td><td>Variable</td></tr><tr><td>Heat duty</td><td>PARAM</td><td>QCALC</td></tr><tr><td>Net heat duty</td><td>RESULTS</td><td>NET-DUTY</td></tr></table></body></html>  