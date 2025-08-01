# COMPR: Compressor/Turbine  

Input Language for COMPR  

BLOCK blockid COMPR PARAM keyword $\mathbf { \bar { \Psi } } = \mathbf { \Psi }$ value  

Keywords:  

TYPE PRES DELP PRATIO POWER Optional keywords:  

MODEL-TYPE TEMP PEFF SEFF MEFF CLFR NPHASE SB-MAXIT SB-TOL MAXIT TOL PS-FLASH INT-METHOD INT-STEP PRAT-STEP PRAT-FINAL INTERVALS PLOSS-FACTOR PLOSS-OFFSET PL-FLOW-UNIT PLOSS-UNITS PL-SP-UNIT  

PERFOR-PARAM keyword $\circleddash$ value  

Optional keywords:  

SUCT-NOZ-DIA SUCT-K-FACT GPSA-BASIS NCURVES EXTRAPOLATECALC-SPEED ACT-SH-SPEED IMPELLER-DIA USER-CURVESREF-SH-SPEED FANEXPH FANEXPE FANEXPP SPLINE-FIT OPT-DESIGNCORR-FLOW CURVE-DIM DEF-PRATIO GEAR-RATIO PIN-DESIGNTIN-DESIGN PIN-UNITS TIN-UNITS GAS-CONST-UNIT  

Optional keywords for head curves:  

HEAD-FACTOR HEAD-OFFSET HEAD-NPOINT H-FLOW-VAR   
H-FLOW-UNIT HEAD-UNITS HEAD-SP-UNIT ACTUAL-HEAD   
Optional keywords for head coefficient curves:   
HEADC-FACTOR HEADC-OFFSET HEADC-NPOINT HC-FLOW-VAR   
HC-FLOW-UNIT ACTUAL-HEADC  

<html><body><table><tr><td colspan="6">Optional keywords for power curves:</td></tr><tr><td>POWER-FACTOR PW-FLOW-UNIT</td><td>POWER-OFFSET POWER-UNITS</td><td></td><td>POWER-NPOINT</td><td colspan="2">PW-FLOW-VAR</td></tr><tr><td>PRES-FACTOR</td><td>Optional keywords for discharge pressure curves: PRES-OFFSET</td><td>PRES-NPOINT</td><td>P-FLOW-VAR</td><td colspan="2">P-FLOW-UNI</td></tr><tr><td>PRES-UNITS Optional keywords for pressure ratio curves:</td><td></td><td></td><td colspan="2"></td><td></td></tr><tr><td>PRAT-FACTOR PRAT-OFFSET UNIT</td><td></td><td>PRAT-NPOINT</td><td></td><td colspan="2">PR-FLOW-VAR PR-FLOW-</td></tr><tr><td>DELP-FACTOR</td><td>Optional keywords for pressure change curves: DELP-OFFSET</td><td>DELP-NPOINT</td><td></td><td colspan="2">DP-FLOW-VAR DP-FLOW-</td></tr><tr><td>UNIT DELP-UNITS</td><td>Optional keywords for efficiency curves:</td><td></td><td></td><td colspan="2"></td></tr><tr><td>EFF-FACTOR EFF-SP-UNIT Optional keywords for surge volume curves:</td><td>EFF-OFFSET</td><td>EFF-NPOINT</td><td>EF-FLOW-VAR</td><td colspan="2">EF-FLOW-UNIT</td></tr><tr><td>SURGE-FACTOR HEAD-TABLE</td><td>SURGE-OFFSET</td><td>SURGE-UNITS flow /</td><td></td><td colspan="2">SG-SP-UNIT</td></tr><tr><td>HEAD-POLY curve Keywords:</td><td>curve point head keyword=value 1</td><td></td><td></td><td colspan="2"></td></tr><tr><td>COEF1 COEF2</td><td>COEF3 COEF4</td><td>SURGE</td><td>STONEWALL</td><td colspan="2"></td></tr><tr><td>HEADC-TABLE HEADC-POLY</td><td>curve point curve keyword=value /</td><td>head-coeff</td><td>flow /</td><td colspan="2"></td></tr><tr><td>Keywords: COEF1 COEF2</td><td>COEF3 COEF4</td><td>SURGE</td><td>STONEWALL</td><td colspan="2"></td></tr><tr><td>POWER-TABLE POWER-POLY</td><td>curve point curve</td><td>power keyword=value /</td><td>flow</td><td colspan="2"></td></tr><tr><td>Keywords: COEF1 COEF2</td><td>COEF3</td><td>COEF4</td><td>SURGE STONEWALL</td><td colspan="2"></td></tr><tr><td>PRES-TABLE PRES-POLY</td><td>curve point curve</td><td>pres keyword=value /</td><td>flow /</td><td colspan="2"></td></tr><tr><td>Keywords: COEF1 COEF2 PRATIO-TABLE PRATIO-POLY</td><td>COEF3 curve curve</td><td>COEF4 point pratio keyword=value</td><td>SURGE flow</td><td colspan="2">STONEWALL</td></tr><tr><td>Keywords:</td><td></td><td></td><td></td><td colspan="2">STONEWALL</td></tr><tr><td>COEF1 COEF2</td><td>COEF3</td><td>COEF4</td><td>SURGE</td><td colspan="2"></td></tr><tr><td>DELP-TABLE</td><td>curve point</td><td></td><td></td><td colspan="2"></td></tr><tr><td></td><td></td><td>delp flow /</td><td></td><td colspan="2"></td></tr></table></body></html>  

DELP-POLY curve keyword $\mathbf { \bar { \rho } } = \mathbf { \rho }$ value  /   . . .  

Keywords:  

<html><body><table><tr><td>COEF1</td><td>COEF2 COEF3</td><td></td><td>COEF4</td><td>SURGE</td><td>STONEWALL</td></tr><tr><td>EFF-TABLE</td><td>curve</td><td>point</td><td>eff</td><td>flow/...</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EFF-POLY</td><td>curve</td><td>keyword=value /</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr></table></body></html>  

Keywords:  

COEF1 COEF2 COEF3 COEF4  

SHAFT-SPEED curve shaft-speed  /  . MACH-NO curve mach-no  / HEAD-CORR keyword=value  

Keywords:  

<html><body><table><tr><td>COEF1</td><td>COEF2</td><td>COEF3</td><td>COEF4</td><td>COEF5</td><td>COEF6</td><td>COEF7</td><td>COEF8</td></tr><tr><td>EFF-CORR</td><td>keyword=value</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table></body></html>  

Keywords:  

<html><body><table><tr><td>COEF1</td><td>COEF2</td><td>COEF3</td><td>COEF4</td><td>COEF5</td><td>COEF6</td><td>COEF7</td><td>COEF8</td></tr><tr><td>SURGE-POLY</td><td></td><td>keyword=value</td><td></td><td></td><td></td><td></td><td></td></tr></table></body></html>  

Keywords:  

COEF1 COEF2 COEF3  

<html><body><table><tr><td>PLOSS-POLY keyword=value</td></tr></table></body></html>  

Keywords:  

COEF1 COEF2 COEF3  

<html><body><table><tr><td>SUBROUTINE CURVES=subrname</td></tr><tr><td>USER-VECS keyword=value</td></tr></table></body></html>  

Optional keywords:  

NINT NREAL NIWORK NWORK  

INT value-list   
REAL value-list   
UTILITY UTILITY-ID $\mathbf { \lambda } =$ utilityid  

# Input Language Description for COMPR  

PARAM  

Use to enter compressor specifications, efficiencies, and optional flash convergence parameters. You can use an inlet work stream to provide a power specification.  

MODEL-TYPE . MODEL-TYPE $\mathbf { \lambda } =$ Model type is compressor. (Default) COMPRESSOR MODEL-TYPE $\mathbf { \lambda } =$ TURBINE Model type is turbine.   
TYPE . TYPE $\mathbf { \lambda } =$ ISENTROPIC Isentropic compressor/turbine (only this option is allowed for turbines)   
TYPE $\mathbf { \lambda } =$ POS-DISP Polytropic positive-displacement compressor calculations   
TYPE= Polytropic compressor calculations using the   
ASME-POLYTROPIC ASME method3   
TYPE $\mathbf { \lambda } = \mathbf { \lambda }$ ASME-ISENTROPIC Isentropic compressor calculations using the ASME method3   
TYPE $\mathbf { \lambda } =$ Polytropic compressor calculations using the   
GPSA-POLYTROPIC GPSA method4   
TYPE $\mathbf { \lambda } =$ GPSA-ISENTROPIC Isentropic compressor calculations using the GPSA method4   
TYPE $\mathbf { \lambda } =$ INT-POLYTROPIC Polytropic compressor calculations using the piecewise integration method (see Note 12.)   
TYPE $\mathbf { \lambda } =$ INT-POS-DISP Polytropic positive-displacement compressor calculation using the integration method (see Note 12.)   
PRES . Outlet pressure   
DELP Pressure change.  When MODEL-TYPE $\ c =$ COMPRESSOR, $\mathsf { D E L P } > 0$ is pressure increase and DELP $\leq 0$ is pressure decrease. You can use DELP $\leq 0$ only when TYPE $\ c =$ ISENTROPIC. When MODELTYPE $\ c =$ TURBINE, DELP is pressure decrease and must be greater than or equal to 0.   
PRATIO . Pressure ratio (outlet pressure/inlet pressure)   
POWER . Power input. When MODEL-TYPE $\ c =$ COMPRESSOR, power supplied to the compressor is positive. Power produced by a turbine is negative. Work streams use the opposite convention. When MODEL-TYPE $\ c = { \overrightarrow { \mathbf { \Gamma } } }$ TURBINE, POWER is power produced and must be positive.   
TEMP. Outlet temperature. Use when TYPE $\ c =$ GPSA-POLYTROPIC, POSDISP, or ASME-POLYTROPIC.   
PEFF. Polytropic efficiency as defined in Note 1. Use when TYPE $\ c =$ GPSAPOLYTROPIC, POS-DISP, or ASME-POLYTROPIC. (Default $_ { : = 0 . 7 2 }$ )   
SEFF. Isentropic efficiency as defined in Note 2. Use only when TYPE $\ c =$ ISENTROPIC, GPSA-ISENTROPIC, or ASME-ISENTROPIC. (Default $_ { = 0 . 7 2 }$ )   
MEFF . Mechanical efficiency as defined in Note 3. (Default $\scriptstyle = 1$ )   
CLFR . Clearance fraction. Use only when TYPE $\ c =$ POS-DISP. (Default $= 0 . 5$ )   
NPHASE . NPHASE $\mathbf { \lambda } = \mathbf { 1 }$ Gas-phase calculations only (Default) NPHASE $\mathbf { \sigma } = \mathbf { 2 }$ Two-phase flash NPHASE $= 3$ Three-phase flash  

<html><body><table><tr><td></td><td colspan="2">phase calculations.At the end of calculations, the outlet stream is flashed at the outlet temperature and pressure to check for any condensation.If needed, the outlet stream is also checked at the outlet pressure and the intermediate isentropic temperature.If the vapor fraction calculated by either flash is less than 1.0,COMPR generates a message recommending you specify NPHASE=2.</td></tr><tr><td>SB-MAXIT</td><td colspan="2">Maximum iterations for entropy balance calculations. Use only When TYPE=ISENTROPIC,ASME-ISENTROPIC,Or ASME- POLYTROPIC. (Default=30)</td></tr><tr><td>SB-TOL</td><td colspan="2">Tolerance for entropy balance calculations. Use only when TYPE=ISENTROPIC,ASME-POLYTROPIC,Or ASME-ISENTROPIC.</td></tr><tr><td>MAXIT.</td><td colspan="2">(Default=1x10-4) Maximum number of flash iterations. (Default=value established by the SIM-OPTIONS paragraph.) (See Chapter 45.)</td></tr><tr><td>TOL</td><td colspan="2">Flash convergence tolerance.(Default=value established by the SIM-OPTIONS paragraph.) (See Chapter 45.)</td></tr><tr><td>PS-FLASH..</td><td colspan="2">For constant entropy flash calculations,determines which algorithm to use:</td></tr><tr><td></td><td colspan="2">PS-FLASH=DIRECT Use direct call to Flash PS-FLASH=INDIRECT Perform a series of PQ flashes until the specified</td></tr><tr><td>INT-METHOD</td><td colspan="2">entropy is obtained (Default) The integration method used in polytropic and positive</td></tr><tr><td></td><td colspan="2">displacement model calculations:</td></tr><tr><td></td><td colspan="2">INT-METHOD=N-METHOD Using a piecewise integration with the relationship of pv"=constant (see Note 12.)</td></tr><tr><td>INT-STEP</td><td colspan="2">INT-METHOD=DIRECT Using a direct piecewise integration (see Note 12.)</td></tr><tr><td></td><td colspan="2">For the integration method,method used for determining pressure change in the integration steps:</td></tr><tr><td></td><td colspan="2">INT-STEP=EQUAL-PRATIO Equal presSure ratio is used.</td></tr><tr><td></td><td colspan="2">INT-STEP=EQUAL-DELPEqual pressure change is used.</td></tr><tr><td>PRAT-STEP</td><td colspan="2">Pressure ratio in each integration step when INT-STEP=EQUAL- PRATIO (Default=1.25).</td></tr><tr><td>PRAT-FINAL</td><td colspan="2">Pressure ratio in the last integration step when INT-STEP=EQUAL-</td></tr><tr><td>INTERVALS</td><td colspan="2">PRATIO (Default=1.375). Number of intervals in piecewise integration of work integral when</td></tr><tr><td>PLOSS-FACTOR</td><td colspan="2">INT-STEP=EQUAL-DELP (DefauIt=5). Scaling factor for power loss</td></tr><tr><td>PLOSS-OFFSET</td><td colspan="2">Offset for power loss. Units of power loss are used.</td></tr><tr><td>PL-FLOW-UNIT</td><td colspan="2">Units of flow rate used in power loss curve. Default is global unit.</td></tr><tr><td></td><td colspan="2"></td></tr><tr><td>PLOSS-UNITS</td><td colspan="2">Units of power loss used in power loss curve.Default is global unit.</td></tr><tr><td>PL-SP-UNIT</td><td colspan="2">Units of shaft speed used in power loss curve. Default is global</td></tr><tr><td></td><td colspan="2">unit. Use to enter optional parameters related to compressor performance curves and suction</td></tr></table></body></html>  

PERFOR-PARAM  

SUCT-NOZ-DIA.. Diameter of suction nozzle. Use to calculate pressure drop across suction nozzle of compressor, using the equation in Note 4.   
SUCT-K-FACT . K-factor (velocity head multiplier) for suction nozzle. Use to calculate pressure drop across suction nozzle of compressor, using the equation in Note 4.   
GPSA-BASIS.. Use when TYPE $\ c =$ GPSA-ISENTROPIC or GPSA-POLYTROPIC5 GPSA-BASIS $\mathbf { \sigma } =$ SUCTION Uses suction conditions in head equation (Default) GPSA-BASIS $\mathbf { \tau } =$ AVERAGE Uses average of suction and discharge conditions in head equation  

NCURVES Number of compressor performance curves. If:  

•  A single curve is supplied, it can be used to rate a compressor at   
a given speed   
•  A reference shaft speed is known, Fan laws will be used to scale   
the performance   
•  Multiple curves are supplied, linear interpolation is performed   
between curves to find the performance at operating point   
•  A user subroutine is used to enter performance specifications,   
set NCURVES ${ \bf \varepsilon } = { \bf 1 }$  

EXTRAPOLATE. Indicates whether to extrapolate performance curve(s) beyond surge and stonewall points:  

EXTRAPOLATE $\mathbf { \lambda } =$ YES Extrapolates (Default) EXTRAPOLATE $= N O$ Does not extrapolate  

CALC-SPEED. Indicates whether compressor shaft speed is calculated or specified:  

CALC-SPEED=NO Specified by user (Default) CALC-SPEED $\mathbf { \tau } =$ YES Calculated by Aspen Plus model  

ACT-SH-SPEED ..... Speed of compressor shaft  

IMPELLER-DIA ... Diameter of the compressor's impeller  

USER-CURVES . Specifies the type of performance variable (in addition to efficiency) supplied by a user subroutine:  

USER-CURVES $\mathbf { \lambda } =$ HEAD Head USER-CURVES= Head coefficient HEAD-COEF USER-CURVES $\mathbf { \tau } =$ POWER Power USER-CURVES $\mathbf { \lambda } =$ PRES Discharge pressure USER-CURVES $\mathbf { \lambda } =$ PRATIO Pressure ratio USER-CURVES $\mathbf { \lambda } =$ DELP Pressure drop  

REF-SH-SPEED Reference speed of compressor shaft. Use when Fan laws are applied to determine compressor performance.  

FANEXPH Fan law exponent for head (Default $= 2 . 0$ ) FANEXPE.. Fan law exponent for efficiency (Default $: = 1 . 0$ ) FANEXPP.. Fan law exponent for power (Default $= 3 . 0$ ) SPLINE-FIT . Interpolation method for tabular data SPLINE-FIT $\mathbf { \bar { \Pi } } = \mathbf { \Phi }$ HARWELL Cubic spline fit using Harwell method  

SPLINE-FIT $\mathbf { \bar { \Pi } } = \mathbf { \Phi }$ HERMITE Cubic spline fit using Hermite method (Default) SPLINE-FIT $\mathbf { \bar { \rho } } = \mathbf { \rho }$ LINEAR Linear interpolation between successive points OPT-DESIGN ... .  Options for off-design adjustments.  

OPT-DESIGN $\mathbf { \lambda } =$ NONE No off design adjustment (Default)   
OPT-DESIGN $\mathbf { \tau } =$ Use a power correction factor to account for   
CORR-FACTOR deviation from design conditions (only allowed for power curves)   
OPT-DESIGN $\mathbf { \lambda } =$ Use corrected flow rate for performance curves   
CORR-FLOW   
OPT-DESIGN $\mathbf { \tau } =$ Use quasi-dimensionless performance curves   
DIMENSIONLESS  

CORR-FLOW ..... .....  Options for corrected flow used in performance curves.  

CORR-FLOW $\mathbf { \tau } = \mathbf { \tau }$ TP  

CORR-FLOW $\mathbf { \lambda } =$ PV  

The flow rate is corrected by the ratio of   
Pressure Temperature at inlet design and   
actual conditions (Default)   
The flow rate is corrected by the ratio of   
Pressure molar volume at inlet design and   
actual conditions  

CURVE-DIM... Options for performance curve dimensionless groups.  

CURVE-DIM $\mathbf { \lambda } =$ QUASI Use quasi-dimensionless groups (Default) CURVE-DIM $\mathbf { \tau } =$ R-QUASI Use quasi-dimensionless groups containing gas constant R  

DEF-PRATIO... Definitions of pressure ratio.  

DEF-PRATIO $\mathbf { \lambda } =$ Outlet pressure divided by inlet pressure POUT-OV-PIN (Default)   
DEF-PRATIO $\mathbf { \lambda } =$ Inlet pressure divided by outlet pressure PIN-OV-POUT  

GEAR-RATIO . The gear ratio between the driver and the compressor (compressor speed/driver speed). Use GEAR-RATIO only if speed is available in the inlet work stream.  

PIN-DESIGN.. Inlet pressure at design conditions  

TIN-DESIGN.. Inlet temperature at design conditions  

PIN-UNITS. Units of inlet pressure used in quasi-dimensionless curves  

TIN-UNITS . Units of inlet temperature used in quasi-dimensionless curves  

GAS-CONST-UNIT .......  Units of gas constant used in quasi-dimensionless curves (when CURVE-DIM $\mathbf { \tau } = \mathbf { \tau }$ R-QUASI)  

HEAD-FACTOR. Scaling factor applied to head values calculated from either tabular (HEAD-TABLE) or polynomial (HEAD-POLY) data (Default ${ \tt = } 1$ )  

HEAD-OFFSET .............  Offset for head developed. Units of HEAD-UNITS are used.  

HEAD-NPOINT. Maximum number of data points in a curve when head versus flow curves are specified in a table  

H-FLOW-VAR.. Independent flow variable used in head versus flow curves:  

H-FLOW-VAR $\mathbf { \tau } =$ VOL-FLOW Volume flow H-FLOW-VAR $\mathbf { \lambda } =$ Mass flow MASS-FLOW  

H-FLOW-UNIT .. Units of the independent flow variable in head versus flow curves  

HEAD-UNITS . Units of head data in head versus flow curves  

ACTUAL-HEAD... Indicates if the head specified in the HEAD-TABLE, HEAD-POLY, or HEAD-CORR sentence is actual or polytropic/isentropic.(See Note 5.)  

ACTUAL-HEAD $\mathbf { \lambda } =$ NO Head is polytropic/isentropic (Default) ACTUAL-HEAD $\mathbf { \tau } =$ YES Head is actual   
HEADC-FACTOR. Scaling factor applied to head coefficient values calculated from either tabular (HEADC-TABLE) or polynomial (HEADC-POLY) data of performance curves (Default $\scriptstyle = 1$ )   
HEADC-OFFSET Offset for head coefficient   
HEADC-NPOINT.. Maximum number of data points in a curve when head coefficient versus flow curves are specified in a table   
HC-FLOW-VAR.. .  Independent flow variable used in head coefficient versus flow curves: H-FLOW-VAR= Volume flow per shaft speed in RPM, or specific "VOL-FLOW/N" flow H-FLOW-VAR $\mathbf { \lambda } =$ Flow coefficient FLOW-COEFF   
HC-FLOW-UNIT .. Units of the independent flow variable in head coefficient versus flow curves   
ACTUAL-HEADC.. .  Indicates if the head coefficient specified in the HEADC-TABLE or HEADC-POLY sentence is actual or polytropic/isentropic. (See Note 5.) ACTUAL-HEADC $= N O$ Head coefficient is polytropic/isentropic (Default) ACTUAL-HEADC $\mathbf { \lambda } =$ YES Head coefficient is actual   
POWER-FACTOR..... .....  Scaling factor applied to power values calculated from either tabular (POWER-TABLE) or polynomial (POWER-POLY) data (Default ${ \bf \Pi } = 1$ )   
POWER-OFFSET Offset for power. Units of POWER-UNITS are used.   
POWER-NPOINT.. ..  Maximum number of data points in a curve when power versus flow curves are specified in a table   
PW-FLOW-VAR.. ...  Independent flow variable used in power versus flow curves: PW-FLOW-VAR $\underline { { \underline { { \mathbf { \Pi } } } } } =$ Volume flow VOL-FLOW PW-FLOW-VAR $\mathbf { \lambda } =$ Mass flow MASS-FLOW   
PW-FLOW-UNIT .. ..  Units of the independent flow variable in power versus flow curves   
POWER-UNITS . ..  Units of power data in power versus flow curves   
PRES-FACTOR ..... ....  Scaling factor applied to discharge pressure values calculated from either tabular (PRES-TABLE) or polynomial (PRES-POLY) data (Default $\scriptstyle = 1$ )   
PRES-OFFSET Offset for discharge pressure. Units of PRES-UNITS are used except for gauge pressure.   
PRES-NPOINT .. Maximum number of data points in a curve when discharge pressure versus flow curves are specified in a table   
P-FLOW-VAR..... ......  Independent flow variable used in discharge pressure versus flow curves:  

P-FLOW-VAR $\mathbf { \lambda } =$ VOL-FLOW Volume flow P-FLOW-VAR $\mathbf { \lambda } =$ MASS- Mass flow FLOW  

Units of the independent flow variable in discharge pressure versus flow curves  

PRES-UNITS.. Units of pressure data in discharge pressure versus flow curves  

PRAT-FACTOR .. Scaling factor applied to pressure ratio values calculated from either tabular (PRATIO-TABLE) or polynomial (PRATIO-POLY) data (Default $\scriptstyle = 1$ )  

PRAT-OFFSET... Offset for pressure ratio.  

PRAT-NPOINT . Maximum number of data points in a curve when pressure ratio versus flow curves are specified in a table  

PR-FLOW-VAR. Independent flow variable used in pressure ratio versus flow curves:  

PR-FLOW-VAR $\mathbf { \tau } =$ VOL-FLOW PR-FLOW-VAR $\mathbf { \tau } =$ MASS-FLOW  

Volume flow Mass flow  

PR-FLOW-UNIT .. Units of the independent flow variable in pressure ratio versus flow curves  

ELP-FACTOR . Scaling factor applied to pressure change values calculated from either tabular (DELP-TABLE) or polynomial (DELP-POLY) data (Default $\scriptstyle = 1$ )  

DELP-OFFSET .... Offset for pressure change. Units of DELP-UNITS are used.  

DELP-NPOINT . Maximum number of data points in a curve when pressure change versus flow curves are specified in a table  

DP-FLOW-VAR.. Independent flow variable used in pressure change versus flow curves:  

DP-FLOW-VAR $\mathbf { \tau } =$ VOL-FLOW DP-FLOW-VAR $\mathbf { \tau } =$ MASS-FLOW  

Volume flow Mass flow  

DP-FLOW-UNIT .. Units of the independent flow variable in pressure change versus flow curves  

DELP-UNITS.......  

....  Units of pressure change data in pressure change versus flow curves  

EFF-FACTOR....  

...  Scaling factor applied to efficiency values calculated from either tabular (EFF-TABLE) or polynomial (EFF-POLY) data (Default ${ \bf \Pi } = 1$ )  

EFF-OFFSET . Offset for efficiency.  

EFF-NPOINT. Maximum number of data points in a curve when efficiency versus flow curves are specified in a table  

EF-FLOW-VAR .... .  Independent flow variable used in efficiency versus flow curves:  

Volume flow  

EF-FLOW-VAR $\mathbf { \lambda } =$ VOL-FLOW EF-FLOW-VAR $\mathbf { \lambda } =$ MASS-FLOW EF-FLOW-VAR= "VOL-FLOW/N"  

Mass flow  

Volume flow per shaft speed in RPM or specific speed  

EF-FLOW-VAR= Flow coefficient FLOW-COEFF  

EF-FLOW-UNIT.. Units of the independent flow variable in efficiency versus flow curves   
EFF-SP-UNIT. Units of shaft speed used in efficiency curve (EFF-CORR sentence). Default is global unit.   
SURGE-FACTOR... Scaling factor for surge volumetric flow rate.   
SURGE-OFFSET ... Offset for surge volumetric flow rate. Units of SURGE-UNITS are used.   
SURGE-UNITS . Units of surge volumetric flow rate used in surge curve. Default is global unit.   
SG-SP-UNIT Units of shaft speed used in surge curve. Default is global unit.  

HEAD-TABLE  

Use to enter values of head developed versus suction flow rate in a table. You must also specify HEAD-NPOINT, HEAD-UNITS, H-FLOW-VAR, and H-FLOW-UNIT in the PERFORPARAM sentence. When performance curves are entered in tabular form, the first point of the table is taken as surge and the last point as stonewall, for a given curve. (See Notes 6 and 7.)  

curve . Curve number   
point . Row number within a table   
head . Head developed. The head can be polytropic, isentropic, or actual, depending on TYPE and ACTUAL-HEAD specifications. (See Note 5.)   
flow . Suction flow rate (volumetric or mass)  

HEAD-POLY  

Use to enter polynomial coefficients to calculate head developed as a function of suction flow rate. You can enter surge and stonewall values. You must also specify H-FLOW-VAR and H-FLOW-UNIT in the PERFOR-PARAM sentence. (See Note 6.) The polynomial used is:  

$$
Y = c o e f 1 + c o e f 2 ^ { * } X + c o e f 3 ^ { * } X ^ { 2 } + c o e f 4 ^ { * } X ^ { 3 }
$$  

Where:  

$x$ $\mathbf { \tau } = \mathbf { \tau }$ Suction flow rate (volumetric or mass) Y $\mathbf { \tau } = \mathbf { \tau }$ Head developed  

curve Curve number  

COEF1 First coefficient of head versus flow polynomial  

COEF2 Second coefficient of head versus flow polynomial  

COEF3 Third coefficient of head versus flow polynomial  

COEF4 . Fourth coefficient of head versus flow polynomial  

SURGE. Suction flow rate value at which the compressor surges  

STONEWALL. Suction flow rate value at which the compressor stonewalls  

HEADC-TABLE  

Use to enter values of head coefficient versus either suction flow rate per shaft speed in rpm or flow coefficient, in a table. You must also specify HEADC-NPOINT, HC-FLOW-VAR, and HC-FLOW-UNIT (if applicable) in the PERFOR-PARAM sentence. When performance curves are entered in tabular form, the first point of the table is taken as surge and the last point as stonewall, for a given curve.   
(See Notes 6, 7, and 8.)  

curve Curve number point Row number within a table  

head-coeff Head coefficient. The value can be polytropic, isentropic, or actual, depending on TYPE and ACTUAL-HEADC specifications. (See Note 5.)   
flow . Suction flow rate per shaft speed in rpm, or value of flow coefficient  

HEADC-POLY  

Use to enter polynomial coefficients to calculate head coefficient as a function of either suction flow rate per shaft speed in rpm or flow coefficient, in polynomial form. You must also specify HC-FLOW-VAR and HC-FLOW-UNIT (if applicable) in the PERFOR-PARAM sentence. (See Notes 6 and 8.) You can also enter surge and stonewall values. The polynomial used is:  

$$
Y = c o e f 1 + c o e f 2 ^ { * } X + c o e f 3 ^ { * } X ^ { 2 } + c o e f 4 ^ { * } X ^ { 3 }
$$  

Where:  

$x$ $\mathbf { \sigma } = \mathbf { \sigma }$ Volumetric flow rate per shaft speed in rpm or flow coefficient Y $\mathbf { \tau } = \mathbf { \tau }$ Head coefficient  

curve Curve number  

COEF1 First coefficient of head coefficient versus flow polynomial  

COEF2 Second coefficient of head coefficient versus flow polynomial  

COEF3 Third coefficient of head coefficient versus flow polynomial  

COEF4 Fourth coefficient of head coefficient versus flow polynomial  

SURGE. Flow coefficient, or specific flow at which the compressor surges  

STONEWALL Flow coefficient, or specific flow at which the compressor stonewalls  

POWER-TABLE  

Use to enter values of power supplied versus suction flow rate in a table. You must also specify POWER-NPOINT, POWER-UNITS, PW-FLOW-VAR, and PW-FLOW-UNIT in the PERFOR-PARAM sentence. When performance curves are entered in tabular form, the first point of the table is taken as surge and the last point as stonewall, for a given curve. (See Notes 6 and 7.)  

curve Curve number point Row number within a table power Power supplied flow Suction flow rate (volumetric or mass)  

POWER-POLY  

Use to enter polynomial coefficients to calculate the power supplied as a function of suction flow rate. You must also specify POWER-UNITS, PW-FLOW-VAR, and PW-FLOW-UNIT in the PERFOR-PARAM sentence. (See Note 6.) You can enter surge and stonewall values. The polynomial used is:  

$$
Y = c o e f 1 + c o e f 2 ^ { * } X + c o e f 3 ^ { * } X ^ { 2 } + c o e f 4 ^ { * } X ^ { 3 }
$$  

Where:   
$x$ $\mathbf { \tau } = \mathbf { \tau }$ Suction flow rate (volumetric or mass)   
Y $\mathbf { \tau } = \mathbf { \tau }$ Power supplied   
curve Curve number   
COEF1 First coefficient of power versus flow polynomial   
COEF2 Second coefficient of power versus flow polynomial   
COEF3 .. Third coefficient of power versus flow polynomial  

COEF4 . Fourth coefficient of power versus flow polynomial  

SURGE. Suction flow rate at which the compressor surges  

STONEWALL.. Suction flow rate at which the compressor stonewalls  

PRES-TABLE  

Use to enter values of discharge pressure versus suction flow rate in a table. You must also specify PRES-NPOINT, PRES-UNITS, P-FLOW-VAR, and P-FLOW-UNIT in the PERFORPARAM sentence. When performance curves are entered in tabular form, the first point of the table is taken as surge and the last point as stonewall, for a given curve. (See Notes 6 and 7.)  

curve Curve number point . Row number within a table pres Discharge pressure flow Suction flow rate (volumetric or mass)  

PRES-POLY  

Use to enter polynomial coefficients to calculate discharge pressure as a function of suction flow rate. You must also specify PRES-UNITS, P-FLOW-VAR, and P-FLOW-UNIT in the PERFOR-PARAM sentence. (See Note 6.) You can enter surge and stonewall values. The polynomial used is:  

$$
Y = c o e f 1 + c o e f 2 ^ { * } X + c o e f 3 ^ { * } X ^ { 2 } + c o e f 4 ^ { * } X ^ { 3 }
$$  

Where:  

$x$ $\mathbf { \sigma } = \mathbf { \sigma }$ Suction flow rate (volumetric or mass) Y $\mathbf { \tau } = \mathbf { \tau }$ Discharge pressure  

curve Curve number  

COEF1 First coefficient of pressure versus flow polynomial  

COEF2 Second coefficient of pressure versus flow polynomial  

COEF3 Third coefficient of pressure versus flow polynomial  

COEF4 . Fourth coefficient of pressure versus flow polynomial  

SURGE. Suction flow rate at which the compressor surges  

STONEWALL.. Suction flow rate at which the compressor stonewalls  

# PRATIO-TABLE  

Use to enter pressure ratio (discharge pressure/suction pressure) versus suction flow rate in a table. You must also specify PRAT-NPOINT, PR-FLOW-VAR, and PR-FLOW-UNIT in the PERFOR-PARAM sentence. When performance curves are entered in tabular form, the first point of the table is taken as surge and the last point as stonewall, for a given curve. (See Notes 6 and 7.)  

curve Curve number point Row number within a table pratio. Pressure ratio flow Suction flow rate (volumetric or mass)  

PRATIO-POLY  

Use to enter polynomial coefficients to calculate pressure ratio (discharge pressure/suction pressure) as a function of suction flow rate. You must also specify PR-FLOW-VAR and PRFLOW-UNIT in the PERFOR-PARAM sentence. (See Note 6.) You can enter surge and stonewall values. The polynomial used is:  

$$
Y = c o e f 1 + c o e f 2 ^ { * } X + c o e f 3 ^ { * } X ^ { 2 } + c o e f 4 ^ { * } X ^ { 3 }
$$  

Where:  

X $\mathbf { \sigma } = \mathbf { \sigma }$ Suction flow rate (volumetric or mass)   
Y $\mathbf { \tau } = \mathbf { \tau }$ Pressure ratio   
curve Curve number   
COEF1 . First coefficient of pratio versus flow polynomial   
COEF2 . Second coefficient of pratio versus flow polynomial   
COEF3 .. Third coefficient of pratio versus flow polynomial   
COEF4 .. Fourth coefficient of pratio versus flow polynomial   
SURGE. Suction flow rate at which the compressor surges   
STONEWALL Suction flow rate at which the compressor stonewalls  

DELP-TABLE  

Use to enter values of pressure change (discharge pressure/suction pressure) versus suction flow rate in a table. You must also specify DELP-NPOINT, DELP-UNITS, DP-FLOWVAR, and DP-FLOW-UNIT in the PERFOR-PARAM sentence. When performance curves are entered in tabular form, the first point of the table is taken as surge and the last point as stonewall, for a given curve. (See Notes 6 and 7.)  

curve Curve number point Row number within a table delp Pressure change flow . Suction flow rate (volumetric or mass)  

DELP-POLY  

Use to enter polynomial coefficients to calculate pressure change (discharge pressuresuction pressure) as a function of suction flow rate. You must also specify DELP-UNITS, DPFLOW-VAR, and DP-FLOW-UNIT in the PERFOR-PARAM sentence. (See Note 6.) You can enter surge and stonewall values. The polynomial used is:  

$$
Y = c o e f 1 + c o e f 2 ^ { * } X + c o e f 3 ^ { * } X ^ { 2 } + c o e f 4 ^ { * } X ^ { 3 }
$$  

Where:  

$x$ $\mathbf { \tau } = \mathbf { \tau }$ Suction flow rate (volumetric or mass) Y $\mathbf { \tau } = \mathbf { \tau }$ Pressure change  

curve Curve number  

COEF1 First coefficient of delp versus flow polynomial  

COEF2 Second coefficient of delp versus flow polynomial  

COEF3 Third coefficient of delp versus flow polynomial  

COEF4 . Fourth coefficient of delp versus flow polynomial  

SURGE. Suction flow rate at which the compressor surges  

STONEWALL. Suction flow rate at which the compressor stonewalls  

EFF-TABLE  

Use to enter values of efficiency versus suction flow rate in a table. You must also specify EFF-NPOINT, EF-FLOW-VAR, and EF-FLOW-UNIT in the PERFOR-PARAM sentence. When performance curves are entered in tabular form, the first point of the table is taken as surge and the last point as stonewall, for a given curve. (See Notes 6, 7 and 9.)  

curve Curve number   
point . Row number within a table   
eff . Efficiency (either polytropic or isentropic, depending on TYPE)   
flow . Suction flow rate (volumetric, mass, specific flow, or flow coefficient)  

EFF-POLY  

Use to enter polynomial coefficients to calculate efficiency as a function of suction flow rate. You must also specify EF-FLOW-VAR and EF-FLOW-UNIT in the PERFOR-PARAM sentence. (See Note 9.) The polynomial used is:  

$$
' = c o e f 1 + c o e f 2 ^ { * } X + c o e f 3 ^ { * } X ^ { 2 } + c o e f 4 ^ { * } X ^ { 3 }
$$  

Where:  

$x$ $\mathbf { \tau } = \mathbf { \tau }$ Suction flow rate (volumetric, mass, specific flow, or flow coefficient) $\mathbf { \tau } = \mathbf { \tau }$ Efficiency  

curve Curve number  

COEF1 First coefficient of efficiency versus flow polynomial  

COEF2 Second coefficient of efficiency versus flow polynomial  

COEF3 Third coefficient of efficiency versus flow polynomial  

COEF4 . Fourth coefficient of efficiency versus flow polynomial  

SHAFT-SPEED  

Use to enter compressor shaft speeds when multiple performance curves, at multiple shaft speeds, are available. (See Note 10.)  

curve Curve number shaft-speed... Shaft speed  

MACH-NO  

Use to enter Mach numbers when multiple performance curves, at multiple Mach numbers, are available. (See Note 11.)  

curve Curve number mach-no . Mach number  

HEAD-CORR  

Use to enter polynomial coefficients to calculate head developed as a function of suction flow rate and shaft speed. You must also specify H-FLOW-VAR and H-FLOW-UNIT in the PERFOR-PARAM sentence. (See Note 6.) The polynomial used is:  

Y $= c o e f { \cal I } + c o e f { 2 } ^ { * } { \cal N } + c o e f { 3 } ^ { * } { \cal N } ^ { 2 } + c o e f { 4 } ^ { * } { \cal X } + c o e f { 5 } ^ { * } { \cal X } ^ { 2 } + c o e f { 6 } ^ { * } ( { \cal X } / { \cal N } ) + c o e f { 7 } ^ { * } ( { \cal X } / { \cal N } ) ^ { 2 } + \frac { 1 } { 2 } \frac { f ^ { 2 } } { \cal U } ,$ coef8\*X4  

Where:  

$N$ $\mathbf { \tau } = \mathbf { \tau }$ Shaft speed $x$ $\mathbf { \tau } = \mathbf { \tau }$ Suction volumetric flow rate Y $\mathbf { \tau } = \mathbf { \tau }$ Head developed  

COEF1 First coefficient of head versus flow correlation COEF2 Second coefficient of head versus flow correlation COEF3 . Third coefficient of head versus flow correlation COEF4 .. Fourth coefficient of head versus flow correlation COEF5 . Fifth coefficient of head versus flow correlation COEF6 . Sixth coefficient of head versus flow correlation COEF7 Seventh coefficient of head versus flow correlation COEF8 . Eighth coefficient of head versus flow correlation  

EFF-CORR  

Use to enter polynomial coefficients to calculate efficiency as a function of suction flow rate and shaft speed. You must also specify EF-FLOW-VAR and EF-FLOW-UNIT in the PERFORPARAM sentence. (See Note 9.) EFF-CORR is allowed only if HEAD-CORR is specified. The polynomial used is:  

Y = coef1 + coef2\*N + coef3\*N2 + coef4\*X + coef5\*X2 + coef6\*(X/N) + coef7\*(X/N)2 + coef8\*X4  

Where:  

N $\mathbf { \tau } = \mathbf { \tau }$ Shaft speed   
$x$ $\mathbf { \tau } = \mathbf { \tau }$ Suction volumetric flow rate   
Y $\mathbf { \tau } = \mathbf { \tau }$ Efficiency  

COEF1 First coefficient of efficiency versus flow correlation COEF2 . Second coefficient of efficiency versus flow correlation COEF3 ... Third coefficient of efficiency versus flow correlation COEF4 .. Fourth coefficient of efficiency versus flow correlation COEF5 .. Fifth coefficient of efficiency versus flow correlation COEF6 ... Sixth coefficient of efficiency versus flow correlation COEF7 . Seventh coefficient of efficiency versus flow correlation COEF8 . Eighth coefficient of efficiency versus flow correlation  

SURGE-POLY  

Use to enter polynomial coefficients to calculate surge volumetric flow rate as a function of shaft speed. You can specify SURGE-UNITS and SG-SP-UNIT in the PERFOR-PARAM sentence. SURGE-POLY is allowed only if HEAD-CORR is specified. The polynomial used is:  

$$
\textsf { Y } = c o e f \thinspace 1 \thinspace + c o e f { 2 ^ { * } } N \thinspace + c o e f { 3 ^ { * } } N ^ { 2 }
$$  

Where:  

$N$ $\mathbf { \sigma } = \mathbf { \sigma }$ Shaft speed $\boldsymbol { Y }$ $\mathbf { \tau } = \mathbf { \tau }$ Surge volumetric flow rate  

COEF1 First coefficient of surge volumetric flow rate polynomial  

COEF2 Second coefficient of surge volumetric flow rate polynomial  

COEF3 . Third coefficient of surge volumetric flow rate polynomial  

PLOSS-POLY  

Use to enter polynomial coefficients to calculate power loss as a function of suction flow rate and shaft speed. You can specify PLOSS-UNITS, PL-FLOW-UNIT, and PL-SP-UNIT in the PARAM sentence. (See Note 3.) The polynomial used is:  

$$
Y = c o e f \ - { \cal { I } } + c o e f { \ o { 2 ^ { * } } { X } } N ^ { 2 } + c o e f { \ o { 3 ^ { * } } { ( X ^ { * } N ) ^ { 2 } } }
$$  

Where:  

$N$ $\mathbf { \tau } = \mathbf { \tau }$ Shaft speed   
$x$ $\mathbf { \tau } = \mathbf { \tau }$ Suction volumetric flow rate   
Y $\mathbf { \tau } = \mathbf { \tau }$ Power loss  

COEF1 First coefficient of power loss polynomial  

COEF2 Second coefficient of power loss polynomial  

COEF3 Third coefficient of power loss polynomial  

SUBROUTINE  

Use to specify user-supplied subroutine for calculating performance curves. You must specify the type of curve using the USER-CURVES keyword in the PERFOR-PARAM sentence. The user subroutine must also calculate efficiency, whenever it is used to calculate any other performance variable. See Aspen Plus User Models, Chapter 22, for information about writing user-supplied subroutines for performance curves.  

CURVES. Name of user-supplied FORTRAN subroutine for performance curve calculations  

USER-VECS  

Use to define the length of arrays for user-supplied performance curve subroutines.  

NINT Length of integer parameter array for the user-supplied performance curve subroutine   
NREAL Length of real parameter array for the user-supplied performance curve subroutine   
NIWORK Length of integer workspace array for the user-supplied performance curve subroutine   
NWORK . Length of real parameter array for the user-supplied performance curve subroutine  

INT  

Use to enter values for the integer parameter array of the user-supplied performance curve subroutine.  

value-list . List of integer values  

REAL  

Use to enter values for the real parameter array of the user-supplied performance curve subroutine.  

value-list .. List of real values  

UTILITY  

Use to specify an optional utility to provide heating or cooling duty.  

UTILITY-ID ... Utility ID.  

# Accessing Variables in COMPR  

Many Aspen Plus features enable you to sample or change block variables. Chapter 29 describes how to access variables. The following tables list variable names and other information needed to sample and/or change variables for a COMPR block.  

Block Input   


<html><body><table><tr><td colspan="2">BiockTnput</td><td colspan="2"></td></tr><tr><td>Sentence</td><td>Variables</td><td>ID1</td><td>ID2</td></tr><tr><td>PARAM</td><td>PRES，DELP，PRATIO，POWER，TEMP，PEFF，SEFF，MEFF, CLFR，SB-MAXIT，SB-TOL,MAXIT,TOL，PLOSS-FACTOR, PLOSS-OFFSET，PRAT-STEP，PRAT-FINAL</td><td></td><td></td></tr><tr><td>PERFOR-PARAM</td><td>SUCT-NOZ-DIA, SUCT-K-FACT,ACT-SH-SPEED, IMPELLER-DIA，REF-SH-SPEED，FANEXPH，FANEXPE FANEXPP，HEAD-FACTOR,HEAD-OFFSET, HEADC-FACTOR,HEADC-OFFSET,POWER-FACTOR, POWER-OFFSET，PRES-FACTOR,PRES-OFFSET, PRAT-FACTOR，PRAT-OFFSET,DELP-FACTOR, DELP-OFFSET，EFF-FACTOR，EFF-OFFSET, SURGE-FACTOR，SURGE-OFFSET，GEAR-RATIO, TIN-DESIGN,PIN-DESIGN</td><td></td><td></td></tr><tr><td>HEAD-TABLE</td><td>HEAD,FLOW</td><td>curve</td><td>point</td></tr><tr><td>HEAD-POLY</td><td>COEF1，COEF2，COEF3，COEF4，SURGE，STONEWALL</td><td>curve</td><td></td></tr><tr><td>HEADC-TABLE</td><td>HEAD-COEF，FLOW</td><td>curve</td><td>point</td></tr><tr><td>HEADC-POLY</td><td>COEF1，COEF2，COEF3，COEF4，SURGE，STONEWALL</td><td>curve</td><td></td></tr><tr><td>POWER-TABLE</td><td>POWER，FLOW</td><td>curve</td><td>point</td></tr><tr><td>POWER-POLY</td><td>COEF1，COEF2，COEF3，COEF4，SURGE，STONEWAL</td><td>curve</td><td></td></tr><tr><td>PRES-TABLE</td><td>PRES，FLOW</td><td>curve</td><td>point</td></tr><tr><td>PRES-POLY</td><td>COEF1，COEF2，COEF3，COEF4，SURGE，STONEWALL</td><td>curve</td><td></td></tr><tr><td>PRATIO-TABLE</td><td>PRATIO，FLOW</td><td>curve</td><td>point</td></tr><tr><td>PRATIO-POLY</td><td>COEF1，COEF2，COEF3，COEF4，SURGE，STONEWALL</td><td>curve</td><td></td></tr><tr><td>DELP-TABLE</td><td>DELP，FLOW</td><td>curve</td><td>point</td></tr><tr><td>DELP-POLY</td><td>COEF1，COEF2，COEF3，COEF4，SURGE，STONEWALL</td><td>curve</td><td></td></tr><tr><td>EFF-TABLE</td><td>EFFICIENCY，FLOW</td><td>curve</td><td>point</td></tr><tr><td>EFF-POLY</td><td>COEF1，COEF2，COEF3，COEF4</td><td>curve</td><td></td></tr><tr><td>SHAFT-SPEED</td><td>SHAFT-SPEED</td><td>curve</td><td></td></tr><tr><td>MACH-NO</td><td>MACH-NO COEF1,COEF2,COEF3,COEF4,COEF5,COEF6,COEF7,</td><td>curve</td><td></td></tr><tr><td>HEAD-CORR</td><td>COEF8</td><td></td><td></td></tr><tr><td>EFF-CORR</td><td>COEF1，COEF2,COEF3,COEF4,COEF5,COEF6,COEF7, COEF8</td><td></td><td></td></tr><tr><td>SURGE-POLY</td><td>COEF1，COEF2，COEF3</td><td></td><td></td></tr><tr><td>PLOSS-POLY</td><td>COEF1,COEF2，COEF3</td><td></td><td></td></tr></table></body></html>  

Block Results   


<html><body><table><tr><td>Description</td><td>Sentence</td><td>Variable</td></tr><tr><td>Indicated horsepower</td><td>RESULTS</td><td>IND-POWER</td></tr><tr><td>Brakehorsepower</td><td>RESULTS</td><td>BRAKE-POWER</td></tr><tr><td>Net work</td><td>RESULTS</td><td>NET-WORK</td></tr><tr><td>Power loss</td><td>RESULTS</td><td>POWER-LOSS</td></tr><tr><td>Polytropicefficiency</td><td>RESULTS</td><td>PEFF-CALC</td></tr><tr><td>Volumetric efficiency</td><td>RESULTS</td><td>VEFF-CALC</td></tr><tr><td>Mechanical efficiency</td><td>RESULTS</td><td>MEFF-CALC</td></tr><tr><td>Isentropic temperature</td><td>RESULTS</td><td>ISENTR-TEMP</td></tr><tr><td>Idealheaddeveloped</td><td>RESULTS</td><td>HEAD-CAL</td></tr><tr><td>Actual head developed</td><td>RESULTS</td><td>HEAD-ACT</td></tr><tr><td>Isentropic powerrequirement</td><td>RESULTS</td><td>ISEN-POWER</td></tr><tr><td>Outlet pressure</td><td>RESULTS</td><td>OUT-PRES-CAL</td></tr><tr><td>Outlet temperature</td><td>RESULTS</td><td>OUT-TEMP-CAL</td></tr><tr><td>Inlet heat capacityratio</td><td>RESULTS</td><td>IN-CPR</td></tr><tr><td>Inletvolumetric flowrate</td><td>RESULTS</td><td>VFLOW-IN</td></tr><tr><td>Outletvolumetricflowrate</td><td>RESULTS</td><td>VFLOW-OUT</td></tr><tr><td>Inletcompressibilityratio</td><td>RESULTS</td><td>Z-IN</td></tr><tr><td>Outletcompressibilityratio</td><td>RESULTS</td><td>Z-OUT</td></tr><tr><td>Averageisentropicvolumeexponent</td><td>RESULTS</td><td>EXP-V-ISEN</td></tr><tr><td>Averageactual volume exponent</td><td>RESULTS</td><td>EXP-V-POLY</td></tr><tr><td>Average isentropic temperature exponent</td><td>RESULTS</td><td>EXP-T-ISEN</td></tr><tr><td>Average actual temperature exponent</td><td>RESULTS</td><td>EXP-T-POLY</td></tr><tr><td>Percent above surge</td><td>PERF-RESULTS</td><td>ABOVE-SURGE</td></tr><tr><td>Percent belowstonewall</td><td>PERF-RESULTS</td><td>BELOW-SWALL</td></tr><tr><td>Surge volumetric flow rate</td><td>PERF-RESULTS</td><td>SURGE-VOLUME</td></tr><tr><td>Stonewallvolumentric flowrate</td><td>PERF-RESULTS</td><td>SWALL-VOLUME</td></tr><tr><td>Calculatedcompressorshaftspeed</td><td>PERF-RESULTS</td><td>SHAFT-SPEED</td></tr><tr><td>Specific shaft speed</td><td>PERF-RESULTS</td><td>SP-SPEED</td></tr><tr><td>Sonicvelocityof gasat suction</td><td>PERF-RESULTS</td><td>SUCT-SONIC-V</td></tr><tr><td>Specificdiameter</td><td>PERF-RESULTS</td><td>SP-DIAM</td></tr><tr><td>Headcoefficient</td><td>PERF-RESULTS</td><td>HEAD-COEF</td></tr><tr><td>Flowcoefficient</td><td>PERF-RESULTS</td><td>FLOW-COEF</td></tr><tr><td>InletMachnumber</td><td>PERF-RESULTS</td><td>IN-MACH-NO</td></tr><tr><td>Rotor tip Machnumber</td><td>PERF-RESULTS</td><td>RT-MACH-NO</td></tr><tr><td>Calculated power correction factor used PERF-RESULTS inoff-designadjustment</td><td></td><td>POWER-FACTOR</td></tr><tr><td>Specified or calculated gear ratio between the driverand the compressor</td><td>PERF-RESULTS</td><td>GEAR-RATIO-C</td></tr></table></body></html>  
