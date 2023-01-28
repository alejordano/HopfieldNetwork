# HopfieldNetwork
### Conforte AJ, et al. Modeling Basins of Attraction for Breas Cancer using Hopfield Networks
Codes for Hopfield Network analysis used in Conforte AJ, et al. Published in Frontiers in Genetics - April/2020 <br>
Use it in the following order <br>
1 - func.py. saving objects <br>
2 - data_xlsx.py - Read excel files in control and treated groups. <br>
3 - pacients_formula.py - Classification of patients according to its group and change in data organization.<br>
4 - binarizing.py - Binarizing gene expression values based on the median of each group.<br>
5 - clusters.py - Definition of attractors. PCA analysis<br>
6 - Hopfield_test.py - Tests how many samples converged towards the each attractor.<br>
7 - energy.py - Creating an energy landscape from Hopfield network analysis <br>
8 - density.py - determining patarameters from interactome and density to prioritize targets<br>
9  - go.py - determining parameters from Gene Ontology to prioritize targets. <br>
10 - parameter_conservative.py - determining the number of patients with the same potential target (active in tumor samples and inhibited in control samples)<br>
11 - Intervention_energy.py - Determines the necessary alterations to withdraw samples from a basin of attraction <br>
12 - simulation_trastuzumabe.py - identifies genes with different states between treated and untreated, changes its state following the treated sample
