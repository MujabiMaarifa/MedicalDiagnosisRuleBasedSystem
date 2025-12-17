class RuleBasedSystem: 
    def __init__(self): 
        self.facts = set() #set is preferred for no duplicates of facts in the kb
        self.rules = [] 
 
    def add_fact(self, fact): 
        self.facts.add(fact) 
 
    def add_rule(self, conditions, conclusion): 
        self.rules.append((set(conditions), conclusion)) 
 
    def forward_chain(self): 
        changed = True 
        while changed: 
            changed = False 
            for conditions, conclusion in self.rules: 
                if conditions.issubset(self.facts): 
                    if conclusion not in self.facts: 
                        self.facts.add(conclusion) 
                        print(f'Derived: {conclusion}') 
                        changed = True 
        return self.facts
    
    #backward chaining 
    def backward_chain(self, goal, visited=None):
        if visited is None:
            visited = set() #stores visited goals to avoid infinite loops during recursion
        if goal in self.facts:
            return True
        if goal in visited:
            return False
        visited.add(goal)

        #keep track of rules that can lead to the goal
        for conditions, conclusion in self.rules:
            #try to prove all conditions (subgoals)
            if conclusion == goal:
                all_proven = True
                for condition in conditions:
                    if not self.backward_chain(condition, visited):
                        all_proven = False
                        break
                    if all_proven:
                        self.facts.add(goal) #add goal to facts if proven
                        print(f'Proven: {goal}')
                        return True
        return False #if no rule or fact can prove the goal

      
# Create system 
system = RuleBasedSystem() 
 
# Add rules 
system.add_rule(['fever', 'cough'], 'suspect_flu') 
system.add_rule(['suspect_flu', 'body_ache'], 'diagnose_flu') 
system.add_rule(['diagnose_flu'], 'prescribe_rest') 
 
# Add initial facts 
for fact in ['fever', 'cough', 'body_ache']: 
    system.add_fact(fact) 
 
# Run inference 
print('Forward Chaining Results:')
result = system.forward_chain() 
print('Final facts:', result) 

print('\nBackward Chaining Results:')
goals = ['prescribe_rest', 'diagnose_flu']
for goal in goals:
    if system.backward_chain(goal):
        print(f'Goal "{goal}" has been achieved.')
    else:
        print(f'Goal "{goal}" could not be achieved.')

print('Final facts after backward chaining:', system.facts)