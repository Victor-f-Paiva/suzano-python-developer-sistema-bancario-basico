def validate_cpf(cpf):
    # Simple validation of format (11 chars)
    return cpf.isdigit() and len(cpf) == 11
