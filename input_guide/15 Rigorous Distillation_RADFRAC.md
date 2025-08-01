 # 15 Rigorous Distillation  

This chapter describes the input language for the rigorous distillation models. The models are:   


<html><body><table><tr><td>Model</td><td>Description Purpose</td><td></td><td>Use to model</td></tr><tr><td>RADFRAC</td><td>Rigorous fractionation</td><td>Rigorous rating and design calculations for single columns</td><td>Ordinary distillation,absorbers，strippers, extractive and azeotropic distillation,three-phase distillation,andreactive distillation</td></tr><tr><td>MULTIFRAC Rigorous</td><td>fractionation for complex columns</td><td>Rigorous rating and complexity</td><td>Heat integrated columns,air separation columns, design calculations forabsorber/stripper combinations,ethylene plant multiple columns of any primary fractionator/quench tower combinations, andpetroleumrefiningapplications</td></tr><tr><td>PETROFRAC Petroleum</td><td>refining fractionation</td><td>Rigorous rating and design calculations for complex columns in petroleum refining applications</td><td>Preflash tower,atmospheric crude unit,vacuum unit,catalytic crackermain fractionator,delayed coker main fractionator,vacuum lube fractionator，and ethylene plant primary fractionator/quench tower combinations</td></tr></table></body></html>

See also Chapter 16 for input language used with these models for rating and sizing calculations for trays and packing, and Chapter 17 for input language used with RADFRAC for the RateSep rate-based distillation feature.  

# RADFRAC: Rigorous Fractionation  

Input Language for RADFRAC  

BLOCK blockid RADFRAC   
SUBOBJECTS PUMPAROUND $\mathbf { \sigma } =$ paid   
PROP-SECTIONS stage1 stage2 opsetname keyword $\circleddash$ value  

Keywords:  

# FREE-WATER SOLU-WATER HENRY-COMPS CHEMISTRY PHASE-EQM  

<html><body><table><tr><td>PARAM</td><td>keyword=value</td></tr></table></body></html>  

Keywords:  

NSTAGE NPA NPHASE Optional keywords:  

ALGORITHM EFF INIT-OPTION SOLID-BAL HYDRAULIC P-UPDATE P-FIX DAMPING MAXOL TOLOL ABSORBER CMAXNI0 CMAXNI1 DSMETH DTMAX EFF-FLASH FLASH-MAXIT FLASH-TOL FLASH-VFRAC FMINFAC GAMMA-MODEL HMODEL1 HMODEL2 ILMETH JMETH KBBMAX KMODEL L2-CUTOFF L2-GAMMA LL-MAXIT LL-METH MAX-BROY MAX-SIZE MAXIL MAXIP PROD-FLASH QMAXBWIL QMAXBWOL QMINBWIL QMINBWOL RMSOL0 RMSOL1 RMSOLJ STOR-FACTOR TOLILFAC TOLILMIN TOLIL0 FLASH-TOLIL PHEQM-FORM RADIUS-FRAC  

COL-CONFIG keyword=value  

Keywords:  

# CONDENSER REBOILER KEY-SELECT  

FEEDS sid stage [feed-conv]  / PRODUCTS sid stage [phase]     [basis-FLOW $\mathbf { \tau } =$ value]  /  . SDRAW:FEED sid ratio keyword $\mathbf { \bar { \rho } } = \mathbf { \rho }$ value  /  

Keywords: STREAMS COMPS  

PSEUDO-STREAM sid stage keyword $\circleddash$ value  /  .  

Keywords: PHASE MOLE-FLOW PA STATE  

P-SPEC stage pres  

Keywords:  

basis-RDV T1 basis-D basis-B D:F B:F basis-D:F basis-B:F basis-L1 basis-VN basis-RR basis-BR Q1 QN Optional keywords:  

RW DP-STAGE DP-COL DP-COND HTLOSS  

PDROP-SEC secno stage1 stage2 pdrop  / . . DB:F-PARAMS keyword $\mathbf { \bar { \rho } } = \mathbf { \rho }$ value  

Keywords: STREAMS COMPS  

SC-REFLUX keyword=value  

Keywords:   
DEGSUB TEMP Optional keyword: OPTION  

THERMOSYPHON keyword=value  

Keywords:  

PRES TEMP DELT VFRAC basis-FLOW RETURN-CONV  

PUMPAROUND paid stage1 stage2 keyword=value  

Keywords:  

DRAW-PHASE TYPE basis-FLOW TEMP DELT DUTY VFRAC PRES NPHASE RETURN-PHASE FEED-CONV QSTREAM-IN QSTREAM-OUT  

HEATERS stage duty  / COOLANT stage cid opsetname keyword=value  

Keywords:  

basis-FLOW UA TEMP PRES PHASE basis-CP  

HTLOSS-SEC  secno  stage1  stage2   HTLOSS-SEC $\backslash =$ value   HTLOSS-VAP $\mathbf { \lambda } =$ value / . . HTLOSS HTLOSS-LIQ $\mathbf { \lambda } =$ value HTLOSS-VAP $\mathbf { \lambda } =$ value   
COMP-EFF stage cid     eff  /   
STAGE-EFF stage eff  /   
STEFF-SEC secno stage1 stage2 eff  /   
DECANTERS stage keyword $\mathbf { \bar { \rho } } = \mathbf { \rho }$ value  

Keywords:  

L1-SPEC L2-SPEC Optional keywords:  

<html><body><table><tr><td>TEMP</td><td>DEGSUB</td><td>DECANT-SOLID</td></tr><tr><td>L2-COMPS</td><td>cid-list</td><td></td></tr><tr><td>L2-STAGES</td><td>stage1</td><td>stage2 /</td></tr><tr><td>L1-RETURN</td><td> stage1</td><td>stage2 I1-rfrac /..</td></tr></table></body></html>  

L2-RETURN stage1 stage2 l2-rfrac  /   
L1-COMP-EFF stage cid eff  / . .   
L2-COMP-EFF stage cid eff  /   
L1-STAGE-EFF stage eff /   
L2-STAGE-EFF stage eff   
KLL-STAGES kllno stage1 stage2   
basis-KLL KLL-NO $\mathbf { \lambda } =$ value KLL-CID $\mathbf { \lambda } =$ cid KLL-A $\mathbf { \lambda } =$ value [KLL-B=value] & [KLL-C $\mathbf { \lambda } =$ value] [KLL-D $\mathbf { \lambda } =$ value]   
REAC-STAGES stage1 stage2 reacid  /   
HOLD-UP stage1 stage2    keyword $\mathbf { \bar { \rho } } = \mathbf { \rho }$ value  /  

Keywords:  

<html><body><table><tr><td>basis-LHLDP</td><td colspan="4">basis-VHLDP</td></tr><tr><td colspan="4">RES-TIME stage1 stage2 keyword=value /</td></tr><tr><td colspan="4">Keywords: LTIME VTIME</td></tr><tr><td colspan="4">CONVERSION stage reacno frac T-EST stage temp / X-EST stage cid x/ Y-EST stage cid y L-EST stage mole-flow / V-EST stage mole-flow / VL-EST stage mole-ratio / REPORT reportopt-list</td></tr><tr><td colspan="4">Special reportoptions: NOPROFILE NOCOMPS NOHYDRAULIC NOENTH NOSPLITS STDVPROI TARGET HYDANAL EXTHYD INT-PROF INT-AREA BULKRXN DIFF- COE MT-RATE MT-COEFF HT-RATE HT-COEFF FILMRXN S-DIMLES V-DIMLES</td></tr><tr><td colspan="4">SPC-OPTIONS keyword=value</td></tr><tr><td colspan="4">Optional keywords: EFF D B RR L1 BR VN Q1 QN L V Q-STAGE WL wv SPEC SC-REFLUX</td></tr><tr><td colspan="4">SPC-OPTION2 keyword=value</td></tr><tr><td colspan="4">Optional keywords: PRES FEEDDP FEEDOPEN CS-ALLBASIS SPLIT-ALL</td></tr><tr><td colspan="4">KEY-COMP secno stage1 stage2 LIGHT-KEY=cid-list HEAVY-KEY=cid-list KEY-TOL keyword=value</td></tr><tr><td colspan="4">Optional keywords: KVAL-TOL COMP-TOL SPF-LIMIT STG-SPAN EXCLD-KEY EXG-TREF</td></tr><tr><td colspan="4">CONVERGENCE keyword=value</td></tr><tr><td colspan="4">Optional keywords: MAN-3P-PASS STABLE-ITER STABLE-METH PROP-DERIV NQ-PROF-MAX NQ-FOPT-METH NQ-TOLOL NQ-TOLOBJ</td></tr></table></body></html>  

Optional keywords:  

TRAY-OPTION FORMAT ORDER PROPERTIES WIDE  

TRAY-REPOPT    keyword=value  

Optional keywords: FLOW-OPTION  

INCL-TRAYS [stage1] [stage2]  /  . COND-HCURVE curveno keyword $\ c =$ value REB-HCURVE curveno keyword $\circleddash$ value PA-HCURVE paid curveno keyword=value  

Optional keywords:  

INDEP-VAR LIST NPOINT INCR HEADING PROPERTIES PRES-  
PROFILE PDROP PRINT-PLOT HIGH-PRECISION LINES X-SCALE Y-  
SCALE  
WIDE GRID INTERPOLATE  

VARY varyno vartype lb ub [step] keyword=value  

Vartypes:  

basis-RDV basis-D basis-B D:F B:F basis-D:F basis-B:F basis-L1   
basis-VN basis-RR basis-BR Q1 QN RW basis-LPROD basis  
VPROD   
DUTY FEED-FLOW HEAT-STREAM MURPHREE TREB DTREB VREB   
basis-RFLOW L1-SPEC L2-SPEC basis-PA-FLOW PA-TEMP PA-DELT   
PA-DUTY PA-VFRAC SDRAW:FEED   
Keywords:  

<html><body><table><tr><td>STAGE</td><td>STREAM</td><td>STAGE1</td><td>STAGE2</td><td></td><td>COMPS PA</td><td></td></tr><tr><td>SPEC</td><td>specno</td><td>spectype</td><td>value</td><td>[scale]</td><td>[weight]</td><td>keyword=value</td></tr></table></body></html>  

Spectypes:  

basis-FRAC basis-RECOV basis-FLOW basis-RATIO TEMP PROP   
PROP-DIFF PROP-RATIO basis-D basis-B basis-L1 basis-VN   
basis-RR basis-BR Q1 QN   
Keywords:  

STAGE BASE-STAGE COMPS BASE-COMPS STREAMSBASE-STREAMS PROPERTY BASE-PROPERTY DEC-STREAMOptional keywords:  

PHASE BASE-PHASE  

DIAGNOSTICS keyword=value  

Keywords:  

MAIN OLVAR1 OLVAR2 CMBAL EMBAL DESIGN TERM TXYEST  

NQ-CURVE keyword=value  

Keywords:   
CURVE-NO NSTAGE-MIN NSTAGE-MAX FEED OBJECT-FUNC   
QR-QC-COST   
Optional keywords:  

NSTAGE-STEP RR-MIN LMT-FROM-TOP LMT-FROM-BOT  

NQCUR-FOPT keyword=value  

Keywords:CURVE-NO SID REMAIN-OPT  

NQCUR-SOPT keyword $\mathbf { \bar { \Psi } } = \mathbf { \Psi }$ value  

Keywords:CURVE-NO SID SDRAW-OPT  

NQCUR-PAOPT keyword=value  

Keywords: CURVE-NO IC-STREAM PA-OPT  

NQCUR-DECTOP keyword $\circleddash$ value  

Keywords:CURVE-NO STAGE DECT-OPT  

PLOT plotno plot-list comp-plot=groupid-list keyword=value  

Plot-list options:  

TEMP PRES LRATE VRATE VL-RATIO LL-RATIO Comp-plot options:  

X     X1     X2     Y     KVL KVL1 KVL2 KLL REL-VOL S-PLOT Optional keywords:  

BASE-COMP S-OPTION HEAVY-KEY BASIS ORDER PLOT-HEADING WIDE  

SUBROUTINE KLL $\ c =$ subrname KLL-USER stage1 stage2  /  . KLL-VECS keyword $\mathbf { \bar { \rho } } = \mathbf { \rho }$ value  

Keywords: NINT NREAL  

KLL-INT VALUE-LIST $\mathbf { \bar { \Pi } } = \mathbf { \bar { \Pi } }$ values KLL-REAL VALUE-LIST $\mathbf { \delta } =$ values USERK-VECS keyword $\circleddash$ value  

Keywords:  

NINT NREAL NIWORK NWORK  

USERK-INT VALUE-LIST $\mathbf { \bar { \Pi } } = \mathbf { \bar { \Pi } }$ values USERK-REAL VALUE-LIST $\mathbf { \lambda } =$ values STG-UTL stage utilityid PA-UTL pid utilityid UTILITIES keyword $\circleddash$ value  

Optional keywords:  

COND-UTIL REB-UTIL  

Keywords: SALTS SAT-LIMIT  

# Input Language Description for RADFRAC  

SUBOBJECTS  

Use to enter a list of IDs for pumparounds. The IDs are character strings of up to eight characters long. They are used for referencing pumparounds in other input statements. If you do not enter IDs using the SUBOBJECTS statement, pumparounds are referenced by sequential integer numbers.  

# PUMPAROUND.... List of pumparound IDs  

PROP-SECTIONS  

Use to specify property options for a column segment, the thermosyphon reboiler, or a decanter. PROP-SECTIONS overrides the PROPERTIES sentence for a column segment, the thermosyphon reboiler, or a decanter. The input language for PROP-SECTIONS is the same as for the PROPERTIES sentence, except that PROP-SECTIONS requires that you specify the column segment. See Chapter 11, for more information about the PROPERTIES sentence. Column initialization calculations are always performed using the specifications in the PROPERTIES sentence, regardless of the specifications given in the PROP-SECTIONS sentence. Therefore, it is important that the property option in the PROPERTIES sentence gives reasonable property representation at the average condition of the column. Any option set name entered in the PROP-SECTIONS sentence must also be named in the PROPERTIES sentence. (For more information about specifying an option set, see Chapter 8.)  

stage1... For column segment, stage1 $\ c =$ starting stage number of column segment; for decanter, stage1 $\ c =$ decanter stage number; for thermosyphon reboiler, stage1 $\ c =$ bottom stage number.   
stage2. For column segment, stage2 $\ c =$ ending stage number of column segment; for decanter, enter D in this position; for thermosyphon reboiler, enter R.   
opsetname... Property option set used for column segment   
PHASE-EQM ... Phase equilibrium for which property option set specification is to be used: PHASE-EQM $\mathbf { \tau } =$ VLL Vapor-liquid1-liquid2 equilibrium (Default) PHASE-EQM $\mathbf { \tau } =$ VL1 Vapor-liquid1 equilibrium PHASE-EQM=LL Liquid1-liquid2 equilibrium  

PARAM  

Use to enter configuration and operating specifications for the column. You must enter the number of stages and pumparounds. You can also specify algorithm option, efficiency type, and optional parameters.  

NSTAGE. Number of stages, including condenser and reboiler. Must be greater than 1. The convention used in RADFRAC is to number the stages from the top down, starting with the condenser.  

NPA. Number of pumparounds  

NPHASE . Number of phases to be considered in distillation calculations. Specify 2 for vapor-liquid and 3 for vapor-liquid1-liquid2 calculations. If you specify FREE-WATER $\ c =$ YES and NPHASE $= 2$ , free-water calculation is performed for the condenser.  

ALGORITHM ...... Algorithm convergence options:  

ALGORITHM $\mathbf { \lambda } =$ STANDARD Normal algorithm. Recommended for most applications. (Default)   
ALGORITHM $\mathbf { \lambda } =$ SUM-RATES Recommended for petroleum and petrochemical applications involving wide-boiling mixtures. Allowed for ${ \mathsf { N P H A S E } } = 2$ only.   
ALGORITHM $\mathbf { \lambda } =$ NONIDEAL Recommended for highly nonideal columns. You cannot specify ALGORITHM $\ c =$ NONIDEAL and FREE-WATER $\ c =$ YES when ${ \mathsf { N P H A S E } } = 2$ .   
ALGORITHM $\mathbf { \tau } =$ NEWTON Recommended for azeotropic distillation columns  

EFF Type of efficiency specified using keywords: COMP-EFF, STAGEEFF, L1-COMP-EFF, L2-COMP-EFF, L1-STAGE-EFF, or L2-STAGE-EFF  

EFF $\mathbf { \lambda } =$ VAPOR Vaporization efficiency (Default) EFF $\mathbf { \lambda } =$ MURPHREE Murphree efficiency EFF $\mathbf { \tau } =$ TH-MURPHREE Thermal-Murphree efficiency  

INIT-OPTION .. .  Initialization options: INIT-OPTION $\mathbf { \lambda } =$ STANDARD Standard initialization (Default) INIT-OPTION $\mathbf { \lambda } =$ CRUDE Special initialization designed for wide-boiling and multidraw columns INIT-OPTION $\mathbf { \tau } =$ CHEMICAL Special initialization designed for narrow-boiling chemical systems INIT- Special initialization designed for azeotropic OPTION $\mathbf { \tau } =$ AZEOTROPIC distillation columns, such as ethanol dehydration using benzene as the entrainer INIT- Special initialization designed for cryogenic OPTION $\mathbf { \lambda } =$ CRYOGENIC applications, such as air separation   
SOLID-BAL. Solids handling options: SOLID-BAL $\vartriangleleft$ STAGE Handles solids rigorously in stage-by-stage mass and energy balance. All flow specifications must include solids. SOLID-BAL $\ c =$ OVERALL Removes solids from feeds and combines them with liquid bottoms to satisfy overall block mass and energy balance. Flow specifications must not include solids. (Default)   
HYDRAULIC. Flag to specify whether to perform calculations of hydraulic parameters (for example, flow parameter, reduced vapor throughput, tray loadings, and various transport properties): YES or NO. (Default $= N O$ )   
P-UPDATE . Update pressure profile during column sizing and rating calculations: YES or NO. (Default $\ O = N O$ )   
P-FIX . Pressure update option: TOP or BOTTOM. Keeps pressure at column top/bottom constant during pressure updating for column sizing and rating calculations. (Default $\mathbf { \epsilon } =$ TOP)   
DAMPING. Damping factor used to stabilize convergence when excessive oscillation is observed in the convergence behavior: DAMPING $\mathbf { \lambda } =$ NONE No damping (Default) DAMPING $\mathbf { \tau } =$ MILD Mild level of damping DAMPING $\mathbf { \lambda } =$ MEDIUM Medium level of damping  

# DAMPING $\mathbf { \lambda } =$ SEVERE  

Severe level of damping. You may need to increase the maximum number of outside loop iterations (keyword MAXOL) to achieve  

convergence.   
MAXOL . Maximum number of outside loop iterations (Default $= 2 5$ )   
TOLOL . Outside loop convergence tolerance (Default $= 1 { \times } 1 0 ^ { - 4 }$ )   
ABSORBER . .  ABSORBER $\ c =$ YES Recommended for absorber/stripper columns when you specify ALGORITHM $\ c =$ STANDARD. You must specify basis- ${ \mathsf { R D V } } = 1$ , Q1 and QN in the COL-SPECS statement. ABSORBER=NO Use for all other cases (Default)   
CMAXNI0 . Maximum value of local gamma model parameters at infinite dilution. Use when ALGORITHM $\ c =$ NONIDEAL and GAMMAMODEL $\ c =$ MARGULES. (Default $: = 1 . 5$ )   
CMAXNI1 . Maximum value of local gamma model parameters at mole fraction $= 0 . 5$ . Use when ALGORITHM $\ c =$ NONIDEAL and GAMMAMODEL $\ c =$ MARGULES. (Default $: = 1 . 3$ )   
DSMETH . Design specification convergence method, allowed when ALGORITHM $\ c =$ NEWTON or ILMETH $\ c =$ NEWTON: DSMETH $\mathbf { \lambda } =$ SIMULT Simultaneous method (Default when ALGORITHM $\ c =$ NEWTON) DSMETH $\mathbf { \lambda } =$ NESTED Nested-iteration method (Default when ILMETH $\ c =$ NEWTON)   
DTMAX . Maximum allowed change in temperature per inside loop. Use when ABSORBER $\ c =$ YES or ILMETH $\ c =$ NEWTON. Default is selected based on column specifications.   
EFF-FLASH . Flashes product streams when efficiency is specified: YES or NO. (Default $\ B = \mathsf { N O }$ )   
FLASH-MAXIT . ..  Maximum number of feed flash iterations (Default $\mathtt { \Omega } = 5 0$ )   
FLASH-TOL. ..  Feed flash tolerance (Default $= 1 \times 1 0 ^ { - 4 }$ )   
FLASH-VFRAC ...... ...  Vapor fraction of composite feed flash in reactive distillation initialization calculations. Default is calculated based on column specifications.   
FMINFAC. .  Minimum allowed value for stage flow as a fraction of the total feed. (Default $\mathtt { \Lambda } = 1 \times 1 0 ^ { - 5 }$ )   
GAMMA-MODEL .. .  Local gamma model options. Use when ALGORITHM $\ c =$ NONIDEAL: GAMMA-MODEL= Uses constant activity coefficient COMBINED GAMMA-MODEL= Uses Margules activity coefficient model (Default) MARGULES   
HMODEL1 Basis for local enthalpy departure model: HMODEL1 $\mathbf { \lambda } =$ MOLE Molar basis HMODEL1 $\mathbf { \lambda } =$ MASS Mass basis HMODEL1 $\mathbf { \tau } = \mathbf { \tau }$ PSEUDO-MASS Pseudo-mass basis, using internally generated molecular weight (Default is selected based on column specifications)   
HMODEL2. Temperature dependence option for local enthalpy departure model: HMODEL2 $\ l =$ NO-TEMP No temperature dependence  

# HMODEL2 $\mathbf { \lambda } =$ TEMP  

HMODEL2 $\mathbf { \lambda } =$ UPDATE  

Temperature dependence term is updated every iteration  

(Default is selected based on column specifications)  

ILMETH . Inside loop convergence methods. Do not use when ALGORITHM $\ c =$ NEWTON:  

ILMETH $\mathbf { \lambda } =$ BROYDEN  

Broyden quasi-Newton method. (Default for all algorithms except SUM-RATES)  

ILMETH $\mathbf { \tau } =$ WEGSTEIN  

Bounded Wegstein method. (Not allowed when ALGORITHM $\ c =$ SUM-RATES)  

ILMETH $\mathbf { \lambda } =$ NEWTON  

Newton method. (Not allowed when ALGORITHM $\ c =$ SUM-RATES)  

ILMETH $\mathbf { \tau } =$ SCHUBERT  

Schubert quasi-Newton method, with Powell's dogleg stabilization. Allowed when ALGORITHM $\ c =$ SUM-RATES only. (Default when ALGORITHM $\ c =$ SUM-RATES)  

JMETH.  

Jacobian calculation method used only when ALGORITHM $\ c =$ SUMRATES:  

JMETH $\mathbf { \tau } =$ INIT  

JMETH $\vDash$ RMSOL  

Jacobian matrix is computed by numerical perturbation until outside loop RMS error is below RMSOLJ. Then the matrix is updated by the Broyden method.  

KBBMAX. Maximum allowable slope value for local average K-value model (Default $\boldsymbol { \mathbf { \rho } } = - 5 0 0 ^ { \cdot }$ )  

KMODEL Weighting option for local average K-value model:  

KMODEL $\mathbf { \eta } _ { \mathbf { \eta } } = \mathbf { \check { Y } }$ KMODEL $\scriptstyle \mathbf { \alpha } = \mathbf { X }$ KMODEL $\mathbf { \sigma } _ { \mathbf { \overline { { \sigma } } } } = \mathbf { \aleph }$  

Liquid mole fraction  

Vapor fraction/( $1 + \mathsf { K }$ -value)  

(Default is selected based on column specifications)  

L2-CUTOFF. Mole fraction threshold for second phase key component (L2- COMPS). When only one-liquid phase is present, the phase is identified as the second-liquid phase if its mole fraction of L2- COMPS is greater than L2-CUTOFF. Use when NPHASE $^ { = 3 }$ . (Default $_ { = 0 . 5 }$ )  

L2-GAMMA Local activity coefficient model option for the second-liquid phase, when NPHASE $^ { = 3 }$ and ALGORITHM $\ c =$ NONIDEAL:  

L2-GAMMA $\ l =$ CONSTANT Uses constant activity coefficient  

L2-GAMMA $\mathbf { \lambda } =$ MARGULES Uses Margules activity coefficient model (Default)  

LL-MAXIT Maximum number of liquid-liquid phase-split calculations in the inside loop used when ${ \mathsf { N P H A S E } } = 3$ . You can set LL-MAXIT to zero to suppress calculations in the inside loop. (Default $= 2 0$ )  

LL-METH Liquid-liquid phase splitting method:  

LL-METH $\mathbf { \lambda } =$ GIBBS Gibbs free energy minimization method (Default)   
LL-METH $\mathbf { \lambda } =$ EQ-SOLVE Equation solving method   
LL-METH $\mathbf { \lambda } =$ HYBRID Combination of Gibbs free energy minimization and equality of fugacities  

MAX-BROY Maximum number of variables converged by the Broyden method in the outside loop. You should not increase MAX-BROY beyond 500. (Default $= 2 0 0$ )  

MAX-SIZE. Maximum size for work space (in real words.) Use when ALGORITHM $\ c =$ NEWTON or ILMETH $\ c =$ NEWTON. (Default $\scriptstyle : = 2 \times 1 0 ^ { 9 }$ )  

MAXIL  

...  Maximum number of inside loop iterations per outside loop (Default $: = 1 0$ )  

MAXIP Maximum number of initialization calculation passes. Use for ABSORBER $\ c =$ YES and three-phase calculations. Default is selected based on column specifications.  

PROD-FLASH. Flash type for product stream in PROP-SET and recycle stream convergence calculations:  

PROD-FLASH $\mathbf { \mu } = \mathsf { P } \boldsymbol { \mathsf { v } }$ Flash with stream pressure and vapor fraction as specifications PROD-FLASH $\mathbf { \lambda } =$ TP Flash with stream temperature and pressure as specifications (Default is selected based on column specifications)   
QMAXBWIL Maximum value of bounded Wegstein acceleration parameter for inside loop convergence (Default $_ { = 0 . 5 }$ )   
QMAXBWOL Maximum value of bounded Wegstein acceleration parameter for outside loop convergence (Default $_ { = 0 . 5 }$ )   
QMINBWIL Minimum value of bounded Wegstein acceleration parameter for inside loop convergence (Default $_ { = 0 }$ )   
QMINBWOL. Minimum value of bounded Wegstein acceleration parameter for outside loop convergence (Default $_ { = 0 }$ )   
RMSOL0 . Threshold value of outside loop RMS error that must be achieved before design specification iterations are performed (Default $= 0 . 1$ )   
RMSOL1 . Threshold value of outside loop RMS error below which Broyden method is used for selected variables (Default $_ { = 0 . 1 }$ )   
RMSOLJ. Value of the outside loop error below which the inside loop Jacobian matrix is updated by the Broyden method. Use when ALGORITHM $\ c =$ SUM-RATES and JMETH $\ c =$ RMSOL.   
STOR-FACTOR .. Storage multiplier to override the internally calculated workspace requirement when ALGORITHM $\ c =$ NEWTON or ILMETH $\ c =$ NEWTON (Default $= 1 . 5$ )   
TOLILFAC Ratio of inside loop tolerance to outside loop RMS error. Default is calculated based on column specifications.   
TOLILMIN . Minimum value of inside loop tolerance. Default is calculated based on column specifications.   
TOLIL0. Initial value of inside loop tolerance (Default $_ { : = 0 . 0 1 }$ )   
FLASH-TOLIL Feed flash tolerance for the inside loop. Use for reactive distillation only. (Default $= 1 { \times } 1 0 ^ { - 7 }$ )   
PHEQM-FORM... Phase equilibrium formulation for Newton-based methods. PHEQM-FORM $\mathbf { \tau } =$ STANDARDIncludes composition derivatives (Default) PHEQM-FORM $\mid =$ TOTAL- Includes total flow as a variable FLOW PHEQM-FORM $\mathbf { \lambda } =$ IDEAL Ignores composition derivatives  

RADIUS-FRAC . Initial dogleg radius when using dogleg strategy to stabilize Newton's method (Default $_ { = 0 . 1 }$ )  

Use to enter column configuration choices. These include condenser and reboiler configurations and the method for selecting key-components for column targeting analysis. If you specify the condenser configuration, you do not need to specify distillate vapor fraction (RDV) in the COL-SPECS sentence, except for partial condensers with both vapor and liquid distillates.  

CONDENSER... Condenser configuration  

Total condenser with a liquid distillate $\boldsymbol { \left[ R \mathsf { D } \mathsf { V } = 0 \right] }$ ) Partial condenser with vapor distillate only $\mathsf { T R D V } = 1$ )  

CONDENSER $\mathbf { \tau } =$ TOTAL   
CONDENSER $\mathbf { \tau } =$ PARTIAL-V   
CONDENSER=   
PARTIAL-V-L   
CONDENSER $\mathbf { \tau } =$ NONE  

Partial condenser with vapor and liquid distillates $( 0 < \mathsf { R D V } < 1 ) ,$ )  

No condenser. Reflux is provided by an external feed or pumparound return to the top stage (condenser heat duty $= 0$ ; ${ \mathsf { R D V } } = 1$ )  

REBOILER . Reboiler configuration  

REBOILER $\mathbf { \lambda } =$ KETTLE REBOILER $\underline { { \underline { { \mathbf { \Pi } } } } } =$ THERMOSYPHON REBOILER $\mathbf { \lambda } =$ NONE  

Kettle type reboiler (Default) Thermosyphon reboiler  

No reboiler (reboiler heat duty $= 0$ ). Boilup is provided by external feed or pumparound return to the bottom stage.  

KEY-SELECT . Method for selection of light and heavy key components for column targeting analysis. Specify KEY-SELECT if TARGET or HYDANAL report option is chosen in the REPORT sentence.  

KEY-SELECT $\mathbf { \tau } =$ USER  

Use specified light and heavy key components from KEY-COMP sentence.  

KEY-SELECT= SPLIT-FRACTION  

Select the light and heavy key components on the basis of component split-fractions in column product streams. This method is best suited for sharp or near-sharp splits.  

KEY-SELECT $\mathop { = } \mathtt { K }$ -VALUE  

Select the light and heavy key components on the basis of component K-values. This method is best suited for sloppy splits. (Default)  

KEY-SELECT= COMP-PROFILE  

Select the light and heavy key components on the basis of composition profiles. In principle, this method is similar to KEY-SELECT $\mathbf { \bar { \rho } } = \mathbf { \rho }$ K-VALUE. It is best suited for sloppy splits and it is, in general, inferior to KEY-SELECT $\mathbf { \sigma } = \mathbf { \sigma }$ K-VALUE.  

Use to enter inlet material and heat stream locations and feed conventions for material streams.  

sid. Stream ID stage.. Stage number feed-conv.. ABOVE-STAGE  

ON-STAGE DECANTER  

Introduces feed between stages, above designated stage (Default) Introduces feed on designated stage Introduces feed to decanter attached to designated stage  

Use to enter outlet material and heat stream locations, phases, and flows. For material streams, you can enter a phase specification. The phase specification for the distillate must be consistent with the specified value of RDV. When RDV does not equal zero or unity, or when RDV is a manipulated variable, two distillate products are required: one vapor, one liquid. If a liquid product contains two phases, the two phases can be separated into two product streams: one with phase L1 and the other with phase L2 or W (for free-water). The flow rate of a distillate or bottoms stream is not specified in a PRODUCTS sentence, but is specified in a COL-SPECS sentence, or left as a calculated value. The flow rate of a decanter product stream is not specified in a PRODUCTS sentence, but is left as a calculated value.  

sid. Stream ID   
stage... Stage number   
phase. L Total liquid (Default) V Vapor L1 First-liquid L2 Second-liquid W Free-water TL Total drawoff of stage liquid TV Total drawoff of stage vapor  

basis-FLOW. Flow rate for side products on a MOLE, MASS, or STDVOL basis. When phase is TL and TV, specified values are treated as initial estimates only.  

SDRAW:FEED  

Use to specify the sidedraw flow rate as a ratio to the feed flow rate.  

sid. Side stream ID  

ratio Molar ratio of sidedraw flow rate to feed flow rate $S / \Sigma \Sigma F _ { i j }$  

Where:   
$\begin{array} { l } { S = } \\ { F = } \\ { \dot { I } = } \\ { \dot { J } = } \end{array}$ Sidedraw flow rate Feed flow rate Component in the COMPS list Stream in the STREAMS list   
STREAMS List of feed streams forming the basis for the ratio specification. Default is all streams.   
COMPS List of components forming the basis for the ratio specification. Default is all components.  

PSEUDO-STREAM  

Use to identify outlet streams as pseudoproduct streams. A pseudostream can be a stage flow, thermosyphon reboiler flow or pumparound. Enter locations, phases, and flows for stage flows. If no flow rate specification is given, the net flow (excluding any product withdrawn) of the specified phase from the specified stage is stored in the pseudoproduct stream.  

sid. Stream ID   
stage. Stage number required for stage flows and thermosyphon reboiler flows   
PHASE. Phase specification required for stage flows and thermosyphon reboiler flows:  

PHASE=L Total liquid (Default) PHASE=V Vapor PHASE=L1 First-liquid PHASE=L2 Second-liquid  

PHASE=W Free-water   
PHASE $\mathbf { \sigma } = \mathbf { R }$ Thermosyphon reboiler circulation flow   
PHASE=RL Liquid portion of thermosyphon reboiler circulation flow   
PHASE=RV Vapor portion of thermosyphon reboiler circulation flow  

MOLE-FLOW ... Molar flow rate (Default $\ c =$ net flow)  

PA Pumparound ID, required for pumparound  

STATE State condition for pumparound or thermosyphon reboiler circulation flow:  

STATE $\mathbf { \lambda } =$ OUTLET Outlet state condition is stored (Default) STATE $\mathbf { \lambda } =$ INLET Inlet state condition is stored  

P-SPEC  

Use to specify the column pressure profile. There are three methods for entering column pressure profile:  

•  Use P-SPEC to enter the pressure profile.   
•  Use P-SPEC to enter the top and second stage pressure. Enter pressure drop using the DP-COL and DP-STAGE keywords in the COL-SPECS sentence.   
•  Use P-SPEC to enter top stage pressure. Use the PDROP-SEC sentence to enter pressure drop for column sections.  

stage.. Stage number pres Pressure  

COL-SPECS  

Use to enter the distillate vapor fraction (RDV) or top stage temperature (T1), and up to two additional column specifications. Tables 15.1 and 15.2 on pages 15-253 and 15-254 list the valid column specification combinations. When specifying top stage temperature (T1), the temperature should correspond to a vapor liquid region. If ALGORITHM $\ c =$ STANDARD and FREE-WATER $\ c =$ YES, COL-SPECS is used to enter the freewater reflux ratio (RW). You can also enter the column pressure drop, condenser pressure drop, or pressure drop per stage.  

For design mode, any quantities specified in a COL-SPECS statement (except DP-STAGE, DP-COL, and DP-COND) can be treated as manipulated variables, in which case the values given in the COL-SPECS statement are initial guesses. Inlet heat streams to the top or bottom stage can be used in place of Q1 or QN. Substitute MOLE, MASS, or STDVOL for the word basis in the following specifications.  

basis-RDV . Distillate vapor fraction (RDV $\ c =$ DV/D) Where: $\mathsf { D V } =$ Distillate vapor flow rate $\begin{array} { r l } { \mathsf { D } } & { { } = } \end{array}$ Total distillate flow rate, excluding any free-water when NPHASE $= 2$ and FREE-WATER $\ c =$ YES You cannot enter basis-RDV if you specify T1. You do not need to specify basis-RDV when CONDENSER $\ c =$ TOTAL, PARTIAL-V or NONE in the COL-CONFIG sentence.   
T1 Condenser temperature, allowed only for partial condenser with both liquid and vapor distillate products. You cannot enter T1 if basis-RDV is specified.   
basis-D Total distillate flow rate, excluding any free-water when NPHASE $= 2$ and FREE-WATER $\ c =$ YES   
basis-B... Bottoms flow rate   
D:F. Molar ratio of distillate flow rate to feed flow rate $( \mathsf { D } / \Sigma \Sigma F _ { i j } )$  

B:F Molar ratio of bottoms flow rate to feed flow rate $( \mathsf { B } / \Sigma \Sigma F _ { i j } )$  

$\begin{array} { r l } { F } & { { } = } \end{array}$ Feed flow rate $i$ $\mathbf { \tau } = \mathbf { \tau }$ Component in the COMPS list of the DB:F-PARAMS sentence $\begin{array} { r l } { j } & { { } = } \end{array}$ Stream in the STREAMS list of the DB:F-PARAMS sentence basis-D:F Ratio of distillate flow rate to feed flow rate. Use when basis is MASS or STDVOL.  

basis-B:F. Ratio of bottoms flow rate to feed flow rate. Use when basis is MASS or STDVOL.  

basis-L1 Reflux flow rate (or the liquid flow rate from the top stage), excluding any free-water when NPHASE $= 2$ and FREE-WATER $\ c =$ YES basis-VN . Boilup flow rate (or the vapor flow rate from the bottom stage)  

basis-RR Reflux ratio (L1/D), excluding any free-water when NPHASE $= 2$ and FREE-WATER $\ c =$ YES  

basis-BR . Boilup ratio (VN/B)  

Q1 Condenser (or top stage) heat duty  

QN Reboiler (or bottom stage) heat duty  

RW. Free-water reflux ratio on a mole basis; RW $\ c =$ LW/DW Where: LW $\mathbf { \tau } = \mathbf { \tau }$ Free-water reflux rate DW $\mathbf { \tau } = \mathbf { \tau }$ Free-water distillate rate (Default $_ { \cdot = 0 }$ )  

DP-STAGE . Pressure drop per stage  

DP-COL Pressure drop for column  

DP-COND . Pressure drop across condenser  

HTLOSS. Heat loss for column. A positive value of heat loss corresponds to heat flow from the tray to the surroundings. The specified value is divided equally among all stages in the column. For rate-based calculations, the heat loss is applied to the liquid phase. You cannot enter HTLOSS if you specify a HTLOSS-SEC or HTLOSS sentence.  

This keyword is still supported, but it is recommended that the HTLOSS-LIQ keyword in the HTLOSS sentence be used instead of this keyword.  

DB:F-PARAMS  

Use to define the basis for the D:F and B:F specifications in the COL-SPECS sentence.  

STREAMS List of feed streams forming the basis for the D:F or B:F specifications (Default $\mathbf { \sigma } =$ all feed streams to the block)   
COMPS . List of components forming the basis for the D:F or B:F specifications (Default $\mathbf { \sigma } =$ all components)  

SC-REFLUX  

Use to specify either the degrees subcooling of the reflux, or the reflux temperature. If you do not enter a SC-REFLUX statement, the reflux is assumed to be a saturated liquid. Subcooled reflux is not allowed when $N P H A S E = 3$ . When FREE-WATER $\ c =$ YES, subcooled reflux is allowed only if you specify ALGORITHM $\ c =$ SUM-RATES and basis- $\scriptstyle \mathtt { R D V } = 0$ .  

DEGSUB Degrees subcooling   
TEMP. Reflux temperature   
OPTION. OPTION $\mathbf { \sigma } = \mathbf { 0 }$ Both reflux and liquid distillate are subcooled (Default) OPTION=1 Only reflux is subcooled  

Use to enter pressure and up to two additional specifications for the thermosyphon reboiler. The thermosyphon reboiler model has five related variables: pressure, circulation rate, temperature, temperature change, and vapor fraction. Pressure may be specified or defaulted to the bottom stage pressure. In addition, one of the following specification options must be chosen:  

1. Temperature   
2. Temperature change   
3. Vapor fraction   
4. Circulation flow   
5. Circulation flow and temperature   
6. Circulation flow and temperature change   
7. Circulation flow and vapor fraction  

Options 5 through 7 are not allowed when NPHASE $^ { = 3 }$ . If options 1 through 4 are chosen, the duty QN is either specified or left as a calculated value. If option 5, 6 or 7 is specified, QN must be specified in the COL-SPECS sentence, but is treated as an initial guess.  

If no THERMOSYPHON statement is given, the reboiler is assumed to be of the kettle type.  

PRES . Reboiler pressure (Default $\ c =$ bottom stage pressure) TEMP.. Temperature of reboiler outlet   
DELT . Temperature change across reboiler   
VFRAC. Vapor fraction of reboiler outlet   
basis-FLOW.. Circulation flow on a MOLE, MASS, or STDVOL basis RETURN-CONV . Convention for returning reboiler outlet to column:  

RETURN-CONV= ABOVE-STAGE RETURN-CONV= ON-STAGE  

Introduces reboiler outlet between Nstage and Nstage–1, with vapor portion going to Nstage–1 and liquid going to Nstage Introduces reboiler outlet to Nstage (Default)  

Use to enter pumparound connectivity and heater/cooler specifications. Pumparounds can be total or partial drawoffs of the stage flow. You must specify the source, and return stage locations for each pumparound. By default RADFRAC assumes the pumparound does not experience any phase change at the heater/cooler outlet. However, you can specify ${ \mathsf { N P H A S E } } = 2$ or 3, and let RADFRAC determine the return phase condition from the heater/cooler specifications.  

paid Pumparound ID   
stage1 Source stage number   
stage2. Destination stage number   
DRAW-PHASE.. Phase of pumparound stream at the source:  

L Liquid (Default) L1 First-liquid L2 Second-liquid V Vapor  

TYPE Pumparound drawoff type:  

TYPE $\mathbf { \lambda } =$ PARTIAL  

Partial drawoff. You must specify two of the following variables: basis-FLOW, DUTY, TEMP (or DELT), or VFRAC. (Default)  

# TYPE $\mathbf { \lambda } =$ TOTAL  

Total drawoff. You must specify one of the following variables: TEMP, DELT, VFRAC or DUTY.  

basis-FLOW.... Pumparound flow rate in MOLE, MASS, or STDVOL basis  

TEMP. Temperature of pumparound stream at associated heater/cooler outlet   
DELT Change in temperature of pumparound stream across associated heater/cooler outlet   
DUTY. Heat duty for associated heater/cooler. Enter a negative value for cooling, a positive value for heating, and 0 for no heating or cooling.   
VFRAC. Vapor fraction of pumparound stream at associated heater/cooler outlet. VFRAC is not allowed when NPHASE ${ \bf \varepsilon } = { \bf 1 }$ .   
PRES . Pressure of pumparound stream at associated heater/cooler outlet (Default $\ c =$ pressure of draw stage)   
NPHASE Number of phases at the associated heater/cooler outlet (Default $\scriptstyle = 1$ )   
RETURN-PHASE.. Phase of pumparound stream at associated heater/cooler outlet when NPHASE ${ \bf \varepsilon } = { \bf 1 }$ : L or V   
FEED-CONV . Feed convention for returning pumparound to column: FEED-CONV= Introduces pumparound above designated stage ABOVE-STAGE FEED-CONV $\mathbf { \bar { \Pi } } = \mathbf { \bar { \Pi } }$ ON-STAGE Introduces pumparound to designated stage (Default) FEED-CONV $\mathbf { \bar { \Pi } } = \mathbf { \bar { \Pi } }$ DECANTER Introduces pumparound to decanter attached to designated stage  

QSTREAM-IN..... Stream ID of inlet heat stream for the pumparound  

QSTREAM-OUT ............  Stream ID of outlet heat stream for the pumparound  

HEATERS  

Use to enter the heater stage locations and duties. Inlet heat streams can be used in place of HEATERS specifications.  

stage... Stage number duty . Heat duty  

COOLANT  

Use to define interstage heaters/coolers with UA and coolant specifications. You must specify the UA and the coolant component, flow rate and inlet temperature. You can specify the heat capacity directly, or RADFRAC calculates it from a coolant property option set. If the heat capacity is to be calculated, you must enter the pressure and phase of the coolant. UA calculations assume that no phase change occurs on the coolant side.  

stage. Stage number   
cid.. Component ID   
opsetname. Property option set name (Default $\ c =$ property option set for corresponding stage)   
basis-FLOW. Coolant flow rate in MOLE, MASS or STDVOL basis   
UA.. Product of the average heat-transfer coefficient and heat-transfer area   
TEMP. Coolant inlet temperature   
PRES . Coolant pressure   
PHASE.. Phase of coolant, L or V  

basis-CP. Average heat capacity for coolant in MOLE, MASS, or STDVOL basis. The basis should be the same as the basis for the coolant flow rate.  

HTLOSS-SEC  

Heat loss for a section of the column, by phase. Heat loss may only be specified by one of the HTLOSS-SEC sentence, the HTLOSS sentence, or the HTLOSS keyword in the COLSPECS sentence.  

secno Section number   
stage1.. Stage number for initial stage of column segment   
stage2.. Stage number for final stage of column segment   
heat loss .. .  Heat loss for the column section. A positive value of heat loss corresponds to heat flow from the tray to the surroundings. The specified value is divided equally among stages in the column section.   
HTLOSS-SEC.. Heat loss for the liquid phase in the section. Enter a positive value for the heat loss, which is split uniformly over the stages in the section.   
HTLOSS-VAP ... Heat loss for the vapor phase in the section. Enter a positive value for the heat loss, which is split uniformly over the stages in the section. In equilibrium calculations, the heat losses specified for HTLOSSSEC and HTLOSS-VAP are combined and applied to the stage as a whole.  

HTLOSS  

Heat loss for the entire column, by phase. Heat loss may only be specified by one of the HTLOSS-SEC sentence, the HTLOSS sentence, or the HTLOSS keyword in the COL-SPECS sentence.  

HTLOSS-LIQ....... Heat loss for the liquid phase. Enter a positive value for the heat loss, which is split uniformly over the stages in the column.   
HTLOSS-VAP ........ ....  Heat loss for the vapor phase. Enter a positive value for the heat loss, which is split uniformly over the stages in the column. In equilibrium calculations, the heat losses specified for HTLOSSLIQ and HTLOSS-VAP are combined and applied to the stage as a whole.  

COMP-EFF  

Use to enter component efficiencies. The type of efficiency is specified by EFF in the PARAM statement. When NPHASE $^ { = 3 }$ , COMP-EFF applies to both liquid phases. You cannot use COMP-EFF if you specify STAGE-EFF, STAGE-EFF-SEC, L1-COMP-EFF, L2-COMP-EFF, L1- STAGE-EFF, or L2-STAGE-EFF.  

stage. Stage number cid. Component ID eff . Efficiency (Default $\scriptstyle = 1$ )  

STAGE-EFF  

Use to enter stage efficiencies. These efficiencies are applied to each component on the stage. The type of efficiency is specified by EFF in the PARAM statement. When NPHASE $^ { = 3 }$ , STAGE-EFF applies to both liquid phases. You cannot use STAGE-EFF if you specify STAGEEFF-SEC, COMP-EFF, L1-COMP-EFF, L2-COMP-EFF, L1-STAGE-EFF, or L2-STAGE-EFF.  

stag Stage number eff Efficiency (Default $\scriptstyle = 1$ )  

Use to enter stage efficiencies for a column section. These efficiencies are applied to each component on each stage in the column section. The type of efficiency is specified by EFF in the PARAM sentence. When NPHASE $^ { = 3 }$ , STEFF-SEC applies to both liquid phases. You cannot use STEFF-SEC if you specify COMP-EFF, STAGE-EFF, L1-COMP-EFF, L2-COMP-EFF, L1-STAGE-EFF, or L2-STAGE-EFF.  

secno Section number   
stage1 Stage number for initial stage of column segment stage2 Stage number for final stage of column segment eff . Efficiency (Default $\scriptstyle = 1$ )  

DECANTERS  

Use to enter location and other specifications for decanters when $N P H A S E = 3$ . For the top stage decanter you must specify the fraction of at least one of the two phases returned. For all other decanters, you must specify the fraction of each of the two liquid phases returned. You can specify temperature or degrees of subcooling.  

stage.. Stage number   
L1-SPEC . Fraction of the first-liquid phase returned   
L2-SPEC . Fraction of the second-liquid phase returned   
TEMP. Temperature of decanter (Default $\mathbf { \sigma } =$ stage temperature)   
DEGSUB . Degrees subcooling (Default ${ } = 0$ )   
DECANT-SOLID .... .....  Solids decant option:  

DECANT-SOLID $\mathbf { \tau } =$ PARTIAL Decant solids partially using L2-SPEC as the solid return fraction (Default)   
DECANT-SOLID $\mid =$ TOTAL Decant solids completely  

NQ-CURVE  

Use to enter NQ-curve specifications. Enter one NQ-CURVE sentence for each NQ-CURVE specification.  

CURVE-NO.. NQ curve number  

NSTAGE-MIN... Lower limit on number of stages  

NSTAGE-MAX .... Upper limit on number of stages  

NSTAGE-STEP Step size for number of stages (Default $= 2 \cdot$ )  

FEED ID of the sampled feed stream. The total number of stages and the location of this feed stream will be optimized.  

RR-MIN. Minimum reflux ratio (Default $\mathbf { \tau } = \mathbf { \tau }$ 1E-6)  

OBJECT-FUNC. Objective function for optimizing total number of stages and feed stream location:  

OBJECT-FUNC= Total heat load of condenser and reboiler   
QREB-QCOND (Default)   
OBJECT-FUNC $\mathbf { \lambda } =$ QCOND Condenser heat load (absolute value)   
OBJECT-FUNC $\mathbf { \lambda } =$ QREB Reboiler heat load   
OBJECT-FUNC $\mathbf { \lambda } =$ MOLE-RR Molar reflux ratio   
OBJECT-FUNC $\mathbf { \lambda } =$ MASS-RR Mass reflux ratio   
OBJECT-FUNC $\mathbf { \tau } =$ Standard liquid volume reflux ratio   
STDVOL-RR  

LMT-FROM-TOP ...........  Limit on feed stage location from the top (Default $\mathbf { \Psi } = \mathbf { 1 } \mathbf { \Psi }$ ) LMT-FROM-BOT.... .....  Limit on feed stage location from the bottom (Default $\mathbf { \Psi } = \mathbf { 1 } \mathbf { \Psi }$ ) QR-QC-COST ..... Reboiler / condenser cost ratio. Used when OBJECT-FUNC $\mathbf { \tau } = \mathbf { \tau }$ QREB-QCOND.  

NQCUR-FOPT  

Use to enter options to vary locations of material feeds other than the sampled one in the corresponding NQ-CURVE sentence. These material feeds are also referred to as "remaining feed streams." REL-FEED is assumed for unspecified streams.  

CURVE-NO.... NQ curve number  

SID Feed stream ID. Only remaining feed streams can be specified.  

REMAIN-OPT.. Method for varying remaining feed stream location:  

REMAIN-OPT $\mathbf { \lambda } =$ REL-FEED Maintain proportional location between the sampled feed and end of column (Default)   
REMAIN-OPT $\mathbf { \lambda } =$ RELATIVE Maintain proportional location within the entire column   
REMAIN-OPT $\mathbf { \lambda } =$ FROM-TOP Maintain absolute number of stages from top   
REMAIN-OPT $\mathbf { \lambda } =$ Maintain absolute number of stages from bottom   
FROM-BOTTOM   
REMAIN-OPT= Maintain absolute number of stages above or   
FROM-FEED below sampled feed  

NQCUR-SOPT  

Use to enter options to vary locations of side-draws. REL-FEED is assumed for unspecified side-draws.  

CURVE-NO. NQ curve number SID . Side-draw product stream ID SDRAW-OPT. Method for varying side-draw location:  

SDRAW-OPT $\mathbf { \lambda } =$ REL-FEED Maintain proportional location between the sampled feed and end of column (Default)   
SDRAW-OPT $\mathbf { \lambda } =$ RELATIVE Maintain proportional location within the entire column   
SDRAW-OPT $\mathbf { \lambda } =$ FROM-TOP Maintain absolute number of stages from top   
SDRAW-OPT $\mathbf { \tau } =$ Maintain absolute number of stages from bottom   
FROM-BOTTOM   
SDRAW-OPT= Maintain absolute number of stages above or   
FROM-FEED below sampled feed  

NQCUR-PAOPT  

Use to enter options to vary locations of pumparounds. REL-FEED is assumed for unspecified pumparounds.  

CURVE-NO.. NQ curve number   
IC-STREAM Pumparound ID   
PA-OPT Method for varying pumparound location:   
PA-OPT $\mathbf { \bar { \rho } } = \mathbf { \rho }$ REL-FEED Maintain proportional location between the sampled feed and end of column (Default)   
PA-OPT $\mathbf { \bar { \Pi } } = \mathbf { \Phi }$ RELATIVE Maintain proportional location within the entire column   
PA-OPT $\mathbf { \bar { \rho } } = \mathbf { \rho }$ FROM-TOP Maintain absolute number of stages from top   
PA-OPT $\mathbf { \bar { \rho } } = \mathbf { \rho }$ FROM-BOTTOM Maintain absolute number of stages from bottom   
PA-OPT $\mathbf { \bar { \rho } } = \mathbf { \rho }$ FROM-FEED Maintain absolute number of stages above or below sampled feed  

NQCUR-DECTOP  

Use to enter options to vary locations of decanters. REL-FEED is assumed for unspecified decanters.  

CURVE-NO. NQ curve number STAGE .. Decanter stage number DECT-OPT Method for varying decanter location:  

DECT-OPT $\mathbf { \lambda } =$ REL-FEED Maintain proportional location between the sampled feed and end of column (Default)  

DECT-OPT $\mathbf { \lambda } =$ RELATIVE Maintain proportional location within the entire column   
DECT-OPT $\mathbf { \lambda } =$ FROM-TOP Maintain absolute number of stages from top   
DECT-OPT= Maintain absolute number of stages from bottom   
FROM-BOTTOM   
DECT-OPT= Maintain absolute number of stages above or   
FROM-FEED below sampled feed  

L2-COMPS  

Use to enter a list of key components that are used to identify the second-liquid phase when NPHASE $^ { = 3 }$ and FREE-WATER $\mathtt { \Omega } = \mathsf { N O }$ . The liquid phase with the larger mole fraction of the key components is designated as the second-liquid phase. If NPHASE $^ { = 3 }$ and FREEWATER $\ c =$ YES, the free-water phase is the second-liquid phase.  

cid-list Key component ID list  

L2-STAGES  

Use to indicate a segment of stages to be tested for the presence of two liquid phases when $N P H A S E = 3$ .  

stage1.. Stage number for initial stage of column segment stage2 Stage number for final stage of column segment. If the segment to be tested consists only of stage1, enter an asterisk for stage2.  

L1-RETURN  

Use to enter optional decanter return specifications for the first-liquid phase. You can split the first-liquid phase into any number of streams, each of which goes to a different stage. If you do not specify L1-RETURN, the first-liquid phase is returned to the stage immediately below the decanter stage.  

stage1 Stage number of decanter   
stage2 Stage number of stage to which the first-liquid phase of decanter is returned   
l1-rfrac Fraction of decanter liquid1 returned to the return stage  

L2-RETURN  

Use to enter optional decanter return specifications for the second-liquid phase. You can split the second-liquid phase into any number of streams, each of which goes to a different stage. If you do not specify L2-RETURN, the second-liquid phase is returned to the stage immediately below the decanter stage.  

stage1. Stage number of decanter   
stage2.. Stage number of stage to which the second-liquid phase of decanter is returned   
l2-rfrac .. Fraction of decanter liquid2 returned to the return stage  

L1-COMP-EFF  

Use to enter component Murphree or vaporization efficiencies for the first-liquid phase when NPHASE $^ { = 3 }$ . The type of efficiency is specified by EFF in the PARAM statement. You cannot use L1-COMP-EFF if you specified L1-STAGE-EFF, L2-STAGE-EFF, STAGE-EFF, STAGE-EFF-SEC, or COMP-EFF.  

stage. Stage number cid. Component ID eff . Efficiency (Default $\scriptstyle = 1$ )  

L2-COMP-EFF  

Use to enter component Murphree or vaporization efficiencies for the second-liquid phase when NPHASE $^ { = 3 }$ . The efficiency type is specified by EFF in the PARAM statement. You cannot use L2-COMP-EFF if you specified L1-STAGE-EFF, L2-STAGE-EFF, STAGE-EFF, STAGE-EFF-SEC, or COMP-EFF.  

stage.. Stage number cid. Component ID eff . Efficiency (Default $\scriptstyle = 1$ )  

L1-STAGE-EFF  

Use to enter component Murphree or vaporization efficiencies for the first-liquid phase when NPHASE $^ { = 3 }$ . These efficiencies are applied to each component on the stage. The efficiency type is specified by EFF in the PARAM statement. You cannot use L1-STAGE-EFF if you specified L1-COMP-EFF, L2-COMP-EFF, STAGE-EFF or COMP-EFF.  

stage... Stage number eff Efficiency (Default $\scriptstyle = 1$ )  

L2-STAGE-EFF  

Use to enter component Murphree or vaporization efficiencies for the second-liquid phase when NPHASE $^ { = 3 }$ . These efficiencies are applied to each component on the stage. The efficiency type is specified by EFF in the PARAM statement. You cannot use L2-STAGE-EFF if you specified L1-COMP-EFF, L2-COMP-EFF, STAGE-EFF or COMP-EFF.  

stage.... Stage number eff Efficiency (Default $\scriptstyle = 1$ )  

KLL-STAGES  

Use to specify column segment for which the built-in KLL expression is used. You must also specify basis-KLL and NPHASE $^ { = 3 }$ .  

kll-no . KLL dataset number stage1. Initial stage of a column segment stage2. Final stage of a column segment  

basis-KLL  

Use to enter coefficients in MOLE, MASS, or STDVOL basis for the built-in KLL expression.   
You must also specify ${ \mathsf { N P H A S E } } = 3$ .  

KLL-NO KLL dataset number  

KLL-CID . Component ID  

KLL-A, KLL-B.. Coefficients for KLL expression. Which is defined as: KLL-C, KLL-D $\mathsf { l n } ( K L L ) = ( K L L - A ) + ( K L L - B ) / T + ( K L L - C ) \times \mathsf { l n } ~ T + ( K L L - D ) \times T$  

Where: $\ K L L =$ Liquid-liquid equilibrium K-value $\begin{array} { r l } { \tau } & { { } = } \end{array}$ Temperature in Kelvin  

You must enter a value for KLL-A. The default values for the other coefficients are zero.  

REAC-STAGES  

Use to specify the set of chemical reactions occurring in a segment of stages.  

stage1 Stage number for initial stage of column segment   
stage2.. Stage number for final stage of column segment. If the segment consists only of stage1, enter an asterisk for stage2.   
reactid . REACTIONS or CHEMISTRY paragraph ID. RADFRAC accepts only REACTIONS types REAC-DIST and USER. (See Chapters 5 and 6.)  

HOLD-UP  

Use to specify liquid and/or vapor holdup for segment(s) of columns in which ratecontrolled reactions occur. You cannot use HOLD-UP if you specified RES-TIME. Substitute MOLE, MASS, or VOL for the word basis in the following specifications.  

stage1.. Stage number for initial stage of column segment   
stage2. Stage number for final stage of column segment. If the segment consists only of stage1, enter an asterisk for stage2.   
basis-LHLDP .. .  Liquid holdup   
basis-VHLDP .. ..  Vapor holdup  

RES-TIME  

Use to specify residence time in the liquid and/or vapor phase for segment(s) of columns in which rate-controlled reactions occur. You cannot use RES-TIME if you specified HOLD-UP.  

stage1.. Stage number for initial stage of column segment stage2 Stage number for final stage of column segment. If the segment consists only of stage1, enter an asterisk for stage2.  

LTIME Residence time in liquid phase  

VTIME Residence time in vapor phase  

CONVERSION  

Use to override fractional conversion for reactions (based on key components) specified in the REACTIONS paragraph. (See Chapter 6.)  

stage.. Stage number reacno Reaction number in REACTIONS paragraph frac . Fractional conversion based on key component  

T-EST  

Use to enter an initial estimate of the column temperature profile. If you do not enter a TEST sentence, an initial profile is generated by RADFRAC.  

stage. Stage number temp ..... Temperature  

X-EST, Y-EST  

Use to enter an initial estimate of the column composition profiles. X-EST and Y-EST are always used together.  

stage... Stage number   
cid. Component ID   
x Liquid mole fraction for total liquid phase   
y Vapor mole fraction  

L-EST, V-EST, VL-EST  

Use to enter initial flow or flow ratio estimates for the liquid phase (L-EST), vapor phase (V-EST), and the ratio of vapor to liquid (VL-EST) when ABSORBER $\ c =$ YES or ALGORITHM $\ c =$ SUM-RATES. You cannot use L-EST (or V-EST), and VL-EST together. The flows or flow ratios entered refer to the net flow on a stage, excluding any side product withdrawn.  

stage... Stage number mole-flow . Molar flow rate (for L-EST or V-EST)  

mole-ratio..... Ratio of vapor mole flow to liquid mole flow (for VL-EST)  

REPORT  

Use to override the default report options. You can use the standard REPORT options for use within a block (see Chapter 11) for RADFRAC.  

reportopt . Standard block report options (see Chapter 11), in addition to the following:  

Suppress the hydraulic parameters reported for this block  

STDVPROF  

TARGET  

Include column targeting thermal analysis results  

HYDANAL Include column targeting hydraulic analysis results   
EXTHYD Include extended hydraulic parameter report. Use only when NOHYDRAULIC report option is not selected or when HYDRAULIC $\ c =$ YES in the PARAM sentence.  

The additional report options below apply only to RateSep ratebased distillation calculations:  

<html><body><table><tr><td>INT-PROF</td><td>Include interfacial fractions,temperatures and K value.</td></tr><tr><td>INT-AREA</td><td>Includeinterfacialarea.</td></tr><tr><td>BULKRXN</td><td>Include bulk reaction rates.</td></tr><tr><td>DIFF-COE</td><td>Include binary diffusion coefficients.</td></tr><tr><td>MT-RATE</td><td>Include mass transfer rates.</td></tr><tr><td>MT-COEFF</td><td>Include binary mass transfer coefficients.</td></tr><tr><td>HT-RATE</td><td>Include heat transferrates.</td></tr><tr><td>HT-COEFF</td><td>Include heattransfercoefficients.</td></tr><tr><td>FILMRXN</td><td>Include reaction rates within films.</td></tr><tr><td>S-DIMLES</td><td>Include scalar dimensionless numbers.</td></tr><tr><td>V-DIMLES</td><td>Include Schmidt and Sherwood numbers.</td></tr></table></body></html>  

Use to specify additional stage and design-spec variables to include or exclude in EO calculations. All options can be set to YES or NO. (Default $\ c =$ YES; these variables are included in EO calculations unless specified otherwise.)  

EFF. Whether to include additional efficiency variable D. Whether to include additional distillate variable B . Whether to include additional bottom flow variable RR.. Whether to include additional reflux ratio variable L1 .. Whether to include additional reflux rate variable BR. Whether to include additional boilup ratio variable VN... Whether to include additional boilup rate variable Q1. Whether to include additional condenser duty variable QN . Whether to include additional reboiler duty variable L Whether to include additional liquid flow variable V . Whether to include additional vapor flow variable Q-STAGE .. Whether to include additional stage duty variable WL Whether to include additional liquid side-draw variable WV ... Whether to include additional vapor side-draw variable SPEC ... Whether to include additional design specification variables SC-REFLUX. Whether to include additional reflux sub-cooling variable Use to specify additional features to include or exclude in EO calculations. All options can be set to YES or NO. (Default $\mathbf { \sigma } = \mathbf { \sigma }$ YES) PRES . Whether to include pressure and pressure drops for all stages FEEDDP. Whether to include feed-to-stage pressure drop FEEDOPEN..... Option for open feed flash. Do not specify when NPHASE $^ { = 3 }$ .  

SPC-OPTION2  

CS-ALLBASIS Whether to include flow rate and ratio specifications in all flow basis (MOLE, MASS, and STDVOL)   
SPLIT-ALL Whether to include second liquid or free-water variables for all stages that are tested for two liquid phases (Default $\cdot = N 0 \cdot$ ). Do not specify when NPHASE $= 2$ .  

KEY-COMP  

Use to specify light and heavy key components for column targeting analysis. Use only when TARGET and/or HYDANAL report option is selected and KEY-SELECT $\mathbf { \bar { \rho } } = \mathbf { \rho }$ USER in the COL-CONFIG sentence.  

secno . Section number for key component specification stage1.. Stage number for the initial stage of the section stage2. Stage number for the final stage of the section  

LIGHT-KEY. List of light key components  

HEAVY-KEY .. List of heavy key components  

KEY-TOL  

Use to specify tolerances and other parameters for light and heavy key component   
selection methods other than KEY-SELECT $\mathbf { \bar { \rho } } = \mathbf { \rho }$ USER and for exergy loss calculations. Use only   
when TARGET and/or HYDANAL report option is selected.   
KVAL-TOL.. Tolerance on component K-values. Specify when KEY-SELECT $\mathbf { \bar { \rho } } = \mathbf { \rho }$ K-VALUE or SPLIT-FRACTION. (Default $= 1 \times 1 0 ^ { - 5 }$ )   
COMP-TOL. Tolerance on component mole-fractions. Specify when KEYSELECT $\mathbf { \bar { \rho } } = \mathbf { \rho }$ K-VALUE, SPLIT-FRACTION, or COMP-PROFILE. (Default $\mathtt { \Gamma } = 1 \mathtt { x } 1 0 ^ { - 6 } .$ )   
SPF-LIMIT Minimum value of component split-fractions, in the top and the bottom products of a column section, necessary for key component selection. Specify when KEY-SELECT $\mathbf { \bar { \rho } } = \mathbf { \rho }$ SPLIT-FRACTION. (Default $_ { = 0 . 9 }$ )   
STG-SPAN . Stage span for computing composition profiles. Specify when KEY-SELECT $\mathbf { \bar { \rho } } = \mathbf { \rho }$ COMP-PROFILE. (Default $^ { = 2 }$ )   
EXCLD-KEY.. List of components to be excluded from key component selection. Specify when KEY-SELECT $\ O = \mathsf { K }$ -VALUE, SPLIT-FRACTION, or COMP-PROFILE.   
EXG-TREF.. Reference temperature for exergy loss calculations (Default $\ c =$ 298.15 K)   
Use to specify advanced convergence parameters.   
MAN-3P-PASS . Number of initialization passes in which two liquid phases are forced to be present. Should not exceed 8. (Default $= 0$ )   
STABLE-ITER Initial number of iterations over which the steps are damped using a stabilization method. Use when ALGORITHM $\ c =$ NEWTON or when ILMETH $\ c =$ NEWTON in the PARAM sentence.   
STABLE-METH . Stabilization method. Use when ALGORITHM $\ c =$ NEWTON or when ILMETH $\ c =$ NEWTON in the PARAM sentence. STABLE-METH $\mathbf { \lambda } =$ DOGLEG Powell's dogleg strategy (Default) STABLE-METH= One-dimensional line search LINE-SEARCH   
PROP-DERIV ... Property derivative calculation method for ALGORITHM $\ c =$ NEWTON. PROP-DERIV $\mathbf { \bar { \Pi } } = \mathbf { \bar { \Pi } }$ Analytical (Default) ANALYTICAL PROP-DERIV $\mathbf { \bar { \Pi } } = \mathbf { \bar { \Pi } }$ NUMERICAL Numerical  

CONVERGENCE  

NQ-PROF-MAX Maximum number of NQ profiles stored for analysis (Default $\mathbf { \sigma } =$ original number of stages \* number of NQ curves)  

NQ-FOPT-METH ...........  Algorithm for feed tray optimization. NQ-FOPT-METH $\mathbf { \lambda } =$ Feed tray optimization by case study CASE-STUDY NQ-FOPT-METH $\mathbf { \lambda } =$ QP-SRCH Feed tray optimization by one-dimensional quadratic search NQ-FOPT-METH $\mathbf { \lambda } =$ HYBRID Feed tray optimization by one-dimensional quadratic search for first case and by case study for subsequent cases (Default)   
NQ-TOLOL. Outside loop tolerance used during NQ curve generation. (Default $\scriptstyle = 1 0 ^ { - 5 }$ )   
NQ-TOLOBJ .. Objective function tolerance for terminating NQ curve generation. Generation terminates when the variation of objective function when increasing the number of stages by 1 falls below this tolerance. (Default $_ { = 0 . 0 1 }$ )  

TRAY-REPORT  

Use to specify the format of the report and additional tray properties to be reported (in addition to the flows, temperatures, pressures, enthalpies, duties, mole fractions, and Kvalues printed in the standard report).  

TRAY-OPTION .............  Specifies stages included in the report:  

TRAY-OPTION $\mathbf { \lambda } =$ BRIEF Reports the stages that have feeds, products, heaters, and maximum and minimum flows, and the stages immediately above and below those stages (Default) TRAY-OPTION= Reports the stages specified in the INCL-TRAYS INCL-TRAYS statement TRAY-OPTION $\mathbf { \lambda } =$ Reports all stages ALL-TRAYS FORMAT .. FORMAT $\mathbf { \sigma } =$ PROFILE Prints tabular column profiles (Default) FORMAT $\mathbf { \tau } =$ STAGE Prints individual stage reports FORMAT $\mathbf { \lambda } =$ COMBINED Prints both tabular column profiles and individual stage reports ORDER . Tray numbering order. Use for report only. ORDER $\mathbf { \lambda } =$ TOP-DOWN Numbers stages from top down (Default) ORDER $\mathbf { \lambda } _ { . = }$ BOTTOM-UP Numbers stages from bottom up PROPERTIES List of property set Ids WIDE . Report width option WIDE $\mathbf { \tau } =$ YES Produce wide (132 columns) reports (Default) WIDE=NO Produce standard (80 columns) reports Use to specify the flow profile option for the block report. FLOW-OPTION .... ..  FLOW-OPTION $\mathbf { \sigma } = \mathbf { 0 }$ Report flows from a stage including side draws, side products, and pumparounds (Default) FLOW-OPTION $\mathbf { \lambda = 1 }$ Report flows from a stage excluding side draws, side products, and pumparounds Use to designate stages to be included in the report when TRAY-OPTION $\ c =$ INCL-TRAYS in the TRAY-REPORT sentence.  

# TRAY-REPOPT  

INCL-TRAYS  

stage1. Stage number of initial stage of column segment to be reported stage2. Stage number of final stage of column segment to be reported (Default $\ c =$ stage1)  

COND-HCURVE  

Use to generate cooling curve tables for the condenser. If you entered efficiency or reaction specification for the condenser using COMP-EFF, STAGE-EFF, L1-COMP-EFF, L2- COMP-EFF, L1-STAGE-EFF, L2-STAGE-EFF, or REAC-STAGES, condenser cooling curves will not be consistent with column results. See Chapter 11 for a description of input keywords.  

REB-HCURVE  

Use to generate heating curve tables for the reboiler. If you entered efficiency or reaction specification for the reboiler using COMP-EFF, STAGE-EFF, L1-COMP-EFF, L2-COMP-EFF, L1-STAGE-EFF, L2-STAGE-EFF, or REAC-STAGES, reboiler heating curves will not be consistent with column results. See Chapter 11 for a description of input keywords.  

PA-HCURVE  

Use to generate heating/cooling curve tables and plots for pumparound heater/cooler. You must specify the pumparound ID. See Chapter 11 for a description of input keywords.  

paid Pumparound ID  

VARY  

Use to specify manipulated variables for the design mode. FEED-FLOW and HEAT-STREAM are initialized in a STREAM paragraph. You must enter initial guesses of the manipulated variables. For other manipulated variables, enter estimates using the usual rating mode specification keywords:  

<html><body><table><tr><td>Sentence</td><td>Variables</td></tr><tr><td>PRODUCTS</td><td>basis-LPROD，basis-VPROD</td></tr><tr><td>HEATERS</td><td>DUTY</td></tr><tr><td>PUMPAROUND</td><td>basiS-PA-FLOW，PA-TEMP，PA-DELT，PA-DUTY，PA-VFRAC</td></tr><tr><td>COMP-EFForSTAGE-EFFMURPHREE</td><td></td></tr><tr><td>THERMOSYPHON</td><td>TREB，DTREB，VREB，basis-RFLOW</td></tr><tr><td>DECANTERS</td><td>L1-SPEC,L2-SPEC</td></tr><tr><td>COL-SPECS</td><td>All others</td></tr></table></body></html>  

The initial guesses must be bracketed by the bounds lb and ub. One VARY sentence is entered for each manipulated variable. Substitute MOLE, MASS, or STDVOL for the word basis.  

varyno . Manipulated variable number vartype .. Manipulated variable type:  

basis-RDV  

Distillate vapor fraction $R \mathsf { D } \mathsf { V } = \mathsf { D } \mathsf { V } / \mathsf { D }$ where DV is the distillate vapor flow rate and D is the total distillate flow rate, excluding any free-water when $N P H A S E = 2$ and FREE-WATER $\ c =$ YES)  

# basis-D  

Total distillate flow rate, excluding any freewater when NPHASE $^ { = 2 }$ and FREE-WATER $\ c =$ YES  

basis-B D:F  

Bottoms flow rate  

Molar ratio of distillate flow rate to feed flow rate $( \mathsf { D } / \Sigma \Sigma F _ { i j } )$  

B:F  

Molar ratio of bottoms flow rate to feed flow rate $( \mathsf { B } / \Sigma \Sigma F _ { i j } )$  

Where:   
$F =$ Feed flow rate   
$\begin{array} { r l } {  \dot { i } } & { { } = } \end{array}$ Component in the COMPS list of the DB:F-PARAMS sentence   
$j ~ =$ Stream in the STREAMS list of the DB:F-PARAMS sentence  

# basis-D:F  

Ratio of distillate flow rate to feed flow rate. Use when basis is MASS or STDVOL.  

basis-B:F  

Ratio of bottoms flow rate to feed flow rate. Use when basis is MASS or STDVOL.  

<html><body><table><tr><td></td><td></td></tr><tr><td>basis-L1</td><td>Reflux flow rate (or the liquid flow rate from the top stage),excluding any free-water when</td></tr><tr><td>basis-VN</td><td>NPHASE=2 and FREE-WATER=YES Boilup flow rate (or the vapor flow rate from the bottom stage)</td></tr><tr><td>basis-RR</td><td>Reflux ratio (L1/D), excluding any free-water when NPHASE=2 and FREE-WATER=YES</td></tr><tr><td>basis-BR</td><td>Boilup ratio (VN/B)</td></tr><tr><td>Q1</td><td>Condenser (or top stage) heat duty</td></tr><tr><td>QN</td><td>Reboiler (or bottom stage) heat duty</td></tr><tr><td>RW</td><td>Free-water reflux ratio on a mole basis (RW=LW/DW)</td></tr><tr><td></td><td>Where: LW= Free-water reflux rate</td></tr><tr><td>basis-LPROD</td><td>DW= Free-water distillate rate Liquid sidestream product flow from a stage</td></tr><tr><td>basis-VPROD</td><td>(specified by STAGE) Vapor sidestream product flow from a stage</td></tr><tr><td>DUTY</td><td>(specified by STAGE) External heater duty of a stage (specified by</td></tr><tr><td>FEED-FLOW</td><td>STAGE) Molar flow rate of a feed stream (specified by</td></tr><tr><td>HEAT-STREAM</td><td>STREAM) Duty of an inlet heat stream (specified by</td></tr><tr><td>MURPHREE</td><td>STREAM) Murphree efficiency of a group of components (specified by COMPS) in a column segment (specified by STAGE1 and STAGE2). Initial guess</td></tr><tr><td>TREB</td><td>components and for ail stages in the column segment. Thermosyphon reboiler outlet temperature</td></tr><tr><td>DTREB</td><td>Temperature change across thermosyphon</td></tr><tr><td>VREB</td><td>reboiler Thermosyphon reboiler outlet vapor fraction</td></tr><tr><td>basis-RFLOW</td><td>Thermosyphon reboiler circulation flow rate</td></tr><tr><td>L1-SPEC</td><td>Fraction of first-liquid phase returned from decanter (specified by STAGE)</td></tr><tr><td>L2-SPEC</td><td>Fraction of second-liquid_phase returned from</td></tr><tr><td>basis-PA-FLOW</td><td>decanter (specified by STAGE) Circulation flow of a pumparound (specified by</td></tr><tr><td>PA-TEMP</td><td>PA) Temperature of a pumparound (specified by PA)</td></tr><tr><td>PA-DELT</td><td>at the heater/cooler outlet Temperature change across the heater/cooler of</td></tr><tr><td>PA-DUTY</td><td>a pumparound (specified by PA) Duty of the heater/cooler for a pumparound</td></tr><tr><td>PA-VFRAC</td><td>(specified by PA) Vapor fraction of a pumparound (specified by PA)</td></tr><tr><td>SDRAW:FEED</td><td>at the heater/cooler outlet Molarratio of sidedraw flow rate to feed flow rate</td></tr><tr><td>Lower bound</td><td></td></tr><tr><td>Upper bound</td><td></td></tr><tr><td colspan="2">Maximum step size (Default=O0.1*(ub - Ib))</td></tr></table></body></html>  

lb   
ub   
step   
STAGE Stage number (required for vartypes LPROD, VPROD, DUTY, L1- SPEC, and L2-SPEC)   
STREAM Stream ID (required for vartypes FEED-FLOW, SDRAW:FEED,  and HEAT-STREAM)   
STAGE1 Stage number for initial stage of column segment (required for vartype MURPHREE)   
STAGE2 Stage number for final stage of column segment (required for vartype MURPHREE)   
COMPS List of component IDs (required for vartype MURPHREE and SDRAW:FEED) (Default $\mathbf { \sigma } =$ all components)   
PA. Pumparound ID (required for vartypes PA-FLOW, PA-TEMP, PADELT, PA-DUTY, and PA-VFRAC) Use to enter design specifications. Enter one SPEC sentence for each design specification.   
Substitute MOLE, MASS, or STDVOL for the word basis.  

specno .. Design specification number spectype ... Design specification type:  

basis-FRAC  

Purity of a product stream (specified by STREAMS), an internal stream (specified by STAGE and PHASE), or a decanter stream (specified by STAGE, DEC-STREAM, and PHASE). $\mathsf { F R A C } = \Sigma X _ { j } / \Sigma x _ { j }$  

# Where:  

$x \ =$ Component fraction $i \ =$ Component in the COMPS list $j ~ =$ Component in the BASE-COMPS list  

The default for BASE-COMPS is all components $( \Sigma { x } _ { j } { = } 1 )$ .  

basis-RECOV  

Component recovery. ${ \sf R E C O V } = \Sigma \Sigma f _ { i j } / \Sigma \Sigma f _ { i k }$  

# Where:  

$\begin{array} { r l } { f } & { { } = } \end{array}$ Component flow rate $\begin{array} { r l } { \boldsymbol { i } } & { { } = } \end{array}$ Component in the COMPS list $\begin{array} { r l } { \boldsymbol { j } } & { { } = } \end{array}$ Product stream in the STREAMS list $k \ =$ Feed stream in the BASE-STREAMS list  

The default for BASE-STREAMS is all feed streams.  

basis-FLOW  

Flow rate of a group of components (specified by COMPS) in a set of product streams (specified by STREAMS), an internal stream (specified by STAGE and PHASE), or a decanter stream (specified by STAGE, DEC-STREAM, and PHASE). The default for COMPS is all components.  

basis-RATIO  

$\mathsf { R A T I O } = \Sigma f _ { j 1 } / \Sigma f _ { j 2 }$ (BASE-STAGE specified) or $\Sigma f _ { j 1 } / \Sigma \Sigma f _ { j k }$ (BASE-STREAMS specified or defaulted)  

For basis-RATIO:  

$\begin{array} { r l } { i } & { { } = } \end{array}$ Component in the COMPS list   
$\begin{array} { r l } { \boldsymbol { j } } & { { } = } \end{array}$ Component in the BASE-COMPS list   
$k \ =$ Stream in the BASE-STREAMS list   
$f _ { i 1 } =$ Component $i$ flow rate in an internal stream specified by STAGE and PHASE   
$f _ { j 2 } =$ Component $j$ flow rate in an internal stream specified by BASE-STAGE and BASE-PHASE   
$f _ { j k } =$ Component $j$ flow rate in a feed or product stream in the BASE-STREAMS list. (The BASESTREAMS list cannot mix feed and product streams.)  

The default for COMPS and BASE-COMPS is all components. The default for BASE-STREAMS is all feed streams.  

<html><body><table><tr><td>TEMP PROP</td><td>Temperature on a given STAGE Property value,as specified by PROPERTY, for a</td></tr><tr><td>PROP-DIFF</td><td>product stream(specified by STREAMS) or an internal stream (specified by STAGE and the property phase qualifier in the corresponding PROP-SET paragraph) Property value minus base property value,as specified by PROPERTY and</td></tr><tr><td></td><td>BASE-PROPERTY. PROPERTY is the property of a product stream (specified by STREAMS) or of an internal stream (specified by STAGE and the phase qualifier in the corresponding PROP-SET paragraph).</td></tr><tr><td></td><td>BASE-PROPERTY is the property of a product stream(specified by BASE-STREAMS) or of an internal stream (specified by BASE-STAGE and the phase qualifier in the corresponding PROP- SET paragraph).</td></tr><tr><td>PROP-RATIO</td><td>Ratio of property value to base property value, asspecified by PROPERTY and BASE-PROPERTY. PROPERTY and BASE-PROPERTY areas defined above forPROP-DIFF.</td></tr><tr><td>basis-D</td><td>Total distillate flow rate,excluding any free- water When NPHASE=2 and FREE-WATER=YES</td></tr><tr><td>basis-B</td><td>Bottoms flow rate</td></tr><tr><td>basis-L1</td><td>Reflux flow rate (or the liquid flow rate from the top stage),excluding any free-water when NPHASE=2 and FREE-WATER=YES</td></tr><tr><td>basis-VN</td><td>Boilup flow rate (or the vapor flow rate from the bottom stage)</td></tr><tr><td>basis-RR</td><td>Reflux ratio (L1/D),excluding any free-water when NPHASE=2 and FREE-WATER=YES</td></tr><tr><td>basis-BR</td><td>Boilup ratio (VN/B)</td></tr><tr><td>Q1</td><td>Condenser (or top stage) heat duty</td></tr><tr><td>QN</td><td>Reboiler (or bottom stage) heat duty</td></tr><tr><td colspan="2">Desired value of the design specification</td></tr></table></body></html>  

value.. scale .. Scale factor (Default ${ \bf \varepsilon } = { \bf 1 }$ ) weight . Weighting factor (Default ${ \bf \varepsilon } = { \bf 1 }$ ) STAGE . Stage number BASE-STAGE Stage number COMPS . List of component IDs BASE-COMPS.. List of component IDs STREAMS List of stream IDs  

BASE-STREAMS.... .....  List of stream IDs   
PROPERTY ID of a property set defined by a PROP-SET paragraph consisting of a single scalar property. (See Chapter 41.)   
BASE-PROPERTY .... .....  ID of a property set defined by a PROP-SET paragraph consisting of a single scalar property. (See Chapter 41.)   
DEC-STREAM... DEC-STREAM $\mathbf { \tau } =$ FEED Decanter feed DEC-STREAM $\mathbf { \tau } =$ PRODUCT Decanter product DEC-STREAM $\mathbf { \lambda } =$ RETURN Decanter return You must also specify PHASE $= \mathsf { L }$ and decanter stage location.   
PHASE. PHASE $\mathbf { \sigma } = \mathbf { L }$ Liquid (Default) PHASE $\mathbf { \mu } = \mathbf { \vec { v } }$ Vapor PHASE=L1 First-liquid PHASE $= 1 2$ Second-liquid PHASE $\mathbf { \sigma } = \mathbf { w }$ Free-water   
BASE-PHASE BASE-PHASE=L Liquid BASE-PHASE $\mathbf { \tau } = \mathbf { \boldsymbol { v } }$ Vapor BASE-PHASE $\mathbf { \tau = L 1 }$ First-liquid BASE-PHASE $= 1 2$ Second-liquid BASE-PHASE $\mathbf { \mu } = \mathbf { w }$ Free-water (Default $\ c =$ value specified for PHASE)  

PDROP-SEC  

Use to enter pressure drop across a section of a column. You must also specify the pressure for stage1 in the P-SPEC sentence. You cannot use PDROP-SEC if you specify DPSTAGE, DP-COND, DP-COL, or P-SPEC.  

secno Section number   
stage1. Stage number for initial stage of column segment stage2. Stage number for final stage of column segment pdrop .... Pressure drop across section  

DIAGNOSTICS  

Use to control the level of convergence diagnostics in the history and log files. You can enter a level between 0 and 10. The amount of diagnostics increases with each level.  

MAIN Controls printouts of initial/final profiles, inside/middle/outside loop iterations, and outside loop variables/functions in the history file (Default $\scriptstyle = 4$ )   
OLVAR1. Controls initial local model parameter diagnostics in the history file (Default $\scriptstyle  = 4$ )   
OLVAR2. Controls local model parameter diagnostics for each outside loop in the history file (Default $\scriptstyle = 4$ )   
CMBAL Controls component mass balance diagnostics for each inside loop in the history file (Default $\scriptstyle = 4$ )   
EMBAL Controls enthalpy balance diagnostics for each inside loop in the history file (Default ${ = } 4$ )   
DESIGN.. Controls middle loop diagnostics in the history file (Default $\scriptstyle : = 4$ )   
TERM . Controls printouts of inside/middle/outside loop iterations in the log file (Default $_ { : = 0 }$ )   
TXYEST Controls printouts of temperature and composition profile results in input estimate formats in the history file (Default ${ = } 4 ^ { \cdot }$ )  

Use to generate stagewise plots of column profiles. Properties can be reported on a MOLE, MASS, or STDVOL basis.  

plotno ... Plot number  

plot-list . List of non-component-dependent properties to be plotted:  

TEMP Temperature   
PRES Pressure   
LRATE Liquid flow rate. If two liquid phases are present, both are plotted, as is the total liquid flow rate.   
VRATE Vapor flow rate   
VL-RATIO Vapor flow rate/liquid flow rate. If two liquid phases are present, the vapor flow rate/total liquid flow rate is plotted.   
LL-RATIO Second-liquid flow rate/first-liquid flow rate. Available only when two liquid phases are present.  

comp-plot .. Keyword for component-dependent property to be plotted:  

X, X1, X2, Y  

Fractions of the components and/or component groups listed are plotted. X1 and X2 can be used only when two liquid phases are present.  

KVL, KVL1, KVL2, KLL  

K-values of the components and/or listed component groups are plotted. KVL1, KVL2, and KLL cause the ratios y/x1, y/x2 and $\times 2 / \times 1$ respectively, to be plotted. They can be used only when two liquid phases are present. When two liquid phases are present, KVL is the ratio of vapor component fraction/total liquid component fraction.  

REL-VOL  

Relative volatilities of the components and/or component groups listed are plotted. You must also specify BASE-COMP. When a component group ID is specified:  

$$
R E L - V O L = \frac { \Sigma y _ { i } / \Sigma x _ { i } } { \left( y / x \right) _ { B A S E - C O M P } }
$$  

S-PLOT  

Separation factors, defined under S-OPTION  

groupid-list ..... List of component IDs and/or component group IDs  

BASE-COMP. Component ID of base component for relative volatility calculations. (Use with the REL-VOL keyword.)  

S-OPTION .. Definition of separation factor:  

# S-OPTION $\mathbf { \lambda } =$ LINEAR  

S-OPTION=LOG  

Separation factor is defined as:   
$( y _ { i } / x _ { j } ) \mid ( \Sigma y _ { h } / \Sigma x _ { h } )$ if a component ID is specified, or:   
$( \Sigma y _ { i } / \Sigma x _ { j } ) \mathrel { \mathop : } ( \Sigma y _ { h } / \Sigma x _ { h } )$ if a component group ID is specified.   
Separation factor is defined as:   
$\mathfrak { m } ( x _ { j } / \Sigma x _ { h } )$   
if a component ID is specified, or:   
$\mathfrak { m } ( \Sigma x _ { i } / \Sigma x _ { h } )$   
if a component group ID is specified.   
Where:   
$\begin{array} { r l } { i } & { { } = } \end{array}$ Component or list of components   
specified by a component group   
$\begin{array} { r l } { h } & { { } = } \end{array}$ Heavy-key component specified by HEAVY-KEY  

S-OPTION $\mathbf { \lambda } =$ COMBINED Both linear and log definition are plotted.  

(Default $\ c =$ LOG)  

HEAVY-KEY Heavy key component ID or component group ID. (Use with the SPLOT keyword.)  

BASIS BASIS $\mathbf { \tau } =$ MOLE Plotted values are on a mole basis (Default) BASIS $\mathbf { \tau } =$ MASS Plotted values are on a mass basis BASIS $\mathbf { \sigma } =$ STDVOL Plotted values are on a standard-liquid-volume  

<html><body><table><tr><td colspan="2"></td><td>BASIS=STDVOL</td><td>basisd vait</td></tr><tr><td rowspan="7"></td><td>ORDER</td><td>ORDER=TOP-DOWN</td><td>Numbers stages from top down (Default)</td></tr><tr><td>PLOT-HEADING...</td><td>ORDER=BOTTOM-UP</td><td>Numbers stages from bottom up</td></tr><tr><td></td><td>of the print-plot</td><td> Heading up to 64 characters enclosed in quotes,printed at the top</td></tr><tr><td>WIDE</td><td>OPTIONS paragraph (See Chapter 46).</td><td>Plot width option. Use to override default established by the PLOT-</td></tr><tr><td></td><td></td><td>Use to specify user-supplied subroutine for KLL. You must also specify NPHASE=3. For</td></tr><tr><td>KLL</td><td></td><td>details on writing user-supplied subroutines,see Aspen Plus User Models,Chapter 16.</td></tr><tr><td></td><td>Use to specify column segment for which the user-supplied KLL subroutine is used.You</td><td>: User-supplied FORTRAN subroutine name for KLL calculations</td></tr><tr><td rowspan="4">KLL-VECS</td><td>must also specify NPHASE=3.</td><td></td><td></td></tr><tr><td>stage1.. stage2..</td><td>. Initial stage of a column segment</td><td></td></tr><tr><td></td><td> Final stage of a column segment</td><td></td></tr><tr><td>specify NPHASE=3.</td><td>Use to define the length of arrays for the user-supplied KLL subroutine. You must also</td><td></td></tr><tr><td rowspan="3">KLL-INT</td><td>NINT...</td><td>... Length of integer parameter</td><td></td></tr><tr><td>NREAL......</td><td>..  Length of real parameter</td><td></td></tr><tr><td>You must also specify NPHASE=3.</td><td>Use to enter values for the integer parameter array of the user-supplied KLL subroutine.</td><td></td></tr><tr><td>KLL-REAL</td><td>VALUE-LIST</td><td>List of integer values</td><td></td></tr><tr><td rowspan="2"></td><td>must also specify NPHASE=3.</td><td>Use to enter values for the real parameter array of the user-supplied KLL subroutine. You</td><td></td></tr><tr><td>VALUE-LIST . List of real values</td><td></td><td></td></tr><tr><td>USERK-VECS</td><td>Use to define the length of arrays for the user-supplied kinetics subroutine.</td><td></td><td></td></tr><tr><td></td><td>NINT....</td><td></td><td></td></tr><tr><td></td><td>NREAL.</td><td>. Length of integer parameter array</td><td></td></tr><tr><td></td><td>NIWORK....</td><td>: Length of real parameter array</td><td></td></tr><tr><td></td><td></td><td>... Length of integer workspace array</td><td></td></tr><tr><td>USERK-INT</td><td>NWORK..</td><td>… Length of real workspace array</td><td></td></tr><tr><td></td><td>subroutine.</td><td></td><td> Use to enter values for the integer parameter array of the user-supplied kinetics</td></tr><tr><td>USERK-REAL</td><td>VALUE-LIST ...</td><td>.List of integer values</td><td></td></tr><tr><td></td><td></td><td> Use to enter values for the real parameter array of the user-supplied kinetics subroutine.</td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td>VALUE-LIST .</td><td>List of real values</td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr></table></body></html>  

STG-UTL  

Use to specify optional utilities to provide heating or cooling duty for stage heaters and coolers.  

stage... Stage number.  

utilityid . Utility ID.  

PA-UTL  

Use to specify optional utilities to provide heating or cooling duty for pumparounds.  

pid Pumparound ID.  

utilityid .. Utility ID.  

UTILITIES  

Use to specify optional utilities to provide heating or cooling duty for condenser and reboiler.  

COND-UTIL Utility ID for condenser.  

REB-UTIL Utility ID for reboiler.  

PARAM2  

Use to specify salt precipitation handling method.  

SALTS  

Salt precipitation handling option.  

SALTS $\mathbf { \lambda } =$ INCLUDE Salt reactions defined in the CHEMISTRY will be rigorously handled during column calculations (Default)   
SALTS $\mathbf { \lambda } =$ IGNORE Salt reactions defined in the CHEMISTRY will not be considered during column calculations.   
SALTS $\mathbf { \lambda } =$ IGNORE-CHECK Same as the IGNORE option, but the solubility index for the salts on each tray will be checked against the value of SAT-LIMIT and a warning will be issued if the limit is exceeded.  

SAT-LIMIT  

Salt concentration/salt solubility limit (Default $\mathtt { \Omega } = 1 . 0$ )  

# Accessing Variables in RADFRAC  

Many Aspen Plus features enable you to sample or change block variables. Chapter 29 describes how to access variables. The following tables list variable names and other information needed to sample and/or change variables for this block.  

Block Input   


<html><body><table><tr><td>RoekInpue</td><td></td><td>ID1</td><td>ID2</td></tr><tr><td>Sentence PARAM</td><td>Variables</td><td>1</td><td>1</td></tr><tr><td>FEEDS</td><td>STAGE NSTAGE+</td><td>sid</td><td>一</td></tr><tr><td>PRODUCTS</td><td>STAGE，basis-FLOW</td><td>sid</td><td></td></tr><tr><td>PSEUDO-STREAM</td><td></td><td></td><td>一</td></tr><tr><td>P-SPEC</td><td>STAGE，MOLE-FLOW PRES</td><td>sid stage</td><td></td></tr><tr><td>COL-SPECS</td><td>basis-RDV,T1，basis-D,basis-B,D:F，B:F，basis- D:F，basis-B:F,basis-L1，basis-VN，basis-RR,basis-</td><td>1</td><td>一</td></tr><tr><td>PDROP-SEC</td><td>BR,Q1,QN,RW,DP-STAGE,DP-COL,DP-COND, HTLOSS</td><td></td><td></td></tr><tr><td>DB:F-PARAMS</td><td>PDROP</td><td>secno</td><td>1</td></tr><tr><td>SC-REFLUX</td><td>STREAMS,CO</td><td>二</td><td>一</td></tr><tr><td>THERMOSYPHON</td><td>DEGSUB，TEMP，OPTION</td><td>二</td><td>二</td></tr><tr><td></td><td>PRES，TEMP，DELTVFRAC，basis-FLOW</td><td>二</td><td>二</td></tr><tr><td>HEATERS</td><td>DUTY</td><td>stage</td><td>一</td></tr><tr><td>COOLANT</td><td>basis-FLOW，UA，TEMP，PRES</td><td>stage</td><td></td></tr><tr><td>HTLOSS-SEC</td><td>HTLOSS-SEC</td><td>secno</td><td></td></tr><tr><td>HTLOSS</td><td>HTLOSS-VAP，HTLOSS-LIQ</td><td>一</td><td></td></tr><tr><td>COMP-EFF STAGE-EFF</td><td>EFF</td><td>stage</td><td>cid</td></tr><tr><td>STAGE-EFF-SEC</td><td>EFF</td><td>stage</td><td>二</td></tr><tr><td>DECANTERS</td><td>EFF</td><td>secno</td><td>1</td></tr><tr><td>L1-RETURN</td><td>L1-SPEC，L2-SPEC，TEMP，DEGSUB</td><td>stage</td><td>二</td></tr><tr><td>L2-RETURN</td><td>L1-RFRAC</td><td>stage1</td><td>stage2</td></tr><tr><td>L1-COMP-EFF</td><td>L2-RFRAC</td><td>stage1</td><td>stage2</td></tr><tr><td>L2-COMP-EFF</td><td>EFF</td><td>stage</td><td>cid</td></tr><tr><td>L1-STAGE-EFF</td><td>EFF</td><td>stage</td><td>cid</td></tr><tr><td></td><td>EFF</td><td>stage</td><td>一</td></tr><tr><td>L2-STAGE-EFF</td><td>EFF</td><td>stage</td><td>一</td></tr><tr><td>L2-STAGES</td><td>STAGE2</td><td>stage1</td><td>一</td></tr><tr><td>HOLD-UPt+</td><td>basis-LHLDP，basis-VHLDP</td><td>stage1</td><td>1</td></tr><tr><td>RES-TIME</td><td>LTIME,VTIME</td><td>stage1</td><td></td></tr></table></body></html>

† NSTAGE cannot be increased from the value in the Block Paragraph, but it can be decreased. †† HOLD-UP is in MOLE, MASS or VOL basis.  

continued  

Block Input (continued)   


<html><body><table><tr><td>Sentence</td><td>Variables</td><td>ID1</td><td>ID2</td></tr><tr><td>REAC-STAGES</td><td>STAGE1，STAGE2，REACID</td><td>stage1</td><td></td></tr><tr><td>T-EST</td><td>TEMP</td><td>stage</td><td></td></tr><tr><td>X-EST</td><td>X</td><td>stage</td><td>cid</td></tr><tr><td>Y-EST</td><td>Y</td><td>stage</td><td>cid</td></tr><tr><td>L-EST</td><td>MOLE-FLOW</td><td>stage</td><td>1</td></tr><tr><td>VL-EST</td><td>MOLE-RATIO</td><td>stage</td><td></td></tr><tr><td>COND-HCURVE</td><td>NPOINT，INCR，PDROP</td><td>curveno</td><td></td></tr><tr><td>REB-HCURVE</td><td>NPOINT，INCR，PDROP</td><td>curveno</td><td>二</td></tr><tr><td>VARY+++</td><td>LB,UB，STEP，STAGE，STAGE1，STAGE2，VARY-IC- STRM</td><td>varyno</td><td></td></tr><tr><td>SPEC+++</td><td>VALUE，SCALE，WEIGHT，STAGE，BASE-STAGE</td><td>specno</td><td>1</td></tr><tr><td>MOLE-KLL</td><td>KLL-A，KLL-B，KLL-C，KLL-D</td><td>kllno</td><td>cid</td></tr><tr><td>PUMPAROUND</td><td>SOURCE-STAGE,DEST-STAGE，PRES baSis-FLOW, TEMP，DELT，DUTY，VFRA</td><td>paid</td><td>1</td></tr></table></body></html>

††† Accessed variables are in SI units. VARY-IC-STRM contains pumparound ID.  

Block Results   


<html><body><table><tr><td>Description</td><td>Sentence Variable</td><td>ID1</td><td>ID2</td></tr><tr><td>Condenserduty</td><td>RESULTS</td><td>COND-DUTY</td><td></td></tr><tr><td>Reboilerduty</td><td>RESULTS</td><td>REB-DUTY</td><td></td></tr><tr><td>Subcooled reflux duty</td><td>RESULTS</td><td>QSC</td><td></td></tr><tr><td>Subcooledtemperature</td><td>RESULTS</td><td>TSC 1</td><td></td></tr><tr><td>Refluxratio</td><td>RESULTS</td><td>RR 二</td><td></td></tr><tr><td>Boilup ratio</td><td>RESULTS</td><td>BR 一</td><td></td></tr><tr><td>Stage temperature</td><td>PROFILE</td><td>TEMP+ stage</td><td>1</td></tr><tr><td>Stage pressure</td><td>PROFILE</td><td>PRES+ stage</td><td>1</td></tr><tr><td>Stage liquid rate</td><td>PROFILE</td><td>LRATE+ stage</td><td>1</td></tr><tr><td>Stage first liquid rate</td><td>PROFILE</td><td>L1RATE+ stage</td><td>1</td></tr><tr><td>Stage second liquid rate</td><td>PROFILE</td><td>L2RATE+ stage</td><td>二</td></tr><tr><td>Stage vapor rate</td><td>PROFILE</td><td>VRATE+ stage</td><td>1</td></tr><tr><td>Stage heat duty</td><td>PROFILE</td><td>DUTY+ stage</td><td>1</td></tr><tr><td>Manipulated variablestt</td><td>MAN-VARS</td><td>VALUE+ varyno</td><td>1</td></tr><tr><td>Liquid compositions</td><td>COMPS x+</td><td>cid</td><td>stage</td></tr><tr><td>First liquid compositions</td><td>COMPS</td><td>×1+ cid</td><td>stage</td></tr><tr><td>Second liquid compositions</td><td>COMPS</td><td>cid x2+</td><td>stage</td></tr><tr><td>Vapor compositions</td><td>COMPS</td><td>Y+ cid</td><td>stage</td></tr><tr><td>Reaction rates</td><td>REAC-RATES RATE+</td><td>stage</td><td>cid</td></tr></table></body></html>

† You can also access variables using the VECTOR-DEF sentence. See Chapter 29. †† Accessed variables are in SI units.  

# Thermosyphon reboiler:  

<html><body><table><tr><td>Description</td><td>Sentence</td><td>Variable ID1</td><td>ID2</td></tr><tr><td>Pressure</td><td>REB- RESULTS</td><td>PRES 1</td><td></td></tr><tr><td>Temperature</td><td>REB- RESULTS</td><td>TEMP 1</td><td></td></tr><tr><td>Vapor fraction</td><td>REB- RESULTS</td><td>VFRAC</td><td></td></tr><tr><td>Flow rate</td><td>REB- RESULTS</td><td>MOLE-FLOW -</td><td></td></tr><tr><td>Liquid composition</td><td>REB-COMP</td><td>x+ cid</td><td></td></tr><tr><td>Liquid1 composition</td><td>REB-COMP</td><td>X1+ cid</td><td>1</td></tr><tr><td>Liquid2 composition</td><td>REB-COMP</td><td>x2+ cid</td><td>1</td></tr><tr><td>Vapor composition</td><td>REB-COMP</td><td>Y+ cid</td><td></td></tr></table></body></html>

† You can also access variables using the VECTOR-DEF sentence. See Chapter 29.  

Pumparound:   


<html><body><table><tr><td>Description</td><td>Sentence Variablet ID1</td><td>ID2</td></tr><tr><td>Temperature</td><td>PA-RESULTS TEMP</td><td>二 paid</td></tr><tr><td>Pressure</td><td>PA-RESULTSPRES</td><td>paid 二</td></tr><tr><td>Duty</td><td>PA-RESULTS DUTY</td><td>paid</td></tr><tr><td>Vapor fraction</td><td>PA-RESULTSVFRAC</td><td>paid 二</td></tr><tr><td>Beta</td><td>PA-RESULTSBETA</td><td>paid 二</td></tr><tr><td>Molar flowrate</td><td>PA-RESULTSMOLE-FLOW paid</td><td>二</td></tr></table></body></html>

† You can also access variables using the VECTOR-DEF sentence. See Chapter 29.  

# Column Specification Combinations for Two-Phase and Three-Phase Calculations  

For rating mode, the column variables that can be specified are variables in the COL-SPECS sentence, and L1-SPEC and L2-SPEC for the first stage in the DECANTERS sentence. The number of variables that can be specified and the allowable combinations of specifications depend on the NPHASE specification in the PARAM sentence.  

When NPHASE $= 2$ , you must specify either basis-RDV or T1. (T1 is allowed only for columns with a partial condenser, and both a vapor and liquid distillate.) In addition, you must specify two column variables. L1-SPEC and L2-SPEC cannot be used. The allowable combinations of column variables are indicated with an X in Table 15.1:  

Table 15.1 Column Specification Combinations for Two-Phase Calculations   


<html><body><table><tr><td></td><td>L1</td><td>VN</td><td>RR</td><td>BR</td><td>Q1</td><td>QN</td></tr><tr><td>D</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td></tr><tr><td>B</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td></tr><tr><td>D:F</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td></tr><tr><td>B:F</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td></tr><tr><td>L1</td><td></td><td></td><td>X</td><td>X</td><td></td><td></td></tr><tr><td>VN</td><td></td><td></td><td>X</td><td>X</td><td></td><td></td></tr><tr><td>RR</td><td>X</td><td>X</td><td></td><td>X</td><td>X</td><td>X</td></tr><tr><td>BR</td><td>X</td><td>X</td><td>X</td><td></td><td>X</td><td>X</td></tr><tr><td>Q1</td><td></td><td></td><td>X</td><td>X</td><td></td><td>X</td></tr><tr><td>QN</td><td></td><td></td><td>X</td><td>X</td><td>X</td><td></td></tr></table></body></html>  

When NPHASE $^ { = 3 }$ , the allowable specifications depend on specifications entered for the top stage decanter. You can choose one of the following specification options:  

1 No top stage decanter is present, or only one of L1-SPEC and L2-SPEC is specified for the top stage decanter. You must specify two column variables. The allowable combinations of column variables are indicated with an X in Table 15.2. You must also specify either RDV or T1. T1 is allowed only if the column has no top stage decanter, and there is a partial condenser with both liquid and vapor distillate streams.   
2 Both L1-SPEC and L2-SPEC are specified for the top stage decanter. Two column variables must be specified. The allowable combinations are indicated with an X in the previous matrix. Both liquid and vapor distillate are assumed to be present, and RDV is calculated. An initial estimate for RDV is required.   
3 Both L1-SPEC and L2-SPEC are specified for the top stage decanter. RDV and one additional column variable must be chosen from the following: D, B, D:F, B:F, Q1, QN. Option 2 is recommended if free-water calculations are performed and a partial condenser is specified.  

Table 15.2 Column Specification Combinations for Three-Phase Calculations   


<html><body><table><tr><td></td><td>L1</td><td>VN</td><td>RR</td><td>BR</td><td>Q1</td><td>QN</td></tr><tr><td>D</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td></tr><tr><td>B</td><td>X</td><td>X</td><td>×</td><td>X</td><td>×</td><td>X</td></tr><tr><td>D:F</td><td>X</td><td>X</td><td>×</td><td>X</td><td>X</td><td>X</td></tr><tr><td>B:F</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td></tr><tr><td>Q1</td><td></td><td></td><td></td><td></td><td></td><td>X</td></tr></table></body></html>  