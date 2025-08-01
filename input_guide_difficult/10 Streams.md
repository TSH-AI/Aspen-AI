# 10 Streams

This chapter describes the input language used to:  

Specify conventional material streams.   
Define and modify general material streams (stream classes, substream classes, and substream attributes).   
Specify general material streams (consisting of any combination of MIXED, CISOLID, and NC substreams, and substream attributes).   
Specify heat and work streams.  

# Specifying Conventional Material Streams  

Input Language for STREAM STREAM sid     keyword $\mathbf { \bar { \rho } } = \mathbf { \rho }$ value  

Keywords:  

TEMP PRES VFRAC basis-FLOW Optional keywords:  

NPHASE   PHASE   SOLVENT   FREE-WATER   MAXIT   TOL   FLASH-OPTION VOL-TREF   CONC-TREF  

basis–FLOW cid flow  / basis–FRAC cid frac  / basis-CONC cid conc  /  . .  

# Input Language Description for STREAM  

Use STREAM paragraphs to define the flow rates, composition, and thermodynamic condition of each process feed stream. Optionally, STREAM paragraphs can provide initial guesses for tear streams.  

sid.. Stream ID   
TEMP. Temperature   
PRES . Pressure   
VFRAC. ...  Molar vapor fraction   
basis–FLOW .. Flow rate on a MOLE, MASS, STDVOL (standard-liquid volume) or VOLUME basis   
NPHASE Number of phases:  

NPHASE $\mathbf { \lambda = 1 }$ One-phase calculation NPHASE $\scriptstyle = 2$ Two-phase flash (Default) NPHASE $= 3$ Three-phase flash  

PHASE. Specifies the phase when NPHASE ${ \bf \varepsilon } = { \bf 1 }$ :  

PHASE=V Vapor (Default) PHASE=L Liquid PHASE $\mathbf { \sigma } = \mathbf { 5 }$ Solid. Use for electrolytes system only.  

SOLVENT. Component ID of solvent. Use only when basis-CONC is specified.  

FREE–WATER .. Use to override the free-water option established by the SIMOPTIONS paragraph. (See Chapter 45.) FREE–WATER $\mathop { : = }$ NO Does not perform free-water calculations (Default) FREE–WATER $\mathbf { \lambda } =$ YES Performs free-water calculations   
MAXIT Maximum number of flash iterations. (Default $\ c =$ value established by the SIM-OPTIONS paragraph.) (See Chapter 45.)  

TOL Flash convergence tolerance. (Default $\mathbf { \sigma } =$ value established by the SIM-OPTIONS paragraph.) (See Chapter 45.)  

FLASH–OPTION.. FLASH-OPTION $\mathbf { \tau } =$ NOFLASH Suppresses the flash calculation (Default $\ c =$ performs flash calculations)  

VOL-TREF. Reference temperature for volume flows  

CONC-TREF . Reference temperature for component concentration  

basis-FLOW  

Use to enter component flows on a MOLE, MASS, or STDVOL basis. If you specify component flows, the total flow is also specified. The component flows are then normalized.  

cid. Component ID (or an assay ID). (See Chapter 7.)  

flow . Component MOLE, MASS, or STDVOL flow rate  

basis-FRAC  

Use to enter component fractions on a MOLE, MASS, or STDVOL basis. You must also specify the total flow using the basis-FLOW tertiary keyword.  

cid. Component ID (or an assay ID). (See Chapter 7.)  

frac . Component MOLE, MASS, or STDVOL fraction  

basis-CONC  

Use to enter component concentration on a MOLE or MASS basis. You must also specify SOLVENT.  

cid. Component ID conc Component concentration  

# Defining General Material Stream Classes  

# Input Language  

DEF-STREAM-CLASS sclass ssid-list DEF-SUBS ssclass ssid DEF-SUBS-CLASS ssclass DEF keyword $\circleddash$ value  

Keywords: TYPE ATTR  

DEF-SUBS-ATTR psdid PSD INTERVALS n SIZE-LIMITS limit1 / . . . / . . . limit n+1  

# Input Language Description for DEF-STREAM-CLASS  

Use the DEF-STREAM-CLASS paragraph to define new stream classes that are not built into the system. (See Table 10.1 for built-in substream classes.) sclass. Stream class. (See Table 10.2.) ssid-list.. Substream ID list. MIXED must be the first substream ID.  

# Input Language Description for DEF-SUBS  

Use the DEF-SUBS paragraph to assign a substream ID to a substream class.  

ssclass . Substream class  

ssid Substream ID  

# Input Language Description for DEF-SUBS-CLASS  

Use the DEF-SUBS-CLASS paragraph to create a new substream class (that is, to associate a substream type with a particle size distribution).  

ssclass Substream class TYPE . Substream type (CISOLID or NC) ATTR . Particle size distribution ID  

# Input Language Description for DEF-SUBS-ATTR  

Use the DEF-SUBS-ATTR paragraph to specify size limits for the particle size distribution (PSD). This paragraph is used only with stream classes MIXCIPSD or MIXNCPSD.  

psdid. Particle size distribution ID  

INTERVALS  

Use to specify the number of discrete intervals in which to divide the particle size distribution  

Number of intervals  

SIZE-LIMITS  

Use to specify size limits for the discrete intervals. You must enter $\mathsf { n } { + } \mathsf { 1 }$ values, in ascending order, and separated by slashes.  

limit Size limit  

Table 10.1 Built-In Substream Classes   


<html><body><table><tr><td>Substream class</td><td>Substream ID</td><td>Substream type</td><td>Substream attribute ID</td></tr><tr><td>MIXED</td><td>MIXED</td><td>MIXED</td><td></td></tr><tr><td>CISOLID</td><td>CISOLID</td><td>CISOLID</td><td>二</td></tr><tr><td>NC</td><td>NC</td><td>NC</td><td></td></tr><tr><td>NCPSD</td><td>NCPSD</td><td>NC</td><td>PSD</td></tr><tr><td>CIPSD</td><td>CIPSD</td><td>CISOLID</td><td>PSD</td></tr></table></body></html>  

Table 10.2 Built-In Material Stream Classes   


<html><body><table><tr><td>Stream class</td><td>Numberof substreams</td><td>Substream type(s)</td><td>Substream ID(s)</td></tr><tr><td>CONVEN</td><td>1</td><td>MIXED</td><td>MIXED</td></tr><tr><td>MIXCISLD</td><td>2</td><td>MIXED,CISOLID</td><td>MIXED,CISOLID</td></tr><tr><td>MIXNC</td><td>2</td><td>MIXED,NC</td><td>MIXED,NC</td></tr><tr><td>MIXCINC</td><td>3</td><td>MIXED,CISOLID，</td><td>MIXED,CISOLID，N</td></tr><tr><td>MIXCIPSD</td><td>2</td><td>MIXED,CISOLID</td><td>MIXED,CIP</td></tr><tr><td>MIXNCPSD</td><td>2</td><td>MIXED,NC</td><td>MIXED，NP</td></tr><tr><td>MCINCPSD</td><td>3</td><td>MIXED,CISOLID，N</td><td>MIXED,CIPSD,NCP</td></tr></table></body></html>  

# Specifying General Material Streams  

Input Language  

ALL DEF-STREAMS sclass secid − list sid − list STREAM sid SUBSTREAM ssid keyword=value  

Keywords:  

TEMP PRES VFRAC basis-FLOW Optional keywords:  

NPHASE PHASE SOLVENT FREE-WATER MAXIT TOL FLASH-OPTION  

basis-FLOW cid flow /   
basis–FRAC cid frac  /  .   
basis-CONC cid conc  /  . .   
COMP-ATTR cid cattrname (value-list) SUBS-ATTR psdid (value-list)  

# Input Language Description for DEF-STREAMS  

Use the DEF-STREAMS paragraph to assign a stream class to a list of streams or to all the streams within flowsheet sections. (See Chapter 9.) There can be any number of DEF-STREAMS paragraphs. If you enter more than one DEFSTREAMS paragraph, the more general specifications should precede the more specific specifications. If you specify ALL, it must be in the first DEF-STREAMS paragraph for any streams in that section.  

sclass Stream class. (See Table 10.2.)   
ALL All streams in the flowsheet that are assigned to a specified stream class   
secid-list . List of flowsheet section IDs   
sid-list . List of stream IDs  

# Input Language Description for STREAM  

SUBSTREAM  

Use the STREAM paragraph to specify inlet streams and initial guesses for tear streams.  

sid. Stream ID  

Use to enter state and flash specifications for substreams. For solid substreams, you must specify TEMP and PRES. The pressure of all substreams must be the same. For most applications the temperature of all substreams should be the same. RPLUG is the only Aspen Plus unit operation model that can treat a stream with substreams at different temperatures. Specify NPHASE and PHASE for the MIXED substream only. (See Table 10.3 for built-in substreams.)  

ssid Substream ID  

TEMP. Temperature   
PRES . Pressure   
VFRAC. Molar vapor fraction (for MIXED substreams only)   
basis-FLOW.. Flow rate on a MOLE, MASS, or STDVOL basis   
NPHASE Number of phases in MIXED substream:  

NPHASE $\mathbf { \lambda = 1 }$ One-phase calculation NPHASE $\scriptstyle = 2$ Two-phase flash (Default) NPHASE $= 3$ Three-phase flash  

PHASE. Specifies the phase when NPHASE ${ \tt = } 1$ :  

PHASE $\mathbf { \tau } = \mathbf { \boldsymbol { v } }$ Vapor   
PHASE $\mathbf { \sigma } = \mathbf { L }$ Liquid   
PHASE $\mathbf { \sigma } = \mathbf { 5 }$ Solid. Use for electrolytes system only.  

SOLVENT. Component ID of solvent. Use only when basis-CONC is specified.  

FREE–WATER . Use to override the free-water option established by the SIMOPTIONS paragraph. (See Chapter 45.) FREE–WATER $\mathbf { \lambda } =$ NO Does not perform free-water calculations (Default) FREE–WATER $\mathbf { \lambda } =$ YES Performs free-water calculations  

MAXIT Maximum number of flash iterations. (Default $\ c =$ value established by the SIM-OPTIONS paragraph.) (See Chapter 45.)  

TOL Flash convergence tolerance. (Default $\mathbf { \sigma } =$ value established by the SIM-OPTIONS paragraph.) (See Chapter 45.)  

FLASH-OPTION .. FLASH-OPTION $\mathbf { \tau } =$ NOFLASH Suppresses the flash calculation (Default $\ c =$ performs flash calculations)  

basis-FLOW  

Use to enter component flow rates on a MOLE, MASS, or STDVOL basis. For substreams of type NC, only MASS basis is allowed. For substream of type CISOLID, only MOLE or MASS basis are allowed. If the basis-FLOW tertiary keyword is specified, the component flows are normalized.  

cid. Component ID flow . Component flow rate  

basis-FRAC  

Use to enter component fractions on a MOLE, MASS, or STDVOL basis. For substreams of type NC, only MASS basis is allowed. For substream of type CISOLID, only MOLE or MASS basis are allowed. You must specify the total flow using the basis-FLOW tertiary keyword.  

cid. Component ID frac . Component fraction  

basis-CONC  

Use to enter component concentration on a MOLE or MASS basis. For substreams of type NC, only MASS basis is allowed.  

cid. Component ID conc Component concentration  

COMP-ATTR  

Use to enter component attributes for substreams of type NC. There should be one COMPATTR sentence for each component attribute specified.  

cid. Component ID cattrname . Component attribute name value-list List of attribute values. You should enter all values for the attribute, even if zero.  

Use to enter particle size distribution values for substreams that have a particle size distribution attribute.  

psdid. Particle size distribution ID value-list List of substream weight fractions that lie within each particle size distribution interval  

Table 10.3 Types of Substreams   


<html><body><table><tr><td colspan="2">This substream type Handles</td></tr><tr><td>MIXED</td><td>Conventional components that participate in vapor-liquid-solid phase equilibrium</td></tr><tr><td>CISOLID</td><td>Conventional components that appear in the solid phase but do not</td></tr><tr><td>(Conventional inert solids) participate in phase equilibrium NC (Nonconventional)</td><td>Nonconventional components</td></tr></table></body></html>  

# Specifying Heat And Work Streams  

Input Language  

DEF-STREAMS HEAT sid-list DEF-STREAMS WORK sid-list STREAM sid INFO HEAT keyword=value  

Keywords:  

DUTY TEMP TEND  

STREAM sid  
INFO LOAD TVEC=t1  t2  t3  t4 QVEC $\backslash =$ q1  q2  q3  q4  
STREAM sid  
INFO WORK POWER $\mathbf { \lambda } =$ power  

# Input Language Description  

Use the DEF-STREAMS paragraph to define streams to be heat streams or work streams. Use the STREAM paragraph to enter the heat and work loads. Heat streams allow heat duties to pass from one process to another. Load streams are heat streams which include vectors describing the temperatures at which the heat was transferred. Work streams are similar to heat streams, except work streams carry information about power.  

sid-list . List of all heat or work streams used in a simulation  

sid. Heat or work stream ID   
DUTY. Enthalpy flow rate   
TEMP.. Starting temperature of a heat or load stream   
TEND... Ending temperature of a heat or load stream   
t1, t2, t3, t4 .. Temperature vector of a load stream   
q1, q2, q3, q4.. Duty vector of a load stream   
POWER Power  

# Specifying Stream Names  

Input Language for STREAM-NAMES  

STREAM-NAMES NAMES sid   text  

# Input Language Description  

Use the STREAM-NAMES paragraph to specify description for streams. sid. Stream id  

text . A string of any length enclosed in quotes. The description is printed under the Stream ID (up to 3 lines, each line is a maximum of 10 chars wide) in the STREAM-REPORT.  