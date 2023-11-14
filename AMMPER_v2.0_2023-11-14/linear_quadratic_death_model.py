from cellDefinition import Cell

import random

def determine_cell_state(cell: Cell):
    """
    Determines the state of a cell based on the number of Double-Strand Breaks (DSBs).

    Args:
        cell (Cell): The cell object to analyze.

    Returns:
        Cell: The updated cell object after determining its state.
    """
    num_DSBs = cell.numDSBs
    print(f"Number of DSBs: {num_DSBs}")

    if num_DSBs == 0:
        return cell
    
    # Define probabilities for different states
    probabilities = {
        "Simple": 0.4,
        "Complex": 0.3,
        "Clustered/Claustrophobic": 0.2,
        "Below G2/M Checkpoint Threshold": 0.1
    }
    
    # Determine the cell state based on probabilities
    cell_state = cell.cell_state = random.choices(list(probabilities.keys()), list(probabilities.values()))[0]
    
    # Handle repair or misrepair based on the cell state
    if cell_state == "Simple":
        """
        TODO: If you repair, include the probability of misrepair/successful repair
        TODO: Chromosone abberation leads to death
        """
        repair_probability = 0.8  # Probability of successful repair
        if random.random() < repair_probability:
            cell = cell.cellRepair(None)
        else:
            cell.health = 2
        
    if cell_state == "Complex":
        # Cell cycle delay, skip a generation
        cell.skip_generation = True
    
    if cell_state == "Clustered/Claustrophobic":
        cell.health = 3
    
    if cell_state == "Below G2/M Checkpoint Threshold":
        cell.health = 3
    
    return cell