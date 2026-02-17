def is_criticality_balanced(temperature, neutrons_emitted):
    if temperature >= 800:
        return False
    if neutrons_emitted <= 500:
        return False
    if temperature * neutrons_emitted >= 500000:
        return False
    return True

def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    efficiency = (generated_power / theoretical_max_power) * 100
    if efficiency >= 80:
        return 'green'
    if efficiency >= 60:
        return 'orange'
    if efficiency >= 30:
        return 'red'
    return 'black'

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    product = temperature * neutrons_produced_per_second
    lower = threshold * 0.9
    upper = threshold * 1.1
    if product < lower:
        return 'LOW'
    if lower <= product <= upper:
        return 'NORMAL'
    return 'DANGER'
