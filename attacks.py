import json
import random

def load_json_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def get_random_attack(attacks):
    return random.choice(attacks)

def format_data_sources(data_sources):
    if isinstance(data_sources, list):
        return '\n'.join(f"- {source}" for source in data_sources)
    else:
        return f"- {data_sources}"

def display_group_profile(group_attacks):
    attacks_by_phase = {}
    for attack in group_attacks:
        phase = attack['phase']
        if phase not in attacks_by_phase:
            attacks_by_phase[phase] = []
        attacks_by_phase[phase].append(attack)
    
    for phase in sorted(attacks_by_phase.keys()):
        attack = get_random_attack(attacks_by_phase[phase])
        data_sources_formatted = format_data_sources(attack['data_sources'])
        print(f"Phase: {phase}")
        print(f"Tactic: {attack['tactic']}")
        print(f"Technique: {attack['technique']}")
        print(f"Data Sources:\n{data_sources_formatted}\n")

def main():
    attacks_data = load_json_data('attacks.json')
    while True:
        group_name = input("Enter the name of the threat actor group: ")
        group_attacks = [attack for attack in attacks_data if attack['group'] == group_name]
        
        if not group_attacks:
            user_choice = input("The group you chose is not in the database. Would you like to choose another group? (yes/no) ")
            if user_choice.lower() == 'no':
                break
            else:
                continue
        
        display_group_profile(group_attacks)
        
        user_choice = input("Would you like to choose another group? (yes/no) ")
        if user_choice.lower() == 'no':
            break

if __name__ == "__main__":
    main()
