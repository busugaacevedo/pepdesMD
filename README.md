# Peptide Design MD (pepdesMD)

## Overview
**Peptide Design MD (pepdesMD)** is a Python-based toolkit designed to facilitate the rational design of novel peptides for any target using Molecular Dynamics (MD) simulations. With a focus on peptide and membrane-protein interactions, the toolkit automates key analyses, enabling efficient extraction of insights from MD trajectories and accelerating peptide-based drug discovery.

## Features
- **Structural Analysis**: Compute RMSD, RMSF, and radius of gyration.
- **Hydrogen Bond Analysis**: Identify and track hydrogen bonds throughout the simulation.
- **Clustering**: Group molecular conformations based on structural similarity.
- **Free Energy Landscapes**: Generate and visualize energy profiles from MD trajectories.
- **Multi-Format Support**: Compatible with GROMACS, AMBER, and CHARMM trajectory formats.

## Installation
To install the required dependencies, use:
```bash
pip install -r requirements.txt
```

## Usage
Import the toolkit and analyze your MD trajectory:
```python
from pepdesMD import MDAnalyzer

analyzer = MDAnalyzer("trajectory.xtc", "topology.pdb")
analyzer.compute_rmsd()
analyzer.plot_free_energy_landscape()
```

## Dependencies
- Python 3.x
- MDAnalysis
- MDTraj
- NumPy
- Pandas
- Matplotlib

## Example Notebooks
Check out the `examples/` directory for Jupyter Notebooks demonstrating different analysis techniques.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

## License
This project is licensed under the MIT License.

## Contact
For questions or suggestions, reach out via GitHub Issues or email me at [brandon.usuga@gmail.com].

