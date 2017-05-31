def delta(state, letter):
    states, inputs = ['A', 'B', 'C', 'D', 'E'], ['b', '0', '1']
    transition = [
        ['E', 'B', 'E'],
        ['C', 'E', 'E'],
        ['E', 'D', 'D'],
        ['E', 'D', 'D'],
        ['E', 'E', 'E']
    ]
    return transition[states.index(state)][inputs.index(letter)]

def fsa(word):
    state = 'A'
    for letter in word:
        state = delta(state, letter)
    return state == 'D'

if __name__ == '__main__':
    for b in ['0b01', '011', '0b1101']:
        print('{} {}'.format(b, fsa(b)))
