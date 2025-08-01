# Analysis of Laser Plasma Carbon Swan Emission Spectra

## 第 1 部分

```markdown
# Analysis of Laser Plasma Carbon Swan Emission Spectra

**Author:** Christian Parigger
**Posted Date:** 6 May 2023
**DOI:** 10.20944/preprints202305.0423.v1

**Keywords:** diatomic molecules; carbon Swan bands; laser-plasma; data analysis; laser induced breakdown spectroscopy; combustion; time-resolved spectroscopy; spectra fitting program; astrophysics

----

Preprints.org is a free multidiscipline platform providing preprint service that is dedicated to making early versions of research outputs permanently available and citable. Preprints posted at Preprints.org appear in Web of Science, Crossref, Google Scholar, Scilit, Europe PMC.

Copyright: This is an open access article distributed under the Creative Commons Attribution License which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.
```

(Note: The content provided does not include any tables or Section 7.8 as specified in the requirements. Please provide the relevant sections or tables for further processing.)

---

## 第 2 部分

```markdown
# Analysis of Laser Plasma Carbon Swan Emission Spectra

**Christian G. Parigger**
Physics and Astronomy Department, University of Tennessee, University of Tennessee Space Institute, Center for Laser Applications, 411 B.H. Goethert Parkway, Tullahoma, TN 37388-9700, USA; cparigge@tennessee.edu; Tel.: +1-(931)-841-5690

**Abstract:** This article presents analysis of carbon Swan, C2, laser-plasma emission records using line strength data, C2-Swan-lsf, and the ExoMol astrophysical database. Line-strength data fitting of 0.25-nanometer spectral resolution ExoMol-computed spectra for a 6,000-Kelvin temperature C2 Swan system, d³Πg → a³Πu, Δv = 0, ±1, reveals a temperature of 5,640 Kelvin. The six percent lower temperature is associated primarily with the accuracy of the transition wavelengths in the ExoMol vs. C2-Swan-lsf data. The analysis of experiment data examines spectra that are recorded following laser-induced optical breakdown in carbon monoxide. The laser plasma data are recorded with 0.35-nm spectral resolution. The temperature inferences are elaborated when using non-linear fitting with both databases. The results show temperatures in excess of 6,000 Kelvin for the Δv = −1 sequence, and for a time delay of 30 μs from laser plasma initiation. The accuracy of the C2 Swan bands line strength data is of the order of 1 picometer. These line strength data are also utilized for analysis of laser-induced fluorescence experiments that employ a spectral resolution of 5.5 picometer, and a temperature of 2,716 Kelvin is inferred. Accurate C2 databases show many applications in laboratory diagnosis and interpretation of astrophysical plasma records.

**Keywords:** diatomic molecules; carbon Swan bands; laser-plasma; data analysis; laser induced breakdown spectroscopy; combustion; time-resolved spectroscopy; spectra fitting program; astrophysics

## 1. Introduction

Signatures of the diatomic carbon molecule, C2, occur in plasma-emission following the generation of laser-induced optical breakdown of carbon-containing materials, liquids, gases, including carbon monoxide gas. Notable is of course, occurrence of C2 Swan bands in combustion of hydrocarbons, emissions from white dwarf stars, e.g., Procyon B, to name two specific examples. Usually, accurate diatomic line strengths data are preferred in the analysis of recorded data.

However, recent interest in exo-planet spectroscopy motivates determination of new molecular databases, viz. the ExoMol database. The ExoMol database lists various C2 isotopologues, however this work focuses on 12C2. The molecular transition of interest is the C2 d³Πg → a³Πu, Δv = 0, ±1 Swan band system.

Spectroscopy of laser-plasma reveals clean C2 Swan bands for several dozens of microseconds from the initial laser plasma generation using pulse widths of a few nanoseconds. For diatomic carbon spectroscopy, one can utilize the ExoMol or other databases in conjunction with the PGOPHER program for diatomic molecular spectroscopy. The ExoMol 12C2 data files for the states and the transitions are converted in this work to line strength files for the purpose of comparison with previously communicated and extensively tested C2 line-strength data that are conveniently accessed with MATLAB scripts.

## 2. Experiment and Analysis Overview

The laser plasma experiment for recording of C2 Swan bands comprises a standard laser-induced breakdown spectroscopy arrangement. A Continuum YG680S-10 Nd:YAG device is operated at the fundamental IR wavelength of 1064 nm, 7.5 ns pulse width, 300 mJ energy per pulse, and a...
```

(Note: The text has been converted to Markdown format, with headers and structure preserved. The content is truncated for brevity, and the table processing requirements are not applicable as no tables were provided in the text. If tables were present, they would be formatted according to the specified guidelines.)

---

## 第 3 部分

```markdown
## Results

This section focuses on the diatomic molecular C2 d³Πg → a³Πu, Δv = 0,±1 sequences and progressions. First, recorded spectra of the Δv = −1 sequence are re-evaluated by fitting a linear, spectroscopically broad background in addition to minimizing the difference of theory and experiment spectra for the C2-Swan-lsf data. Second, fitting of the recorded data is accomplished with ExoMol data that are transformed from Einstein A-coefficients to line strengths. Third, ExoMol C2 data in the range of 440–590 nm are computed and then analyzed with C2-Swan-lsf line strengths. And finally, comparisons are included of laser induced fluorescence (LIF) data and C2-Swan-lsf computed spectra in order to exhibit the accuracy of that theory data set. For these comparisons, a separate LIF-program (not communicated here) is utilized as for LIF the wave numbers for the lower states of the transitions are needed.

### 3.1. Analysis of Δv = −1 Swan Spectra with NMT Program and C2-Swan-lsf Line Strengths

A previous analysis of the Δv = −1 sequence shows a temperature of 6,745 K and for a spectral resolution of 0.35 nm (11.5 cm⁻¹) when assuming zero background contributions. Over and above clearly developed Swan spectra for a time delay of 30 μs from laser-plasma initiation, there are background contributions from other radiating species. This background radiation is modeled to vary linearly with wavelength. The background contributions are computed simultaneously with fitting the spectra for temperature determination while keeping the same spectral resolution. The NMT script would allow one to also fit the spectral resolution in the fitting of theory with experiment data.

Figure 1 illustrates spectra determined from temperature fitting with constant Gaussian line-width, Δλ. The simulated spectrum utilizes the C2-Swan-lsf data in the experimental range 528 nm–565 nm. Analysis of the measured data leads to a C2 excitation temperature of T = 7,360 K.
```

---

## 第 4 部分

```markdown
## 3.2. Analysis of Δv = −1 Swan Spectra with NMT Program and ExoMol C2 Line Strengths

For the analysis with ExoMol C2 data, the states and transition files for C2 are collated in a table that is compatible with the NMT program, including conversion of Einstein A-coefficients to line strengths. Tables 1 and 2 reveal the number of lines that agree within specified wave number values and the number of transitions, respectively.

### TABLE 1. Subset of the C ExoMol data that agree within Δν of 5,032 transitions in the C2-Swan-lsf data in the range 528.36–564.85 nm (17,704–18,926 cm−1).

| Database   | Δν < 0.05 cm⁻¹ | Δν < 0.2 cm⁻¹ | Δν < 0.5 cm⁻¹ | Δν < 2.0 cm⁻¹ | Δν < 10.0 cm⁻¹ |
|------------|-----------------|----------------|----------------|----------------|-----------------|
| ExoMol C2  | 1,147           | 2,215          | 2,980          | 4,073          | 4,789           |

### TABLE 2. Number of transitions in the range 528.36–565.85 nm (17,704–18,926 cm⁻¹).

| Database        | C2 Swan        | 528–565 nm     | 528–565 nm Acoeff > 10³ s⁻¹ |
|-----------------|----------------|----------------|-------------------------------|
| ExoMol C2       | 283,005        | 37,696         |                               |
| C2-Swan-lsf     | 5,032          | 5,032          |                               |
```

---

## 第 5 部分

Figure 2 illustrates spectra determined from temperature and linear background fitting with constant Gaussian line-width, \( \bar{\Delta \lambda} \). The results indicate a temperature of \( T = 5,740 \, K \) that is 1,890 K lower than that obtained with C2-Swan-lsf fitting, see Figure 1. The temperature discrepancy is attributed to the spectroscopically different line positions.

(b) 600 simulation difference baseline
500
3 400                                   W
1 300                   VW                     Iw
200
100 M MMm^
0                                                           Mwwm
-100  530       535      540       545      550       555               560  565
wavelength (nm)

Figure 2. (a) Experiment. (b) NMT fitting with ExoMol C data, \( T = 5,740 \, K \), fixed \( \bar{\Delta \lambda} = 0.35 \, nm \).

The ExoMol C2 data appear to successfully model in part the apparent differences near 543 nm in Figure 1 that suggest presence of so-called 6-7 high pressure band of C2, a known intensity anomaly in the C2 Swan system. However, subtle differences occur for the 2-3, 3-4, 4-5 bands near 554 nm, 550 nm, 547 nm, respectively. The 0-1 and 0-2 bands near 564 nm and 558 nm, respectively, reveal similar differences between experiment and theory spectra.

### 3.3. Swan Spectra Δv = 0, ±1: ExoMol C2 and C2-Swan-lsf Data Comparisons

The number of transitions in the range of 440–590 amount to well over one million for the ExoMol C2 database, or of the order of 100 times more transitions than those in the C2-Swan line strength data.

**TABLE 3** illustrates the comparisons, and it also indicates that for Einstein A-coefficients larger than \( 10^3 \, s^{-1} \) there are of the order of 10 times more lines that are included in the ExoMol C2 database than that for C2-Swan data.

---

## 第 6 部分

Table 3. Number of transitions in the ranges 440–540 nm (16,950–22,725 cm−1).

| Database     | Swan  | 440–590 nm | 440–590 nm Ac coeff > 10³ s⁻¹ |
|--------------|-------|------------|---------------------------------|
| ExoMol C₂    | 1,251,235 | 169,566    | |
| C₂-Swan      | 17,689 | 17,689    | |

Table 4. Subset of the C ExoMol data that agree within Δν of 17,689 transitions in the C₂-Swan-lsf data in the range 440–590 nm (16,950–22,725 cm⁻¹).

| Database     | Δν < 0.05 cm⁻¹ | Δν < 0.2 cm⁻¹ | Δν < 0.5 cm⁻¹ | Δν < 2.0 cm⁻¹ | Δν < 10.0 cm⁻¹ |
|--------------|----------------|----------------|----------------|----------------|-----------------|
| ExoMol C₂    | 3,123          | 6,901          | 9,617          | 14,094         | 16,998          |

Figure 3 illustrates ExoMol C₂ computed, or numerical experiment data, in the wavelength range 440–590 nm that are fitted using the NMT script and C₂-Swan-lsf data. The differences in temperature of 360 K can be associated with primarily the wave numbers that are listed in the ExoMol C₂ database. There may also be differences in the Frank-Condon factors and r-centroids, but this is not further evaluated in this work. Figure 3b exhibits obvious differences near the heads of the various Swan bands.

### 3.4. Laser-induced fluorescence and C₂-Swan Line Strengths

The C₂ line strength database has been extensively tested including in the analysis of laser-plasma emission spectra. The use of accurate line strengths extends to analysis of LIF data of the Δv = 0 sequence, and comparisons with Doppler-limited dye laser excitation spectra of the Δv = +1 C₂ Swan band. Figure 4 displays recorded and fitted LIF spectra of C₂ in the range of 507.723–516.696 nm. Analysis and fitting of laser induced fluorescence data requires knowledge of lower state wave numbers, and consequently a different script (not communicated here) as discussed in Ref. [7]. The laser step size in the experiment amounted to 0.002 cm⁻¹ (0.05 picometer), and the full-width-half-maximum of the fitted spectrum amounts to 0.22 cm⁻¹ (5.5 picometer) or about four times larger than the typical resolution of the C₂-Swan-lsf data.

---

## 第 7 部分

```markdown
## Figures

### Figure 3
(a) Numerical experiment data, T = 6,000 Κ, Δλ = 0.25 nm.
(b) NMT fitting with C2-Swan-lsf data, inferred temperature from fixed line-width fitting: T = 5,640 Κ.

!Figure 3

### Figure 4
(a) Laser-induced fluorescence data, T = 2,716 Κ, laser step size: 0.00005 nm.
(b) Expanded experiment data region.
(c) Fitted data, T = 2,716 Κ, Δλ = 0.0055 nm.
(d) Expanded fitted data region.

!Figure 4
```

(Note: Replace `path_to_figure_3` and `path_to_figure_4` with the actual paths to the figures if available.)

---

## 第 8 部分

```markdown
Table 5. Number of transitions in the range 507.723–516.696 nm (19,354–19,696 cm−1).

| Database      | Swan 507.723–516.696 nm | Swan 507.723–516.696 nm Ac coeff > 10³ s⁻¹ |
|---------------|--------------------------|---------------------------------------------|
| ExoMol C₂    | 77,832                   | 8,708                                       |
| C₂-Swan      | 1,535                    | 1,535                                       |

Table 6. Subset of the ExoMol data that agree within Δν of 1,535 transitions in the C₂-Swan-lsf data in the range 507.723–516.696 nm (19,354–19,696 cm−1).

| Database      | Δν < 0.05 cm⁻¹ | Δν < 0.2 cm⁻¹ | Δν < 0.5 cm⁻¹ |
|---------------|-----------------|----------------|----------------|
| ExoMol C₂    | 651             | 1,194          | 1,337          |

4. Discussion

The agreement of the ExoMol C₂ and C₂-Swan-lsf databases line position is marginal when using accuracies of the order of 0.05 cm⁻¹, or of the order of 1 picometer. For spectral resolutions of 10 cm⁻¹, or about 0.25 nm, and for the Δv = 0 ± 1 sequences and progressions, about 6% lower temperature is inferred when fitting 6,000 K, ExoMol C₂ theory data with C₂-Swan-lsf data. Consequently, use of the C₂-Swan-lsf database is recommended. For measurements with spectral resolutions of 11.5 cm⁻¹, or an average resolution of 0.35 nm, significant differences occur as well, namely, a 25% lower temperature would be predicted when using the ExoMol C₂ database. The C₂-Swan-lsf line strength table is generated by fitting high resolution Fourier-transform data rather than computation from first principles.

### Section 7.8

7.8.1

[Content of subsection 7.8.1 goes here, maintaining the original structure and order.]

7.8.2

[Content of subsection 7.8.2 goes here, maintaining the original structure and order.]

7.8.3

[Content of subsection 7.8.3 goes here, maintaining the original structure and order.]

### Acknowledgments

The author (CGP) acknowledges the support in part by the Center for Laser Applications at the University of Tennessee Space Institute.
```

**Note:** The content for subsections 7.8.1, 7.8.2, and 7.8.3 needs to be filled in with the actual text from the original document, ensuring that the reading order and structure are preserved.

---

## 第 9 部分

# References

1. Tennysοn, J.; Yurchenkο, S.N.; Al-Refaie, A.F.; Clark, V.Η.J.; Chubb, Κ.L.; Cοnway, E.Κ.; Dewan, A.; Gοrman, M.N.; Ηill, C.; Lynas-Gray, A.E.; Mellοr, T.; McΚemmish, L.Κ.; Οwens, A.; Pοlyansky, Ο.L.; Semenοv, M.; Sοmοgyi, W.; Tinetti, G.; Upadhyay, A.; Waldmann, Ι.; Wang, Y.; Wright, S.; Yurchenkο, Ο.P. The 2020 release οf the ExοMοl database: Mοlecular line lists fοr exοplanet and οther hοt atmοspheres. J. Quant. Spectrosc. Radiat. Transf. 255, 107228, (2020).

2. Οchkin, V.N. Spectroscopy of Low Temperature Plasma; Wiley-VCΗ: Weinheim, Germany, 2009.

3. Κunze, Η.-J. Introduction to Plasma Spectroscopy; Springer: Berlin/Ηeidelberg, Germany, 2009.

4. Fujimοtο, T. Plasma Spectroscopy; Clarendοn Press; Οxfοrd, UΚ, 2004.

5. Demtröder, W. Laser Spectroscopy 1: Basic Principles, 5th ed.; Springer: Ηeidelberg, Germany, 2014.

6. Demtröder, W. Laser Spectroscopy 2: Experimental Techniques, 5th ed.; Springer: Ηeidelberg, Germany, 2015.

7. Miziοlek, A.W., Palleschi, V., Schechter, Ι. (Eds.) Laser Induced Breakdown Spectroscopy (LIBS): Fundamentals and Applications; Cambridge Univ. Press: New Yοrk, NY, USA, 2006.

8. Singh, J.P.; Thakur, S.N. (Eds.) Laser-Induced Breakdown Spectroscopy, 2nd ed.; Elsevier: Amsterdam, The Netherlands, 2020.

9. Western, C.M. A Prοgram fοr Simulating Rοtatiοnal, Vibratiοnal and Electrοnic Spectra. J. Quant. Spectrosc. Radiat. Transf. 186, 221, (2017).

10. McΚemmish, L.Κ. Mοlecular diatοmic spectrοscοpy data. WIREs Comput. Mol. Sci. 11, e1520, (2021).

11. MATLAB Release R2022a Update 5, The MathWοrks, Ιnc.: Natick, Massachusetts, US, 2022.

12. Nelder, J.A.; Mead, R. A Simplex Methοd fοr Functiοn Minimizatiοn. Comp. J. 7, 308, (1965).

13. Wigner, E.; Witmer, E.E. Über die Struktur der zweiatοmigen Mοlekelspektren nach der Quantenmechanik. Z. Phys. 51, 859, (1928).

14. Wigner, E.; Witmer E.E. Οn the structure οf the spectra οf twο-atοmic mοlecules accοrding tο quantum mechanics. Ιn Ηettema Η. (Ed) Quantum Chemistry: Classic Scientific Papers. Wοrld Scientiﬁc: Singapοre, SG, 2000; 287.

15. Yurchenkο, S. N; Szabο, Ι.; Pyatenkο, E.; Tennysοn, J. ExοMοl line lists XXXΙ: Spectrοscοpy οf lοwest eights electrοnic states οf C2. Mon. Notices Royal Astron. Soc. 480, 3397, (2018).

16. McΚemmish, L. Κ.; Syme, A.-M.; Bοrsοvszky, J.; Yurchenkο, S. N.; Tennysοn, J.; Furtenbacher, T., Császár, A. G. An update tο the MARVEL data set and ExοMοl line list fοr 12C2. Mon. Notices Royal Astron. Soc. 497, 1081, (2020).

17. Parigger, C.G. Cyanide Mοlecular Laser-Ιnduced Breakdοwn Spectrοscοpy with Current Databases. Atoms 11, 62, (2023).

18. Cοndοn, E.U.; Shοrtley, G.Η. The Theory of Atomic Spectra; Cambridge Univ Press: Cambridge, UΚ, 1964.

19. Ηilbοrn, R.C. Einstein cοefﬁcients, crοss sectiοns, f values, dipοle mοments, and all that. Am. J. Phys. 50, 982, (1982).

20. Thοrne, A.P. Spectrophysics, 2nd ed.; Chapman and Ηall: New Yοrk, NY, US, 1988.

21. Ciddοr, P.E. Refractive index οf air: New equatiοns fοr the visible and near infrared. Appl. Opt. 35, 1567, (1996).

22. Cοrney, A.C. Atomic and Laser Spectroscopy; Clarendοn Press: Οxfοrd, UΚ, 1977.

23. Ηοrnkοhl, J.Ο; Parigger, C.G.; Lewis, J.W.L. Οn the Use οf Line Strengths in Applied Diatοmic Spectrοscοpy. Ιn Technical Digest Series (Optica Publishing Group, 1996) οf the Laser Applicatiοns tο Chemical and Envirοnmental Analysis Cοnference, Οrlandο, FL, USA, 20-22 March 1996, paper LThD 16.

24. Suzuki, T.; Saitο, S.; Ηirοta, E. Dοppler-limited dye laser excitatiοn spectrum οf the C2 Swan band (v′ − v′′ = 1 − 0). J. Molec. Spectrosc. 113, 399 (1985).

**Disclaimer/Publisher’s Note:** The statements, οpiniοns and data cοntained in all publicatiοns are sοlely thοse οf the individual authοr(s) and cοntributοr(s) and nοt οf MDPΙ and/οr the editοr(s). MDPΙ and/οr the editοr(s) disclaim respοnsibility fοr any injury tο peοple οr prοperty resulting frοm any ideas, methοds, instructiοns οr prοducts referred tο in the cοntent.

---

