def mcculloch_pitts(inputs, weights, threshold):
    """McCulloch-Pitts neuron model."""
    assert len(inputs) == len(weights), "Number of inputs must match number of weights"
    return int(sum(x * w for x, w in zip(inputs, weights)) >= threshold)

def test_logic_gate(logic_gate):
    """Test a logic gate using McCulloch-Pitts neuron."""
    print(f"Testing {logic_gate} gate:")

    gate_params = {
        "AND": ([(0, 0), (0, 1), (1, 0), (1, 1)], (1, 1), 2),
        "OR": ([(0, 0), (0, 1), (1, 0), (1, 1)], (1, 1), 1),
        "XOR": ([(0, 0), (0, 1), (1, 0), (1, 1)], [(1, 1), (1, 1), (-1,)], 1),
        "AND NOT": ([(0, 0), (0, 1), (1, 0), (1, 1)], (1, -1), 0),
    }

    if logic_gate in gate_params:
        inputs, weights, threshold = gate_params[logic_gate]

        for input_pair in inputs:
            if logic_gate == "XOR":
                and_result = mcculloch_pitts(input_pair, weights[0], threshold)
                or_result = mcculloch_pitts(input_pair, weights[1], threshold)
                not_result = mcculloch_pitts((and_result,), weights[2], threshold)
                xor_result = mcculloch_pitts((or_result, not_result), weights[0], threshold)
                print(f"{input_pair}: {xor_result}")
            else:
                result = mcculloch_pitts(input_pair, weights, threshold)
                print(f"{input_pair}: {result}")
    else:
        print("Invalid logic gate.")

# Test different logic gates
test_logic_gate("AND")
test_logic_gate("OR")
test_logic_gate("XOR")
test_logic_gate("AND NOT")
