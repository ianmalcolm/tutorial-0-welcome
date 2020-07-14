"""
This module saves a welcome message.
"""
import json

def welcome():
    message = "Welcome to Orquestra!"

    message_dict = {}
    message_dict["message"] = message
    message_dict["schema"] = "message"

    with open("welcome.json",'w') as f:
        f.write(json.dumps(message_dict, indent=2)) # Write message to file as this will serve as output artifact
        
def zquantumtest():

    from zquantum.core.circuit import (build_ansatz_circuit,
                                       load_circuit_template,
                                       load_circuit_template_params,
                                       save_circuit)

    ansatz = load_circuit_template('ansatz.json');
    params = load_circuit_template_params('params.json');
    circuit = build_ansatz_circuit(ansatz, params);
    save_circuit(circuit, 'circuit.json')
